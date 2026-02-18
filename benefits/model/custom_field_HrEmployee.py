from odoo import fields, models

class CustomFieldHrEmployee(models.Model):
    _inherit = 'hr.employee'

    dashboard_id = fields.One2many(
        'benefits.dashboard',
        'employee_id',
        string='Benefits Dashboard'
    )

    benefits_total = fields.Monetary(string='Benefits Total', related='dashboard_id.total', currency_field='company_currency_id', readonly=True)

    company_currency_id = fields.Many2one(related='company_id.currency_id',readonly=True)

    show_benefits = fields.Boolean(compute='_compute_show_benefits')

    @api.depends('user_id')
    def _compute_show_benefits(self):
        for record in self:
            record.show_benefits = (
                    record.user_id == self.env.user
                    or self.env.user.has_group('hr.group_hr_manager')
            )