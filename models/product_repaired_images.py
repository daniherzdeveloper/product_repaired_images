from odoo import models, fields, api

class RepairedOrderInherit(models.Model):
    _inherit = 'repair.order'

    repair_template_image_ids = fields.One2many('repair.order.image', 'repair_tmpl_id', string="Extra Repair Media", copy=True)

class RepairImage(models.Model):
    _name = 'repair.order.image'
    _description = "Repair Image"
    _inherit = ['image.mixin']
    _order = 'sequence, id'

    name = fields.Char("Name", required=True)
    sequence = fields.Integer(default=10)

    image_1920 = fields.Image()

    repair_tmpl_id = fields.Many2one('repair.order', "Repair", index=True, ondelete='cascade')
