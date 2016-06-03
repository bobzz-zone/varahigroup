# Copyright (c) 2013, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from addons.addons.report.accounts_receivable.accounts_receivable_detail import ReceivablePayableReport

def execute(filters=None):
		args = {
				"party_type": "Supplier",
				"naming_by": ["Buying Settings", "supp_master_name"],
		}
		return ReceivablePayableReport(filters).run(args)
