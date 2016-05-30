# Copyright (c) 2013, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Posting Date:Date:200","Name:Data:200","Total:Currency:200","Summary:Text:400","Type:Data:200","Voucher No:Data:200"], []
	data=frappe.db.sql("""select dn.posting_date,dn.customer_name,dn.base_grand_total,group_concat(di.item_code) ,group_concat(di.qty),dn.name 
			from `tabDelivery Note` dn left join `tabDelivery Note Item` di on di.parent=dn.name 
			where dn.posting_date between "{0}" and "{1}" and (dn.customer like "%{2}%" or dn.customer_name like "%{2}%") group by dn.name 
		""".format(filters.get("from"),filters.get("to"),filters.get("name")),as_list=1)
	return columns, data