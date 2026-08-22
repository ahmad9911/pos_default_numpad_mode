{
    "name": "POS Default Numpad Mode",
    "version": "18.0.1.0.0",
    "category": "Point of Sale",
    "summary": "Choose Quantity, Price, or Discount as the initial POS numpad mode.",
    "author": "Optramo",
    "maintainer": "Optramo",
    "website": "https://optramo.com",
    "support": "hello@optramo.com",
    "license": "LGPL-3",
    "depends": ["point_of_sale"],
    "data": [
        "views/res_config_settings_views.xml",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_default_numpad_mode/static/src/app/store/pos_store.js",
        ],
    },
    "images": [
        "static/description/main_screenshot.png",
        "static/description/price_mode.png",
    ],
    "installable": True,
    "application": False,
}
