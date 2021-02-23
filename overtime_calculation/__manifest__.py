# -*- coding: utf-8 -*-
{
    'name': 'Hr Overtime Calculation',
    'version': '13.0.1.0.0',
    'summary': 'Overtime Calculation',
    'description': """
        Helps you to Calculate Overtime.
        """,
    'category': 'Generic Modules/Human Resources',
    'depends': [
        'base', 'hr', 'project', 'hr_payroll_community'
    ],

    'data': [
        'views/payroll_inherit.xml'
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
