import frappe
from frappe.utils import nowdate
from datetime import datetime, timedelta

def execute(filters=None):
    columns = get_columns()
    data = get_summary_data(filters)
    return columns, data

def get_columns():
    columns = [
        {"label": "Partner", "fieldname": "partner", "fieldtype": "Data", "width": 120},
        {"label": "State", "fieldname": "state", "fieldtype": "Data", "width": 120},
        {"label": "District", "fieldname": "district", "fieldtype": "Data", "width": 120},
        {"label": "Block", "fieldname": "block", "fieldtype": "Data", "width": 120},
        {"label": "GP", "fieldname": "gp", "fieldtype": "Data", "width": 120},
        {"label": "Village", "fieldname": "village", "fieldtype": "Data", "width": 120},
        {"label": "Creche", "fieldname": "creche", "fieldtype": "Data", "width": 120},
        {"label": "Date", "fieldname": "date", "fieldtype": "Date", "width": 120},
        {"label": "Enrolled Children", "fieldname": "e_children", "fieldtype": "Data", "width": 120},
        {"label": "Children Present", "fieldname": "c_present", "fieldtype": "Data", "width": 120},

        {"label": "Creche Open Time", "fieldname": "open_time", "fieldtype": "Time", "width": 120},
        {"label": "Creche Close Time", "fieldname": "close_time", "fieldtype": "Time", "width": 120},
        {"label": "ECD Activity Done", "fieldname": "ecd_activity_done", "fieldtype": "Data", "width": 150},
        {"label": "Breakfast", "fieldname": "breakfast", "fieldtype": "Int", "width": 100},
        {"label": "Lunch", "fieldname": "lunch", "fieldtype": "Int", "width": 100},
        {"label": "Egg", "fieldname": "egg", "fieldtype": "Int", "width": 100},
        {"label": "Evening Snacks", "fieldname": "evening_snacks", "fieldtype": "Int", "width": 120},
    ]
    return columns

@frappe.whitelist()
def get_summary_data(filters=None):
    partner = filters.get("partner") if filters else None
    state = filters.get("state") if filters else None
    district = filters.get("district") if filters else None
    block = filters.get("block") if filters else None
    gp = filters.get("gp") if filters else None
    village = filters.get("village") if filters else None
    creche = filters.get("creche") if filters else None
    month = filters.get("month") if filters else None
    year = filters.get("year") if filters else None

    conditions = []
    if partner:
        conditions.append(f"att.partner_id = '{partner}'")
    if state:
        conditions.append(f"att.state_id = '{state}'")
    if district:
        conditions.append(f"att.district_id = '{district}'")
    if block:
        conditions.append(f"att.block_id = '{block}'")
    if gp:
        conditions.append(f"att.gp_id = '{gp}'")
    if village:
        conditions.append(f"att.village_id = '{village}'")
    if creche:
        conditions.append(f"att.creche_id = '{creche}'")
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
            p.partner_name AS partner,
            s.state_name AS state,
            d.district_name AS district,
            b.block_name AS block,
            g.gp_name AS gp,
            v.village_name AS village,
            c.creche_name AS creche,
            att.date_of_attendance AS date,
		(SELECT count(*) FROM `tabChild Profile` as cp WHERE cp.is_active=1 AND cp.creche_id = att.creche_id ) as e_children,
		(SELECT count(*) FROM `tabChild Attendance List` as cal WHERE cal.parent= att.name) as c_present,

            att.open_time AS open_time,
            att.close_time AS close_time,
            CASE WHEN att.isecd_activities_done_for_the_day = 1 THEN 'Yes' ELSE 'No' END AS ecd_activity_done,
            att.breakfast AS breakfast,
            att.lunch AS lunch,
            att.egg AS egg,
            att.evening_snacks AS evening_snacks
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
        JOIN
            `tabVillage` AS v ON c.village_id = v.name
        JOIN
            `tabPartner` AS p ON c.partner_id = p.name

        {where_clause}
        GROUP BY
            p.partner_name, s.state_name, d.district_name, b.block_name, g.gp_name, v.village_name, c.creche_name, att.date_of_attendance, att.open_time, att.close_time, ecd_activity_done
        ORDER BY
            p.partner_name, s.state_name, d.district_name, b.block_name, g.gp_name, v.village_name, c.creche_name, att.date_of_attendance
    """

    data = frappe.db.sql(sql_query, as_dict=True)
    return data
