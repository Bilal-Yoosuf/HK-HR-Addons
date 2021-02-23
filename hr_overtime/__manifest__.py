# -*- coding: utf-8 -*-
{
    'name': 'Hr Overtime',
    'version': '13.0.1.0.0',
    'summary': 'Manage Employee Overtime',
    'description': """
        Helps you to manage Employee Overtime.
        """,
    'category': 'Generic Modules/Human Resources',
    'depends': [
        'base', 'hr', 'hr_contract','hr_attendance', 'hr_holidays', 'project','hr_payroll_community'
    ],
    'external_dependencies': {
        'python': ['pandas'],
    },
    'data': [

        'data/data.xml',
        'views/overtime_request_view.xml',
        'views/overtime_type.xml',
        'views/hr_contract.xml',
        # 'views/hr_payslip.xml',
        'security/ir.model.access.csv',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
