# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CrecheStock(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		app_updated_by: DF.Data | None
		app_updated_on: DF.Data | None
		appcreated_by: DF.Data | None
		appcreated_on: DF.Data | None
		block_id: DF.Link
		closing_stock: DF.Float
		creche_id: DF.Link
		district_id: DF.Link
		gp_id: DF.Link
		month: DF.Link
		name: DF.Int | None
		opening_stock: DF.Float
		partner_id: DF.Link
		quantity_received: DF.Float
		sguid: DF.Data | None
		state_id: DF.Link
		stock_item: DF.Link
		usage: DF.Float
		village_id: DF.Link
		wastage: DF.Float
		year: DF.Link
	# end: auto-generated types

	pass
