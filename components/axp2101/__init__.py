import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c
from esphome.const import CONF_ID


DEPENDENCIES = ["i2c"]
CODEOWNERS = ["@m5stack"]

CONF_AXP2101_ID = "axp2101_id"
CONF_DISABLE_WATCHDOG = "disable_watchdog"
CONF_DISABLE_POWER_RAIL_CHANGES = "disable_power_rail_changes"

axp2101_ns = cg.esphome_ns.namespace("axp2101")
AXP2101 = axp2101_ns.class_("AXP2101", cg.Component, i2c.I2CDevice)


BASE_SCHEMA = cv.Schema({
    cv.GenerateID(CONF_AXP2101_ID): cv.use_id(AXP2101),
})

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(AXP2101),
            cv.Optional(CONF_DISABLE_WATCHDOG, default=False): cv.boolean,
            cv.Optional(CONF_DISABLE_POWER_RAIL_CHANGES, default=False): cv.boolean,
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
    .extend(i2c.i2c_device_schema(0x34))
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)
    cg.add(var.set_disable_watchdog(config[CONF_DISABLE_WATCHDOG]))
    cg.add(var.set_disable_power_rail_changes(config[CONF_DISABLE_POWER_RAIL_CHANGES]))
