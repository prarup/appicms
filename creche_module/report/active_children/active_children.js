frappe.query_reports["Active Children"] = {
    "filters": [
        {
            "fieldname": "state",
            "label": __("State"),
            "fieldtype": "Link",
            "options": "State"
        },
        {
            "fieldname": "district",
            "label": __("District"),
            "fieldtype": "Link",
            "options": "District"
        },
        {
            "fieldname": "block",
            "label": __("Block"),
            "fieldtype": "Link",
            "options": "Block"
        },
        {
            "fieldname": "gp",
            "label": __("Gram Panchayat"),
            "fieldtype": "Link",
            "options": "Gram Panchayat"
        },
        {
            "fieldname": "creche",
            "label": __("Creche"),
            "fieldtype": "Link",
            "options": "Creche"
        },
        {
            "fieldname": "year",
            "label": __("Year"),
            "fieldtype": "Select",
            "options": [
                "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032", "2033", 
                "2034", "2035", "2036", "2037", "2038", "2039", "2040", "2041", "2042", "2043", 
                "2044", "2045", "2046", "2047", "2048", "2049", "2050"
            ],
            "default": (new Date()).getFullYear()
        }
    ]
};
