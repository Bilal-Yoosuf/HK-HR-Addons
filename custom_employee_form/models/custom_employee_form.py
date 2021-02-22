# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CustomEmployeeForm(models.Model):
    _inherit = 'hr.employee'

    id_card_number = fields.Integer(string="ID Card Number", required=True)
    date_of_commencement = fields.Date("Date of Commencement", required=True)
    wage_period = fields.Char("Wage Period", required=True)
    wages_paid_in_period = fields.Integer("Wages Paid", required=True)
    total_hours_worked = fields.Integer("Total Hours Worked")
    annual_leave = fields.Integer("Annual Leaves Taken")
    annual_leave_payment = fields.Integer("Annual Leaves Payment")
    sick_leave = fields.Integer("Sick Leaves Taken")
    sick_leave_payment = fields.Integer("Sick Leaves Payment")
    maternity_leave = fields.Integer("Maternity Leaves Taken")
    maternity_leave_payment = fields.Integer("Maternity Leaves Payment")
    paternity_leave = fields.Integer("Paternity Leaves Taken")
    paternity_leave_payment = fields.Integer("Paternity Leaves Payment")
    holidays = fields.Integer("Holidays Taken")
    holidays_payment = fields.Integer("Holidays Payment")
    year_end_payment_amount = fields.Integer("Year End Payment Amount", required=True)
    year_end_payment_period = fields.Integer("Period")
    notice_period = fields.Char("Period of Notice", required=True)
    date_of_termination = fields.Date("Date of Termination of Contract", required=True)
