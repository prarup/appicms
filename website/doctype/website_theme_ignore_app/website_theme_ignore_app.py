# Copyright (c) 2020, Frappe Technologies and contributors
# License: MIT. See LICENSE

# import frappe
from frappe.model.document import Document


class WebsiteThemeIgnoreApp(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		app: DF.Data
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		website_theme_ignore_app_hi: DF.Data | None
		website_theme_ignore_app_od: DF.Data | None
	# end: auto-generated types

	pass
