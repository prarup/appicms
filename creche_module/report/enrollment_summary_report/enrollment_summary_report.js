// Copyright (c) 2024, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.query_reports["Enrollment Summary Report"] = {
    "filters": [
{
            "fieldname": "partner_name",
            "label": __("Partner"),
            "fieldtype": "Link",
            "options": "Partner",
            "reqd": 0        },
        {
            "fieldname": "state_name",
            "label": __("State"),
            "fieldtype": "Link",
            "options": "State",
            "reqd": 0,
            "get_query": function() {
                return {
                    // Optionally restrict query based on other conditions
                };
            }
        },
        {
            "fieldname": "district_name",
            "label": __("District"),
            "fieldtype": "Link",
            "options": "District",
            "reqd": 0,
            "get_query": function() {
                let state_name = frappe.query_report.get_filter_value("state_name");
                return {
                    filters: {
                        state_id: state_name ? state_name : undefined
                    }
                };
            }
        },
        {
            "fieldname": "block_name",
            "label": __("Block"),
            "fieldtype": "Link",
            "options": "Block",
            "reqd": 0,
            "get_query": function() {
                let district_name = frappe.query_report.get_filter_value("district_name");
                return {
                    filters: {
                        district_id: district_name ? district_name : undefined
                    }
                };
            }
        },
        {
            "fieldname": "gp_name",
            "label": __("Gram Panchayat"),
            "fieldtype": "Link",
            "options": "Gram Panchayat",
            "reqd": 0,
            "get_query": function() {
                let block_name = frappe.query_report.get_filter_value("block_name");
                return {
                    filters: {
                        block_id: block_name ? block_name : undefined
                    }
                };
            }
        }
    ]
};
