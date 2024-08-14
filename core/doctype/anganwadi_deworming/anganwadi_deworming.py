# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Anganwadideworming(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		add_deworming: DF.Data | None
		anganwadi_deworming_hi: DF.Data | None
		anganwadi_deworming_od: DF.Data | None
		name: DF.Int | None
	# end: auto-generated types

	pass
