import frappe
from frappe.utils import nowdate
from datetime import datetime, timedelta

def execute(filters=None):
    columns = get_columns()
    data = get_summary_data(filters)
    return columns, data

def get_columns():
    columns = [
        {"label": "State", "fieldname": "state", "fieldtype": "Data", "width": 120},
        {"label": "District", "fieldname": "district", "fieldtype": "Data", "width": 120},
        {"label": "Block", "fieldname": "block", "fieldtype": "Data", "width": 120},
        {"label": "GP", "fieldname": "gp", "fieldtype": "Data", "width": 120},
        {"label": "Creche", "fieldname": "creche", "fieldtype": "Data", "width": 120},
        {"label": "No of days creche was open", "fieldname": "days_creche_open", "fieldtype": "Int", "width": 180},
        {"label": "Average Children Present", "fieldname": "avg_children_present", "fieldtype": "Float", "width": 180},
        {"label": "Average Children having Breakfast", "fieldname": "avg_breakfast", "fieldtype": "Float", "width": 180},
        {"label": "Average Children having Lunch", "fieldname": "avg_lunch", "fieldtype": "Float", "width": 180},
        {"label": "Average Children having Eggs", "fieldname": "avg_egg", "fieldtype": "Float", "width": 180},
        {"label": "Average Children having Evening Snacks", "fieldname": "avg_evening_snacks", "fieldtype": "Float", "width": 200},
        {"label": "Average No of days ECD activity was done", "fieldname": "avg_ecd_activity", "fieldtype": "Float", "width": 200},
    ]
    return columns

@frappe.whitelist()
def get_summary_data(filters=None):
    state = filters.get("state") if filters else None
    district = filters.get("district") if filters else None
    block = filters.get("block") if filters else None
    gp = filters.get("gp") if filters else None
    creche = filters.get("creche") if filters else None
    month = filters.get("month") if filters else None
    year = filters.get("year") if filters else None

    conditions = []
    if state:
        conditions.append(f"s.state_id = '{state}'")
    if district:
        conditions.append(f"d.district_id = '{district}'")
    if block:
        conditions.append(f"b.block_id = '{block}'")
    if gp:
        conditions.append(f"g.gp_id = '{gp}'")
    if creche:
        conditions.append(f"c.name = '{creche}'")
    if month and year:
        try:
            # Convert month to number
            month_num = datetime.strptime(month, '%B').strftime('%m')
            start_date = f"{year}-{month_num}-01"
            # Calculate end date of the month
            next_month = (datetime(int(year), int(month_num), 1) + timedelta(days=31)).replace(day=1)
            end_date = (next_month - timedelta(days=1)).strftime('%Y-%m-%d')
            conditions.append(f"att.date_of_attendance BETWEEN '{start_date}' AND '{end_date}'")
        except ValueError:
            # Handle invalid month
            conditions.append("1=0")  # No results if month is invalid

    condition_str = " AND ".join(conditions)
    where_clause = f"WHERE 1=1 AND {condition_str}" if condition_str else "WHERE 1=1"

    sql_query = f"""
        SELECT
            s.state_name AS state,
            d.district_name AS district,
            b.block_name AS block,
            g.gp_name AS gp,
            c.creche_name AS creche,
            COUNT(att.date_of_attendance) AS days_creche_open,
            AVG((SELECT COUNT(*) FROM `tabChild Attendance List` AS cal WHERE cal.parent = att.name)) AS avg_children_present,
            AVG(att.breakfast) AS avg_breakfast,
            AVG(att.lunch) AS avg_lunch,
            AVG(att.egg) AS avg_egg,
            AVG(att.evening_snacks) AS avg_evening_snacks,
            AVG(CASE WHEN att.isecd_activities_done_for_the_day = 1 THEN 1 ELSE 0 END) AS avg_ecd_activity
        FROM
            `tabChild Attendance` AS att
        JOIN
            `tabCreche` AS c ON att.creche_id = c.name
        JOIN
            `tabState` AS s ON c.state_id = s.name
        JOIN
            `tabDistrict` AS d ON c.district_id = d.name
        JOIN
            `tabBlock` AS b ON c.block_id = b.name
        JOIN
            `tabGram Panchayat` AS g ON c.gp_id = g.name
        {where_clause}
        GROUP BY
            s.state_name, d.district_name, b.block_name, g.gp_name, c.creche_name
        ORDER BY
            s.state_name, d.district_name, b.block_name, g.gp_name, c.creche_name
    """

    data = frappe.db.sql(sql_query, as_dict=True)
    return data
