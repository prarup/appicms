# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class WeightforageGirls(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		age_in_months: DF.Int
		green: DF.Float
		name: DF.Int | None
		red: DF.Float
		yellow_max: DF.Float
		yellow_min: DF.Float
	# end: auto-generated types

	pass
