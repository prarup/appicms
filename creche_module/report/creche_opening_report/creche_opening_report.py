import frappe
from frappe.utils import nowdate

def execute(filters=None):
    columns = get_columns(filters)
    data = get_enrollment_data(filters)
    return columns, data

def get_columns(filters):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    selected_year = filters.get("year") if filters else nowdate().split('-')[0]

    columns = [
        {"label": "Partner", "fieldname": "partner", "fieldtype": "Data", "width": 120},
        {"label": "State", "fieldname": "state", "fieldtype": "Data", "width": 120},
        {"label": "District", "fieldname": "district", "fieldtype": "Data", "width": 120},
        {"label": "Block", "fieldname": "block", "fieldtype": "Data", "width": 120},
        {"label": "GP", "fieldname": "gp", "fieldtype": "Data", "width": 120},
        {"label": "Creche", "fieldname": "creche", "fieldtype": "Data", "width": 120}
    ]

    for month in months:
        month_label = f"{month[:3]}-{selected_year}"
        columns.append({"label": month_label, "fieldname": month.lower(), "fieldtype": "Int", "width": 80})

    return columns

@frappe.whitelist()
def get_enrollment_data(filters=None):
    state = filters.get("state") if filters else None
    district = filters.get("district") if filters else None
    block = filters.get("block") if filters else None
    gp = filters.get("gp") if filters else None
    creche = filters.get("creche") if filters else None
    year = filters.get("year") if filters else nowdate().split('-')[0]

    conditions = []
    if state:
        conditions.append(f"AND s.state_name = '{state}'")
    if district:
        conditions.append(f"AND d.district_name = '{district}'")
    if block:
        conditions.append(f"AND b.block_name = '{block}'")
    if gp:
        conditions.append(f"AND g.gp_name = '{gp}'")
    if creche:
        conditions.append(f"AND c.creche_name = '{creche}'")

    condition_str = " ".join(conditions)

    sql_query = f"""
        SELECT
            p.partner_name AS partner,
            s.state_name AS state,
            d.district_name AS district,
            b.block_name AS block,
            g.gp_name AS gp,
            c.creche_name AS creche,
            SUM(IF(MONTH(ci.date_of_checkin) = 1 AND YEAR(ci.date_of_checkin) = {year}, 1, 0)) AS january,
            SUM(IF(MONTH(ci.date_of_checkin) = 2 AND YEAR(ci.date_of_checkin) = {year}, 1, 0)) AS february,
            SUM(IF(MONTH(ci.date_of_checkin) = 3 AND YEAR(ci.date_of_checkin) = {year}, 1, 0)) AS march,
            SUM(IF(MONTH(ci.date_of_checkin) = 4 AND YEAR(ci.date_of_checkin) = {year}, 1, 0)) AS april,
            SUM(IF(MONTH(ci.date_of_checkin) = 5 AND YEAR(ci.date_of_checkin) = {year}, 1, 0)) AS may,
            SUM(IF(MONTH(ci.date_of_checkin) = 6 AND YEAR(ci.date_of_checkin) = {year}, 1, 0)) AS june,
            SUM(IF(MONTH(ci.date_of_checkin) = 7 AND YEAR(ci.date_of_checkin) = {year}, 1, 0)) AS july,
            SUM(IF(MONTH(ci.date_of_checkin) = 8 AND YEAR(ci.date_of_checkin) = {year}, 1, 0)) AS august,
            SUM(IF(MONTH(ci.date_of_checkin) = 9 AND YEAR(ci.date_of_checkin) = {year}, 1, 0)) AS september,
            SUM(IF(MONTH(ci.date_of_checkin) = 10 AND YEAR(ci.date_of_checkin) = {year}, 1, 0)) AS october,
            SUM(IF(MONTH(ci.date_of_checkin) = 11 AND YEAR(ci.date_of_checkin) = {year}, 1, 0)) AS november,
            SUM(IF(MONTH(ci.date_of_checkin) = 12 AND YEAR(ci.date_of_checkin) = {year}, 1, 0)) AS december
        FROM
            `tabCreche Check In` AS ci
        JOIN
            `tabCreche` AS c ON ci.creche_id = c.name
        JOIN
            `tabState` AS s ON c.state_id = s.name
        JOIN
            `tabDistrict` AS d ON c.district_id = d.name
        JOIN
            `tabBlock` AS b ON c.block_id = b.name
        JOIN
            `tabGram Panchayat` AS g ON c.gp_id = g.name
        JOIN
            `tabPartner` AS p ON c.partner_id = p.name
        WHERE
            YEAR(ci.date_of_checkin) = {year}
            {condition_str}
        GROUP BY
            p.partner_name, s.state_name, d.district_name, b.block_name, g.gp_name, c.creche_name
        ORDER BY
            p.partner_name, s.state_name, d.district_name, b.block_name, g.gp_name, c.creche_name
    """

    data = frappe.db.sql(sql_query, as_dict=True)
    return data
