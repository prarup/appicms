frappe.query_reports["Immunization (Vaccine wise)"] = {
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
            "fieldname": "vaccine",
            "label": __("Vaccine"),
            "fieldtype": "Link",
            "options": "Vaccines",
            "width": 200,
	"reqd":1
        }    
]
};
