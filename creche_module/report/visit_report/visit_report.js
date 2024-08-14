frappe.query_reports["Visit Report"] = {
    filters: [
        {
            fieldname: "state",
            label: __("State"),
            fieldtype: "Link",
            options: "State",
            reqd: 0
        },
        {
            fieldname: "district",
            label: __("District"),
            fieldtype: "Link",
            options: "District",
            reqd: 0
        },
        {
            fieldname: "user_type",
            label: __("User Type"),
            fieldtype: "Link",
            options: "Role Profile",
            reqd: 0
        }
    ]
};
