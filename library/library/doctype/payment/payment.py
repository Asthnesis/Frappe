import frappe
from frappe.model.document import Document
from frappe import _

class Payment(Document):

    def on_submit(self):
        member = frappe.get_doc("Member", self.member)
        member.outstanding_amt -= self.amount
        member.save()

    def on_cancel(self):
        member = frappe.get_doc("Member", self.member)
        member.outstanding_amt += self.amount
        member.save()