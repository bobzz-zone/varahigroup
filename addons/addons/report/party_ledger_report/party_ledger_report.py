# Copyright (c) 2013, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Posting Date:Date:200","Name:Data:200","Total:Currency:200","Summary:Text:400","AWB No:Data:200","Type:Data:200","Voucher No:Data:200"], []
	keyword=""
	if filters.get("name") and filters.get("name")!="":
		keyword=filters.get("name")
	if filters.get("type")=="Customer":
		data=frappe.db.sql("""select dn.posting_date,dn.customer_name,dn.base_grand_total,group_concat(di.item_code," -> ",di.item_name," = ",di.qty), dn.awb_no,"Delivery Note",dn.name 
				from `tabDelivery Note` dn left join `tabDelivery Note Item` di on di.parent=dn.name 
				where dn.posting_date between "{0}" and "{1}" and (dn.customer like "%{2}%" or dn.customer_name like "%{2}%") group by dn.name 
			""".format(filters.get("from"),filters.get("to"),keyword),as_list=1)
	if filters.get("type")=="Supplier":
		data=frappe.db.sql("""select pr.posting_date,pr.supplier_name,pr.base_grand_total,group_concat(pi.item_code," -> ",pi.item_name," = ",pi.qty), pr.awb_no,"Purchase Receipt",pr.name 
				from `tabPurchase Receipt` pr left join `tabPurchase Receipt Item` pi on pi.parent=pr.name 
				where pr.posting_date between "{0}" and "{1}" and (pr.supplier like "%{2}%" or pr.supplier_name like "%{2}%") group by pr.name 
			""".format(filters.get("from"),filters.get("to"),keyword),as_list=1)
	if filters.get("type")=="All":
		data=frappe.db.sql("""select * from (select dn.posting_date,dn.customer_name,dn.base_grand_total,group_concat(di.item_code," -> ",di.item_name," = ",di.qty), dn.awb_no,"Delivery Note",dn.name 
				from `tabDelivery Note` dn left join `tabDelivery Note Item` di on di.parent=dn.name 
				where dn.posting_date between "{0}" and "{1}" and (dn.customer like "%{2}%" or dn.customer_name like "%{2}%") group by dn.name 
				UNION
				select pr.posting_date,pr.supplier_name,pr.base_grand_total,group_concat(pi.item_code," -> ",pi.item_name," = ",pi.qty), pr.awb_no,"Purchase Receipt",pr.name 
				from `tabPurchase Receipt` pr left join `tabPurchase Receipt Item` pi on pi.parent=pr.name 
				where pr.posting_date between "{0}" and "{1}" and (pr.supplier like "%{2}%" or pr.supplier_name like "%{2}%") group by pr.name ) order by posting_date
			""".format(filters.get("from"),filters.get("to"),keyword),as_list=1)
	return columns, data