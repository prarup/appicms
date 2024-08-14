# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Block(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		block_code: DF.Data
		block_name: DF.Data
		district_id: DF.Link
		is_active: DF.Check
		name: DF.Int | None
		state_id: DF.Link
	# end: auto-generated types

	pass
