import frappe

def execute(filters=None):
    columns = [
        {"label": "Partner Name", "fieldname": "Partner Name", "fieldtype": "Link", "options": "Partner", "width": 200},
        {"label": "Date of Visit", "fieldname": "Date of Visit"},
        {"label": "State", "fieldname": "State", "fieldtype": "Link", "options": "State", "width": 200},
        {"label": "District", "fieldname": "District"},
        {"label": "Block", "fieldname": "Block"},
        {"label": "GP", "fieldname": "GP"},
        {"label": "Village", "fieldname": "Village"},
        {"label": "Hamlet", "fieldname": "Hamlet"},
        {"label": "Landmark", "fieldname": "Landmark"},
        {"label": "Respondent Name", "fieldname": "Respondent Name"},
        {"label": "Respondent Age", "fieldname": "Respondent Age"},
        {"label": "Respondent Gender", "fieldname": "Respondent Gender"},
        {"label": "Household Head Name", "fieldname": "Household Head Name"},
        {"label": "Social Category", "fieldname": "Social Category"},
        {"label": "Is the family a PVTG?", "fieldname": "Is the family a PVTG?"},
        {"label": "PVTG Name", "fieldname": "PVTG Name"},
        {"label": "Primary Occupation", "fieldname": "Primary Occupation"},
        {"label": "Primary Occupation Other", "fieldname": "Primary Occupation Other"},
        {"label": "Verification Status", "fieldname": "Verification Status"},
        {"label": "Number of Family Members", "fieldname": "Number of Family Members"},
        {"label": "Children Under 3 years", "fieldname": "Children Under 3 years"},
        {"label": "Children 3 to 6 years", "fieldname": "Children 3 to 6 years"},
        {"label": "Children 6 to 18 years", "fieldname": "Children 6 to 18 years"},
        {"label": "Adults above 18 years", "fieldname": "Adults above 18 years"},
        {"label": "Child Name", "fieldname": "Child Name"},
        {"label": "Child Gender", "fieldname": "Child Gender"},
        {"label": "Relation with Child", "fieldname": "Relation with Child"},
        {"label": "Child DOB", "fieldname": "Child DOB"},
        {"label": "Child Age in Months", "fieldname": "Child Age in Months"},
        {"label": "Child Is Verified?", "fieldname": "Child Is Verified?"},
        {"label": "Family Members Engaged as Migrant Workers", "fieldname": "Family Members Engaged as Migrant Workers"},
        {"label": "Number of Months the migrants were away last year", "fieldname": "Number of Months the migrants were away last year"},
        {"label": "Does anyone from the family migrate every year?", "fieldname": "Does anyone from the family migrate every year?"},
        {"label": "Who looks after the children at home?", "fieldname": "Who looks after the children at home?"}
    ]

    data = get_report_data(filters)
    return columns, data

@frappe.whitelist()
def get_report_data(filters=None):
    partner = filters.get("partner") if filters else None
    state = filters.get("state") if filters else None
    district = filters.get("district") if filters else None
    block = filters.get("block") if filters else None
    gp = filters.get("gp") if filters else None
    village = filters.get("village") if filters else None

    conditions = ""
    user_partner = frappe.get_value("User", frappe.session.user, "partner")  # Replace 'partner_field' with the actual fieldname in the User doctype
    if user_partner:
        conditions += f" AND P.name = '{user_partner}'"
    if state:
        conditions += f" AND state.name = '{state}'"
    if district:
        conditions += f" AND district.name = '{district}'"
    if block:
        conditions += f" AND block.name = '{block}'"
    if gp:
        conditions += f" AND gp.name = '{gp}'"
    if village:
        conditions += f" AND village.name = '{village}'"

    sql_query = f"""
        SELECT
            P.partner_name AS 'Partner Name',
            hh.date_of_visit AS 'Date of Visit',
            state.state_name AS 'State',
            district.district_name AS 'District',
            block.block_name AS 'Block',
            gp.gp_name AS 'GP',
            village.village_name AS 'Village',
            hh.hamlet AS 'Hamlet',
            hh.landmark AS 'Landmark',
            hh.respondent_name AS 'Respondent Name',
            hh.respondent_age AS 'Respondent Age',
            gender.gender AS 'Respondent Gender',
            hh.hosuehold_head_name AS 'Household Head Name',
            sc.social_category_name AS 'Social Category',
            CASE
                WHEN hh.is_the_family_a_pvtg = 1 THEN 'YES'
                ELSE 'NO'
            END AS 'Is the family a PVTG?',
            hh.pvtg_name AS 'PVTG Name',
            po.primary_occupation AS 'Primary Occupation',
            hh.primary_occupation_other AS 'Primary Occupation Other',
            vs.verfication_status_name AS 'Verification Status',
            hh.number_of_family_members AS 'Number of Family Members',
            hh.children__3_years AS 'Children Under 3 years',
            hh.children_3_to_6_years AS 'Children 3 to 6 years',
            hh.children_6_to_18_years AS 'Children 6 to 18 years',
            hh.adults_above_18_years AS 'Adults above 18 years',
            hhc.child_name AS 'Child Name',
            child_gender.gender AS 'Child Gender',
            relation.relation_name AS 'Relation with Child',
            hhc.child_dob AS 'Child DOB',
            hhc.child_age AS 'Child Age in Months',
            CASE
                WHEN hhc.is_verified = 1 THEN 'YES'
                ELSE 'NO'
            END AS 'Child Is Verified?',
            hh.family_members_enganged_as_migrant_workers AS 'Family Members Engaged as Migrant Workers',
            hh.no_of_months_the_migrants_were_away_last_year AS 'Number of Months the migrants were away last year',
            CASE
                WHEN hh.does_anyone_from_your_family_migrate_every_year = 1 THEN 'YES'
                ELSE 'NO'
            END AS 'Does anyone from the family migrate every year?',
            hh.who_looks_after_them_at_home AS 'Who looks after the children at home?'
        FROM
            `tabHousehold Form` AS hh
        JOIN
            `tabHousehold Child Form` AS hhc ON hh.name = hhc.parent
        JOIN
            `tabPartner` AS P ON P.name = hh.partner_id
        JOIN
            `tabState` AS state ON state.name = hh.state_id
        JOIN
            `tabDistrict` AS district ON district.name = hh.district_id
        JOIN
            `tabBlock` AS block ON block.name = hh.block_id
        JOIN
            `tabGram Panchayat` AS gp ON gp.name = hh.gp_id
        JOIN
            `tabVillage` AS village ON village.name = hh.village_id
        JOIN
            `tabGender` AS gender ON gender.name = hh.respondent_gender_id
        JOIN
            `tabSocial Category` AS sc ON sc.name = hh.social_category_id
        JOIN
            `tabPrimary Occupation` AS po ON po.name = hh.primary_occupation_id
        JOIN
            `tabVerfication Status` AS vs ON vs.name = hh.verification_status
        JOIN
            `tabGender` AS child_gender ON child_gender.name = hhc.gender_id
        JOIN
            `tabRelation` AS relation ON relation.name = hhc.relationship_with_child
        WHERE
            1 = 1 {conditions}
        ORDER BY
            P.partner_name, state.state_name ASC
    """
    data = frappe.db.sql(sql_query, as_dict=True)
    return data
