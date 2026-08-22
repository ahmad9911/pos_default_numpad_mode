from odoo import fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    default_numpad_mode = fields.Selection(
        selection=[
            ("quantity", "Quantity"),
            ("price", "Price"),
            ("discount", "Discount"),
        ],
        string="Default Numpad Mode",
        default="quantity",
        required=True,
        help="Initially selected numpad function when the Point of Sale interface opens.",
    )
