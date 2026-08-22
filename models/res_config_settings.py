from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    pos_default_numpad_mode = fields.Selection(
        related="pos_config_id.default_numpad_mode",
        readonly=False,
    )
