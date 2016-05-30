from __future__ import unicode_literals
from frappe import _

def get_data():
	return [{
			"label": _("Billing"),
			"items": [
				{
					"type": "doctype",
					"name": "Sales Invoice",
					"description": _("Bills raised to Customers.")
				},
				{
					"type": "doctype",
					"name": "Purchase Invoice",
					"description": _("Bills raised by Suppliers.")
				},
				{
					"type": "doctype",
					"name": "Payment Request",
					"description": _("Payment Request")
				},
				
			]

		},
		{
			"label": _("Report"),
			"icon": "icon-list",
			"items": [
				{
					"type": "report",
					"name": "Party Ledger Report",
					"is_query_report": True,
					"doctype":"Account"
				},{
					"type": "report",
					"name": "Accounts Receivable",
					"doctype": "Sales Invoice",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Accounts Payable",
					"doctype": "Purchase Invoice",
					"is_query_report": True
				},
			]
		}]