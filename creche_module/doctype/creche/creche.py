# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Creche(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.creche_module.doctype.creche_caregiver.creche_caregiver import CrecheCaregiver
		from frappe.types import DF

		app_created_by: DF.Data | None
		app_created_on: DF.Date | None
		app_updated_by: DF.Data | None
		app_updated_on: DF.Date | None
		block_id: DF.Link
		creche_caregiver_table: DF.Table[CrecheCaregiver]
		creche_closing_time: DF.Time | None
		creche_id: DF.Data | None
		creche_name: DF.Data
		creche_openning_time: DF.Time | None
		deleted_by: DF.Data | None
		deleted_on: DF.Date | None
		district_id: DF.Link
		gp_id: DF.Link
		is_active: DF.Check
		latitude: DF.Data | None
		longitude: DF.Data | None
		name: DF.Int | None
		partner_id: DF.Link
		state_id: DF.Link
		supervisor_id: DF.Link
		village_id: DF.Link
		weekly_holiday_id: DF.Link | None
	# end: auto-generated types

	pass
