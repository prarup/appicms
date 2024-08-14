# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RedFlagChildActiontaken(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		action_taken: DF.Data | None
		is_active: DF.Check
		name: DF.Int | None
		red_flag_child_action_taken_hi: DF.Data | None
		red_flag_child_action_taken_od: DF.Data | None
		seq_id: DF.Int
	# end: auto-generated types

	pass
