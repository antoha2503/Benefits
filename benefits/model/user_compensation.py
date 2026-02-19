from odoo import fields, models
from odoo.exceptions import UserError

class UserCompensation(models.Model):
    _name = 'user.compensation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'employee_id'

    employee_id = fields.Many2one('hr.employee')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)
    amount = fields.Monetary(currency_field='currency_id', readonly=False)
    state = fields.Selection([
        ('canceled', 'Canceled'),
        ('done', 'Dono'),
        ('waiting', 'Waiting')
    ], default='waiting', tracking=True)
    dashboard_id = fields.Many2one('benefits.dashboard', ondelete='cascade')
    type_compensation = fields.Many2one('category.compensation', string='Compensation Type', required=True)

    # import_file = fields.Binary('Import file')

    date_create = fields.Date(string='Date', default=fields.Date.context_today, readonly=True)

    # Поле для отображения прикрепленных файлов
    attachment_ids = fields.Many2many(
        'ir.attachment',
        relation='user_compensation_attachment_rel',
        column1='compensation_id',
        column2='attachment_id',
        compute='_compute_attachment_ids',
        string="Attachments"
    )

    def _compute_attachment_ids(self):
        for record in self:
            record.attachment_ids = self.env['ir.attachment'].search([
                ('res_model', '=', self._name),
                ('res_id', '=', record.id)
            ])

    def action_canceled(self):
        self.dashboard_id.write({'total':self.dashboard_id.total+self.amount})
        self.write({'state': 'canceled'})

    def action_done(self):
        self.write({'state': 'done'})
