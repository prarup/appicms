# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HygieneYesNo(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		add_yes_no: DF.Data | None
		hygiene_yesno_hi: DF.Data | None
		hygiene_yesno_od: DF.Data | None
		name: DF.Int | None
	# end: auto-generated types

	pass
