// Copyright (c) 2016, bobzz.zone@gmail.com and contributors
// For license information, please see license.txt

frappe.query_reports["Party Ledger Report"] = {
	"filters": [
		{
			"fieldname":"from",
			"label": __("From Date"),
			"fieldtype": "Date",
			"width": "80",
			"reqd":1
		},
		{
			"fieldname":"to",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": get_today(),
			"reqd":1
		},
		{
			"fieldname":"name",
			"label": __("Name"),
			"fieldtype": "Data"
		},
		{
			"fieldname":"type",
			"label": __("Type"),
			"fieldtype": "Select",
			"options":["All","Customer","Supplier"],
			"default":"All"
		}
	]
}
