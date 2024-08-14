# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ChildFollowup(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		any_other_illness: DF.Data | None
		app_updated_by: DF.Data | None
		app_updated_on: DF.Datetime | None
		appcreated_by: DF.Data | None
		appcreated_on: DF.Datetime | None
		block_id: DF.Link
		child_followup_guid: DF.Data | None
		child_id: DF.Link | None
		child_referral_guid: DF.Data | None
		childenrolledguid: DF.Data | None
		creche_id: DF.Link
		district_id: DF.Link
		followup_visit_date: DF.Date
		gp_id: DF.Link
		height: DF.Float
		name: DF.Int | None
		partner_id: DF.Link
		recoverd: DF.Link
		schedule_next_visit: DF.Link
		state_id: DF.Link
		village_id: DF.Link
		weight: DF.Float
	# end: auto-generated types

	pass
