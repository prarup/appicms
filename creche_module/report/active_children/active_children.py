import frappe
from frappe import _
from frappe.utils import getdate
from collections import defaultdict

def execute(filters=None):
    if not filters:
        filters = {}
    if not filters.get('year'):
        filters['year'] = getdate().year

    columns = get_columns(filters)
    data = get_data(filters)
    return columns, data

def get_columns(filters):
    year = filters.get("year")
    # Define columns dynamically for each month
    months = [
        {"label": _("January"), "fieldname": "january", "fieldtype": "Int", "width": 100},
        {"label": _("February"), "fieldname": "february", "fieldtype": "Int", "width": 100},
        {"label": _("March"), "fieldname": "march", "fieldtype": "Int", "width": 100},
        {"label": _("April"), "fieldname": "april", "fieldtype": "Int", "width": 100},
        {"label": _("May"), "fieldname": "may", "fieldtype": "Int", "width": 100},
        {"label": _("June"), "fieldname": "june", "fieldtype": "Int", "width": 100},
        {"label": _("July"), "fieldname": "july", "fieldtype": "Int", "width": 100},
        {"label": _("August"), "fieldname": "august", "fieldtype": "Int", "width": 100},
        {"label": _("September"), "fieldname": "september", "fieldtype": "Int", "width": 100},
        {"label": _("October"), "fieldname": "october", "fieldtype": "Int", "width": 100},
        {"label": _("November"), "fieldname": "november", "fieldtype": "Int", "width": 100},
        {"label": _("December"), "fieldname": "december", "fieldtype": "Int", "width": 100}
    ]
    
    # Static columns for State, District, Block, GP, Creche
    static_columns = [
        {"label": _("State"), "fieldname": "state", "fieldtype": "Data", "width": 100},
        {"label": _("District"), "fieldname": "district", "fieldtype": "Data", "width": 100},
        {"label": _("Block"), "fieldname": "block", "fieldtype": "Data", "width": 100},
        {"label": _("GP"), "fieldname": "gp", "fieldtype": "Data", "width": 100},
        {"label": _("Creche"), "fieldname": "creche", "fieldtype": "Data", "width": 200}
    ]
    
    columns = static_columns + months
    return columns

def get_data(filters):
    year = filters.get('year')
    conditions = get_conditions(filters)
    data = defaultdict(lambda: defaultdict(int))

    query = f"""
        SELECT
            state.state_name AS state,
            district.district_name AS district,
            block.block_name AS block,
            gp.gp_name AS gp,
            creche.creche_name AS creche,
            MONTH(attendance.date_of_attendance) AS month,
            SUM(LENGTH(childlist.parent))/2 AS total_count
        FROM
            `tabChild Attendance` AS attendance
        JOIN
            `tabCreche` AS creche ON attendance.creche_id = creche.name
        JOIN
            `tabState` AS state ON state.name = creche.state_id
        JOIN
            `tabDistrict` AS district ON district.name = creche.district_id
        JOIN
            `tabBlock` AS block ON block.name = creche.block_id
        JOIN
            `tabGram Panchayat` AS gp ON gp.name = creche.gp_id
        LEFT JOIN
            `tabChild Attendance List` AS childlist ON childlist.parent = attendance.name
        WHERE
            YEAR(attendance.date_of_attendance) = %(year)s
            {conditions}
        GROUP BY
            state.state_name, district.district_name, block.block_name, gp.gp_name, creche.creche_name, MONTH(attendance.date_of_attendance)
        ORDER BY
            state.state_name, district.district_name, block.block_name, gp.gp_name, creche.creche_name, MONTH(attendance.date_of_attendance)
    """

    rows = frappe.db.sql(query, {"year": year}, as_dict=True)

    for row in rows:
        key = (row['state'], row['district'], row['block'], row['gp'], row['creche'])
        month = row['month']
        total_count = row['total_count'] or 0
        data[key][month] = total_count

    formatted_data = []

    for key, months_data in data.items():
        row = {
            "state": key[0],
            "district": key[1],
            "block": key[2],
            "gp": key[3],
            "creche": key[4],
            "january": months_data.get(1, 0),
            "february": months_data.get(2, 0),
            "march": months_data.get(3, 0),
            "april": months_data.get(4, 0),
            "may": months_data.get(5, 0),
            "june": months_data.get(6, 0),
            "july": months_data.get(7, 0),
            "august": months_data.get(8, 0),
            "september": months_data.get(9, 0),
            "october": months_data.get(10, 0),
            "november": months_data.get(11, 0),
            "december": months_data.get(12, 0)
        }
        formatted_data.append(row)

    return formatted_data

def get_conditions(filters):
    conditions = ""
    if filters.get("state"):
        conditions += " AND state.name = %(state)s"
    if filters.get("district"):
        conditions += " AND district.name = %(district)s"
    if filters.get("block"):
        conditions += " AND block.name = %(block)s"
    if filters.get("gp"):
        conditions += " AND gp.name = %(gp)s"
    if filters.get("creche"):
        conditions += " AND creche.name = %(creche)s"
    return conditions
