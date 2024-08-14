# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AttendeesDetails(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		attendees: DF.Link
		attendees_details_hi: DF.Data | None
		attendees_details_od: DF.Data | None
		name: DF.Int | None
		other_specify: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		yes_no: DF.Link | None
	# end: auto-generated types

	pass
