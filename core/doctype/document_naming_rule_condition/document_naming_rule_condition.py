# Copyright (c) 2020, Frappe Technologies and contributors
# License: MIT. See LICENSE

# import frappe
from frappe.model.document import Document


class DocumentNamingRuleCondition(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		condition: DF.Literal["=", "!=", ">", "<", ">=", "<="]
		document_naming_rule_condition_hi: DF.Data | None
		document_naming_rule_condition_od: DF.Data | None
		field: DF.Literal
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		value: DF.Data
	# end: auto-generated types

	pass