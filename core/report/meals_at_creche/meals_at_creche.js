frappe.query_reports["Meals at Creche"] = {
    filters: [
        {
            fieldname: "partner",
            label: __("Partner"),
            fieldtype: "Link",
            options: "Partner",
            default: "",
            ignore_case: true,
        },
        {
            fieldname: "state",
            label: __("State"),
            fieldtype: "Link",
            options: "State",
            default: "",
            ignore_case: true,
        },
        {
            fieldname: "district",
            label: __("District"),
            fieldtype: "Link",
            options: "District",
            default: "",
            ignore_case: true,
        },
        {
            fieldname: "block",
            label: __("Block"),
            fieldtype: "Link",
            options: "Block",
            default: "",
            ignore_case: true,
        },
        {
            fieldname: "gp",
            label: __("Gram Panchayat"),
            fieldtype: "Link",
            options: "Gram Panchayat",
            default: "",
            ignore_case: true,
        },
        {
            fieldname: "village",
            label: __("Village"),
            fieldtype: "Link",
            options: "Village",
            default: "",
            ignore_case: true,
        },
        {
            fieldname: "creche",
            label: __("Creche"),
            fieldtype: "Link",
            options: "Creche",
            default: "",
            ignore_case: true,
        },
        {
            fieldname: "month",
            label: __("Month"),
            fieldtype: "Select",
            options: [
                { "value": "01", "label": "January" },
                { "value": "02", "label": "February" },
                { "value": "03", "label": "March" },
                { "value": "04", "label": "April" },
                { "value": "05", "label": "May" },
                { "value": "06", "label": "June" },
                { "value": "07", "label": "July" },
                { "value": "08", "label": "August" },
                { "value": "09", "label": "September" },
                { "value": "10", "label": "October" },
                { "value": "11", "label": "November" },
                { "value": "12", "label": "December" }
            ],
            default: frappe.datetime.get_today().split('-')[1],
        },
        {
            fieldname: "year",
            label: __("Year"),
            fieldtype: "Select",
            options: [
                "2024", "2025", "2026", "2027", "2028", "2029", "2030",
                "2031", "2032", "2033", "2034", "2035", "2036", "2037",
                "2038", "2039", "2040", "2041", "2042", "2043", "2044",
                "2045", "2046", "2047", "2048", "2049", "2050"
            ],
            default: frappe.datetime.get_today().split('-')[0],
        },
    ],
};