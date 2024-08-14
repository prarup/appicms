# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class MoneyReceivedbyCaregiver(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		is_active: DF.Check
		money_received: DF.Data | None
		money_received_by_caregiver_hi: DF.Data | None
		money_received_by_caregiver_od: DF.Data | None
		name: DF.Int | None
		seq_id: DF.Int
	# end: auto-generated types

	pass