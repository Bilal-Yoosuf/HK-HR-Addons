# -*- coding: utf-8 -*-

from odoo import api, fields, models


class OverTimeFromTimesheet(models.Model):
    _inherit = 'hr.payslip'
    overtime = fields.Float(string="Over Time", related='employee_id.dummy_overtime')

    #
    # @api.depends('employee_id.dummy_overtime')
    # def _overtime(self):
    #     for rec in self:
    #         if rec.employee_id:
    #             employee = self.env['hr.employee'].search([])
    #             for line in employee:
    #                 if rec.employee_id.name == line.name:
    #                     rec.overtime = line.dummy_overtime
    #                     print('hi', rec.overtime)

    # overtime = fields.Float(compute="_get_overtime", store=True)
    # checked = fields.Boolean(default=False)
    # total_days = fields.Integer()

    # @api.depends('unit_amount')
    # def _get_overtime(self):
    #     for rec in self:
    # same_date = self.env['account.analytic.line'].search([('date', '=', rec.date)])
    # total_days = self.env['account.analytic.line'].search([]).date
    # total_days_count = len(set(total_days))
    # rec.total_days = total_days_count

    # for line in same_date:
    #     total_time += line.unit_amount
    # if total_time > 8.0:
    #     rec.overtime = total_time - 8.0
