# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class TreatmentNRCchildtable(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		name: DF.Int | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		treatment_nrc_child_table_hi: DF.Data | None
		treatment_nrc_child_table_od: DF.Data | None
		treatment_nrc_select: DF.Link | None
	# end: auto-generated types

	pass
