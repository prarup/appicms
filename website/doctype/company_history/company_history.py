# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

# License: MIT. See LICENSE

import frappe
from frappe.model.document import Document


class CompanyHistory(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		company_history_hi: DF.Data | None
		company_history_od: DF.Data | None
		highlight: DF.Text | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		year: DF.Data | None
	# end: auto-generated types

	pass
