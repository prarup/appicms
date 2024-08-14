frappe.query_reports["Monthly Tracker (Meals)"] = {
    "filters": [
        {
            "fieldname": "partner",
            "label": __("Partner"),
            "fieldtype": "Link",
            "options": "Partner",
            "width": 200
        },
        {
            "fieldname": "state",
            "label": __("State"),
            "fieldtype": "Link",
            "options": "State",
            "width": 200
        },
        {
            "fieldname": "district",
            "label": __("District"),
            "fieldtype": "Link",
            "options": "District",
            "width": 200
        },
        {
            "fieldname": "block",
            "label": __("Block"),
            "fieldtype": "Link",
            "options": "Block",
            "width": 200
        },
        {
            "fieldname": "gp",
            "label": __("GP"),
            "fieldtype": "Link",
            "options": "Gram Panchayat",
            "width": 200
        },
        {
            "fieldname": "village",
            "label": __("Village"),
            "fieldtype": "Link",
            "options": "Village",
            "width": 200
        },
        {
            "fieldname": "creche",
            "label": __("Creche"),
            "fieldtype": "Link",
            "options": "Creche",
            "width": 200
        },
        {
            "fieldname": "month",
            "label": __("Month"),
            "fieldtype": "Select",
            "options": [
                "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
            ],
            "default": (new Date()).toLocaleString('default', { month: 'long' }),
            "width": 150
        },
        {
            "fieldname": "year",
            "label": __("Year"),
            "fieldtype": "Select",
            "options": [
                "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034", "2035", "2036", "2037", "2038", "2039", "2040", "2041", "2042", "2043", "2044", "2045", "2046", "2047", "2048", "2049", "2050"
            ],
            "default": (new Date()).getFullYear().toString(),
            "width": 150
        }
    ]
};
