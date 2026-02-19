{
    "name": "Benefits for employee",
    "version": "1.0.0",
    "category": "Human Resources",
    "summary": "benefits for you",
    "description": "benefits for your employee",
    "author": "Anton Titenko",
    "website": "https://example.com",
    "license": "LGPL-3",
    'price': "0",
    'currency': 'USD',
    'images': ['static/description/icon.png'],
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
