from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Report"),
			"icon": "icon-list",
			"items": [
				{
					"type": "report",
					"name": "Party Ledger Report",
					"is_query_report": True,
					"doctype":"Account"
				},
			]
		}]