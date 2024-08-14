# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

# License: MIT. See LICENSE

import frappe
from frappe.model.document import Document


class WebsiteScript(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		javascript: DF.Code | None
		website_script_hi: DF.Data | None
		website_script_od: DF.Data | None
	# end: auto-generated types

	def on_update(self):
		"""clear cache"""
		frappe.clear_cache(user="Guest")

		from frappe.website.utils import clear_cache

		clear_cache()
