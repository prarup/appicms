import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
    columns = get_columns(filters)
    data = get_data(filters)
    return columns, data

def get_columns(filters):
    return [
        {"label": _("State"), "fieldname": "state", "fieldtype": "Data", "width": 150},
        {"label": _("District"), "fieldname": "district", "fieldtype": "Data", "width": 150},
        {"label": _("User"), "fieldname": "supervisor_id", "fieldtype": "Data", "width": 150},
        {"label": _("Creche"), "fieldname": "creche_id", "fieldtype": "Data", "width": 150},
        {"label": _("No of Check-ins"), "fieldname": "no_of_checkins", "fieldtype": "Int", "width": 150},
        {"label": _("No of Visit Checklist form filled"), "fieldname": "no_of_visit_checklist", "fieldtype": "Int", "width": 200},
        {"label": _("Visit %"), "fieldname": "visit_percentage", "fieldtype": "Percent", "width": 100},
    ]

def get_data(filters):
    conditions = get_conditions(filters)
    query = f"""
        SELECT
            state.state_name AS state,
            district.district_name AS district,
            checkin.supervisor_id AS supervisor_id,
            checkin.creche AS creche_id,
            COUNT(checkin.name) AS no_of_checkins,
            SUM(CASE WHEN checklist.name IS NOT NULL THEN 1 ELSE 0 END) AS no_of_visit_checklist,
            (SUM(CASE WHEN checklist.name IS NOT NULL THEN 1 ELSE 0 END) / COUNT(checkin.name)) * 100 AS visit_percentage
        FROM
            `tabCreche Check In` AS checkin
        LEFT JOIN
            `tabCreche Monitoring Checklist` AS checklist ON checklist.parent = checkin.name
        LEFT JOIN
            `tabCreche` AS creche ON creche.name = checkin.creche
        LEFT JOIN
            `tabState` AS state ON state.name = creche.state_id
        LEFT JOIN
            `tabDistrict` AS district ON district.name = creche.district_id
        WHERE
            {conditions}
        GROUP BY
            state.state_name, district.district_name, checkin.supervisor_id, checkin.creche
    """
    data = frappe.db.sql(query, as_dict=True)
    return data

def get_conditions(filters):
    conditions = "1 = 1"
    if filters.get("state"):
        conditions += f" AND state.name = '{filters.get('state')}'"
    if filters.get("district"):
        conditions += f" AND district.name = '{filters.get('district')}'"
    if filters.get("user_type"):
        conditions += f" AND supervisor_id IN (SELECT user FROM `tabRole Profile` WHERE role = '{filters.get('user_type')}')"
    return conditions
