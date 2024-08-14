# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class WeighttoHeightBoys(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		green: DF.Float
		height: DF.Float
		length: DF.Float
		name: DF.Int | None
		red: DF.Float
		weight_to_height_boys_hi: DF.Data | None
		weight_to_height_boys_od: DF.Data | None
		yellow_max: DF.Float
		yellow_min: DF.Float
	# end: auto-generated types

	pass
