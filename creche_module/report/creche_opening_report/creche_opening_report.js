frappe.query_reports["Creche Opening Report"] = {
    filters: [
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
            default: "2024"
        },
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
            fieldname: "block",
            label: __("Block"),
            fieldtype: "Link",
            options: "Block",
            reqd: 0
        },
        {
            fieldname: "gp",
            label: __("GP"),
            fieldtype: "Link",
            options: "GP",
            reqd: 0
        },
        {
            fieldname: "creche",
            label: __("Creche"),
            fieldtype: "Link",
            options: "Creche",
            reqd: 0
        }
    ]
};
