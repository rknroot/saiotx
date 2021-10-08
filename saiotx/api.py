# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def get_employee_info():
    employee_doc = frappe.db.get_list("Employee",filters={"user_id":frappe.session.user},fields=["name"])

    if employee_doc:
        checks = frappe.db.sql("""
            SELECT time,log_type 
            FROM `tabEmployee Checkin`
            WHERE employee = '{employee}'
                AND time like "{date}%"
        """.format(employee=employee_doc[0].get('name'),
                    date=frappe.utils.today()),as_dict=1)

        if checks:
            return checks


    return None