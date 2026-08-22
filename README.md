# POS Default Numpad Mode

Free addon tested on Odoo 18 Community that lets an administrator choose which
native numpad mode is initially selected for each Point of Sale configuration.

## Features

- Quantity, Price, or Discount as the initial mode
- Quantity remains the default for existing and new POS configurations
- Independent setting for each Point of Sale
- Native cashier switching remains unchanged after initialization
- No replacement numpad, external library, or external service

## Installation

1. Add this addon directory to the Odoo addons path.
2. Update the Apps list.
3. Install **POS Default Numpad Mode**.

## Configuration

Open **Point of Sale > Configuration > Settings**, select a Point of Sale, then
set **Default Numpad Mode** in the **PoS Interface** section.

## Usage

Open the configured POS and add or select the first order line. The configured
mode is selected when the native numpad first appears. Cashiers can then switch
between Quantity, Price, and Discount normally, subject to standard Odoo access
rights and POS settings.

## Compatibility and dependencies

- Odoo 18.0 Community Edition tested
- Self-hosted Odoo or Odoo.sh with custom addon support
- Technical dependency: `point_of_sale`
- No external Python libraries or services

Odoo Online SaaS does not support installing this custom Python/JavaScript
addon.

## Troubleshooting

After installation or upgrade, refresh the browser assets before reopening the
POS if an older frontend bundle is still cached.

## License

LGPL-3
