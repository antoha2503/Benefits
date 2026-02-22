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
        ('waiting', 'Waiting'),
        ('done', 'Dono'),
        ('canceled', 'Canceled')
    ], default='waiting', tracking=True)
    dashboard_id = fields.Many2one('benefits.dashboard', ondelete='cascade')
    type_compensation = fields.Many2one('category.compensation', string='Compensation Type', required=True)


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
        # self.dashboard_id.write({'total':self.dashboard_id.total+self.amount})
        self.write({'state': 'canceled'})

    def action_done(self):
        self.write({'state': 'done'})

    def _apply_cancel_logic(self):
        self.dashboard_id.write({'total':self.dashboard_id.total + self.amount})

    def _apply_done_logic(self):
        pass

    def write(self, vals):
        if 'state' not in vals:
            return super().write(vals)

        for record in self:
            old_state = record.state
            new_state = vals['state']

            # если статус не меняется
            if old_state == new_state:
                continue

            # ❌ запрещаем менять финальные статусы
            if old_state in ['done', 'canceled']:
                raise UserError("Status is final and cannot be changed.")

            # ❌ разрешены только переходы из waiting
            if old_state != 'waiting':
                raise UserError("Invalid state transition.")

        res = super().write(vals)

        # применяем математику только для waiting → ...
        for record in self:
            if record.state == 'canceled':
                record.dashboard_id.total += record.amount

        return res

