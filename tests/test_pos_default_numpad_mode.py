from odoo.tests.common import TransactionCase


class TestPosDefaultNumpadMode(TransactionCase):
    def test_default_and_available_modes(self):
        config = self.env["pos.config"].create(
            {"name": "Numpad Mode Test", "payment_method_ids": False}
        )

        self.assertEqual(config.default_numpad_mode, "quantity")

        for mode in ("quantity", "price", "discount"):
            config.default_numpad_mode = mode
            self.assertEqual(config.default_numpad_mode, mode)

        with self.assertRaises(ValueError):
            config.default_numpad_mode = "invalid"

    def test_settings_field_updates_selected_pos(self):
        config = self.env["pos.config"].create(
            {"name": "Settings Numpad Mode Test", "payment_method_ids": False}
        )
        settings = self.env["res.config.settings"].create(
            {
                "pos_config_id": config.id,
                "pos_default_numpad_mode": "discount",
            }
        )

        self.assertEqual(settings.pos_default_numpad_mode, "discount")
        self.assertEqual(config.default_numpad_mode, "discount")

    def test_each_pos_loads_its_own_mode(self):
        quantity_config = self.env["pos.config"].create(
            {
                "name": "Quantity POS",
                "payment_method_ids": False,
                "default_numpad_mode": "quantity",
            }
        )
        price_config = self.env["pos.config"].create(
            {
                "name": "Price POS",
                "payment_method_ids": False,
                "default_numpad_mode": "price",
            }
        )

        def loaded_mode(config):
            data = {"pos.session": {"data": [{"config_id": config.id}]}}
            return config._load_pos_data(data)["data"][0]["default_numpad_mode"]

        self.assertEqual(loaded_mode(quantity_config), "quantity")
        self.assertEqual(loaded_mode(price_config), "price")
