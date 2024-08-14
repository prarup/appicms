# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Treatmentdetails(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		name: DF.Int | None
		treatment_detail: DF.Data | None
		treatment_details_hi: DF.Data | None
		treatment_details_od: DF.Data | None
	# end: auto-generated types

	pass
