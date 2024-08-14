# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Livesin(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		family_lives_in: DF.Data | None
		is_active: DF.Check
		lives_in_hi: DF.Data | None
		lives_in_od: DF.Data | None
		name: DF.Int | None
		seq_id: DF.Int
	# end: auto-generated types

	pass
