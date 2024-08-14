# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AnthropromaticData(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		age_months: DF.Int
		any_medical_major_illness: DF.Check
		awc: DF.Check
		cgmguid: DF.Data | None
		chhguid: DF.Data | None
		child_id: DF.Link | None
		childenrollguid: DF.Data | None
		do_you_have_height_weight: DF.Link
		height: DF.Float
		height_for_age: DF.Float
		illness_id: DF.Data | None
		illness_multi: DF.Data | None
		illness_other: DF.Data | None
		measurement_equipment: DF.Link | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		thr: DF.Check
		vhsnd: DF.Check
		weight: DF.Float
		weight_for_age: DF.Float
		weight_for_height: DF.Float
	# end: auto-generated types

	pass
