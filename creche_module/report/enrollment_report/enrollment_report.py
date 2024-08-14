import frappe
from frappe.utils import nowdate

def execute(filters=None):
    columns, data = [], []
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    # Get the selected year from filters or use the current year if not provided
    selected_year = filters.get("year") if filters else frappe.utils.nowdate().split('-')[0]

    # Define columns
    columns = [
        {"label": "State", "fieldname": "state", "fieldtype": "Data", "width": 120},
        {"label": "District", "fieldname": "district", "fieldtype": "Data", "width": 120},
        {"label": "Block", "fieldname": "block", "fieldtype": "Data", "width": 120},
        {"label": "GP", "fieldname": "gp", "fieldtype": "Data", "width": 120},
        {"label": "Creche", "fieldname": "creche", "fieldtype": "Data", "width": 120}
    ]

    for month in months:
        month_label = f"{month[:3]}-{selected_year}"
        columns.append({"label": month_label, "fieldname": month.lower(), "fieldtype": "Int", "width": 80})

    data = get_enrollment_data(filters, months, selected_year)
    return columns, data

@frappe.whitelist()
def get_enrollment_data(filters=None, months=None, year=None):
    state = filters.get("state") if filters else None
    district = filters.get("district") if filters else None
    block = filters.get("block") if filters else None
    gp = filters.get("gp") if filters else None
    creche = filters.get("creche") if filters else None

    conditions = ""
    if state:
        conditions += f" AND creche.state_id = '{state}'"
    if district:
        conditions += f" AND creche.district_id = '{district}'"
    if block:
        conditions += f" AND creche.block_id = '{block}'"
    if gp:
        conditions += f" AND creche.gp_id = '{gp}'"
    if creche:
        conditions += f" AND creche.name = '{creche}'"

    sql_query = f"""
        SELECT
            state.state_name AS state,
            district.district_name AS district,
            block.block_name AS block,
            gp.gp_name AS gp,
            creche.creche_name AS creche,
            SUM(IF(MONTH(cp.date_of_enrollment) = 1 AND YEAR(cp.date_of_enrollment) = {year}, 1, 0)) AS january,
            SUM(IF(MONTH(cp.date_of_enrollment) = 2 AND YEAR(cp.date_of_enrollment) = {year}, 1, 0)) AS february,
            SUM(IF(MONTH(cp.date_of_enrollment) = 3 AND YEAR(cp.date_of_enrollment) = {year}, 1, 0)) AS march,
            SUM(IF(MONTH(cp.date_of_enrollment) = 4 AND YEAR(cp.date_of_enrollment) = {year}, 1, 0)) AS april,
            SUM(IF(MONTH(cp.date_of_enrollment) = 5 AND YEAR(cp.date_of_enrollment) = {year}, 1, 0)) AS may,
            SUM(IF(MONTH(cp.date_of_enrollment) = 6 AND YEAR(cp.date_of_enrollment) = {year}, 1, 0)) AS june,
            SUM(IF(MONTH(cp.date_of_enrollment) = 7 AND YEAR(cp.date_of_enrollment) = {year}, 1, 0)) AS july,
            SUM(IF(MONTH(cp.date_of_enrollment) = 8 AND YEAR(cp.date_of_enrollment) = {year}, 1, 0)) AS august,
            SUM(IF(MONTH(cp.date_of_enrollment) = 9 AND YEAR(cp.date_of_enrollment) = {year}, 1, 0)) AS september,
            SUM(IF(MONTH(cp.date_of_enrollment) = 10 AND YEAR(cp.date_of_enrollment) = {year}, 1, 0)) AS october,
            SUM(IF(MONTH(cp.date_of_enrollment) = 11 AND YEAR(cp.date_of_enrollment) = {year}, 1, 0)) AS november,
            SUM(IF(MONTH(cp.date_of_enrollment) = 12 AND YEAR(cp.date_of_enrollment) = {year}, 1, 0)) AS december
        FROM
            `tabChild Profile` AS cp
        JOIN
            `tabCreche` AS creche ON cp.creche_id = creche.name
        JOIN
            `tabState` AS state ON state.name = creche.state_id
        JOIN
            `tabDistrict` AS district ON district.name = creche.district_id
        JOIN
            `tabBlock` AS block ON block.name = creche.block_id
        JOIN
            `tabGram Panchayat` AS gp ON gp.name = creche.gp_id
        WHERE
            1 = 1
            {conditions}
        GROUP BY
            state.state_name, district.district_name, block.block_name, gp.gp_name, creche.creche_name
        ORDER BY
            state.state_name, district.district_name, block.block_name, gp.gp_name, creche.creche_name
    """

    data = frappe.db.sql(sql_query, as_dict=True)
    return data
