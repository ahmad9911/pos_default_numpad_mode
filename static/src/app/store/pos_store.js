/** @odoo-module */

import { PosStore } from "@point_of_sale/app/store/pos_store";
import { patch } from "@web/core/utils/patch";

patch(PosStore.prototype, {
    async processServerData() {
        await super.processServerData(...arguments);
        this.numpadMode = this.config.default_numpad_mode || "quantity";
        this._defaultNumpadModePending = true;
    },
    async afterProcessServerData() {
        const result = await super.afterProcessServerData(...arguments);
        if (this.get_order()?.uiState.selected_orderline_uuid) {
            this._applyDefaultNumpadMode();
        }
        return result;
    },
    selectOrderLine(...args) {
        const result = super.selectOrderLine(...args);
        this._applyDefaultNumpadMode();
        return result;
    },
    _applyDefaultNumpadMode() {
        if (this._defaultNumpadModePending) {
            this.numpadMode = this.config.default_numpad_mode || "quantity";
            this._defaultNumpadModePending = false;
        }
    },
});
