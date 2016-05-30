# Copyright (c) 2013, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Posting Date:Date:200","Name:Data:200","Total:Currency:200","Summary:Text:400","Type:Data:200","Voucher No:Data:200"], []
	#data = frappe.db.sql("""select gl.posting_date,ifnull(dn.customer_name,pr.supplier_name),sum(gl.debit),  from `tabGL Entry` gl 
	#	left join `tabDelivery Note` dn on gl.voucher_type="Delivery Note" and gl.voucher_no =dn.name and (dn.customer like "%{0}%" or dn.customer_name like "%{0}%")
	#	left join `tabPurchase Receipt` pr on gl.voucher_type="Purchase Receipt" and gl.voucher_no =pr.name  and (pr.supplier like "%{0}%" or pr.supplier_name like "%{0}%") 
	#	where gl.voucher_type IN ("Purchase Receipt","Delivery Note") and gl.debit>0 group by gl.voucher_no
	#	""".format(filters.get("name")))
	#if filters.get("type")=="All":
	data=frappe.db.sql("""select dn.posting_date,dn.customer_name,dn.base_grand_total,concat(group_concat(concat(di.item_code,"->",di.item_name,"=",di.qty)),dn.awb_no) ,"Delivery Note",dn.name
			from `tabDelivery Note` dn left join `tabDelivery Note Item` di on di.parent=dn.name 
			where dn.posting_date between "{0}" and "{1}" and (dn.customer like "%{2}%" or dn.customer_name like "%{2}%") group by dn.name
		""".format(filters.get("from"),filters.get("to"),filters.get("name")),as_dict=1)
	return columns, data