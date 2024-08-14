# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Anganwadiimmunisation(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		add_immunization: DF.Data | None
		anganwadi_immunisation_hi: DF.Data | None
		anganwadi_immunisation_od: DF.Data | None
		name: DF.Int | None
	# end: auto-generated types

	pass
