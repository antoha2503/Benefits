{
    "name": "Benefits Dashboard",
    "version": "1.0.0",
    "category": "Human Resources",
    "summary": "The Benefits Dashboard module allows companies to automatically allocate funds for employee benefits and submit reimbursement requests for expenses such as business trips, health, education, and other corporate perks. Everything is managed directly in Odoo, easily and transparently.",
    "description": "The Benefits Dashboard module allows companies to automatically allocate funds for employee benefits and submit reimbursement requests for expenses such as business trips, health, education, and other corporate perks. Everything is managed directly in Odoo, easily and transparently.",
    "author": "Anton Tytenko",
    "website": "https://github.com/antoha2503",
    "license": "LGPL-3",
    'price': "0",
    'currency': 'USD',
    'images': ['static/description/icon_screenshot.png
'],
    "depends": [
        "base",
        "purchase"
    ],
    "data": [
        "views/add_benefits_employee.xml",
        'views/request_benefits_employee.xml',
        'views/custom_field_HrEmployee.xml',
        'views/create_user_compensation.xml',
        'views/benefits_for_employee.xml',
        'views/category_compensation.xml',
        'views/menu.xml',
        "views/ir_cron.xml",
        "security/ir.model.access.csv"
    ],
    "installable": True,
    "auto_install": False,
}
