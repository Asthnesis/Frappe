# Copyright (c) 2025, Edward Rasto and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
from frappe import _

class Transaction(Document):
    def validate(self):
        self.set_fee_and_status()
        self.validate_member_debt_limit()

    def set_fee_and_status(self):
        book = frappe.get_doc("Book", self.book)
        if self.transaction_type == "Issue":
            if book.qty_available <= 0:
                frappe.throw(_("'{0}' is not available for issue.").format(book.title))
            self.lending_status = "Issued"
            self.fee = 0
        elif self.transaction_type == "Return":
            self.lending_status = "Returned"
            self.fee = book.fee

    def validate_member_debt_limit(self):
        member = frappe.get_doc("Member", self.member)

        if self.transaction_type == "Issue":
            book = frappe.get_doc("Book", self.book)
            projected_debt = member.outstanding_amt + book.fee

            if projected_debt > 500:
                frappe.throw(_("Member '{0}' has exceeded the debt limit of 500. Outstanding amount: {1}. Projected debt: {2}.")
                .format(member.member_name, member.outstanding_amt, projected_debt))

    def on_submit(self):
        self.update_book_and_member_records()

    def update_book_and_member_records(self):
        book = frappe.get_doc("Book", self.book)
        member = frappe.get_doc("Member", self.member)

        if self.transaction_type == "Issue":
            book.qty_available -= 1
        elif self.transaction_type == "Return":
            book.qty_available += 1
            member.outstanding_amt += self.fee

        book.save()
        member.save()

    def on_cancel(self):
        book = frappe.get_doc("Book", self.book)
        member = frappe.get_doc("Member", self.member)

        if self.transaction_type == "Issue":
            book.qty_available += 1
        elif self.transaction_type == "Return":
            book.qty_available -= 1
            member.outstanding_amt -= self.fee

        book.save()
        member.save()
