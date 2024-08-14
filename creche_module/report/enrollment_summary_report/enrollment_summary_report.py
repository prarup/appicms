import frappe
from frappe import _
from datetime import datetime, timedelta

def execute(filters=None):
    columns = [
        {"label": _("Partner"), "fieldname": "partner_name", "fieldtype": "Data", "width": 100},
        {"label": _("State Name"), "fieldname": "state_name", "fieldtype": "Data", "width": 100},
        {"label": _("District Name"), "fieldname": "district_name", "fieldtype": "Data", "width": 100},
        {"label": _("Block Name"), "fieldname": "block_name", "fieldtype": "Data", "width": 100},
        {"label": _("GP Name"), "fieldname": "gp_name", "fieldtype": "Data", "width": 100},
        {"label": _("Creche Name"), "fieldname": "creche_name", "fieldtype": "Data", "width": 100},
        {"label": _("Cumulative Enrollment"), "fieldname": "cumulative_enrollment", "fieldtype": "Int", "width": 150},
        {"label": _("New Enrollment (In this month)"), "fieldname": "new_enrollment", "fieldtype": "Int", "width": 150},
        {"label": _("Currently Active"), "fieldname": "currently_active", "fieldtype": "Int", "width": 150},
        {"label": _("Total Cumulative Exit"), "fieldname": "total_cumulative_exit", "fieldtype": "Int", "width": 150},
        {"label": _("Total Exit This Month"), "fieldname": "new_exit", "fieldtype": "Int", "width": 150},
    ]

    reason_for_exit_types = [1, 2, 3, 4]
    for reason in reason_for_exit_types:
        columns.append({
            "label": _("Exit Reason {0}").format(reason),
            "fieldname": f"reason_{reason}",
            "fieldtype": "Int",
            "width": 150
        })

    data = get_report_data(filters)
    return columns, data

def get_report_data(filters):
    current_month = datetime.now().month
    current_year = datetime.now().year

    # Calculate the date 30 days ago
    thirty_days_ago = datetime.now() - timedelta(days=30)

    conditions = ""
    if filters:
        if filters.get("state_name"):
            conditions += f" AND s.name = '{filters['state_name']}'"
        if filters.get("district_name"):
            conditions += f" AND d.name = '{filters['district_name']}'"
        if filters.get("block_name"):
            conditions += f" AND b.name = '{filters['block_name']}'"
        if filters.get("gp_name"):
            conditions += f" AND g.name = '{filters['gp_name']}'"
        if filters.get("partner_name"):
            conditions += f" AND p.partner_name = '{filters['partner_name']}'"

    query = f"""
        SELECT
            p.partner_name,
            s.state_name,
            d.district_name,
            b.block_name,
            g.gp_name,
            c.creche_name,
            COUNT(DISTINCT cp.name) as cumulative_enrollment,
            SUM(CASE WHEN cp.date_of_enrollment >= '{thirty_days_ago.strftime('%Y-%m-%d')}' THEN 1 ELSE 0 END) as new_enrollment,
	COUNT(DISTINCT cp.child_id) as currently_active,
	COUNT(DISTINCT cp.date_of_exit) as total_cumulative_exit

        FROM
            `tabChild Enrollment and Exit` cp
        LEFT JOIN
            `tabCreche` c ON cp.creche_id = c.name
        LEFT JOIN
            `tabState` s ON s.name = c.state_id
        LEFT JOIN
            `tabDistrict` d ON d.name = c.district_id
        LEFT JOIN
            `tabBlock` b ON b.name = c.block_id
        LEFT JOIN
            `tabGram Panchayat` g ON g.name = c.gp_id
        LEFT JOIN
            `tabPartner` p ON c.partner_id = p.name
	left join
		`tabChild Profile` cpr on cpr.chhguid = cp.hhcguid
        WHERE 1=1
        {conditions}
        GROUP BY
            c.name, s.state_name, d.district_name, b.block_name, g.gp_name, c.creche_name
    """

    data = frappe.db.sql(query, as_dict=True)
    return data
