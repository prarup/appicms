import frappe
from frappe.utils import nowdate

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
        {"label": "Creche Open", "fieldname": "creche_open", "fieldtype": "Int", "width": 120},
        {"label": "Breakfast Days", "fieldname": "breakfast_days", "fieldtype": "Int", "width": 120},
        {"label": "Lunch Days", "fieldname": "lunch_days", "fieldtype": "Int", "width": 120},
        {"label": "Egg Days", "fieldname": "egg_days", "fieldtype": "Int", "width": 120},
        {"label": "Evening Snacks Days", "fieldname": "evening_snacks_days", "fieldtype": "Int", "width": 120},
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

    # Default values if not provided
    if not month:
        month = nowdate().split('-')[1]
    if not year:
        year = nowdate().split('-')[0]

    conditions = []
    if partner:
        conditions.append(f"AND p.partner_name = '{partner}'")
    if state:
        conditions.append(f"AND s.state_name = '{state}'")
    if district:
        conditions.append(f"AND d.district_name = '{district}'")
    if block:
        conditions.append(f"AND b.block_name = '{block}'")
    if gp:
        conditions.append(f"AND g.gp_name = '{gp}'")
    if village:
        conditions.append(f"AND v.village_name = '{village}'")
    if creche:
        conditions.append(f"AND c.creche_name = '{creche}'")

    condition_str = " ".join(conditions)

    # Filtering data by month and year
    date_condition = f"AND MONTH(att.date_of_attendance) = {month} AND YEAR(att.date_of_attendance) = {year}"

    sql_query = f"""
        SELECT
            p.partner_name AS partner,
            s.state_name AS state,
            d.district_name AS district,
            b.block_name AS block,
            g.gp_name AS gp,
            v.village_name AS village,
            c.creche_name AS creche,
            COUNT(DISTINCT CASE WHEN att.date_of_attendance IS NOT NULL THEN att.name END) AS creche_open,
            COUNT(DISTINCT CASE WHEN att.breakfast IS NOT NULL AND att.breakfast > 0 THEN att.date_of_attendance END) AS breakfast_days,
            COUNT(DISTINCT CASE WHEN att.lunch IS NOT NULL AND att.lunch > 0 THEN att.date_of_attendance END) AS lunch_days,
            COUNT(DISTINCT CASE WHEN att.egg IS NOT NULL AND att.egg > 0 THEN att.date_of_attendance END) AS egg_days,
            COUNT(DISTINCT CASE WHEN att.evening_snacks IS NOT NULL AND att.evening_snacks > 0 THEN att.date_of_attendance END) AS evening_snacks_days
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
        WHERE
            1=1
            {condition_str}
            {date_condition}
        GROUP BY
            p.partner_name, s.state_name, d.district_name, b.block_name, g.gp_name, v.village_name, c.creche_name
        ORDER BY
            p.partner_name, s.state_name, d.district_name, b.block_name, g.gp_name, v.village_name, c.creche_name
    """

    data = frappe.db.sql(sql_query, as_dict=True)
    return data
