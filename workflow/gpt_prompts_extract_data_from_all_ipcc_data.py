#  please note that the gpt_prompts_extract_data_from_all_ipcc_data.py file is not really a script but an input for the extract_data_from_all_ipcc_data.py script. it contains all the prompts and mappings that i used to get the data from chatgpt. i have left it in here so that you can see what i did, as wella s import and udpate the mappings when you need to.
residential_mapping = {
    # Coal mappings
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "01_coal$01_01_coking_coal"): ("1.A.4.b - Residential", "Coking Coal"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "01_coal$01_05_lignite"): ("1.A.4.b - Residential", "Lignite"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "01_coal$01_x_thermal_coal"): ("1.A.4.b - Residential", "Other Bituminous Coal"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "01_coal$x"): ("1.A.4.b - Residential", "Other Bituminous Coal"),
    
    # Coal products mappings
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "02_coal_products$x"): ("1.A.4.b - Residential", "Coke Oven Coke and Lignite Coke"),
    
    # Peat mappings
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "03_peat$x"): ("1.A.4.b - Residential", "Peat"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "04_peat_products$x"): ("1.A.4.b - Residential", "Peat"),
    
    # Petroleum products mappings
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "07_petroleum_products$07_01_motor_gasoline"): ("1.A.4.b - Residential", "Motor Gasoline"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "07_petroleum_products$07_02_aviation_gasoline"): ("1.A.4.b - Residential", "Aviation Gasoline"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "07_petroleum_products$07_03_naphtha"): ("1.A.4.b - Residential", "Naphtha"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "07_petroleum_products$07_06_kerosene"): ("1.A.4.b - Residential", "Other Kerosene"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "07_petroleum_products$07_07_gas_diesel_oil"): ("1.A.4.b - Residential", "Diesel Oil"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "07_petroleum_products$07_08_fuel_oil"): ("1.A.4.b - Residential", "Residual Fuel Oil"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "07_petroleum_products$07_09_lpg"): ("1.A.4.b - Residential", "Liquefied Petroleum Gases"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"): ("1.A.4.b - Residential", "Refinery Gas"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "07_petroleum_products$07_11_ethane"): ("1.A.4.b - Residential", "Ethane"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "07_petroleum_products$07_x_jet_fuel"): ("1.A.4.b - Residential", "Jet Kerosene"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "07_petroleum_products$07_x_other_petroleum_products"): ("1.A.4.b - Residential", "Other Petroleum Products"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "07_petroleum_products$x"): ("1.A.4.b - Residential", "Other Petroleum Products"),
    
    # Gas mappings
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "08_gas$08_01_natural_gas"): ("1.A.4.b - Residential", "Natural Gas"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "08_gas$08_02_lng"): ("1.A.4.b - Residential", "Natural Gas"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "08_gas$08_03_gas_works_gas"): ("1.A.4.b - Residential", "Gas Works Gas"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "08_gas$x"): ("1.A.4.b - Residential", "Natural Gas"),
    
    # Solid Biomass mappings
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "15_solid_biomass$15_01_fuelwood_and_woodwaste"): ("1.A.4.b - Residential", "Wood/Wood Waste"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "15_solid_biomass$15_02_bagasse"): ("1.A.4.b - Residential", "Other Primary Solid Biomass"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "15_solid_biomass$15_03_charcoal"): ("1.A.4.b - Residential", "Charcoal"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "15_solid_biomass$15_04_black_liquor"): ("1.A.4.b - Residential", "Sulphite Lyes (Black Liquor)"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "15_solid_biomass$15_05_other_biomass"): ("1.A.4.b - Residential", "Other Primary Solid Biomass"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "15_solid_biomass$x"): ("1.A.4.b - Residential", "Other Primary Solid Biomass"),
    
    # Other fuels mappings
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "16_others$16_01_biogas"): ("1.A.4.b - Residential", "Other Biogas"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "16_others$16_02_industrial_waste"): ("1.A.4.b - Residential", "Industrial Wastes"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "16_others$16_03_municipal_solid_waste_renewable"): ("1.A.4.b - Residential", "Municipal Wastes (biomass fraction)"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "16_others$16_04_municipal_solid_waste_nonrenewable"): ("1.A.4.b - Residential", "Municipal Wastes (non-biomass fraction)"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "16_others$16_05_biogasoline"): ("1.A.4.b - Residential", "Biogasoline"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "16_others$16_06_biodiesel"): ("1.A.4.b - Residential", "Biodiesels"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "16_others$16_07_bio_jet_kerosene"): ("1.A.4.b - Residential", "Other Liquid Biofuels"),
    ("16_other_sector$16_01_buildings$16_01_02_residential$x", "16_others$16_08_other_liquid_biofuels"): ("1.A.4.b - Residential", "Other Liquid Biofuels"),
}

transport_mapping = {
    # Coal mappings
    ("15_transport_sector$15_03_rail$x$x", "01_coal$01_01_coking_coal"): ("1.A.3.c - Railways", "Sub-Bituminous Coal"),
    ("15_transport_sector$15_04_domestic_navigation$x$x", "01_coal$01_01_coking_coal"): ("1.A.1 - Energy Industries", "Coking Coal"),
    ("15_transport_sector$x$x$x", "01_coal$01_01_coking_coal"): ("1.A.1 - Energy Industries", "Coking Coal"),
    ("15_transport_sector$15_03_rail$x$x", "01_coal$01_05_lignite"): ("1.A.3.c - Railways", "Sub-Bituminous Coal"),
    ("15_transport_sector$x$x$x", "01_coal$01_05_lignite"): ("1.A.1 - Energy Industries", "Lignite"),
    ("15_transport_sector$15_03_rail$x$x", "01_coal$01_x_thermal_coal"): ("1.A.3.c - Railways", "Sub-Bituminous Coal"),
    ("15_transport_sector$15_04_domestic_navigation$x$x", "01_coal$01_x_thermal_coal"): ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    ("15_transport_sector$15_06_nonspecified_transport$x$x", "01_coal$01_x_thermal_coal"): ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    ("15_transport_sector$x$x$x", "01_coal$01_x_thermal_coal"): ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    ("15_transport_sector$15_03_rail$x$x", "01_coal$x"): ("1.A.3.c - Railways", "Sub-Bituminous Coal"),
    ("15_transport_sector$15_04_domestic_navigation$x$x", "01_coal$x"): ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    ("15_transport_sector$15_06_nonspecified_transport$x$x", "01_coal$x"): ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    ("15_transport_sector$x$x$x", "01_coal$x"): ("1.A.1 - Energy Industries", "Other Bituminous Coal"),

    # Coal products mappings
    ("15_transport_sector$15_03_rail$x$x", "02_coal_products$x"): ("1.A.3.c - Railways", "Sub-Bituminous Coal"),
    ("15_transport_sector$15_04_domestic_navigation$x$x", "02_coal_products$x"): ("1.A.1 - Energy Industries", "Coke Oven Coke and Lignite Coke"),
    ("15_transport_sector$x$x$x", "02_coal_products$x"): ("1.A.1 - Energy Industries", "Coke Oven Coke and Lignite Coke"),

    # Crude oil and NGL mappings
    ("15_transport_sector$15_05_pipeline_transport$x$x", "06_crude_oil_and_ngl$06_01_crude_oil"): ("1.A.1 - Energy Industries", "Crude Oil"),
    ("15_transport_sector$15_06_nonspecified_transport$x$x", "06_crude_oil_and_ngl$06_01_crude_oil"): ("1.A.1 - Energy Industries", "Crude Oil"),
    ("15_transport_sector$x$x$x", "06_crude_oil_and_ngl$06_01_crude_oil"): ("1.A.1 - Energy Industries", "Crude Oil"),
    ("15_transport_sector$15_02_road$x$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"): ("1.A.1 - Energy Industries", "Natural Gas Liquids (NGLs)"),
    ("15_transport_sector$x$x$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"): ("1.A.1 - Energy Industries", "Natural Gas Liquids (NGLs)"),
    ("15_transport_sector$15_02_road$x$x", "06_crude_oil_and_ngl$x"): ("1.A.1 - Energy Industries", "Crude Oil"),
    ("15_transport_sector$15_05_pipeline_transport$x$x", "06_crude_oil_and_ngl$x"): ("1.A.1 - Energy Industries", "Crude Oil"),
    ("15_transport_sector$15_06_nonspecified_transport$x$x", "06_crude_oil_and_ngl$x"): ("1.A.1 - Energy Industries", "Crude Oil"),
    ("15_transport_sector$x$x$x", "06_crude_oil_and_ngl$x"): ("1.A.1 - Energy Industries", "Crude Oil"),

    # Petroleum products - Motor Gasoline mappings
    ("15_transport_sector$15_01_domestic_air_transport$x$x", "07_petroleum_products$07_01_motor_gasoline"): ("1.A.3.a - Civil Aviation", "Motor Gasoline"),
    ("15_transport_sector$15_02_road$x$x", "07_petroleum_products$07_01_motor_gasoline"): ("1.A.3.b - Road Transportation", "Motor Gasoline"),
    ("15_transport_sector$15_03_rail$x$x", "07_petroleum_products$07_01_motor_gasoline"): ("1.A.3.c - Railways", "Motor Gasoline"),
    ("15_transport_sector$15_04_domestic_navigation$x$x", "07_petroleum_products$07_01_motor_gasoline"): ("1.A.3.d - Water-borne Navigation", "Motor Gasoline"),
    ("15_transport_sector$15_05_pipeline_transport$x$x", "07_petroleum_products$07_01_motor_gasoline"): ("1.A.1 - Energy Industries", "Motor Gasoline"),
    ("15_transport_sector$15_06_nonspecified_transport$x$x", "07_petroleum_products$07_01_motor_gasoline"): ("1.A.3.b - Road Transportation", "Motor Gasoline"),
    ("15_transport_sector$x$x$x", "07_petroleum_products$07_01_motor_gasoline"): ("1.A.3.b - Road Transportation", "Motor Gasoline"),

    # Petroleum products - Aviation Gasoline mappings
    ("15_transport_sector$15_01_domestic_air_transport$x$x", "07_petroleum_products$07_02_aviation_gasoline"): ("1.A.3.a - Civil Aviation", "Aviation Gasoline"),
    ("15_transport_sector$15_06_nonspecified_transport$x$x", "07_petroleum_products$07_02_aviation_gasoline"): ("1.A.3.a - Civil Aviation", "Aviation Gasoline"),
    ("15_transport_sector$x$x$x", "07_petroleum_products$07_02_aviation_gasoline"): ("1.A.3.a - Civil Aviation", "Aviation Gasoline"),

    # Petroleum products - Kerosene mappings
    ("15_transport_sector$15_01_domestic_air_transport$x$x", "07_petroleum_products$07_06_kerosene"): ("1.A.3.a - Civil Aviation", "Jet Kerosene"),
    ("15_transport_sector$15_02_road$x$x", "07_petroleum_products$07_06_kerosene"): ("1.A.3.b - Road Transportation", "Other Kerosene"),
    ("15_transport_sector$15_03_rail$x$x", "07_petroleum_products$07_06_kerosene"): ("1.A.3.c - Railways", "Other Kerosene"),
    ("15_transport_sector$15_04_domestic_navigation$x$x", "07_petroleum_products$07_06_kerosene"): ("1.A.3.d - Water-borne Navigation", "Other Kerosene"),
    ("15_transport_sector$15_05_pipeline_transport$x$x", "07_petroleum_products$07_06_kerosene"): ("1.A.1 - Energy Industries", "Other Kerosene"),
    ("15_transport_sector$15_06_nonspecified_transport$x$x", "07_petroleum_products$07_06_kerosene"): ("1.A.3.b - Road Transportation", "Other Kerosene"),
    ("15_transport_sector$x$x$x", "07_petroleum_products$07_06_kerosene"): ("1.A.3.b - Road Transportation", "Other Kerosene"),

    # Petroleum products - Gas/Diesel Oil mappings
    ("15_transport_sector$15_01_domestic_air_transport$x$x", "07_petroleum_products$07_07_gas_diesel_oil"): ("1.A.3.a - Civil Aviation", "Diesel Oil"),
    ("15_transport_sector$15_02_road$x$x", "07_petroleum_products$07_07_gas_diesel_oil"): ("1.A.3.b - Road Transportation", "Diesel Oil"),
    ("15_transport_sector$15_03_rail$x$x", "07_petroleum_products$07_07_gas_diesel_oil"): ("1.A.3.c - Railways", "Diesel Oil"),
    ("15_transport_sector$15_04_domestic_navigation$x$x", "07_petroleum_products$07_07_gas_diesel_oil"): ("1.A.3.d - Water-borne Navigation", "Diesel Oil"),
    ("15_transport_sector$15_05_pipeline_transport$x$x", "07_petroleum_products$07_07_gas_diesel_oil"): ("1.A.1 - Energy Industries", "Diesel Oil"),
    ("15_transport_sector$15_06_nonspecified_transport$x$x", "07_petroleum_products$07_07_gas_diesel_oil"): ("1.A.3.b - Road Transportation", "Diesel Oil"),
    ("15_transport_sector$x$x$x", "07_petroleum_products$07_07_gas_diesel_oil"): ("1.A.3.b - Road Transportation", "Diesel Oil"),

    # Petroleum products - Fuel Oil mappings
    ("15_transport_sector$15_01_domestic_air_transport$x$x", "07_petroleum_products$07_08_fuel_oil"): ("1.A.3.a - Civil Aviation", "Residual Fuel Oil"),
    ("15_transport_sector$15_02_road$x$x", "07_petroleum_products$07_08_fuel_oil"): ("1.A.3.b - Road Transportation", "Residual Fuel Oil"),
    ("15_transport_sector$15_03_rail$x$x", "07_petroleum_products$07_08_fuel_oil"): ("1.A.3.c - Railways", "Residual Fuel Oil"),
    ("15_transport_sector$15_04_domestic_navigation$x$x", "07_petroleum_products$07_08_fuel_oil"): ("1.A.3.d - Water-borne Navigation", "Residual Fuel Oil"),
    ("15_transport_sector$15_05_pipeline_transport$x$x", "07_petroleum_products$07_08_fuel_oil"): ("1.A.1 - Energy Industries", "Residual Fuel Oil"),
    ("15_transport_sector$15_06_nonspecified_transport$x$x", "07_petroleum_products$07_08_fuel_oil"): ("1.A.3.b - Road Transportation", "Residual Fuel Oil"),
    ("15_transport_sector$x$x$x", "07_petroleum_products$07_08_fuel_oil"): ("1.A.3.b - Road Transportation", "Residual Fuel Oil"),

    # Petroleum products - LPG mappings
    ("15_transport_sector$15_01_domestic_air_transport$x$x", "07_petroleum_products$07_09_lpg"): ("1.A.3.a - Civil Aviation", "Liquefied Petroleum Gases"),
    ("15_transport_sector$15_02_road$x$x", "07_petroleum_products$07_09_lpg"): ("1.A.3.b - Road Transportation", "Liquefied Petroleum Gases"),
    ("15_transport_sector$15_03_rail$x$x", "07_petroleum_products$07_09_lpg"): ("1.A.3.c - Railways", "Liquefied Petroleum Gases"),
    ("15_transport_sector$15_04_domestic_navigation$x$x", "07_petroleum_products$07_09_lpg"): ("1.A.3.d - Water-borne Navigation", "Liquefied Petroleum Gases"),
    ("15_transport_sector$15_05_pipeline_transport$x$x", "07_petroleum_products$07_09_lpg"): ("1.A.1 - Energy Industries", "Liquefied Petroleum Gases"),
    ("15_transport_sector$15_06_nonspecified_transport$x$x", "07_petroleum_products$07_09_lpg"): ("1.A.3.b - Road Transportation", "Liquefied Petroleum Gases"),
    ("15_transport_sector$x$x$x", "07_petroleum_products$07_09_lpg"): ("1.A.3.b - Road Transportation", "Liquefied Petroleum Gases"),

    # Petroleum products - Jet Fuel mappings
    ("15_transport_sector$15_01_domestic_air_transport$x$x", "07_petroleum_products$07_x_jet_fuel"): ("1.A.3.a - Civil Aviation", "Jet Kerosene"),
    ("15_transport_sector$15_06_nonspecified_transport$x$x", "07_petroleum_products$07_x_jet_fuel"): ("1.A.3.a - Civil Aviation", "Jet Kerosene"),
    ("15_transport_sector$x$x$x", "07_petroleum_products$07_x_jet_fuel"): ("1.A.3.a - Civil Aviation", "Jet Kerosene"),

    # Petroleum products - Other Petroleum Products mappings
    ("15_transport_sector$15_02_road$x$x", "07_petroleum_products$07_x_other_petroleum_products"): ("1.A.3.b - Road Transportation", "Other Petroleum Products"),
    ("15_transport_sector$15_03_rail$x$x", "07_petroleum_products$07_x_other_petroleum_products"): ("1.A.3.c - Railways", "Other Petroleum Products"),
    ("15_transport_sector$15_04_domestic_navigation$x$x", "07_petroleum_products$07_x_other_petroleum_products"): ("1.A.3.d - Water-borne Navigation", "Other Petroleum Products"),
    ("15_transport_sector$15_06_nonspecified_transport$x$x", "07_petroleum_products$07_x_other_petroleum_products"): ("1.A.3.b - Road Transportation", "Other Petroleum Products"),
    ("15_transport_sector$x$x$x", "07_petroleum_products$07_x_other_petroleum_products"): ("1.A.3.b - Road Transportation", "Other Petroleum Products"),

    # Petroleum products - Unspecified mappings
    ("15_transport_sector$15_01_domestic_air_transport$x$x", "07_petroleum_products$x"): ("1.A.3.a - Civil Aviation", "Jet Kerosene"),
    ("15_transport_sector$15_02_road$x$x", "07_petroleum_products$x"): ("1.A.3.b - Road Transportation", "Motor Gasoline"),
    ("15_transport_sector$15_03_rail$x$x", "07_petroleum_products$x"): ("1.A.3.c - Railways", "Diesel Oil"),
    ("15_transport_sector$15_04_domestic_navigation$x$x", "07_petroleum_products$x"): ("1.A.3.d - Water-borne Navigation", "Diesel Oil"),
    ("15_transport_sector$15_05_pipeline_transport$x$x", "07_petroleum_products$x"): ("1.A.1 - Energy Industries", "Diesel Oil"),
    ("15_transport_sector$15_06_nonspecified_transport$x$x", "07_petroleum_products$x"): ("1.A.3.b - Road Transportation", "Motor Gasoline"),
    ("15_transport_sector$x$x$x", "07_petroleum_products$x"): ("1.A.3.b - Road Transportation", "Motor Gasoline"),

    # Gas mappings
    ("15_transport_sector$15_02_road$x$x", "08_gas$08_01_natural_gas"): ("1.A.3.b - Road Transportation", "Natural Gas"),
    ("15_transport_sector$15_03_rail$x$x", "08_gas$08_01_natural_gas"): ("1.A.3.c - Railways", "Natural Gas"),
    ("15_transport_sector$15_05_pipeline_transport$x$x", "08_gas$08_01_natural_gas"): ("1.A.1 - Energy Industries", "Natural Gas"),
    ("15_transport_sector$15_06_nonspecified_transport$x$x", "08_gas$08_01_natural_gas"): ("1.A.3.b - Road Transportation", "Natural Gas"),
    ("15_transport_sector$x$x$x", "08_gas$08_01_natural_gas"): ("1.A.3.b - Road Transportation", "Natural Gas"),
    ("15_transport_sector$15_03_rail$x$x", "08_gas$08_03_gas_works_gas"): ("1.A.3.c - Railways", "Gas Works Gas"),
    ("15_transport_sector$x$x$x", "08_gas$08_03_gas_works_gas"): ("1.A.1 - Energy Industries", "Gas Works Gas"),
    ("15_transport_sector$15_02_road$x$x", "08_gas$x"): ("1.A.3.b - Road Transportation", "Natural Gas"),
    ("15_transport_sector$15_03_rail$x$x", "08_gas$x"): ("1.A.3.c - Railways", "Natural Gas"),
    ("15_transport_sector$15_05_pipeline_transport$x$x", "08_gas$x"): ("1.A.1 - Energy Industries", "Natural Gas"),
    ("15_transport_sector$15_06_nonspecified_transport$x$x", "08_gas$x"): ("1.A.3.b - Road Transportation", "Natural Gas"),
    ("15_transport_sector$x$x$x", "08_gas$x"): ("1.A.3.b - Road Transportation", "Natural Gas"),

    # Others - Biogasoline mappings
    ("15_transport_sector$15_02_road$x$x", "16_others$16_05_biogasoline"): ("1.A.3.b - Road Transportation", "Biogasoline"),
    ("15_transport_sector$x$x$x", "16_others$16_05_biogasoline"): ("1.A.3.b - Road Transportation", "Biogasoline"),

    # Others - Biodiesel mappings
    ("15_transport_sector$15_02_road$x$x", "16_others$16_06_biodiesel"): ("1.A.3.b - Road Transportation", "Biodiesels"),
    ("15_transport_sector$15_03_rail$x$x", "16_others$16_06_biodiesel"): ("1.A.3.c - Railways", "Biodiesels"),
    ("15_transport_sector$15_04_domestic_navigation$x$x", "16_others$16_06_biodiesel"): ("1.A.3.d - Water-borne Navigation", "Biodiesels"),
    ("15_transport_sector$15_06_nonspecified_transport$x$x", "16_others$16_06_biodiesel"): ("1.A.3.b - Road Transportation", "Biodiesels"),
    ("15_transport_sector$x$x$x", "16_others$16_06_biodiesel"): ("1.A.3.b - Road Transportation", "Biodiesels"),
}

industry_mapping = {
    # Construction Sector Mappings
    ("14_industry_sector$14_02_construction$x$x", "06_crude_oil_and_ngl$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),
    ("14_industry_sector$14_02_construction$x$x", "07_petroleum_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Petroleum Products"),

    # Manufacturing Sector Mappings
    # Iron and Steel Sector
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "06_crude_oil_and_ngl$x"):
        ("1.A.2.a - Iron and Steel", "Crude Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "07_petroleum_products$07_01_motor_gasoline"):
        ("1.A.2.a - Iron and Steel", "Motor Gasoline"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.2.a - Iron and Steel", "Other Kerosene"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.2.a - Iron and Steel", "Gas/Diesel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.2.a - Iron and Steel", "Residual Fuel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.2.a - Iron and Steel", "Liquefied Petroleum Gases"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"):
        ("1.A.2.a - Iron and Steel", "Refinery Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.2.a - Iron and Steel", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "07_petroleum_products$x"):
        ("1.A.2.a - Iron and Steel", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "08_gas$08_01_natural_gas"):
        ("1.A.2.a - Iron and Steel", "Natural Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "08_gas$08_03_gas_works_gas"):
        ("1.A.2.a - Iron and Steel", "Gas Works Gas"),

    # Chemical (including Petrochemical) Sector
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "06_crude_oil_and_ngl$x"):
        ("1.A.2.c - Chemicals", "Crude Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "07_petroleum_products$07_01_motor_gasoline"):
        ("1.A.2.c - Chemicals", "Motor Gasoline"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "07_petroleum_products$07_03_naphtha"):
        ("1.A.2.c - Chemicals", "Naphtha"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.2.c - Chemicals", "Other Kerosene"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.2.c - Chemicals", "Gas/Diesel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.2.c - Chemicals", "Residual Fuel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.2.c - Chemicals", "Liquefied Petroleum Gases"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"):
        ("1.A.2.c - Chemicals", "Refinery Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "07_petroleum_products$07_x_jet_fuel"):
        ("1.A.2.c - Chemicals", "Jet Kerosene"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.2.c - Chemicals", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "07_petroleum_products$x"):
        ("1.A.2.c - Chemicals", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "08_gas$08_01_natural_gas"):
        ("1.A.2.c - Chemicals", "Natural Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "08_gas$08_03_gas_works_gas"):
        ("1.A.2.c - Chemicals", "Gas Works Gas"),

    # Non-Ferrous Metals Sector
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "06_crude_oil_and_ngl$x"):
        ("1.A.2.b - Non-Ferrous Metals", "Crude Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "07_petroleum_products$07_01_motor_gasoline"):
        ("1.A.2.b - Non-Ferrous Metals", "Motor Gasoline"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "07_petroleum_products$07_03_naphtha"):
        ("1.A.2.b - Non-Ferrous Metals", "Naphtha"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.2.b - Non-Ferrous Metals", "Other Kerosene"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.2.b - Non-Ferrous Metals", "Gas/Diesel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.2.b - Non-Ferrous Metals", "Residual Fuel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.2.b - Non-Ferrous Metals", "Liquefied Petroleum Gases"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"):
        ("1.A.2.b - Non-Ferrous Metals", "Refinery Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.2.b - Non-Ferrous Metals", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "07_petroleum_products$x"):
        ("1.A.2.b - Non-Ferrous Metals", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "08_gas$08_01_natural_gas"):
        ("1.A.2.b - Non-Ferrous Metals", "Natural Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "08_gas$08_03_gas_works_gas"):
        ("1.A.2.b - Non-Ferrous Metals", "Gas Works Gas"),

    # Non-Metallic Mineral Products Sector
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "06_crude_oil_and_ngl$x"):
        ("1.A.2.f - Non-Metallic Minerals", "Crude Oil"),
    # Adding mappings for all fuels in this sector
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "07_petroleum_products$07_01_motor_gasoline"):
        ("1.A.2.f - Non-Metallic Minerals", "Motor Gasoline"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "07_petroleum_products$07_03_naphtha"):
        ("1.A.2.f - Non-Metallic Minerals", "Naphtha"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.2.f - Non-Metallic Minerals", "Other Kerosene"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.2.f - Non-Metallic Minerals", "Gas/Diesel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.2.f - Non-Metallic Minerals", "Residual Fuel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.2.f - Non-Metallic Minerals", "Liquefied Petroleum Gases"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"):
        ("1.A.2.f - Non-Metallic Minerals", "Refinery Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.2.f - Non-Metallic Minerals", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "07_petroleum_products$x"):
        ("1.A.2.f - Non-Metallic Minerals", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "08_gas$08_01_natural_gas"):
        ("1.A.2.f - Non-Metallic Minerals", "Natural Gas"),

    # Transportation Equipment Sector
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "06_crude_oil_and_ngl$x"):
        ("1.A.2.g - Transport Equipment", "Crude Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "07_petroleum_products$07_01_motor_gasoline"):
        ("1.A.2.g - Transport Equipment", "Motor Gasoline"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "07_petroleum_products$07_03_naphtha"):
        ("1.A.2.g - Transport Equipment", "Naphtha"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.2.g - Transport Equipment", "Other Kerosene"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.2.g - Transport Equipment", "Gas/Diesel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.2.g - Transport Equipment", "Residual Fuel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.2.g - Transport Equipment", "Liquefied Petroleum Gases"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"):
        ("1.A.2.g - Transport Equipment", "Refinery Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "07_petroleum_products$07_x_jet_fuel"):
        ("1.A.2.g - Transport Equipment", "Jet Kerosene"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.2.g - Transport Equipment", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "07_petroleum_products$x"):
        ("1.A.2.g - Transport Equipment", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "08_gas$08_01_natural_gas"):
        ("1.A.2.g - Transport Equipment", "Natural Gas"),

    # Machinery Sector
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "06_crude_oil_and_ngl$x"):
        ("1.A.2.h - Machinery", "Crude Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "07_petroleum_products$07_01_motor_gasoline"):
        ("1.A.2.h - Machinery", "Motor Gasoline"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "07_petroleum_products$07_03_naphtha"):
        ("1.A.2.h - Machinery", "Naphtha"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.2.h - Machinery", "Other Kerosene"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.2.h - Machinery", "Gas/Diesel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.2.h - Machinery", "Residual Fuel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.2.h - Machinery", "Liquefied Petroleum Gases"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"):
        ("1.A.2.h - Machinery", "Refinery Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.2.h - Machinery", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "07_petroleum_products$x"):
        ("1.A.2.h - Machinery", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "08_gas$08_01_natural_gas"):
        ("1.A.2.h - Machinery", "Natural Gas"),

    # Food, Beverages, and Tobacco Sector
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "06_crude_oil_and_ngl$x"):
        ("1.A.2.e - Food Processing, Beverages and Tobacco", "Crude Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "07_petroleum_products$07_01_motor_gasoline"):
        ("1.A.2.e - Food Processing, Beverages and Tobacco", "Motor Gasoline"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "07_petroleum_products$07_03_naphtha"):
        ("1.A.2.e - Food Processing, Beverages and Tobacco", "Naphtha"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.2.e - Food Processing, Beverages and Tobacco", "Other Kerosene"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.2.e - Food Processing, Beverages and Tobacco", "Gas/Diesel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.2.e - Food Processing, Beverages and Tobacco", "Residual Fuel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.2.e - Food Processing, Beverages and Tobacco", "Liquefied Petroleum Gases"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"):
        ("1.A.2.e - Food Processing, Beverages and Tobacco", "Refinery Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.2.e - Food Processing, Beverages and Tobacco", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "07_petroleum_products$x"):
        ("1.A.2.e - Food Processing, Beverages and Tobacco", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "08_gas$08_01_natural_gas"):
        ("1.A.2.e - Food Processing, Beverages and Tobacco", "Natural Gas"),

    # Pulp, Paper, and Printing Sector
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "06_crude_oil_and_ngl$x"):
        ("1.A.2.d - Pulp, Paper and Print", "Crude Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "07_petroleum_products$07_01_motor_gasoline"):
        ("1.A.2.d - Pulp, Paper and Print", "Motor Gasoline"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "07_petroleum_products$07_03_naphtha"):
        ("1.A.2.d - Pulp, Paper and Print", "Naphtha"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.2.d - Pulp, Paper and Print", "Other Kerosene"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.2.d - Pulp, Paper and Print", "Gas/Diesel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.2.d - Pulp, Paper and Print", "Residual Fuel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.2.d - Pulp, Paper and Print", "Liquefied Petroleum Gases"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"):
        ("1.A.2.d - Pulp, Paper and Print", "Refinery Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.2.d - Pulp, Paper and Print", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "07_petroleum_products$x"):
        ("1.A.2.d - Pulp, Paper and Print", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "08_gas$08_01_natural_gas"):
        ("1.A.2.d - Pulp, Paper and Print", "Natural Gas"),

    # Wood and Wood Products Sector
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"):
        ("1.A.2.j - Wood and Wood Products", "Natural Gas Liquids (NGLs)"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "06_crude_oil_and_ngl$x"):
        ("1.A.2.j - Wood and Wood Products", "Crude Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "07_petroleum_products$07_01_motor_gasoline"):
        ("1.A.2.j - Wood and Wood Products", "Motor Gasoline"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.2.j - Wood and Wood Products", "Other Kerosene"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.2.j - Wood and Wood Products", "Gas/Diesel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.2.j - Wood and Wood Products", "Residual Fuel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.2.j - Wood and Wood Products", "Liquefied Petroleum Gases"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.2.j - Wood and Wood Products", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "07_petroleum_products$x"):
        ("1.A.2.j - Wood and Wood Products", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "08_gas$08_01_natural_gas"):
        ("1.A.2.j - Wood and Wood Products", "Natural Gas"),

    # Textiles and Leather Sector
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"):
        ("1.A.2.l - Textile and Leather", "Natural Gas Liquids (NGLs)"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "06_crude_oil_and_ngl$x"):
        ("1.A.2.l - Textile and Leather", "Crude Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "07_petroleum_products$07_01_motor_gasoline"):
        ("1.A.2.l - Textile and Leather", "Motor Gasoline"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "07_petroleum_products$07_03_naphtha"):
        ("1.A.2.l - Textile and Leather", "Naphtha"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.2.l - Textile and Leather", "Other Kerosene"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.2.l - Textile and Leather", "Gas/Diesel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.2.l - Textile and Leather", "Residual Fuel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.2.l - Textile and Leather", "Liquefied Petroleum Gases"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"):
        ("1.A.2.l - Textile and Leather", "Refinery Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.2.l - Textile and Leather", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "07_petroleum_products$x"):
        ("1.A.2.l - Textile and Leather", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "08_gas$08_01_natural_gas"):
        ("1.A.2.l - Textile and Leather", "Natural Gas"),

    # Non-specified Industry Sector
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"):
        ("1.A.2.m - Non-specified Industry", "Natural Gas Liquids (NGLs)"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "06_crude_oil_and_ngl$x"):
        ("1.A.2.m - Non-specified Industry", "Crude Oil"),
    # Include mappings for all the fuels
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "07_petroleum_products$07_01_motor_gasoline"):
        ("1.A.2.m - Non-specified Industry", "Motor Gasoline"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "07_petroleum_products$07_03_naphtha"):
        ("1.A.2.m - Non-specified Industry", "Naphtha"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.2.m - Non-specified Industry", "Other Kerosene"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.2.m - Non-specified Industry", "Gas/Diesel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.2.m - Non-specified Industry", "Residual Fuel Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.2.m - Non-specified Industry", "Liquefied Petroleum Gases"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"):
        ("1.A.2.m - Non-specified Industry", "Refinery Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "07_petroleum_products$07_x_jet_fuel"):
        ("1.A.2.m - Non-specified Industry", "Jet Kerosene"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.2.m - Non-specified Industry", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "07_petroleum_products$x"):
        ("1.A.2.m - Non-specified Industry", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "08_gas$08_01_natural_gas"):
        ("1.A.2.m - Non-specified Industry", "Natural Gas"),

    # Manufacturing (Unspecified) Sector
    ("14_industry_sector$14_03_manufacturing$x$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas Liquids (NGLs)"),
    ("14_industry_sector$14_03_manufacturing$x$x", "06_crude_oil_and_ngl$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),
    # Include mappings for all the fuels
    ("14_industry_sector$14_03_manufacturing$x$x", "07_petroleum_products$07_01_motor_gasoline"):
        ("1.A.2 - Manufacturing Industries and Construction", "Motor Gasoline"),
    ("14_industry_sector$14_03_manufacturing$x$x", "07_petroleum_products$07_03_naphtha"):
        ("1.A.2 - Manufacturing Industries and Construction", "Naphtha"),
    ("14_industry_sector$14_03_manufacturing$x$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Kerosene"),
    ("14_industry_sector$14_03_manufacturing$x$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.2 - Manufacturing Industries and Construction", "Gas/Diesel Oil"),
    ("14_industry_sector$14_03_manufacturing$x$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.2 - Manufacturing Industries and Construction", "Residual Fuel Oil"),
    ("14_industry_sector$14_03_manufacturing$x$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.2 - Manufacturing Industries and Construction", "Liquefied Petroleum Gases"),
    ("14_industry_sector$14_03_manufacturing$x$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"):
        ("1.A.2 - Manufacturing Industries and Construction", "Refinery Gas"),
    ("14_industry_sector$14_03_manufacturing$x$x", "07_petroleum_products$07_x_jet_fuel"):
        ("1.A.2 - Manufacturing Industries and Construction", "Jet Kerosene"),
    ("14_industry_sector$14_03_manufacturing$x$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$x$x", "07_petroleum_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Petroleum Products"),
    ("14_industry_sector$14_03_manufacturing$x$x", "08_gas$08_01_natural_gas"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas"),
    # Gas Works Gas mappings
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "08_gas$08_03_gas_works_gas"):
        ("1.A.2 - Manufacturing Industries and Construction", "Gas Works Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "08_gas$08_03_gas_works_gas"):
        ("1.A.2 - Manufacturing Industries and Construction", "Gas Works Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "08_gas$08_03_gas_works_gas"):
        ("1.A.2 - Manufacturing Industries and Construction", "Gas Works Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "08_gas$08_03_gas_works_gas"):
        ("1.A.2 - Manufacturing Industries and Construction", "Gas Works Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "08_gas$08_03_gas_works_gas"):
        ("1.A.2 - Manufacturing Industries and Construction", "Gas Works Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "08_gas$08_03_gas_works_gas"):
        ("1.A.2 - Manufacturing Industries and Construction", "Gas Works Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "08_gas$08_03_gas_works_gas"):
        ("1.A.2 - Manufacturing Industries and Construction", "Gas Works Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "08_gas$08_03_gas_works_gas"):
        ("1.A.2 - Manufacturing Industries and Construction", "Gas Works Gas"),
    ("14_industry_sector$14_03_manufacturing$x$x", "08_gas$08_03_gas_works_gas"):
        ("1.A.2 - Manufacturing Industries and Construction", "Gas Works Gas"),
    ("14_industry_sector$x$x$x", "08_gas$08_03_gas_works_gas"):
        ("1.A.2 - Manufacturing Industries and Construction", "Gas Works Gas"),

    # Unspecified Gas mappings (mapped to Natural Gas)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "08_gas$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas"),
    ("14_industry_sector$14_02_construction$x$x", "08_gas$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "08_gas$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "08_gas$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "08_gas$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "08_gas$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "08_gas$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "08_gas$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "08_gas$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "08_gas$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "08_gas$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "08_gas$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "08_gas$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas"),
    ("14_industry_sector$14_03_manufacturing$x$x", "08_gas$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas"),
    ("14_industry_sector$x$x$x", "08_gas$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas"),

    # Solid Biomass - Fuelwood and Wood Waste mappings
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "15_solid_biomass$15_01_fuelwood_and_woodwaste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Wood/Wood Waste"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "15_solid_biomass$15_01_fuelwood_and_woodwaste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Wood/Wood Waste"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "15_solid_biomass$15_01_fuelwood_and_woodwaste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Wood/Wood Waste"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "15_solid_biomass$15_01_fuelwood_and_woodwaste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Wood/Wood Waste"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "15_solid_biomass$15_01_fuelwood_and_woodwaste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Wood/Wood Waste"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "15_solid_biomass$15_01_fuelwood_and_woodwaste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Wood/Wood Waste"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "15_solid_biomass$15_01_fuelwood_and_woodwaste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Wood/Wood Waste"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "15_solid_biomass$15_01_fuelwood_and_woodwaste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Wood/Wood Waste"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "15_solid_biomass$15_01_fuelwood_and_woodwaste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Wood/Wood Waste"),
    ("14_industry_sector$14_03_manufacturing$x$x", "15_solid_biomass$15_01_fuelwood_and_woodwaste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Wood/Wood Waste"),
    ("14_industry_sector$x$x$x", "15_solid_biomass$15_01_fuelwood_and_woodwaste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Wood/Wood Waste"),

    # Solid Biomass - Bagasse mappings
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "15_solid_biomass$15_02_bagasse"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "15_solid_biomass$15_02_bagasse"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "15_solid_biomass$15_02_bagasse"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$x$x", "15_solid_biomass$15_02_bagasse"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$x$x$x", "15_solid_biomass$15_02_bagasse"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),

    # Solid Biomass - Charcoal mappings
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "15_solid_biomass$15_03_charcoal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Charcoal"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "15_solid_biomass$15_03_charcoal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Charcoal"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "15_solid_biomass$15_03_charcoal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Charcoal"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "15_solid_biomass$15_03_charcoal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Charcoal"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "15_solid_biomass$15_03_charcoal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Charcoal"),
    ("14_industry_sector$14_03_manufacturing$x$x", "15_solid_biomass$15_03_charcoal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Charcoal"),
    ("14_industry_sector$x$x$x", "15_solid_biomass$15_03_charcoal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Charcoal"),

    # Solid Biomass - Black Liquor mappings
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "15_solid_biomass$15_04_black_liquor"):
        ("1.A.2 - Manufacturing Industries and Construction", "Sulphite Lyes (Black Liquor)"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "15_solid_biomass$15_04_black_liquor"):
        ("1.A.2 - Manufacturing Industries and Construction", "Sulphite Lyes (Black Liquor)"),
    ("14_industry_sector$14_03_manufacturing$x$x", "15_solid_biomass$15_04_black_liquor"):
        ("1.A.2 - Manufacturing Industries and Construction", "Sulphite Lyes (Black Liquor)"),
    ("14_industry_sector$x$x$x", "15_solid_biomass$15_04_black_liquor"):
        ("1.A.2 - Manufacturing Industries and Construction", "Sulphite Lyes (Black Liquor)"),

    # Solid Biomass - Other Biomass mappings
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "15_solid_biomass$15_05_other_biomass"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_02_construction$x$x", "15_solid_biomass$15_05_other_biomass"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "15_solid_biomass$15_05_other_biomass"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "15_solid_biomass$15_05_other_biomass"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "15_solid_biomass$15_05_other_biomass"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "15_solid_biomass$15_05_other_biomass"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "15_solid_biomass$15_05_other_biomass"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "15_solid_biomass$15_05_other_biomass"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "15_solid_biomass$15_05_other_biomass"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "15_solid_biomass$15_05_other_biomass"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "15_solid_biomass$15_05_other_biomass"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "15_solid_biomass$15_05_other_biomass"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "15_solid_biomass$15_05_other_biomass"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$x$x", "15_solid_biomass$15_05_other_biomass"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$x$x$x", "15_solid_biomass$15_05_other_biomass"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),

    # Unspecified Solid Biomass mappings (mapped to Other Primary Solid Biomass)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "15_solid_biomass$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_02_construction$x$x", "15_solid_biomass$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "15_solid_biomass$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "15_solid_biomass$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "15_solid_biomass$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "15_solid_biomass$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "15_solid_biomass$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "15_solid_biomass$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "15_solid_biomass$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "15_solid_biomass$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "15_solid_biomass$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "15_solid_biomass$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "15_solid_biomass$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$14_03_manufacturing$x$x", "15_solid_biomass$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),
    ("14_industry_sector$x$x$x", "15_solid_biomass$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Primary Solid Biomass"),

    # Other Fuels - Biogas mappings
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "16_others$16_01_biogas"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Biogas"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "16_others$16_01_biogas"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Biogas"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "16_others$16_01_biogas"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Biogas"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "16_others$16_01_biogas"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Biogas"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "16_others$16_01_biogas"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Biogas"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "16_others$16_01_biogas"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Biogas"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "16_others$16_01_biogas"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Biogas"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "16_others$16_01_biogas"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Biogas"),
    ("14_industry_sector$14_03_manufacturing$x$x", "16_others$16_01_biogas"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Biogas"),
    ("14_industry_sector$x$x$x", "16_others$16_01_biogas"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Biogas"),

    # Other Fuels - Industrial Waste mappings
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "16_others$16_02_industrial_waste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Industrial Wastes"),
    ("14_industry_sector$14_02_construction$x$x", "16_others$16_02_industrial_waste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Industrial Wastes"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "16_others$16_02_industrial_waste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Industrial Wastes"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "16_others$16_02_industrial_waste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Industrial Wastes"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "16_others$16_02_industrial_waste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Industrial Wastes"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "16_others$16_02_industrial_waste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Industrial Wastes"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "16_others$16_02_industrial_waste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Industrial Wastes"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "16_others$16_02_industrial_waste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Industrial Wastes"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "16_others$16_02_industrial_waste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Industrial Wastes"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "16_others$16_02_industrial_waste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Industrial Wastes"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "16_others$16_02_industrial_waste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Industrial Wastes"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "16_others$16_02_industrial_waste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Industrial Wastes"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "16_others$16_02_industrial_waste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Industrial Wastes"),
    ("14_industry_sector$14_03_manufacturing$x$x", "16_others$16_02_industrial_waste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Industrial Wastes"),
    ("14_industry_sector$x$x$x", "16_others$16_02_industrial_waste"):
        ("1.A.2 - Manufacturing Industries and Construction", "Industrial Wastes"),

    # Other Fuels - Municipal Solid Waste (renewable) mappings
    ("14_industry_sector$14_02_construction$x$x", "16_others$16_03_municipal_solid_waste_renewable"):
        ("1.A.2 - Manufacturing Industries and Construction", "Municipal Wastes (biomass fraction)"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "16_others$16_03_municipal_solid_waste_renewable"):
        ("1.A.2 - Manufacturing Industries and Construction", "Municipal Wastes (biomass fraction)"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "16_others$16_03_municipal_solid_waste_renewable"):
        ("1.A.2 - Manufacturing Industries and Construction", "Municipal Wastes (biomass fraction)"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "16_others$16_03_municipal_solid_waste_renewable"):
        ("1.A.2 - Manufacturing Industries and Construction", "Municipal Wastes (biomass fraction)"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "16_others$16_03_municipal_solid_waste_renewable"):
        ("1.A.2 - Manufacturing Industries and Construction", "Municipal Wastes (biomass fraction)"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "16_others$16_03_municipal_solid_waste_renewable"):
        ("1.A.2 - Manufacturing Industries and Construction", "Municipal Wastes (biomass fraction)"),
    ("14_industry_sector$14_03_manufacturing$x$x", "16_others$16_03_municipal_solid_waste_renewable"):
        ("1.A.2 - Manufacturing Industries and Construction", "Municipal Wastes (biomass fraction)"),
    ("14_industry_sector$x$x$x", "16_others$16_03_municipal_solid_waste_renewable"):
        ("1.A.2 - Manufacturing Industries and Construction", "Municipal Wastes (biomass fraction)"),

    # Other Fuels - Municipal Solid Waste (non-renewable) mappings
    ("14_industry_sector$14_02_construction$x$x", "16_others$16_04_municipal_solid_waste_nonrenewable"):
        ("1.A.2 - Manufacturing Industries and Construction", "Municipal Wastes (non-biomass fraction)"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "16_others$16_04_municipal_solid_waste_nonrenewable"):
        ("1.A.2 - Manufacturing Industries and Construction", "Municipal Wastes (non-biomass fraction)"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "16_others$16_04_municipal_solid_waste_nonrenewable"):
        ("1.A.2 - Manufacturing Industries and Construction", "Municipal Wastes (non-biomass fraction)"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "16_others$16_04_municipal_solid_waste_nonrenewable"):
        ("1.A.2 - Manufacturing Industries and Construction", "Municipal Wastes (non-biomass fraction)"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "16_others$16_04_municipal_solid_waste_nonrenewable"):
        ("1.A.2 - Manufacturing Industries and Construction", "Municipal Wastes (non-biomass fraction)"),
    ("14_industry_sector$14_03_manufacturing$x$x", "16_others$16_04_municipal_solid_waste_nonrenewable"):
        ("1.A.2 - Manufacturing Industries and Construction", "Municipal Wastes (non-biomass fraction)"),
    ("14_industry_sector$x$x$x", "16_others$16_04_municipal_solid_waste_nonrenewable"):
        ("1.A.2 - Manufacturing Industries and Construction", "Municipal Wastes (non-biomass fraction)"),

    # Other Fuels - Biogasoline mappings
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "16_others$16_05_biogasoline"):
        ("1.A.2 - Manufacturing Industries and Construction", "Biogasoline"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "16_others$16_05_biogasoline"):
        ("1.A.2 - Manufacturing Industries and Construction", "Biogasoline"),
    ("14_industry_sector$14_03_manufacturing$x$x", "16_others$16_05_biogasoline"):
        ("1.A.2 - Manufacturing Industries and Construction", "Biogasoline"),
    ("14_industry_sector$x$x$x", "16_others$16_05_biogasoline"):
        ("1.A.2 - Manufacturing Industries and Construction", "Biogasoline"),

    # Other Fuels - Biodiesels mappings
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "16_others$16_06_biodiesel"):
        ("1.A.2 - Manufacturing Industries and Construction", "Biodiesels"),
    ("14_industry_sector$14_02_construction$x$x", "16_others$16_06_biodiesel"):
        ("1.A.2 - Manufacturing Industries and Construction", "Biodiesels"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "16_others$16_06_biodiesel"):
        ("1.A.2 - Manufacturing Industries and Construction", "Biodiesels"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "16_others$16_06_biodiesel"):
        ("1.A.2 - Manufacturing Industries and Construction", "Biodiesels"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "16_others$16_06_biodiesel"):
        ("1.A.2 - Manufacturing Industries and Construction", "Biodiesels"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "16_others$16_06_biodiesel"):
        ("1.A.2 - Manufacturing Industries and Construction", "Biodiesels"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "16_others$16_06_biodiesel"):
        ("1.A.2 - Manufacturing Industries and Construction", "Biodiesels"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "16_others$16_06_biodiesel"):
        ("1.A.2 - Manufacturing Industries and Construction", "Biodiesels"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "16_others$16_06_biodiesel"):
        ("1.A.2 - Manufacturing Industries and Construction", "Biodiesels"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "16_others$16_06_biodiesel"):
        ("1.A.2 - Manufacturing Industries and Construction", "Biodiesels"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "16_others$16_06_biodiesel"):
        ("1.A.2 - Manufacturing Industries and Construction", "Biodiesels"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "16_others$16_06_biodiesel"):
        ("1.A.2 - Manufacturing Industries and Construction", "Biodiesels"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "16_others$16_06_biodiesel"):
        ("1.A.2 - Manufacturing Industries and Construction", "Biodiesels"),
    ("14_industry_sector$14_03_manufacturing$x$x", "16_others$16_06_biodiesel"):
        ("1.A.2 - Manufacturing Industries and Construction", "Biodiesels"),
    ("14_industry_sector$x$x$x", "16_others$16_06_biodiesel"):
        ("1.A.2 - Manufacturing Industries and Construction", "Biodiesels"),

    # Other Fuels - Other Liquid Biofuels mappings
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "16_others$16_08_other_liquid_biofuels"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Liquid Biofuels"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "16_others$16_08_other_liquid_biofuels"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Liquid Biofuels"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "16_others$16_08_other_liquid_biofuels"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Liquid Biofuels"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "16_others$16_08_other_liquid_biofuels"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Liquid Biofuels"),
    ("14_industry_sector$14_03_manufacturing$x$x", "16_others$16_08_other_liquid_biofuels"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Liquid Biofuels"),
    ("14_industry_sector$x$x$x", "16_others$16_08_other_liquid_biofuels"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Liquid Biofuels"),
    
    # Coking Coal Mappings
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "01_coal$01_01_coking_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_02_construction$x$x", "01_coal$01_01_coking_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "01_coal$01_01_coking_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "01_coal$01_01_coking_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "01_coal$01_01_coking_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "01_coal$01_01_coking_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "01_coal$01_01_coking_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "01_coal$01_01_coking_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "01_coal$01_01_coking_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "01_coal$01_01_coking_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "01_coal$01_01_coking_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "01_coal$01_01_coking_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "01_coal$01_01_coking_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$x$x", "01_coal$01_01_coking_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$x$x$x", "01_coal$01_01_coking_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),

    # Lignite Mappings
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "01_coal$01_05_lignite"):
        ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_02_construction$x$x", "01_coal$01_05_lignite"):
        ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "01_coal$01_05_lignite"):
        ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "01_coal$01_05_lignite"):
        ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "01_coal$01_05_lignite"):
        ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "01_coal$01_05_lignite"):
        ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "01_coal$01_05_lignite"):
        ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "01_coal$01_05_lignite"):
        ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "01_coal$01_05_lignite"):
        ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "01_coal$01_05_lignite"):
        ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "01_coal$01_05_lignite"):
        ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "01_coal$01_05_lignite"):
        ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "01_coal$01_05_lignite"):
        ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$x$x", "01_coal$01_05_lignite"):
        ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$x$x$x", "01_coal$01_05_lignite"):
        ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),

    # Thermal Coal Mappings (mapped to Other Bituminous Coal)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "01_coal$01_x_thermal_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_02_construction$x$x", "01_coal$01_x_thermal_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "01_coal$01_x_thermal_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "01_coal$01_x_thermal_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "01_coal$01_x_thermal_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "01_coal$01_x_thermal_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "01_coal$01_x_thermal_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "01_coal$01_x_thermal_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "01_coal$01_x_thermal_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "01_coal$01_x_thermal_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "01_coal$01_x_thermal_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "01_coal$01_x_thermal_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "01_coal$01_x_thermal_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$x$x", "01_coal$01_x_thermal_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$x$x$x", "01_coal$01_x_thermal_coal"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),

    # Unspecified Coal Mappings (mapped to Other Bituminous Coal)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "01_coal$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_02_construction$x$x", "01_coal$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "01_coal$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "01_coal$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "01_coal$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "01_coal$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "01_coal$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "01_coal$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "01_coal$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "01_coal$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "01_coal$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "01_coal$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "01_coal$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$x$x", "01_coal$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$x$x$x", "01_coal$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),

    # Coal Products Mappings
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "02_coal_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coke Oven Coke and Lignite Coke"),
    ("14_industry_sector$14_02_construction$x$x", "02_coal_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coke Oven Coke and Lignite Coke"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "02_coal_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coke Oven Coke and Lignite Coke"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "02_coal_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coke Oven Coke and Lignite Coke"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "02_coal_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coke Oven Coke and Lignite Coke"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "02_coal_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coke Oven Coke and Lignite Coke"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "02_coal_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coke Oven Coke and Lignite Coke"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "02_coal_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coke Oven Coke and Lignite Coke"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "02_coal_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coke Oven Coke and Lignite Coke"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "02_coal_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coke Oven Coke and Lignite Coke"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "02_coal_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coke Oven Coke and Lignite Coke"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "02_coal_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coke Oven Coke and Lignite Coke"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "02_coal_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coke Oven Coke and Lignite Coke"),
    ("14_industry_sector$14_03_manufacturing$x$x", "02_coal_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coke Oven Coke and Lignite Coke"),
    ("14_industry_sector$x$x$x", "02_coal_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Coke Oven Coke and Lignite Coke"),

    # Peat Mappings
    ("14_industry_sector$14_02_construction$x$x", "03_peat$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Peat"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "03_peat$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Peat"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "03_peat$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Peat"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "03_peat$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Peat"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "03_peat$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Peat"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "03_peat$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Peat"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "03_peat$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Peat"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "03_peat$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Peat"),
    ("14_industry_sector$14_03_manufacturing$x$x", "03_peat$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Peat"),
    ("14_industry_sector$x$x$x", "03_peat$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Peat"),

    # Peat Products Mappings (mapped to Peat)
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "04_peat_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Peat"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "04_peat_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Peat"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "04_peat_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Peat"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "04_peat_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Peat"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "04_peat_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Peat"),
    ("14_industry_sector$14_03_manufacturing$x$x", "04_peat_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Peat"),
    ("14_industry_sector$x$x$x", "04_peat_products$x"):
        ("1.A.2 - Manufacturing Industries and Construction", "Peat"),

    # Crude Oil Mappings
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "06_crude_oil_and_ngl$06_01_crude_oil"):
        ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),
    ("14_industry_sector$14_02_construction$x$x", "06_crude_oil_and_ngl$06_01_crude_oil"):
        ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "06_crude_oil_and_ngl$06_01_crude_oil"):
        ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "06_crude_oil_and_ngl$06_01_crude_oil"):
        ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "06_crude_oil_and_ngl$06_01_crude_oil"):
        ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "06_crude_oil_and_ngl$06_01_crude_oil"):
        ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "06_crude_oil_and_ngl$06_01_crude_oil"):
        ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "06_crude_oil_and_ngl$06_01_crude_oil"):
        ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "06_crude_oil_and_ngl$06_01_crude_oil"):
        ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "06_crude_oil_and_ngl$06_01_crude_oil"):
        ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "06_crude_oil_and_ngl$06_01_crude_oil"):
        ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "06_crude_oil_and_ngl$06_01_crude_oil"):
        ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "06_crude_oil_and_ngl$06_01_crude_oil"):
        ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),
    ("14_industry_sector$14_03_manufacturing$x$x", "06_crude_oil_and_ngl$06_01_crude_oil"):
        ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),
    ("14_industry_sector$x$x$x", "06_crude_oil_and_ngl$06_01_crude_oil"):
        ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),

    # Natural Gas Liquids (NGLs) Mappings
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas Liquids (NGLs)"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas Liquids (NGLs)"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas Liquids (NGLs)"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas Liquids (NGLs)"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas Liquids (NGLs)"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas Liquids (NGLs)"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas Liquids (NGLs)"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas Liquids (NGLs)"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"):
        ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas Liquids (NGLs)"),
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "01_coal$01_01_coking_coal"): ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_02_construction$x$x", "01_coal$01_01_coking_coal"): ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "01_coal$01_01_coking_coal"): ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "01_coal$01_01_coking_coal"): ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "01_coal$01_01_coking_coal"): ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "01_coal$01_01_coking_coal"): ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "01_coal$01_01_coking_coal"): ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "01_coal$01_01_coking_coal"): ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "01_coal$01_01_coking_coal"): ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "01_coal$01_01_coking_coal"): ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "01_coal$01_01_coking_coal"): ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "01_coal$01_01_coking_coal"): ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "01_coal$01_01_coking_coal"): ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$14_03_manufacturing$x$x", "01_coal$01_01_coking_coal"): ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),
    ("14_industry_sector$x$x$x", "01_coal$01_01_coking_coal"): ("1.A.2 - Manufacturing Industries and Construction", "Coking Coal"),

    # Lignite Mappings (IDs 184-207)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "01_coal$01_05_lignite"): ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_02_construction$x$x", "01_coal$01_05_lignite"): ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "01_coal$01_05_lignite"): ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "01_coal$01_05_lignite"): ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x", "01_coal$01_05_lignite"): ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x", "01_coal$01_05_lignite"): ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x", "01_coal$01_05_lignite"): ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_06_machinery$x", "01_coal$01_05_lignite"): ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x", "01_coal$01_05_lignite"): ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x", "01_coal$01_05_lignite"): ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x", "01_coal$01_05_lignite"): ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x", "01_coal$01_05_lignite"): ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "01_coal$01_05_lignite"): ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$14_03_manufacturing$x$x", "01_coal$01_05_lignite"): ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),
    ("14_industry_sector$x$x$x", "01_coal$01_05_lignite"): ("1.A.2 - Manufacturing Industries and Construction", "Lignite"),

    # Thermal Coal Mappings (IDs 410-456, mapped to Other Bituminous Coal)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "01_coal$01_x_thermal_coal"): ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_02_construction$x$x", "01_coal$01_x_thermal_coal"): ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "01_coal$01_x_thermal_coal"): ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    # ... (continue with IDs 430-456)
    ("14_industry_sector$14_03_manufacturing$x$x", "01_coal$01_x_thermal_coal"): ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$x$x$x", "01_coal$01_x_thermal_coal"): ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),

    # Unspecified Coal Mappings (IDs 734-780, mapped to Other Bituminous Coal)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "01_coal$x"): ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$14_02_construction$x$x", "01_coal$x"): ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    # ... (continue with IDs 748-780)
    ("14_industry_sector$14_03_manufacturing$x$x", "01_coal$x"): ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),
    ("14_industry_sector$x$x$x", "01_coal$x"): ("1.A.2 - Manufacturing Industries and Construction", "Other Bituminous Coal"),

    # Coal Products Mappings (IDs 1178-1247)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "02_coal_products$x"): ("1.A.2 - Manufacturing Industries and Construction", "Coke Oven Coke and Lignite Coke"),
    ("14_industry_sector$14_02_construction$x$x", "02_coal_products$x"): ("1.A.2 - Manufacturing Industries and Construction", "Coke Oven Coke and Lignite Coke"),
    # ... (continue with IDs 1199-1247)
    ("14_industry_sector$14_03_manufacturing$x$x", "02_coal_products$x"): ("1.A.2 - Manufacturing Industries and Construction", "Coke Oven Coke and Lignite Coke"),
    ("14_industry_sector$x$x$x", "02_coal_products$x"): ("1.A.2 - Manufacturing Industries and Construction", "Coke Oven Coke and Lignite Coke"),

    # Peat Mappings (IDs 1493-1515)
    ("14_industry_sector$14_02_construction$x$x", "03_peat$x"): ("1.A.2 - Manufacturing Industries and Construction", "Peat"),
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "03_peat$x"): ("1.A.2 - Manufacturing Industries and Construction", "Peat"),
    # ... (continue with IDs 1503-1515)
    ("14_industry_sector$14_03_manufacturing$x$x", "03_peat$x"): ("1.A.2 - Manufacturing Industries and Construction", "Peat"),
    ("14_industry_sector$x$x$x", "03_peat$x"): ("1.A.2 - Manufacturing Industries and Construction", "Peat"),

    # Peat Products Mappings (IDs 1643-1659, mapped to Peat)
    ("14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x", "04_peat_products$x"): ("1.A.2 - Manufacturing Industries and Construction", "Peat"),
    # ... (continue with IDs 1647-1659)
    ("14_industry_sector$x$x$x", "04_peat_products$x"): ("1.A.2 - Manufacturing Industries and Construction", "Peat"),

    # Crude Oil Mappings (IDs 1946-1969)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "06_crude_oil_and_ngl$06_01_crude_oil"): ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),
    ("14_industry_sector$14_02_construction$x$x", "06_crude_oil_and_ngl$06_01_crude_oil"): ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),
    # ... (continue with IDs 1953-1969)
    ("14_industry_sector$x$x$x", "06_crude_oil_and_ngl$06_01_crude_oil"): ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),

    # Natural Gas Liquids (NGLs) Mappings (IDs 2060-2083)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"): ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas Liquids (NGLs)"),
    # ... (continue with IDs 2067-2083)
    ("14_industry_sector$x$x$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"): ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas Liquids (NGLs)"),

    # Unspecified Crude Oil and NGLs Mappings (IDs 2426-2449, mapped to Crude Oil)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "06_crude_oil_and_ngl$x"): ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),
    # ... (continue with IDs 2433-2449)
    ("14_industry_sector$x$x$x", "06_crude_oil_and_ngl$x"): ("1.A.2 - Manufacturing Industries and Construction", "Crude Oil"),

    # Motor Gasoline Mappings (IDs 2550-2573)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "07_petroleum_products$07_01_motor_gasoline"): ("1.A.2 - Manufacturing Industries and Construction", "Motor Gasoline"),
    ("14_industry_sector$14_02_construction$x$x", "07_petroleum_products$07_01_motor_gasoline"): ("1.A.2 - Manufacturing Industries and Construction", "Motor Gasoline"),
    # ... (continue with IDs 2557-2573)
    ("14_industry_sector$x$x$x", "07_petroleum_products$07_01_motor_gasoline"): ("1.A.2 - Manufacturing Industries and Construction", "Motor Gasoline"),

    # Aviation Gasoline Mappings (IDs 2710-2712)
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "07_petroleum_products$07_02_aviation_gasoline"): ("1.A.2 - Manufacturing Industries and Construction", "Aviation Gasoline"),
    ("14_industry_sector$14_03_manufacturing$x$x", "07_petroleum_products$07_02_aviation_gasoline"): ("1.A.2 - Manufacturing Industries and Construction", "Aviation Gasoline"),
    ("14_industry_sector$x$x$x", "07_petroleum_products$07_02_aviation_gasoline"): ("1.A.2 - Manufacturing Industries and Construction", "Aviation Gasoline"),

    # Naphtha Mappings (IDs 2828-2851)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "07_petroleum_products$07_03_naphtha"): ("1.A.2 - Manufacturing Industries and Construction", "Naphtha"),
    ("14_industry_sector$14_02_construction$x$x", "07_petroleum_products$07_03_naphtha"): ("1.A.2 - Manufacturing Industries and Construction", "Naphtha"),
    # ... (continue with IDs 2838-2851)
    ("14_industry_sector$x$x$x", "07_petroleum_products$07_03_naphtha"): ("1.A.2 - Manufacturing Industries and Construction", "Naphtha"),

    # Kerosene Mappings (IDs 2992-3038)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "07_petroleum_products$07_06_kerosene"): ("1.A.2 - Manufacturing Industries and Construction", "Other Kerosene"),
    ("14_industry_sector$14_02_construction$x$x", "07_petroleum_products$07_06_kerosene"): ("1.A.2 - Manufacturing Industries and Construction", "Other Kerosene"),
    # ... (continue with IDs 3006-3038)
    ("14_industry_sector$x$x$x", "07_petroleum_products$07_06_kerosene"): ("1.A.2 - Manufacturing Industries and Construction", "Other Kerosene"),

    # Gas/Diesel Oil Mappings (IDs 3360-3406)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "07_petroleum_products$07_07_gas_diesel_oil"): ("1.A.2 - Manufacturing Industries and Construction", "Gas Oil"),
    ("14_industry_sector$14_02_construction$x$x", "07_petroleum_products$07_07_gas_diesel_oil"): ("1.A.2 - Manufacturing Industries and Construction", "Gas Oil"),
    # ... (continue with IDs 3374-3406)
    ("14_industry_sector$x$x$x", "07_petroleum_products$07_07_gas_diesel_oil"): ("1.A.2 - Manufacturing Industries and Construction", "Gas Oil"),

    # Fuel Oil Mappings (IDs 3655-3678)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "07_petroleum_products$07_08_fuel_oil"): ("1.A.2 - Manufacturing Industries and Construction", "Residual Fuel Oil"),
    ("14_industry_sector$14_02_construction$x$x", "07_petroleum_products$07_08_fuel_oil"): ("1.A.2 - Manufacturing Industries and Construction", "Residual Fuel Oil"),
    # ... (continue with IDs 3662-3678)
    ("14_industry_sector$x$x$x", "07_petroleum_products$07_08_fuel_oil"): ("1.A.2 - Manufacturing Industries and Construction", "Residual Fuel Oil"),

    # Liquefied Petroleum Gases (LPG) Mappings (IDs 3805-3828)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "07_petroleum_products$07_09_lpg"): ("1.A.2 - Manufacturing Industries and Construction", "Liquefied Petroleum Gases"),
    ("14_industry_sector$14_02_construction$x$x", "07_petroleum_products$07_09_lpg"): ("1.A.2 - Manufacturing Industries and Construction", "Liquefied Petroleum Gases"),
    # ... (continue with IDs 3812-3828)
    ("14_industry_sector$x$x$x", "07_petroleum_products$07_09_lpg"): ("1.A.2 - Manufacturing Industries and Construction", "Liquefied Petroleum Gases"),

    # Refinery Gas Mappings (IDs 3954-3977)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"): ("1.A.2 - Manufacturing Industries and Construction", "Refinery Gas"),
    ("14_industry_sector$14_02_construction$x$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"): ("1.A.2 - Manufacturing Industries and Construction", "Refinery Gas"),
    # ... (continue with IDs 3961-3977)
    ("14_industry_sector$x$x$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"): ("1.A.2 - Manufacturing Industries and Construction", "Refinery Gas"),

    # Ethane Mappings (IDs 4077-4090)
    ("14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x", "07_petroleum_products$07_11_ethane"): ("1.A.2 - Manufacturing Industries and Construction", "Ethane"),
    ("14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x", "07_petroleum_products$07_11_ethane"): ("1.A.2 - Manufacturing Industries and Construction", "Ethane"),
    ("14_industry_sector$14_03_manufacturing$x$x", "07_petroleum_products$07_11_ethane"): ("1.A.2 - Manufacturing Industries and Construction", "Ethane"),
    ("14_industry_sector$x$x$x", "07_petroleum_products$07_11_ethane"): ("1.A.2 - Manufacturing Industries and Construction", "Ethane"),

    # Jet Fuel Mappings (IDs 4177-4200, mapped to Jet Kerosene)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "07_petroleum_products$07_x_jet_fuel"): ("1.A.2 - Manufacturing Industries and Construction", "Jet Kerosene"),
    # ... (continue with IDs 4187-4200)
    ("14_industry_sector$x$x$x", "07_petroleum_products$07_x_jet_fuel"): ("1.A.2 - Manufacturing Industries and Construction", "Jet Kerosene"),

    # Other Petroleum Products Mappings (IDs 4665-4780)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "07_petroleum_products$07_x_other_petroleum_products"): ("1.A.2 - Manufacturing Industries and Construction", "Other Petroleum Products"),
    ("14_industry_sector$14_02_construction$x$x", "07_petroleum_products$07_x_other_petroleum_products"): ("1.A.2 - Manufacturing Industries and Construction", "Other Petroleum Products"),
    # ... (continue with IDs 4700-4780)
    ("14_industry_sector$x$x$x", "07_petroleum_products$07_x_other_petroleum_products"): ("1.A.2 - Manufacturing Industries and Construction", "Other Petroleum Products"),

    # Unspecified Petroleum Products Mappings (IDs 5279-5302, mapped to Other Petroleum Products)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "07_petroleum_products$x"): ("1.A.2 - Manufacturing Industries and Construction", "Other Petroleum Products"),
    # ... (continue with IDs 5286-5302)
    ("14_industry_sector$x$x$x", "07_petroleum_products$x"): ("1.A.2 - Manufacturing Industries and Construction", "Other Petroleum Products"),

    # Natural Gas Mappings (IDs 5463-5486)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "08_gas$08_01_natural_gas"): ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas"),
    ("14_industry_sector$14_02_construction$x$x", "08_gas$08_01_natural_gas"): ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas"),
    # ... (continue with IDs 5470-5486)
    ("14_industry_sector$x$x$x", "08_gas$08_01_natural_gas"): ("1.A.2 - Manufacturing Industries and Construction", "Natural Gas"),

    # Gas Works Gas Mappings (IDs 5707-5718)
    ("14_industry_sector$14_01_mining_and_quarrying$x$x", "08_gas$08_03_gas_works_gas"): ("1.A.2 - Manufacturing Industries and Construction", "Gas Works Gas"),
    ("14_industry_sector$14_02_construction$x$x", "08_gas$08_03_gas_works_gas"): ("1.A.2 - Manufacturing Industries and Construction", "Gas Works Gas"),
    # ... (continue with IDs 5714-5718)
    ("14_industry_sector$x$x$x", "08_gas$08_03_gas_works_gas"): ("1.A.2 - Manufacturing Industries and Construction", "Gas Works Gas")

    # Add any additional mappings for the remaining combinations as per your data
}

# Complete Mapping Dictionary for SERVICES
services_mappings = {
    # Coal Mappings
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "01_coal$01_01_coking_coal"):
        ("1.A.4.a - Commercial/Institutional", "Coking Coal"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "01_coal$01_05_lignite"):
        ("1.A.4.a - Commercial/Institutional", "Lignite"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "01_coal$01_x_thermal_coal"):
        ("1.A.4.a - Commercial/Institutional", "Other Bituminous Coal"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "01_coal$x"):
        ("1.A.4.a - Commercial/Institutional", "Other Bituminous Coal"),

    # Coal Products Mappings
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "02_coal_products$x"):
        ("1.A.4.a - Commercial/Institutional", "Coke Oven Coke and Lignite Coke"),

    # Peat Mappings
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "03_peat$x"):
        ("1.A.4.a - Commercial/Institutional", "Peat"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "04_peat_products$x"):
        ("1.A.4.a - Commercial/Institutional", "Peat"),

    # Petroleum Products Mappings
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "07_petroleum_products$07_01_motor_gasoline"):
        ("1.A.4.a - Commercial/Institutional", "Motor Gasoline"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "07_petroleum_products$07_02_aviation_gasoline"):
        ("1.A.4.a - Commercial/Institutional", "Aviation Gasoline"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "07_petroleum_products$07_03_naphtha"):
        ("1.A.4.a - Commercial/Institutional", "Naphtha"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.4.a - Commercial/Institutional", "Other Kerosene"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.4.a - Commercial/Institutional", "Gas Oil"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.4.a - Commercial/Institutional", "Residual Fuel Oil"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.4.a - Commercial/Institutional", "Liquefied Petroleum Gases"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"):
        ("1.A.4.a - Commercial/Institutional", "Refinery Gas"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "07_petroleum_products$07_11_ethane"):
        ("1.A.4.a - Commercial/Institutional", "Ethane"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "07_petroleum_products$07_x_jet_fuel"):
        ("1.A.4.a - Commercial/Institutional", "Jet Kerosene"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.4.a - Commercial/Institutional", "Other Petroleum Products"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "07_petroleum_products$x"):
        ("1.A.4.a - Commercial/Institutional", "Other Petroleum Products"),

    # Gas Mappings
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "08_gas$08_01_natural_gas"):
        ("1.A.4.a - Commercial/Institutional", "Natural Gas"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "08_gas$08_02_lng"):
        ("1.A.4.a - Commercial/Institutional", "Natural Gas"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "08_gas$08_03_gas_works_gas"):
        ("1.A.4.a - Commercial/Institutional", "Gas Works Gas"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "08_gas$x"):
        ("1.A.4.a - Commercial/Institutional", "Natural Gas"),

    # Solid Biomass Mappings
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "15_solid_biomass$15_01_fuelwood_and_woodwaste"):
        ("1.A.4.a - Commercial/Institutional", "Wood/Wood Waste"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "15_solid_biomass$15_02_bagasse"):
        ("1.A.4.a - Commercial/Institutional", "Other Primary Solid Biomass"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "15_solid_biomass$15_03_charcoal"):
        ("1.A.4.a - Commercial/Institutional", "Charcoal"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "15_solid_biomass$15_04_black_liquor"):
        ("1.A.4.a - Commercial/Institutional", "Sulphite Lyes (Black Liquor)"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "15_solid_biomass$15_05_other_biomass"):
        ("1.A.4.a - Commercial/Institutional", "Other Primary Solid Biomass"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "15_solid_biomass$x"):
        ("1.A.4.a - Commercial/Institutional", "Other Primary Solid Biomass"),

    # Other Fuels Mappings
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "16_others$16_01_biogas"):
        ("1.A.4.a - Commercial/Institutional", "Other Biogas"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "16_others$16_02_industrial_waste"):
        ("1.A.4.a - Commercial/Institutional", "Industrial Wastes"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "16_others$16_03_municipal_solid_waste_renewable"):
        ("1.A.4.a - Commercial/Institutional", "Municipal Wastes (biomass fraction)"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "16_others$16_04_municipal_solid_waste_nonrenewable"):
        ("1.A.4.a - Commercial/Institutional", "Municipal Wastes (non-biomass fraction)"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "16_others$16_05_biogasoline"):
        ("1.A.4.a - Commercial/Institutional", "Biogasoline"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "16_others$16_06_biodiesel"):
        ("1.A.4.a - Commercial/Institutional", "Biodiesels"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "16_others$16_07_bio_jet_kerosene"):
        ("1.A.4.a - Commercial/Institutional", "Other Liquid Biofuels"),
    ("16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x", "16_others$16_08_other_liquid_biofuels"):
        ("1.A.4.a - Commercial/Institutional", "Other Liquid Biofuels"),
}

transformation_mappings =  {
    ('09_total_transformation_sector$x$x$x', '01_coal$01_05_lignite'): ('1.A.1 - Energy Industries', 'Lignite'),
    ('09_total_transformation_sector$x$x$x', '01_coal$01_x_thermal_coal'): ('1.A.1 - Energy Industries', 'Other Bituminous Coal'),
    ('09_total_transformation_sector$x$x$x', '01_coal$x'): ('1.A.1 - Energy Industries', 'Other Bituminous Coal'),
    ('09_total_transformation_sector$x$x$x', '02_coal_products$x'): ('1.A.1 - Energy Industries', 'Patent Fuel'),
    ('09_total_transformation_sector$x$x$x', '03_peat$x'): ('1.A.1 - Energy Industries', 'Peat'),
    ('09_total_transformation_sector$x$x$x', '04_peat_products$x'): ('1.A.1 - Energy Industries', 'Peat'),
    ('09_total_transformation_sector$x$x$x', '06_crude_oil_and_ngl$06_01_crude_oil'): ('1.A.1 - Energy Industries', 'Crude Oil'),
    ('09_total_transformation_sector$x$x$x', '06_crude_oil_and_ngl$06_02_natural_gas_liquids'): ('1.A.1 - Energy Industries', 'Natural Gas Liquids (NGLs)'),
    ('09_total_transformation_sector$x$x$x', '06_crude_oil_and_ngl$06_x_other_hydrocarbons'): ('1.A.1 - Energy Industries', 'Other Petroleum Products'),
    ('09_total_transformation_sector$x$x$x', '06_crude_oil_and_ngl$x'): ('1.A.1 - Energy Industries', 'Crude Oil'),
    ('09_total_transformation_sector$x$x$x', '07_petroleum_products$07_01_motor_gasoline'): ('1.A.1 - Energy Industries', 'Motor Gasoline'),
    ('09_total_transformation_sector$x$x$x', '07_petroleum_products$07_03_naphtha'): ('1.A.1 - Energy Industries', 'Naphtha'),
    ('09_total_transformation_sector$x$x$x', '07_petroleum_products$07_06_kerosene'): ('1.A.1 - Energy Industries', 'Other Kerosene'),
    ('09_total_transformation_sector$x$x$x', '07_petroleum_products$07_07_gas_diesel_oil'): ('1.A.1 - Energy Industries', 'Diesel Oil'),
    ('09_total_transformation_sector$x$x$x', '07_petroleum_products$07_08_fuel_oil'): ('1.A.1 - Energy Industries', 'Residual Fuel Oil'),
    ('09_total_transformation_sector$x$x$x', '07_petroleum_products$07_09_lpg'): ('1.A.1 - Energy Industries', 'Liquefied Petroleum Gases'),
    ('09_total_transformation_sector$x$x$x', '07_petroleum_products$07_10_refinery_gas_not_liquefied'): ('1.A.1 - Energy Industries', 'Refinery Gas'),
    ('09_total_transformation_sector$x$x$x', '07_petroleum_products$07_11_ethane'): ('1.A.1 - Energy Industries', 'Ethane'),
    ('09_total_transformation_sector$x$x$x', '07_petroleum_products$07_x_jet_fuel'): ('1.A.1 - Energy Industries', 'Jet Kerosene'),
    ('09_total_transformation_sector$x$x$x', '07_petroleum_products$07_x_other_petroleum_products'): ('1.A.1 - Energy Industries', 'Other Petroleum Products'),
    ('09_total_transformation_sector$x$x$x', '07_petroleum_products$x'): ('1.A.1 - Energy Industries', 'Other Petroleum Products'),
    ('09_total_transformation_sector$x$x$x', '08_gas$08_01_natural_gas'): ('1.A.1 - Energy Industries', 'Natural Gas'),
    ('09_total_transformation_sector$x$x$x', '08_gas$08_02_lng'): ('1.A.1 - Energy Industries', 'Natural Gas'),
    ('09_total_transformation_sector$x$x$x', '08_gas$08_03_gas_works_gas'): ('1.A.1 - Energy Industries', 'Gas Works Gas'),
    ('09_total_transformation_sector$x$x$x', '08_gas$x'): ('1.A.1 - Energy Industries', 'Natural Gas'),
    ('09_total_transformation_sector$x$x$x', '15_solid_biomass$15_01_fuelwood_and_woodwaste'): ('1.A.1 - Energy Industries', 'Wood/Wood Waste'),
    ('09_total_transformation_sector$x$x$x', '15_solid_biomass$15_02_bagasse'): ('1.A.1 - Energy Industries', 'Other Primary Solid Biomass'),
    ('09_total_transformation_sector$x$x$x', '15_solid_biomass$15_03_charcoal'): ('1.A.1 - Energy Industries', 'Charcoal'),
    ('09_total_transformation_sector$x$x$x', '15_solid_biomass$15_04_black_liquor'): ('1.A.1 - Energy Industries', 'Sulphite Lyes (Black Liquor)'),
    ('09_total_transformation_sector$x$x$x', '15_solid_biomass$15_05_other_biomass'): ('1.A.1 - Energy Industries', 'Other Primary Solid Biomass'),
    ('09_total_transformation_sector$x$x$x', '15_solid_biomass$x'): ('1.A.1 - Energy Industries', 'Other Primary Solid Biomass'),
    ('09_total_transformation_sector$x$x$x', '16_others$16_01_biogas'): ('1.A.1 - Energy Industries', 'Other Biogas'),
    ('09_total_transformation_sector$x$x$x', '16_others$16_02_industrial_waste'): ('1.A.1 - Energy Industries', 'Industrial Wastes'),
    ('09_total_transformation_sector$x$x$x', '16_others$16_03_municipal_solid_waste_renewable'): ('1.A.1 - Energy Industries', 'Municipal Wastes (biomass fraction)'),
    ('09_total_transformation_sector$x$x$x', '16_others$16_04_municipal_solid_waste_nonrenewable'): ('1.A.1 - Energy Industries', 'Municipal Wastes (non-biomass fraction)'),
    ('09_total_transformation_sector$x$x$x', '16_others$16_06_biodiesel'): ('1.A.1 - Energy Industries', 'Biodiesels'),
    ('09_total_transformation_sector$x$x$x', '16_others$16_08_other_liquid_biofuels'): ('1.A.1 - Energy Industries', 'Other Liquid Biofuels'),
    ('09_total_transformation_sector$09_11_charcoal_processing$x$x', '15_solid_biomass$15_03_charcoal'): ('1.A.1 - Energy Industries', 'Charcoal'),
    ('09_total_transformation_sector$09_11_charcoal_processing$x$x', '15_solid_biomass$15_05_other_biomass'): ('1.A.1 - Energy Industries', 'Other Primary Solid Biomass'),
    ('09_total_transformation_sector$09_11_charcoal_processing$x$x', '15_solid_biomass$x'): ('1.A.1 - Energy Industries', 'Other Primary Solid Biomass'),
    ('09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x', '01_coal$01_05_lignite'): ('1.A.1 - Energy Industries', 'Lignite'),
    ('09_total_transformation_sector$09_06_gas_processing_plants$x$x', '01_coal$01_05_lignite'): ('1.A.1 - Energy Industries', 'Lignite'),
    ('09_total_transformation_sector$09_06_gas_processing_plants$x$x', '07_petroleum_products$07_08_fuel_oil'): ('1.A.1 - Energy Industries', 'Residual Fuel Oil'),
    ('09_total_transformation_sector$09_06_gas_processing_plants$x$x', '07_petroleum_products$07_10_refinery_gas_not_liquefied'): ('1.A.1 - Energy Industries', 'Refinery Gas'),
    ('09_total_transformation_sector$09_x_heat_plants$x$x', '07_petroleum_products$07_03_naphtha'): ('1.A.1 - Energy Industries', 'Naphtha'),
    ('09_total_transformation_sector$09_11_charcoal_processing$x$x', '15_solid_biomass$15_01_fuelwood_and_woodwaste'): ('1.A.1 - Energy Industries', 'Wood/Wood Waste'),
    ('09_total_transformation_sector$09_02_chp_plants$x$x', '07_petroleum_products$07_x_jet_fuel'): ('1.A.1 - Energy Industries', 'Jet Kerosene'),
    # Gas Processing Plants
    ("09_total_transformation_sector$09_06_gas_processing_plants$x$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Bituminous Coal"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$x$x", "01_coal$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Bituminous Coal"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$x$x", "02_coal_products$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Coke Oven Coke and Lignite Coke"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$x$x", "07_petroleum_products$07_03_naphtha"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Naphtha"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$x$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Liquefied Petroleum Gases"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$x$x", "07_petroleum_products$07_01_motor_gasoline"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Motor Gasoline"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$x$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Kerosene"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$x$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Gas/Diesel Oil"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$x$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Petroleum Products"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$x$x", "07_petroleum_products$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Petroleum Products"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$x$x", "08_gas$08_01_natural_gas"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Natural Gas"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$x$x", "08_gas$08_03_gas_works_gas"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Gas Works Gas"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$x$x", "08_gas$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Natural Gas"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$x$x", "16_others$16_01_biogas"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Biogas"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$x$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Natural Gas Liquids (NGLs)"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$x$x", "06_crude_oil_and_ngl$06_x_other_hydrocarbons"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Hydrocarbons"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$x$x", "06_crude_oil_and_ngl$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Crude Oil"),

    # Coal Transformation
    ("09_total_transformation_sector$09_08_coal_transformation$x$x", "01_coal$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Bituminous Coal"),
    ("09_total_transformation_sector$09_08_coal_transformation$x$x", "02_coal_products$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Patent Fuel"),
    ("09_total_transformation_sector$09_08_coal_transformation$x$x", "03_peat$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Peat"),
    ("09_total_transformation_sector$09_08_coal_transformation$x$x", "04_peat_products$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Brown Coal Briquettes"),
    ("09_total_transformation_sector$09_08_coal_transformation$x$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Gas/Diesel Oil"),
    ("09_total_transformation_sector$09_08_coal_transformation$x$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Residual Fuel Oil"),
    ("09_total_transformation_sector$09_08_coal_transformation$x$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Petroleum Products"),
    ("09_total_transformation_sector$09_08_coal_transformation$x$x", "07_petroleum_products$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Petroleum Products"),
    ("09_total_transformation_sector$09_08_coal_transformation$x$x", "08_gas$08_01_natural_gas"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Natural Gas"),
    ("09_total_transformation_sector$09_08_coal_transformation$x$x", "08_gas$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Natural Gas"),
    ("09_total_transformation_sector$09_08_coal_transformation$x$x", "16_others$16_02_industrial_waste"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Industrial Wastes"),

    # Non-specified Transformation
    ("09_total_transformation_sector$09_12_nonspecified_transformation$x$x", "06_crude_oil_and_ngl$06_x_other_hydrocarbons"):
        ("1.A.1 - Energy Industries", "Other Hydrocarbons"),
    ("09_total_transformation_sector$09_12_nonspecified_transformation$x$x", "06_crude_oil_and_ngl$x"):
        ("1.A.1 - Energy Industries", "Crude Oil"),
    ("09_total_transformation_sector$09_12_nonspecified_transformation$x$x", "08_gas$08_01_natural_gas"):
        ("1.A.1 - Energy Industries", "Natural Gas"),
    ("09_total_transformation_sector$09_12_nonspecified_transformation$x$x", "08_gas$x"):
        ("1.A.1 - Energy Industries", "Natural Gas"),
    ("09_total_transformation_sector$09_12_nonspecified_transformation$x$x", "15_solid_biomass$15_05_other_biomass"):
        ("1.A.1 - Energy Industries", "Other Primary Solid Biomass"),
    ("09_total_transformation_sector$09_12_nonspecified_transformation$x$x", "15_solid_biomass$x"):
        ("1.A.1 - Energy Industries", "Wood/Wood Waste"),
    ("09_total_transformation_sector$09_12_nonspecified_transformation$x$x", "16_others$16_02_industrial_waste"):
        ("1.A.1 - Energy Industries", "Industrial Wastes"),
    ("09_total_transformation_sector$09_12_nonspecified_transformation$x$x", "16_others$16_01_biogas"):
        ("1.A.1 - Energy Industries", "Other Biogas"),
    ("09_total_transformation_sector$09_12_nonspecified_transformation$x$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"):
        ("1.A.1 - Energy Industries", "Natural Gas Liquids (NGLs)"),
    ("09_total_transformation_sector$09_12_nonspecified_transformation$x$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.1 - Energy Industries", "Residual Fuel Oil"),
    ("09_total_transformation_sector$09_12_nonspecified_transformation$x$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.1 - Energy Industries", "Liquefied Petroleum Gases"),
    ("09_total_transformation_sector$09_12_nonspecified_transformation$x$x", "07_petroleum_products$x"):
        ("1.A.1 - Energy Industries", "Other Petroleum Products"),
    ("09_total_transformation_sector$09_12_nonspecified_transformation$x$x", "07_petroleum_products$07_11_ethane"):
        ("1.A.1 - Energy Industries", "Ethane"),

    # Heat Plants
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "01_coal$01_05_lignite"):
        ("1.A.1.a - Public Electricity and Heat Production", "Lignite"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1.a - Public Electricity and Heat Production", "Other Bituminous Coal"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "01_coal$x"):
        ("1.A.1.a - Public Electricity and Heat Production", "Other Bituminous Coal"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "02_coal_products$x"):
        ("1.A.1.a - Public Electricity and Heat Production", "Patent Fuel"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "03_peat$x"):
        ("1.A.1.a - Public Electricity and Heat Production", "Peat"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "04_peat_products$x"):
        ("1.A.1.a - Public Electricity and Heat Production", "Brown Coal Briquettes"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "06_crude_oil_and_ngl$x"):
        ("1.A.1.a - Public Electricity and Heat Production", "Crude Oil"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.1.a - Public Electricity and Heat Production", "Gas/Diesel Oil"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.1.a - Public Electricity and Heat Production", "Residual Fuel Oil"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.1.a - Public Electricity and Heat Production", "Other Petroleum Products"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "07_petroleum_products$x"):
        ("1.A.1.a - Public Electricity and Heat Production", "Other Petroleum Products"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "08_gas$08_01_natural_gas"):
        ("1.A.1.a - Public Electricity and Heat Production", "Natural Gas"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "08_gas$x"):
        ("1.A.1.a - Public Electricity and Heat Production", "Natural Gas"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "15_solid_biomass$x"):
        ("1.A.1.a - Public Electricity and Heat Production", "Wood/Wood Waste"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "16_others$16_01_biogas"):
        ("1.A.1.a - Public Electricity and Heat Production", "Other Biogas"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "16_others$16_03_municipal_solid_waste_renewable"):
        ("1.A.1.a - Public Electricity and Heat Production", "Municipal Wastes (biomass fraction)"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "16_others$16_04_municipal_solid_waste_nonrenewable"):
        ("1.A.1.a - Public Electricity and Heat Production", "Municipal Wastes (non-biomass fraction)"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "01_coal$01_01_coking_coal"):
        ("1.A.1.a - Public Electricity and Heat Production", "Coking Coal"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "06_crude_oil_and_ngl$06_01_crude_oil"):
        ("1.A.1.a - Public Electricity and Heat Production", "Crude Oil"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "07_petroleum_products$07_01_motor_gasoline"):
        ("1.A.1.a - Public Electricity and Heat Production", "Motor Gasoline"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.1.a - Public Electricity and Heat Production", "Other Kerosene"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.1.a - Public Electricity and Heat Production", "Liquefied Petroleum Gases"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"):
        ("1.A.1.a - Public Electricity and Heat Production", "Refinery Gas"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "08_gas$08_03_gas_works_gas"):
        ("1.A.1.a - Public Electricity and Heat Production", "Gas Works Gas"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "15_solid_biomass$15_05_other_biomass"):
        ("1.A.1.a - Public Electricity and Heat Production", "Other Primary Solid Biomass"),
    ("09_total_transformation_sector$09_x_heat_plants$x$x", "16_others$16_02_industrial_waste"):
        ("1.A.1.a - Public Electricity and Heat Production", "Industrial Wastes"),

    # Transformation Sector (Unspecified)
    ("09_total_transformation_sector$x$x$x", "01_coal$01_01_coking_coal"):
        ("1.A.1 - Energy Industries", "Coking Coal"),
    # ... Continue with all other combinations in your list, following the same pattern ...

    # Petrochemical Industry
    ("09_total_transformation_sector$09_09_petrochemical_industry$x$x", "06_crude_oil_and_ngl$06_x_other_hydrocarbons"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Hydrocarbons"),
    ("09_total_transformation_sector$09_09_petrochemical_industry$x$x", "06_crude_oil_and_ngl$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Crude Oil"),
    ("09_total_transformation_sector$09_09_petrochemical_industry$x$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Petroleum Products"),
    ("09_total_transformation_sector$09_09_petrochemical_industry$x$x", "07_petroleum_products$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Petroleum Products"),
    ("09_total_transformation_sector$09_09_petrochemical_industry$x$x", "07_petroleum_products$07_03_naphtha"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Naphtha"),
    ("09_total_transformation_sector$09_09_petrochemical_industry$x$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Liquefied Petroleum Gases"),
    ("09_total_transformation_sector$09_09_petrochemical_industry$x$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Kerosene"),
    ("09_total_transformation_sector$09_09_petrochemical_industry$x$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Gas/Diesel Oil"),
    ("09_total_transformation_sector$09_09_petrochemical_industry$x$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Residual Fuel Oil"),
    ("09_total_transformation_sector$09_09_petrochemical_industry$x$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Refinery Gas"),
    # Electricity Plants
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "08_gas$x"):
        ("1.A.1.a - Public Electricity and Heat Production", "Natural Gas"),
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "15_solid_biomass$15_05_other_biomass"):
        ("1.A.1.a - Public Electricity and Heat Production", "Other Primary Solid Biomass"),
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "15_solid_biomass$x"):
        ("1.A.1.a - Public Electricity and Heat Production", "Wood/Wood Waste"),
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "06_crude_oil_and_ngl$06_x_other_hydrocarbons"):
        ("1.A.1.a - Public Electricity and Heat Production", "Other Hydrocarbons"),
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "15_solid_biomass$15_04_black_liquor"):
        ("1.A.1.a - Public Electricity and Heat Production", "Sulphite Lyes (Black Liquor)"),
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "15_solid_biomass$15_02_bagasse"):
        ("1.A.1.a - Public Electricity and Heat Production", "Bagasse"),

    # Combined Heat and Power (CHP) Plants
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1.a - Public Electricity and Heat Production", "Other Bituminous Coal"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "01_coal$x"):
        ("1.A.1.a - Public Electricity and Heat Production", "Other Bituminous Coal"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "02_coal_products$x"):
        ("1.A.1.a - Public Electricity and Heat Production", "Coke Oven Coke and Lignite Coke"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "03_peat$x"):
        ("1.A.1.a - Public Electricity and Heat Production", "Peat"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "06_crude_oil_and_ngl$x"):
        ("1.A.1.a - Public Electricity and Heat Production", "Crude Oil"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.1.a - Public Electricity and Heat Production", "Gas/Diesel Oil"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.1.a - Public Electricity and Heat Production", "Residual Fuel Oil"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.1.a - Public Electricity and Heat Production", "Other Petroleum Products"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "07_petroleum_products$x"):
        ("1.A.1.a - Public Electricity and Heat Production", "Other Petroleum Products"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "08_gas$08_01_natural_gas"):
        ("1.A.1.a - Public Electricity and Heat Production", "Natural Gas"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "08_gas$x"):
        ("1.A.1.a - Public Electricity and Heat Production", "Natural Gas"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "15_solid_biomass$15_05_other_biomass"):
        ("1.A.1.a - Public Electricity and Heat Production", "Other Primary Solid Biomass"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "15_solid_biomass$x"):
        ("1.A.1.a - Public Electricity and Heat Production", "Wood/Wood Waste"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "16_others$16_01_biogas"):
        ("1.A.1.a - Public Electricity and Heat Production", "Other Biogas"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "16_others$16_02_industrial_waste"):
        ("1.A.1.a - Public Electricity and Heat Production", "Industrial Wastes"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "07_petroleum_products$07_03_naphtha"):
        ("1.A.1.a - Public Electricity and Heat Production", "Naphtha"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.1.a - Public Electricity and Heat Production", "Other Kerosene"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"):
        ("1.A.1.a - Public Electricity and Heat Production", "Refinery Gas"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.1.a - Public Electricity and Heat Production", "Liquefied Petroleum Gases"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "16_others$16_03_municipal_solid_waste_renewable"):
        ("1.A.1.a - Public Electricity and Heat Production", "Municipal Wastes (biomass fraction)"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "16_others$16_04_municipal_solid_waste_nonrenewable"):
        ("1.A.1.a - Public Electricity and Heat Production", "Municipal Wastes (non-biomass fraction)"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "16_others$16_06_biodiesel"):
        ("1.A.1.a - Public Electricity and Heat Production", "Biodiesels"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "16_others$16_08_other_liquid_biofuels"):
        ("1.A.1.a - Public Electricity and Heat Production", "Other Liquid Biofuels"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "15_solid_biomass$15_04_black_liquor"):
        ("1.A.1.a - Public Electricity and Heat Production", "Sulphite Lyes (Black Liquor)"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "15_solid_biomass$15_01_fuelwood_and_woodwaste"):
        ("1.A.1.a - Public Electricity and Heat Production", "Wood/Wood Waste"),

    # Gas Processing Plants - Gas Works Plants
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Bituminous Coal"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x", "01_coal$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Bituminous Coal"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x", "02_coal_products$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Coke Oven Coke and Lignite Coke"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x", "07_petroleum_products$07_03_naphtha"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Naphtha"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Liquefied Petroleum Gases"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x", "07_petroleum_products$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Petroleum Products"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x", "08_gas$08_01_natural_gas"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Natural Gas"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x", "08_gas$08_03_gas_works_gas"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Gas Works Gas"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x", "08_gas$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Natural Gas"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x", "16_others$16_01_biogas"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Biogas"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Residual Fuel Oil"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Refinery Gas"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Petroleum Products"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Natural Gas Liquids (NGLs)"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x", "06_crude_oil_and_ngl$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Crude Oil"),

    # Gas Processing Plants - Liquefaction/Regasification Plants
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_02_liquefaction_regasification_plants$x", "07_petroleum_products$07_01_motor_gasoline"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Motor Gasoline"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_02_liquefaction_regasification_plants$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Liquefied Petroleum Gases"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_02_liquefaction_regasification_plants$x", "07_petroleum_products$07_03_naphtha"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Naphtha"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_02_liquefaction_regasification_plants$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Petroleum Products"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_02_liquefaction_regasification_plants$x", "07_petroleum_products$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Petroleum Products"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_02_liquefaction_regasification_plants$x", "08_gas$08_01_natural_gas"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Natural Gas"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_02_liquefaction_regasification_plants$x", "08_gas$08_02_lng"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Liquefied Natural Gas (LNG)"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_02_liquefaction_regasification_plants$x", "08_gas$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Natural Gas"),

    # Gas Processing Plants - Natural Gas Blending Plants
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Liquefied Petroleum Gases"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x", "07_petroleum_products$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Petroleum Products"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x", "08_gas$08_01_natural_gas"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Natural Gas"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x", "08_gas$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Natural Gas"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x", "16_others$16_01_biogas"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Biogas"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x", "02_coal_products$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Coke Oven Coke and Lignite Coke"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Kerosene"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x", "07_petroleum_products$07_03_naphtha"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Naphtha"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Gas/Diesel Oil"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Refinery Gas"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x", "08_gas$08_03_gas_works_gas"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Gas Works Gas"),

    # Gas Processing Plants - Gas to Liquids Plants
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_04_gastoliquids_plants$x", "08_gas$08_01_natural_gas"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Natural Gas"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_04_gastoliquids_plants$x", "08_gas$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Natural Gas"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_04_gastoliquids_plants$x", "06_crude_oil_and_ngl$06_x_other_hydrocarbons"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Hydrocarbons"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_04_gastoliquids_plants$x", "06_crude_oil_and_ngl$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Crude Oil"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_04_gastoliquids_plants$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Kerosene"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_04_gastoliquids_plants$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Gas/Diesel Oil"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_04_gastoliquids_plants$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Refinery Gas"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_04_gastoliquids_plants$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Petroleum Products"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_04_gastoliquids_plants$x", "07_petroleum_products$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Petroleum Products"),

    # Oil Refineries
    ("09_total_transformation_sector$09_07_oil_refineries$x$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"):
        ("1.A.1.b - Petroleum Refining", "Natural Gas Liquids (NGLs)"),
    ("09_total_transformation_sector$09_07_oil_refineries$x$x", "06_crude_oil_and_ngl$06_x_other_hydrocarbons"):
        ("1.A.1.b - Petroleum Refining", "Other Hydrocarbons"),
    ("09_total_transformation_sector$09_07_oil_refineries$x$x", "06_crude_oil_and_ngl$x"):
        ("1.A.1.b - Petroleum Refining", "Crude Oil"),
    ("09_total_transformation_sector$09_07_oil_refineries$x$x", "07_petroleum_products$07_01_motor_gasoline"):
        ("1.A.1.b - Petroleum Refining", "Motor Gasoline"),
    ("09_total_transformation_sector$09_07_oil_refineries$x$x", "07_petroleum_products$07_03_naphtha"):
        ("1.A.1.b - Petroleum Refining", "Naphtha"),
    ("09_total_transformation_sector$09_07_oil_refineries$x$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.1.b - Petroleum Refining", "Other Kerosene"),
    ("09_total_transformation_sector$09_07_oil_refineries$x$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.1.b - Petroleum Refining", "Gas/Diesel Oil"),
    ("09_total_transformation_sector$09_07_oil_refineries$x$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.1.b - Petroleum Refining", "Residual Fuel Oil"),
    ("09_total_transformation_sector$09_07_oil_refineries$x$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.1.b - Petroleum Refining", "Liquefied Petroleum Gases"),
    ("09_total_transformation_sector$09_07_oil_refineries$x$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"):
        ("1.A.1.b - Petroleum Refining", "Refinery Gas"),
    ("09_total_transformation_sector$09_07_oil_refineries$x$x", "07_petroleum_products$07_x_jet_fuel"):
        ("1.A.1.b - Petroleum Refining", "Jet Kerosene"),
    ("09_total_transformation_sector$09_07_oil_refineries$x$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.1.b - Petroleum Refining", "Other Petroleum Products"),
    ("09_total_transformation_sector$09_07_oil_refineries$x$x", "07_petroleum_products$x"):
        ("1.A.1.b - Petroleum Refining", "Other Petroleum Products"),

    # Coal Transformation - Coke Ovens
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x", "01_coal$01_05_lignite"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Lignite"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Bituminous Coal"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x", "01_coal$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Bituminous Coal"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x", "02_coal_products$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Coke Oven Coke and Lignite Coke"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Gas/Diesel Oil"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Residual Fuel Oil"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Petroleum Products"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x", "07_petroleum_products$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Petroleum Products"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x", "08_gas$08_01_natural_gas"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Natural Gas"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x", "08_gas$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Natural Gas"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x", "16_others$16_02_industrial_waste"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Industrial Wastes"),

    # Coal Transformation - Blast Furnaces
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_02_blast_furnaces$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Bituminous Coal"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_02_blast_furnaces$x", "01_coal$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Bituminous Coal"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_02_blast_furnaces$x", "02_coal_products$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Coke Oven Coke and Lignite Coke"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_02_blast_furnaces$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Residual Fuel Oil"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_02_blast_furnaces$x", "07_petroleum_products$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Petroleum Products"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_02_blast_furnaces$x", "08_gas$08_01_natural_gas"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Natural Gas"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_02_blast_furnaces$x", "08_gas$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Natural Gas"),

    # Coal Transformation - Patent Fuel Plants
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_03_patent_fuel_plants$x", "01_coal$01_01_coking_coal"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Coking Coal"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_03_patent_fuel_plants$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Bituminous Coal"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_03_patent_fuel_plants$x", "01_coal$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Bituminous Coal"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_03_patent_fuel_plants$x", "02_coal_products$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Coke Oven Coke and Lignite Coke"),

    # Coal Transformation - BKB/PB Plants
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_04_bkb_pb_plants$x", "01_coal$01_01_coking_coal"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Coking Coal"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_04_bkb_pb_plants$x", "01_coal$01_05_lignite"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Lignite"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_04_bkb_pb_plants$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Bituminous Coal"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_04_bkb_pb_plants$x", "01_coal$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Bituminous Coal"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_04_bkb_pb_plants$x", "02_coal_products$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Patent Fuel"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_04_bkb_pb_plants$x", "03_peat$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Peat"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_04_bkb_pb_plants$x", "04_peat_products$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Brown Coal Briquettes"),

    # Coal Transformation - Liquefaction (Coal to Oil)
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_05_liquefaction_coal_to_oil$x", "01_coal$01_01_coking_coal"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Coking Coal"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_05_liquefaction_coal_to_oil$x", "01_coal$01_05_lignite"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Lignite"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_05_liquefaction_coal_to_oil$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Bituminous Coal"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_05_liquefaction_coal_to_oil$x", "01_coal$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Bituminous Coal"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_05_liquefaction_coal_to_oil$x", "02_coal_products$x"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Coke Oven Coke and Lignite Coke"),

    # Coal Transformation - Other
    ("09_total_transformation_sector$09_08_coal_transformation$x$x", "01_coal$01_01_coking_coal"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Coking Coal"),
    ("09_total_transformation_sector$09_08_coal_transformation$x$x", "01_coal$01_05_lignite"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Lignite"),
    ("09_total_transformation_sector$09_08_coal_transformation$x$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries", "Other Bituminous Coal"),
        
    # Coking Coal Mappings
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "01_coal$01_01_coking_coal"):
        ("1.A.1 - Energy Industries", "Coking Coal"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x", "01_coal$01_01_coking_coal"):
        ("1.A.1 - Energy Industries", "Coking Coal"),
    ("09_total_transformation_sector$09_06_gas_processing_plants$x$x", "01_coal$01_01_coking_coal"):
        ("1.A.1 - Energy Industries", "Coking Coal"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x", "01_coal$01_01_coking_coal"):
        ("1.A.1 - Energy Industries", "Coking Coal"),
    ("09_total_transformation_sector$09_08_coal_transformation$09_08_02_blast_furnaces$x", "01_coal$01_01_coking_coal"):
        ("1.A.1 - Energy Industries", "Coking Coal"),
    # ... (include all other mappings as per the provided data)
    
    # Lignite Mappings
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "01_coal$01_05_lignite"):
        ("1.A.1 - Energy Industries", "Lignite"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "01_coal$01_05_lignite"):
        ("1.A.1 - Energy Industries", "Lignite"),
    # ... (continue with all lignite mappings)
    
    # Thermal Coal Mappings (mapped to Other Bituminous Coal)
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    # ... (continue with all thermal coal mappings)
    
    # Unspecified Coal Mappings (mapped to Other Bituminous Coal)
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "01_coal$x"):
        ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    # ... (continue with all unspecified coal mappings)
    
    # Coal Products Mappings
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "02_coal_products$x"):
        ("1.A.1 - Energy Industries", "Coke Oven Coke and Lignite Coke"),
    # ... (continue with all coal products mappings)
    
    # Peat Mappings
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "03_peat$x"):
        ("1.A.1 - Energy Industries", "Peat"),
    # ... (continue with all peat mappings)
    
    # Peat Products Mappings (mapped to Peat)
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "04_peat_products$x"):
        ("1.A.1 - Energy Industries", "Peat"),
    # ... (continue with all peat products mappings)
    
    # Crude Oil Mappings
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "06_crude_oil_and_ngl$06_01_crude_oil"):
        ("1.A.1 - Energy Industries", "Crude Oil"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "06_crude_oil_and_ngl$06_01_crude_oil"):
        ("1.A.1 - Energy Industries", "Crude Oil"),
    ("09_total_transformation_sector$09_07_oil_refineries$x$x", "06_crude_oil_and_ngl$06_01_crude_oil"):
        ("1.A.1 - Energy Industries", "Crude Oil"),
    # ... (continue with all crude oil mappings)
    
    # Natural Gas Liquids (NGLs) Mappings
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"):
        ("1.A.1 - Energy Industries", "Natural Gas Liquids (NGLs)"),
    # ... (continue with all NGLs mappings)
    
    # Unspecified Crude Oil and NGLs Mappings (mapped to Crude Oil)
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "06_crude_oil_and_ngl$x"):
        ("1.A.1 - Energy Industries", "Crude Oil"),
    # ... (continue with all unspecified crude oil and NGLs mappings)
    
    # Motor Gasoline Mappings
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "07_petroleum_products$07_01_motor_gasoline"):
        ("1.A.1 - Energy Industries", "Motor Gasoline"),
    # ... (continue with all motor gasoline mappings)
    
    # Aviation Gasoline Mappings
    ("09_total_transformation_sector$09_07_oil_refineries$x$x", "07_petroleum_products$07_02_aviation_gasoline"):
        ("1.A.1 - Energy Industries", "Aviation Gasoline"),
    ("09_total_transformation_sector$x$x$x", "07_petroleum_products$07_02_aviation_gasoline"):
        ("1.A.1 - Energy Industries", "Aviation Gasoline"),
    
    # Naphtha Mappings
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "07_petroleum_products$07_03_naphtha"):
        ("1.A.1 - Energy Industries", "Naphtha"),
    # ... (continue with all naphtha mappings)
    
    # Kerosene Mappings
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.1 - Energy Industries", "Other Kerosene"),
    # ... (continue with all kerosene mappings)
    
    # Gas/Diesel Oil Mappings
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.1 - Energy Industries", "Gas Oil"),
    # ... (continue with all gas/diesel oil mappings)
    
    # Fuel Oil Mappings
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.1 - Energy Industries", "Residual Fuel Oil"),
    # ... (continue with all fuel oil mappings)
    
    # Liquefied Petroleum Gases (LPG) Mappings
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.1 - Energy Industries", "Liquefied Petroleum Gases"),
    # ... (continue with all LPG mappings)
    
    # Refinery Gas Mappings
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"):
        ("1.A.1 - Energy Industries", "Refinery Gas"),
    # ... (continue with all refinery gas mappings)
    
    # Ethane Mappings
    ("09_total_transformation_sector$09_07_oil_refineries$x$x", "07_petroleum_products$07_11_ethane"):
        ("1.A.1 - Energy Industries", "Ethane"),
    # ... (continue with all ethane mappings)
    
    # Jet Fuel Mappings (mapped to Jet Kerosene)
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "07_petroleum_products$07_x_jet_fuel"):
        ("1.A.1 - Energy Industries", "Jet Kerosene"),
    # ... (continue with all jet fuel mappings)
    
    # Other Petroleum Products Mappings
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.1 - Energy Industries", "Other Petroleum Products"),
    # ... (continue with all other petroleum products mappings)
    
    # Unspecified Petroleum Products Mappings (mapped to Other Petroleum Products)
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "07_petroleum_products$x"):
        ("1.A.1 - Energy Industries", "Other Petroleum Products"),
    # ... (continue with all unspecified petroleum products mappings)
    
    # Natural Gas Mappings
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "08_gas$08_01_natural_gas"):
        ("1.A.1 - Energy Industries", "Natural Gas"),
    # ... (continue with all natural gas mappings)
    
    # LNG Mappings (mapped to Natural Gas)
    ("09_total_transformation_sector$09_06_gas_processing_plants$x$x", "08_gas$08_02_lng"):
        ("1.A.1 - Energy Industries", "Natural Gas"),
    # ... (continue with all LNG mappings)
    
    # Gas Works Gas Mappings
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "08_gas$08_03_gas_works_gas"):
        ("1.A.1 - Energy Industries", "Gas Works Gas"),
    # ... (continue with all gas works gas mappings)
    
    # Solid Biomass Mappings
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "15_solid_biomass$15_01_fuelwood_and_woodwaste"):
        ("1.A.1 - Energy Industries", "Wood/Wood Waste"),
    ("09_total_transformation_sector$09_02_chp_plants$x$x", "15_solid_biomass$15_02_bagasse"):
        ("1.A.1 - Energy Industries", "Other Primary Solid Biomass"),
    # ... (continue with all solid biomass mappings)
    
    # Other Fuels Mappings
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "16_others$16_01_biogas"):
        ("1.A.1 - Energy Industries", "Other Biogas"),
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "16_others$16_02_industrial_waste"):
        ("1.A.1 - Energy Industries", "Industrial Wastes"),
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "16_others$16_03_municipal_solid_waste_renewable"):
        ("1.A.1 - Energy Industries", "Municipal Wastes (biomass fraction)"),
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "16_others$16_04_municipal_solid_waste_nonrenewable"):
        ("1.A.1 - Energy Industries", "Municipal Wastes (non-biomass fraction)"),
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "16_others$16_06_biodiesel"):
        ("1.A.1 - Energy Industries", "Biodiesels"),
    ("09_total_transformation_sector$09_01_electricity_plants$x$x", "16_others$16_08_other_liquid_biofuels"):
        ("1.A.1 - Energy Industries", "Other Liquid Biofuels"),
    # ... (continue with all other fuels mappings)
}

other_mappings= {
    ('10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x', '06_crude_oil_and_ngl$06_01_crude_oil'): ('1.A.1 - Energy Industries', 'Crude Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x', '06_crude_oil_and_ngl$x'): ('1.A.1 - Energy Industries', 'Natural Gas Liquids (NGLs)'),
    ('10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x', '07_petroleum_products$07_01_motor_gasoline'): ('1.A.1 - Energy Industries', 'Motor Gasoline'),
    ('10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x', '07_petroleum_products$07_06_kerosene'): ('1.A.1 - Energy Industries', 'Other Kerosene'),
    ('10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x', '07_petroleum_products$07_08_fuel_oil'): ('1.A.1 - Energy Industries', 'Residual Fuel Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x', '07_petroleum_products$07_10_refinery_gas_not_liquefied'): ('1.A.1 - Energy Industries', 'Refinery Gas'),

    # Natural Gas Blending Plants
    ('10_losses_and_own_use$10_01_own_use$10_01_05_natural_gas_blending_plants$x', '08_gas$x'): ('1.A.1 - Energy Industries', 'Natural Gas'),

    # Nonspecified Own Uses
    ('10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x', '15_solid_biomass$15_05_other_biomass'): ('1.A.4 - Other Sectors', 'Other Primary Solid Biomass'),
    ('10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x', '15_solid_biomass$x'): ('1.A.4 - Other Sectors', 'Other Primary Solid Biomass'),

    # Non-specified Others
    ('16_other_sector$16_05_nonspecified_others$x$x', '08_gas$08_03_gas_works_gas'): ('1.A.4 - Other Sectors', 'Gas Works Gas'),

    # Gas to Liquids Plants
    ('10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x', '07_petroleum_products$07_06_kerosene'): ('1.A.1 - Energy Industries', 'Other Kerosene'),
    ('10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x', '07_petroleum_products$07_07_gas_diesel_oil'): ('1.A.1 - Energy Industries', 'Diesel Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x', '07_petroleum_products$07_09_lpg'): ('1.A.1 - Energy Industries', 'Liquefied Petroleum Gases'),

    # BKB/PB Plants
    ('10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x', '07_petroleum_products$07_02_aviation_gasoline'): ('1.A.1 - Energy Industries', 'Aviation Gasoline'),
    ('10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x', '01_coal$x'): ('1.A.1 - Energy Industries', 'Coking Coal'),
    ('10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x', '08_gas$08_03_gas_works_gas'): ('1.A.1 - Energy Industries', 'Gas Works Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x', '15_solid_biomass$15_05_other_biomass'): ('1.A.4 - Other Sectors', 'Other Primary Solid Biomass'),
    ('10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x', '15_solid_biomass$x'): ('1.A.4 - Other Sectors', 'Other Primary Solid Biomass'),
    ('10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x', '16_others$16_02_industrial_waste'): ('1.A.4 - Other Sectors', 'Industrial Wastes'),

    # Gas Separation
    ('10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x', '07_petroleum_products$07_06_kerosene'): ('1.A.1 - Energy Industries', 'Other Kerosene'),
    ('10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x', '03_peat$x'): ('1.A.4 - Other Sectors', 'Peat'),
    ('10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x', '16_others$16_02_industrial_waste'): ('1.A.4 - Other Sectors', 'Industrial Wastes'),

    # Liquefaction Plants (Coal to Oil)
    ('10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x', '07_petroleum_products$07_03_naphtha'): ('1.A.1 - Energy Industries', 'Naphtha'),

    # Aviation Gasoline
    ('16_other_sector$16_05_nonspecified_others$x$x', '07_petroleum_products$07_02_aviation_gasoline'): ('1.A.1 - Energy Industries', 'Aviation Gasoline'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '07_petroleum_products$07_03_naphtha'): ('1.A.1 - Energy Industries', 'Naphtha'),

    # Gas to Liquids (Coal)
    ('10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x', '01_coal$x'): ('1.A.1 - Energy Industries', 'Coking Coal'),

    # Gas Separation (Motor Gasoline and Biodiesel)
    ('10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x', '07_petroleum_products$07_01_motor_gasoline'): ('1.A.1 - Energy Industries', 'Motor Gasoline'),
    ('10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x', '16_others$16_06_biodiesel'): ('1.A.4 - Other Sectors', 'Biodiesels'),

    # Liquefaction Plants (Coal to Oil and Biodiesel)
    ('10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x', '16_others$16_06_biodiesel'): ('1.A.4 - Other Sectors', 'Biodiesels'),

    # Natural Gas Blending (Motor Gasoline, Diesel, Kerosene, etc.)
    ('10_losses_and_own_use$10_01_own_use$10_01_05_natural_gas_blending_plants$x', '07_petroleum_products$07_01_motor_gasoline'): ('1.A.1 - Energy Industries', 'Motor Gasoline'),
    ('10_losses_and_own_use$10_01_own_use$10_01_05_natural_gas_blending_plants$x', '07_petroleum_products$07_06_kerosene'): ('1.A.1 - Energy Industries', 'Other Kerosene'),
    ('10_losses_and_own_use$10_01_own_use$10_01_05_natural_gas_blending_plants$x', '07_petroleum_products$07_07_gas_diesel_oil'): ('1.A.1 - Energy Industries', 'Diesel Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_05_natural_gas_blending_plants$x', '07_petroleum_products$07_08_fuel_oil'): ('1.A.1 - Energy Industries', 'Residual Fuel Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_05_natural_gas_blending_plants$x', '07_petroleum_products$07_09_lpg'): ('1.A.1 - Energy Industries', 'Liquefied Petroleum Gases'),
    ('10_losses_and_own_use$10_01_own_use$10_01_05_natural_gas_blending_plants$x', '07_petroleum_products$x'): ('1.A.1 - Energy Industries', 'Other Petroleum Products'),

    # Coal Uses and Peat
    ('10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x', '01_coal$x'): ('1.A.1 - Energy Industries', 'Coking Coal'),
    ('10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x', '03_peat$x'): ('1.A.4 - Other Sectors', 'Peat'),

    # Sector: 10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x
    ('10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x', '07_petroleum_products$07_10_refinery_gas_not_liquefied'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Refinery Gas'),
    
    # Sector: 10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x
    ('10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x', '07_petroleum_products$07_01_motor_gasoline'): ('1.A.1.b - Petroleum Refining', 'Motor Gasoline'),
    ('10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x', '07_petroleum_products$07_03_naphtha'): ('1.A.1.b - Petroleum Refining', 'Naphtha'),
    ('10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x', '07_petroleum_products$07_06_kerosene'): ('1.A.1.b - Petroleum Refining', 'Other Kerosene'),

    # Sector: 10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x
    ('10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x', '07_petroleum_products$07_06_kerosene'): ('1.A.2 - Manufacturing Industries and Construction', 'Other Kerosene'),
    ('10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x', '07_petroleum_products$07_10_refinery_gas_not_liquefied'): ('1.A.2 - Manufacturing Industries and Construction', 'Refinery Gas'),

    # Sector: 10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x
    ('10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x', '07_petroleum_products$07_07_gas_diesel_oil'): ('1.A.1.b - Petroleum Refining', 'Gas/Diesel Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x', '08_gas$08_01_natural_gas'): ('1.A.3.b - Road Transportation', 'Natural Gas'),

    # Sector: 10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x
    ('10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x', '15_solid_biomass$15_05_other_biomass'): ('1.A.4.a - Commercial/Institutional', 'Solid Biomass'),
    ('10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x', '15_solid_biomass$x'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Solid Biomass'),

    # Sector: 10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x
    ('10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x', '16_others$16_01_biogas'): ('1.A.4.a - Commercial/Institutional', 'Biogas'),

    # Sector: 10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x
    ('10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x', '02_coal_products$x'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Coal Products'),

    # Sector: 10_losses_and_own_use$10_01_own_use$10_01_05_natural_gas_blending_plants$x
    ('10_losses_and_own_use$10_01_own_use$10_01_05_natural_gas_blending_plants$x', '08_gas$08_01_natural_gas'): ('1.A.3.b - Road Transportation', 'Natural Gas'),

    # Sector: 10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x
    ('10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x', '08_gas$x'): ('1.A.2.f - Chemical Industry', 'Natural Gas'),

    # Sector: 16_other_sector$16_01_buildings$x$x
    ('16_other_sector$16_01_buildings$x$x', '06_crude_oil_and_ngl$06_02_natural_gas_liquids'): ('1.A.4.b - Residential', 'Natural Gas Liquids'),

    # Sector: 16_other_sector$16_02_agriculture_and_fishing$x$x
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '06_crude_oil_and_ngl$06_02_natural_gas_liquids'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Natural Gas Liquids'),
    ('10_losses_and_own_use$x$x$x', '08_gas$08_02_lng'): ('1.A.4.a - Commercial/Institutional', 'Natural Gas Liquids (NGLs)'),
    ('10_losses_and_own_use$x$x$x', '16_others$16_06_biodiesel'): ('1.A.4.a - Commercial/Institutional', 'Biodiesels'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '02_coal_products$x'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Coke Oven Coke and Lignite Coke'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '03_peat$x'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Peat'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '04_peat_products$x'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Peat'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '06_crude_oil_and_ngl$06_01_crude_oil'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Crude Oil'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '06_crude_oil_and_ngl$x'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Natural Gas Liquids (NGLs)'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '07_petroleum_products$07_01_motor_gasoline'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Motor Gasoline'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '07_petroleum_products$07_06_kerosene'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Other Kerosene'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '07_petroleum_products$07_07_gas_diesel_oil'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Diesel Oil'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '07_petroleum_products$07_08_fuel_oil'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Residual Fuel Oil'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '07_petroleum_products$07_09_lpg'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Liquefied Petroleum Gases'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '07_petroleum_products$07_x_other_petroleum_products'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Other Petroleum Products'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '07_petroleum_products$x'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Refinery Feedstocks'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '08_gas$08_01_natural_gas'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Natural Gas'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '08_gas$x'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Gas Works Gas'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '15_solid_biomass$15_01_fuelwood_and_woodwaste'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Wood/Wood Waste'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '15_solid_biomass$15_02_bagasse'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Sulphite Lyes (Black Liquor)'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '15_solid_biomass$15_03_charcoal'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Charcoal'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '15_solid_biomass$15_05_other_biomass'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Other Primary Solid Biomass'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '15_solid_biomass$x'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Wood/Wood Waste'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '16_others$16_01_biogas'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Biogasoline'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '16_others$16_02_industrial_waste'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Industrial Wastes'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '16_others$16_04_municipal_solid_waste_nonrenewable'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Municipal Wastes (non-biomass fraction)'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '16_others$16_05_biogasoline'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Biogasoline'),
    ('16_other_sector$16_02_agriculture_and_fishing$x$x', '16_others$16_06_biodiesel'): ('1.A.4.c - Agriculture/Forestry/Fishing', 'Biodiesels'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '02_coal_products$x'): ('1.A.5 - Other, Non-Specified', 'Coke Oven Coke and Lignite Coke'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '03_peat$x'): ('1.A.5 - Other, Non-Specified', 'Peat'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '04_peat_products$x'): ('1.A.5 - Other, Non-Specified', 'Peat'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '06_crude_oil_and_ngl$06_01_crude_oil'): ('1.A.5 - Other, Non-Specified', 'Crude Oil'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '06_crude_oil_and_ngl$x'): ('1.A.5 - Other, Non-Specified', 'Natural Gas Liquids (NGLs)'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '07_petroleum_products$07_01_motor_gasoline'): ('1.A.5 - Other, Non-Specified', 'Motor Gasoline'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '07_petroleum_products$07_06_kerosene'): ('1.A.5 - Other, Non-Specified', 'Other Kerosene'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '07_petroleum_products$07_07_gas_diesel_oil'): ('1.A.5 - Other, Non-Specified', 'Diesel Oil'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '07_petroleum_products$07_08_fuel_oil'): ('1.A.5 - Other, Non-Specified', 'Residual Fuel Oil'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '07_petroleum_products$07_09_lpg'): ('1.A.5 - Other, Non-Specified', 'Liquefied Petroleum Gases'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '07_petroleum_products$07_x_other_petroleum_products'): ('1.A.5 - Other, Non-Specified', 'Other Petroleum Products'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '07_petroleum_products$x'): ('1.A.5 - Other, Non-Specified', 'Refinery Feedstocks'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '08_gas$08_01_natural_gas'): ('1.A.5 - Other, Non-Specified', 'Natural Gas'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '08_gas$x'): ('1.A.5 - Other, Non-Specified', 'Gas Works Gas'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '15_solid_biomass$15_05_other_biomass'): ('1.A.5 - Other, Non-Specified', 'Other Primary Solid Biomass'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '15_solid_biomass$x'): ('1.A.5 - Other, Non-Specified', 'Wood/Wood Waste'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '16_others$16_01_biogas'): ('1.A.5 - Other, Non-Specified', 'Biogasoline'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '16_others$16_02_industrial_waste'): ('1.A.5 - Other, Non-Specified', 'Industrial Wastes'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '16_others$16_03_municipal_solid_waste_renewable'): ('1.A.5 - Other, Non-Specified', 'Municipal Wastes (biomass fraction)'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '16_others$16_04_municipal_solid_waste_nonrenewable'): ('1.A.5 - Other, Non-Specified', 'Municipal Wastes (non-biomass fraction)'),
    ('16_other_sector$16_05_nonspecified_others$x$x', '16_others$16_06_biodiesel'): ('1.A.5 - Other, Non-Specified', 'Biodiesels'),
    ('16_other_sector$x$x$x', '02_coal_products$x'): ('1.A.5 - Other, Non-Specified', 'Coke Oven Coke and Lignite Coke'),
    ('16_other_sector$x$x$x', '03_peat$x'): ('1.A.5 - Other, Non-Specified', 'Peat'),
    ('16_other_sector$x$x$x', '04_peat_products$x'): ('1.A.5 - Other, Non-Specified', 'Peat'),
    ('16_other_sector$x$x$x', '06_crude_oil_and_ngl$06_01_crude_oil'): ('1.A.5 - Other, Non-Specified', 'Crude Oil'),
    ('16_other_sector$x$x$x', '06_crude_oil_and_ngl$06_02_natural_gas_liquids'): ('1.A.5 - Other, Non-Specified', 'Natural Gas Liquids (NGLs)'),
    ('16_other_sector$x$x$x', '06_crude_oil_and_ngl$x'): ('1.A.5 - Other, Non-Specified', 'Natural Gas Liquids (NGLs)'),
    ('16_other_sector$x$x$x', '07_petroleum_products$07_01_motor_gasoline'): ('1.A.5 - Other, Non-Specified', 'Motor Gasoline'),
    ('16_other_sector$x$x$x', '07_petroleum_products$07_02_aviation_gasoline'): ('1.A.5 - Other, Non-Specified', 'Aviation Gasoline'),
    ('16_other_sector$x$x$x', '07_petroleum_products$07_03_naphtha'): ('1.A.5 - Other, Non-Specified', 'Naphtha'),
    ('16_other_sector$x$x$x', '07_petroleum_products$07_06_kerosene'): ('1.A.5 - Other, Non-Specified', 'Other Kerosene'),
    ('16_other_sector$x$x$x', '07_petroleum_products$07_07_gas_diesel_oil'): ('1.A.5 - Other, Non-Specified', 'Diesel Oil'),
    ('16_other_sector$x$x$x', '07_petroleum_products$07_08_fuel_oil'): ('1.A.5 - Other, Non-Specified', 'Residual Fuel Oil'),
    ('16_other_sector$x$x$x', '07_petroleum_products$07_09_lpg'): ('1.A.5 - Other, Non-Specified', 'Liquefied Petroleum Gases'),
    ('16_other_sector$x$x$x', '07_petroleum_products$07_10_refinery_gas_not_liquefied'): ('1.A.5 - Other, Non-Specified', 'Refinery Gas'),
    ('16_other_sector$x$x$x', '07_petroleum_products$07_x_other_petroleum_products'): ('1.A.5 - Other, Non-Specified', 'Other Petroleum Products'),
    ('16_other_sector$x$x$x', '07_petroleum_products$x'): ('1.A.5 - Other, Non-Specified', 'Refinery Feedstocks'),
    ('16_other_sector$x$x$x', '08_gas$08_01_natural_gas'): ('1.A.5 - Other, Non-Specified', 'Natural Gas'),
    ('16_other_sector$x$x$x', '08_gas$08_03_gas_works_gas'): ('1.A.5 - Other, Non-Specified', 'Gas Works Gas'),
    ('16_other_sector$x$x$x', '08_gas$x'): ('1.A.5 - Other, Non-Specified', 'Gas Works Gas'),
    ('16_other_sector$x$x$x', '15_solid_biomass$15_01_fuelwood_and_woodwaste'): ('1.A.5 - Other, Non-Specified', 'Wood/Wood Waste'),
    ('16_other_sector$x$x$x', '15_solid_biomass$15_02_bagasse'): ('1.A.5 - Other, Non-Specified', 'Sulphite Lyes (Black Liquor)'),
    ('16_other_sector$x$x$x', '15_solid_biomass$15_03_charcoal'): ('1.A.5 - Other, Non-Specified', 'Charcoal'),
    ('16_other_sector$x$x$x', '15_solid_biomass$15_05_other_biomass'): ('1.A.5 - Other, Non-Specified', 'Other Primary Solid Biomass'),
    ('16_other_sector$x$x$x', '15_solid_biomass$x'): ('1.A.5 - Other, Non-Specified', 'Wood/Wood Waste'),
    ('16_other_sector$x$x$x', '16_others$16_01_biogas'): ('1.A.5 - Other, Non-Specified', 'Biogasoline'),
    ('16_other_sector$x$x$x', '16_others$16_02_industrial_waste'): ('1.A.5 - Other, Non-Specified', 'Industrial Wastes'),
    ('16_other_sector$x$x$x', '16_others$16_03_municipal_solid_waste_renewable'): ('1.A.5 - Other, Non-Specified', 'Municipal Wastes (biomass fraction)'),
    ('16_other_sector$x$x$x', '16_others$16_04_municipal_solid_waste_nonrenewable'): ('1.A.5 - Other, Non-Specified', 'Municipal Wastes (non-biomass fraction)'),
    ('16_other_sector$x$x$x', '16_others$16_05_biogasoline'): ('1.A.5 - Other, Non-Specified', 'Biogasoline'),
    ('16_other_sector$x$x$x', '16_others$16_06_biodiesel'): ('1.A.5 - Other, Non-Specified', 'Biodiesels'),
    ('16_other_sector$x$x$x', '16_others$16_08_other_liquid_biofuels'): ('1.A.5 - Other, Non-Specified', 'Other Liquid Biofuels'),
    ('17_nonenergy_use$x$x$x', '02_coal_products$x'): ('1.A.5 - Other, Non-Specified', 'Coke Oven Coke and Lignite Coke'),
    ('17_nonenergy_use$x$x$x', '04_peat_products$x'): ('1.A.5 - Other, Non-Specified', 'Peat'),
    ('17_nonenergy_use$x$x$x', '06_crude_oil_and_ngl$06_01_crude_oil'): ('1.A.5 - Other, Non-Specified', 'Crude Oil'),
    ('17_nonenergy_use$x$x$x', '06_crude_oil_and_ngl$06_02_natural_gas_liquids'): ('1.A.5 - Other, Non-Specified', 'Natural Gas Liquids (NGLs)'),
    ('17_nonenergy_use$x$x$x', '06_crude_oil_and_ngl$06_x_other_hydrocarbons'): ('1.A.5 - Other, Non-Specified', 'Other Hydrocarbons'),
    ('17_nonenergy_use$x$x$x', '06_crude_oil_and_ngl$x'): ('1.A.5 - Other, Non-Specified', 'Natural Gas Liquids (NGLs)'),
    ('17_nonenergy_use$x$x$x', '07_petroleum_products$07_01_motor_gasoline'): ('1.A.5 - Other, Non-Specified', 'Motor Gasoline'),
    ('17_nonenergy_use$x$x$x', '07_petroleum_products$07_03_naphtha'): ('1.A.5 - Other, Non-Specified', 'Naphtha'),
    ('17_nonenergy_use$x$x$x', '07_petroleum_products$07_06_kerosene'): ('1.A.5 - Other, Non-Specified', 'Other Kerosene'),
    ('17_nonenergy_use$x$x$x', '07_petroleum_products$07_07_gas_diesel_oil'): ('1.A.5 - Other, Non-Specified', 'Diesel Oil'),
    ('17_nonenergy_use$x$x$x', '07_petroleum_products$07_08_fuel_oil'): ('1.A.5 - Other, Non-Specified', 'Residual Fuel Oil'),
    ('17_nonenergy_use$x$x$x', '07_petroleum_products$07_09_lpg'): ('1.A.5 - Other, Non-Specified', 'Liquefied Petroleum Gases'),
    ('17_nonenergy_use$x$x$x', '07_petroleum_products$07_10_refinery_gas_not_liquefied'): ('1.A.5 - Other, Non-Specified', 'Refinery Gas'),
    ('17_nonenergy_use$x$x$x', '07_petroleum_products$07_x_other_petroleum_products'): ('1.A.5 - Other, Non-Specified', 'Other Petroleum Products'),
    ('17_nonenergy_use$x$x$x', '07_petroleum_products$x'): ('1.A.5 - Other, Non-Specified', 'Refinery Feedstocks'),
    ('17_nonenergy_use$x$x$x', '08_gas$08_01_natural_gas'): ('1.A.5 - Other, Non-Specified', 'Natural Gas'),
    ('17_nonenergy_use$x$x$x', '08_gas$x'): ('1.A.5 - Other, Non-Specified', 'Gas Works Gas'),
    ('10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x', '02_coal_products$x'): ('1.A.1 - Energy Industries', 'Other Bituminous Coal'),
    ('10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x', '03_peat$x'): ('1.A.1 - Energy Industries', 'Peat'),
    ('10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x', '06_crude_oil_and_ngl$06_01_crude_oil'): ('1.A.1 - Energy Industries', 'Crude Oil'),
    ('10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x', '06_crude_oil_and_ngl$x'): ('1.A.1 - Energy Industries', 'Natural Gas Liquids (NGLs)'),
    ('10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x', '07_petroleum_products$07_01_motor_gasoline'): ('1.A.1 - Energy Industries', 'Motor Gasoline'),
    ('10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x', '07_petroleum_products$07_03_naphtha'): ('1.A.1 - Energy Industries', 'Naphtha'),
    ('10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x', '07_petroleum_products$07_06_kerosene'): ('1.A.1 - Energy Industries', 'Jet Kerosene'),
    ('10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x', '07_petroleum_products$07_07_gas_diesel_oil'): ('1.A.1 - Energy Industries', 'Diesel Oil'),
    ('10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x', '07_petroleum_products$07_08_fuel_oil'): ('1.A.1 - Energy Industries', 'Residual Fuel Oil'),
    ('10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x', '07_petroleum_products$07_09_lpg'): ('1.A.1 - Energy Industries', 'Liquefied Petroleum Gases'),
    ('10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x', '07_petroleum_products$07_10_refinery_gas_not_liquefied'): ('1.A.1 - Energy Industries', 'Refinery Gas'),
    ('10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x', '07_petroleum_products$07_x_other_petroleum_products'): ('1.A.1 - Energy Industries', 'Other Petroleum Products'),
    ('10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x', '07_petroleum_products$x'): ('1.A.1 - Energy Industries', 'Other Petroleum Products'),
    ('10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x', '08_gas$08_01_natural_gas'): ('1.A.1 - Energy Industries', 'Natural Gas'),
    ('10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x', '08_gas$08_03_gas_works_gas'): ('1.A.1 - Energy Industries', 'Gas Works Gas'),
    ('10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x', '08_gas$x'): ('1.A.1 - Energy Industries', 'Natural Gas'),
    ('10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x', '15_solid_biomass$15_05_other_biomass'): ('1.A.4 - Other Sectors', 'Other Primary Solid Biomass'),
    ('10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x', '15_solid_biomass$x'): ('1.A.4 - Other Sectors', 'Other Primary Solid Biomass'),
    ('10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x', '16_others$16_01_biogas'): ('1.A.4 - Other Sectors', 'Other Biogas'),
    ('10_losses_and_own_use$x$x$x', '02_coal_products$x'): ('1.A.1 - Energy Industries', 'Other Bituminous Coal'),
    ('10_losses_and_own_use$x$x$x', '03_peat$x'): ('1.A.1 - Energy Industries', 'Peat'),
    ('10_losses_and_own_use$x$x$x', '04_peat_products$x'): ('1.A.1 - Energy Industries', 'Peat'),
    ('10_losses_and_own_use$x$x$x', '06_crude_oil_and_ngl$06_01_crude_oil'): ('1.A.1 - Energy Industries', 'Crude Oil'),
    ('10_losses_and_own_use$x$x$x', '06_crude_oil_and_ngl$06_02_natural_gas_liquids'): ('1.A.1 - Energy Industries', 'Natural Gas Liquids (NGLs)'),
    ('10_losses_and_own_use$x$x$x', '06_crude_oil_and_ngl$x'): ('1.A.1 - Energy Industries', 'Natural Gas Liquids (NGLs)'),
    ('10_losses_and_own_use$x$x$x', '07_petroleum_products$07_01_motor_gasoline'): ('1.A.1 - Energy Industries', 'Motor Gasoline'),
    ('10_losses_and_own_use$x$x$x', '07_petroleum_products$07_02_aviation_gasoline'): ('1.A.1 - Energy Industries', 'Aviation Gasoline'),
    ('10_losses_and_own_use$x$x$x', '07_petroleum_products$07_03_naphtha'): ('1.A.1 - Energy Industries', 'Naphtha'),
    ('10_losses_and_own_use$x$x$x', '07_petroleum_products$07_06_kerosene'): ('1.A.1 - Energy Industries', 'Jet Kerosene'),
    ('10_losses_and_own_use$x$x$x', '07_petroleum_products$07_07_gas_diesel_oil'): ('1.A.1 - Energy Industries', 'Diesel Oil'),
    ('10_losses_and_own_use$x$x$x', '07_petroleum_products$07_08_fuel_oil'): ('1.A.1 - Energy Industries', 'Residual Fuel Oil'),
    ('10_losses_and_own_use$x$x$x', '07_petroleum_products$07_09_lpg'): ('1.A.1 - Energy Industries', 'Liquefied Petroleum Gases'),
    ('10_losses_and_own_use$x$x$x', '07_petroleum_products$07_10_refinery_gas_not_liquefied'): ('1.A.1 - Energy Industries', 'Refinery Gas'),
    ('10_losses_and_own_use$x$x$x', '07_petroleum_products$07_x_other_petroleum_products'): ('1.A.1 - Energy Industries', 'Other Petroleum Products'),
    ('10_losses_and_own_use$x$x$x', '07_petroleum_products$x'): ('1.A.1 - Energy Industries', 'Other Petroleum Products'),
    ('10_losses_and_own_use$x$x$x', '08_gas$08_01_natural_gas'): ('1.A.1 - Energy Industries', 'Natural Gas'),
    ('10_losses_and_own_use$x$x$x', '08_gas$08_03_gas_works_gas'): ('1.A.1 - Energy Industries', 'Gas Works Gas'),
    ('10_losses_and_own_use$x$x$x', '08_gas$x'): ('1.A.1 - Energy Industries', 'Natural Gas'),
    ('10_losses_and_own_use$x$x$x', '15_solid_biomass$15_05_other_biomass'): ('1.A.4 - Other Sectors', 'Other Primary Solid Biomass'),
    ('10_losses_and_own_use$x$x$x', '15_solid_biomass$x'): ('1.A.4 - Other Sectors', 'Other Primary Solid Biomass'),
    ('10_losses_and_own_use$x$x$x', '16_others$16_01_biogas'): ('1.A.4 - Other Sectors', 'Other Biogas'),
    ('10_losses_and_own_use$x$x$x', '16_others$16_02_industrial_waste'): ('1.A.4 - Other Sectors', 'Industrial Wastes'),
    ('12_total_final_consumption$x$x$x', '02_coal_products$x'): ('1.A.4 - Other Sectors', 'Other Bituminous Coal'),
    ('12_total_final_consumption$x$x$x', '03_peat$x'): ('1.A.4 - Other Sectors', 'Peat'),
    ('12_total_final_consumption$x$x$x', '04_peat_products$x'): ('1.A.4 - Other Sectors', 'Peat'),
    ('12_total_final_consumption$x$x$x', '06_crude_oil_and_ngl$06_01_crude_oil'): ('1.A.4 - Other Sectors', 'Crude Oil'),
    ('12_total_final_consumption$x$x$x', '06_crude_oil_and_ngl$06_02_natural_gas_liquids'): ('1.A.4 - Other Sectors', 'Natural Gas Liquids (NGLs)'),
    ('12_total_final_consumption$x$x$x', '06_crude_oil_and_ngl$06_x_other_hydrocarbons'): ('1.A.4 - Other Sectors', 'Other Hydrocarbons'),
    ('12_total_final_consumption$x$x$x', '06_crude_oil_and_ngl$x'): ('1.A.4 - Other Sectors', 'Natural Gas Liquids (NGLs)'),
    ('12_total_final_consumption$x$x$x', '07_petroleum_products$07_01_motor_gasoline'): ('1.A.4 - Other Sectors', 'Motor Gasoline'),
    ('12_total_final_consumption$x$x$x', '07_petroleum_products$07_02_aviation_gasoline'): ('1.A.4 - Other Sectors', 'Aviation Gasoline'),
    ('12_total_final_consumption$x$x$x', '07_petroleum_products$07_03_naphtha'): ('1.A.4 - Other Sectors', 'Naphtha'),
    ('12_total_final_consumption$x$x$x', '07_petroleum_products$07_06_kerosene'): ('1.A.4 - Other Sectors', 'Jet Kerosene'),
    ('12_total_final_consumption$x$x$x', '07_petroleum_products$07_07_gas_diesel_oil'): ('1.A.4 - Other Sectors', 'Diesel Oil'),
    ('12_total_final_consumption$x$x$x', '07_petroleum_products$07_08_fuel_oil'): ('1.A.4 - Other Sectors', 'Residual Fuel Oil'),
    ('12_total_final_consumption$x$x$x', '07_petroleum_products$07_09_lpg'): ('1.A.4 - Other Sectors', 'Liquefied Petroleum Gases'),
    ('12_total_final_consumption$x$x$x', '07_petroleum_products$07_10_refinery_gas_not_liquefied'): ('1.A.4 - Other Sectors', 'Refinery Gas'),
    ('12_total_final_consumption$x$x$x', '07_petroleum_products$07_x_other_petroleum_products'): ('1.A.4 - Other Sectors', 'Other Petroleum Products'),
    ('12_total_final_consumption$x$x$x', '07_petroleum_products$x'): ('1.A.4 - Other Sectors', 'Other Petroleum Products'),
    ('12_total_final_consumption$x$x$x', '08_gas$08_01_natural_gas'): ('1.A.4 - Other Sectors', 'Natural Gas'),
    ('12_total_final_consumption$x$x$x', '08_gas$08_03_gas_works_gas'): ('1.A.4 - Other Sectors', 'Gas Works Gas'),
    ('12_total_final_consumption$x$x$x', '08_gas$x'): ('1.A.4 - Other Sectors', 'Natural Gas'),
    ('12_total_final_consumption$x$x$x', '15_solid_biomass$15_03_charcoal'): ('1.A.4 - Other Sectors', 'Charcoal'),
    ('12_total_final_consumption$x$x$x', '15_solid_biomass$15_04_black_liquor'): ('1.A.4 - Other Sectors', 'Sulphite Lyes (Black Liquor)'),
    ('12_total_final_consumption$x$x$x', '15_solid_biomass$15_05_other_biomass'): ('1.A.4 - Other Sectors', 'Other Primary Solid Biomass'),
    ('12_total_final_consumption$x$x$x', '15_solid_biomass$x'): ('1.A.4 - Other Sectors', 'Other Primary Solid Biomass'),
    ('12_total_final_consumption$x$x$x', '16_others$16_01_biogas'): ('1.A.4 - Other Sectors', 'Other Biogas'),
    ('12_total_final_consumption$x$x$x', '16_others$16_02_industrial_waste'): ('1.A.4 - Other Sectors', 'Industrial Wastes'),
    ('12_total_final_consumption$x$x$x', '16_others$16_03_municipal_solid_waste_renewable'): ('1.A.4 - Other Sectors', 'Municipal Wastes (biomass fraction)'),
    ('12_total_final_consumption$x$x$x', '16_others$16_04_municipal_solid_waste_nonrenewable'): ('1.A.4 - Other Sectors', 'Municipal Wastes (non-biomass fraction)'),
    ('12_total_final_consumption$x$x$x', '16_others$16_05_biogasoline'): ('1.A.4 - Other Sectors', 'Biogasoline'),
    ('12_total_final_consumption$x$x$x', '16_others$16_06_biodiesel'): ('1.A.4 - Other Sectors', 'Biodiesels'),
    ('12_total_final_consumption$x$x$x', '16_others$16_08_other_liquid_biofuels'): ('1.A.4 - Other Sectors', 'Other Liquid Biofuels'),
    ('13_total_final_energy_consumption$x$x$x', '02_coal_products$x'): ('1.A.4 - Other Sectors', 'Other Bituminous Coal'),
    ('13_total_final_energy_consumption$x$x$x', '03_peat$x'): ('1.A.4 - Other Sectors', 'Peat'),
    ('13_total_final_energy_consumption$x$x$x', '04_peat_products$x'): ('1.A.4 - Other Sectors', 'Peat'),
    ('13_total_final_energy_consumption$x$x$x', '06_crude_oil_and_ngl$06_01_crude_oil'): ('1.A.4 - Other Sectors', 'Crude Oil'),
    ('13_total_final_energy_consumption$x$x$x', '06_crude_oil_and_ngl$06_02_natural_gas_liquids'): ('1.A.4 - Other Sectors', 'Natural Gas Liquids (NGLs)'),
    ('13_total_final_energy_consumption$x$x$x', '06_crude_oil_and_ngl$x'): ('1.A.4 - Other Sectors', 'Natural Gas Liquids (NGLs)'),
    ('13_total_final_energy_consumption$x$x$x', '07_petroleum_products$07_01_motor_gasoline'): ('1.A.4 - Other Sectors', 'Motor Gasoline'),
    ('13_total_final_energy_consumption$x$x$x', '07_petroleum_products$07_02_aviation_gasoline'): ('1.A.4 - Other Sectors', 'Aviation Gasoline'),
    ('13_total_final_energy_consumption$x$x$x', '07_petroleum_products$07_03_naphtha'): ('1.A.4 - Other Sectors', 'Naphtha'),
    ('13_total_final_energy_consumption$x$x$x', '07_petroleum_products$07_06_kerosene'): ('1.A.4 - Other Sectors', 'Jet Kerosene'),
    ('13_total_final_energy_consumption$x$x$x', '07_petroleum_products$07_07_gas_diesel_oil'): ('1.A.4 - Other Sectors', 'Diesel Oil'),
    ('13_total_final_energy_consumption$x$x$x', '07_petroleum_products$07_08_fuel_oil'): ('1.A.4 - Other Sectors', 'Residual Fuel Oil'),
    ('13_total_final_energy_consumption$x$x$x', '07_petroleum_products$07_09_lpg'): ('1.A.4 - Other Sectors', 'Liquefied Petroleum Gases'),
    ('13_total_final_energy_consumption$x$x$x', '07_petroleum_products$07_10_refinery_gas_not_liquefied'): ('1.A.4 - Other Sectors', 'Refinery Gas'),
    ('13_total_final_energy_consumption$x$x$x', '07_petroleum_products$07_x_other_petroleum_products'): ('1.A.4 - Other Sectors', 'Other Petroleum Products'),
    ('13_total_final_energy_consumption$x$x$x', '07_petroleum_products$x'): ('1.A.4 - Other Sectors', 'Other Petroleum Products'),
    ('13_total_final_energy_consumption$x$x$x', '08_gas$08_01_natural_gas'): ('1.A.4 - Other Sectors', 'Natural Gas'),
    ('13_total_final_energy_consumption$x$x$x', '08_gas$08_03_gas_works_gas'): ('1.A.4 - Other Sectors', 'Gas Works Gas'),
    ('13_total_final_energy_consumption$x$x$x', '08_gas$x'): ('1.A.4 - Other Sectors', 'Natural Gas'),
    ('13_total_final_energy_consumption$x$x$x', '15_solid_biomass$15_02_bagasse'): ('1.A.4 - Other Sectors', 'Bagasse'),
    ('13_total_final_energy_consumption$x$x$x', '15_solid_biomass$15_03_charcoal'): ('1.A.4 - Other Sectors', 'Charcoal'),
    ('13_total_final_energy_consumption$x$x$x', '15_solid_biomass$15_04_black_liquor'): ('1.A.4 - Other Sectors', 'Sulphite Lyes (Black Liquor)'),
    ('13_total_final_energy_consumption$x$x$x', '15_solid_biomass$15_05_other_biomass'): ('1.A.4 - Other Sectors', 'Other Primary Solid Biomass'),
    ('13_total_final_energy_consumption$x$x$x', '15_solid_biomass$x'): ('1.A.4 - Other Sectors', 'Other Primary Solid Biomass'),
    ('13_total_final_energy_consumption$x$x$x', '16_others$16_01_biogas'): ('1.A.4 - Other Sectors', 'Other Biogas'),
    ('13_total_final_energy_consumption$x$x$x', '16_others$16_02_industrial_waste'): ('1.A.4 - Other Sectors', 'Industrial Wastes'),
    ('13_total_final_energy_consumption$x$x$x', '16_others$16_03_municipal_solid_waste_renewable'): ('1.A.4 - Other Sectors', 'Municipal Wastes (biomass fraction)'),
    ('13_total_final_energy_consumption$x$x$x', '16_others$16_04_municipal_solid_waste_nonrenewable'): ('1.A.4 - Other Sectors', 'Municipal Wastes (non-biomass fraction)'),
    ('13_total_final_energy_consumption$x$x$x', '16_others$16_05_biogasoline'): ('1.A.4 - Other Sectors', 'Biogasoline'),
    ('13_total_final_energy_consumption$x$x$x', '16_others$16_06_biodiesel'): ('1.A.4 - Other Sectors', 'Biodiesels'),
    ('13_total_final_energy_consumption$x$x$x', '16_others$16_08_other_liquid_biofuels'): ('1.A.4 - Other Sectors', 'Other Liquid Biofuels'),
    ('16_other_sector$16_01_buildings$x$x', '02_coal_products$x'): ('1.A.4.b - Residential', 'Other Bituminous Coal'),
    ('16_other_sector$16_01_buildings$x$x', '03_peat$x'): ('1.A.4.b - Residential', 'Peat'),
    ('16_other_sector$16_01_buildings$x$x', '04_peat_products$x'): ('1.A.4.b - Residential', 'Peat'),
    ('16_other_sector$16_01_buildings$x$x', '06_crude_oil_and_ngl$06_01_crude_oil'): ('1.A.4.b - Residential', 'Crude Oil'),
    ('16_other_sector$16_01_buildings$x$x', '06_crude_oil_and_ngl$x'): ('1.A.4.b - Residential', 'Natural Gas Liquids (NGLs)'),
    ('16_other_sector$16_01_buildings$x$x', '07_petroleum_products$07_01_motor_gasoline'): ('1.A.4.b - Residential', 'Motor Gasoline'),
    ('16_other_sector$16_01_buildings$x$x', '07_petroleum_products$07_02_aviation_gasoline'): ('1.A.4.b - Residential', 'Aviation Gasoline'),
    ('16_other_sector$16_01_buildings$x$x', '07_petroleum_products$07_03_naphtha'): ('1.A.4.b - Residential', 'Naphtha'),
    ('16_other_sector$16_01_buildings$x$x', '07_petroleum_products$07_06_kerosene'): ('1.A.4.b - Residential', 'Jet Kerosene'),
    ('16_other_sector$16_01_buildings$x$x', '07_petroleum_products$07_07_gas_diesel_oil'): ('1.A.4.b - Residential', 'Diesel Oil'),
    ('16_other_sector$16_01_buildings$x$x', '07_petroleum_products$07_08_fuel_oil'): ('1.A.4.b - Residential', 'Residual Fuel Oil'),
    ('16_other_sector$16_01_buildings$x$x', '07_petroleum_products$07_09_lpg'): ('1.A.4.b - Residential', 'Liquefied Petroleum Gases'),
    ('16_other_sector$16_01_buildings$x$x', '07_petroleum_products$07_10_refinery_gas_not_liquefied'): ('1.A.4.b - Residential', 'Refinery Gas'),
    ('16_other_sector$16_01_buildings$x$x', '07_petroleum_products$07_x_other_petroleum_products'): ('1.A.4.b - Residential', 'Other Petroleum Products'),
    ('16_other_sector$16_01_buildings$x$x', '07_petroleum_products$x'): ('1.A.4.b - Residential', 'Other Petroleum Products'),
    ('16_other_sector$16_01_buildings$x$x', '08_gas$08_01_natural_gas'): ('1.A.4.b - Residential', 'Natural Gas'),
    ('16_other_sector$16_01_buildings$x$x', '08_gas$08_03_gas_works_gas'): ('1.A.4.b - Residential', 'Gas Works Gas'),
    ('16_other_sector$16_01_buildings$x$x', '08_gas$x'): ('1.A.4.b - Residential', 'Natural Gas'),
    ('16_other_sector$16_01_buildings$x$x', '15_solid_biomass$15_02_bagasse'): ('1.A.4.b - Residential', 'Bagasse'),
    ('16_other_sector$16_01_buildings$x$x', '15_solid_biomass$15_03_charcoal'): ('1.A.4.b - Residential', 'Charcoal'),
    ('16_other_sector$16_01_buildings$x$x', '15_solid_biomass$15_05_other_biomass'): ('1.A.4.b - Residential', 'Other Primary Solid Biomass'),
    ('16_other_sector$16_01_buildings$x$x', '15_solid_biomass$x'): ('1.A.4.b - Residential', 'Other Primary Solid Biomass'),
    ('16_other_sector$16_01_buildings$x$x', '16_others$16_01_biogas'): ('1.A.4.b - Residential', 'Other Biogas'),
    ('16_other_sector$16_01_buildings$x$x', '16_others$16_02_industrial_waste'): ('1.A.4.b - Residential', 'Industrial Wastes'),
    ('16_other_sector$16_01_buildings$x$x', '16_others$16_03_municipal_solid_waste_renewable'): ('1.A.4.b - Residential', 'Municipal Wastes (biomass fraction)'),
    ('16_other_sector$16_01_buildings$x$x', '16_others$16_04_municipal_solid_waste_nonrenewable'): ('1.A.4.b - Residential', 'Municipal Wastes (non-biomass fraction)'),
    ('16_other_sector$16_01_buildings$x$x', '16_others$16_05_biogasoline'): ('1.A.4.b - Residential', 'Biogasoline'),
    ('16_other_sector$16_01_buildings$x$x', '16_others$16_06_biodiesel'): ('1.A.4.b - Residential', 'Biodiesels'),
    ('16_other_sector$16_01_buildings$x$x', '16_others$16_08_other_liquid_biofuels'): ('1.A.4.b - Residential', 'Other Liquid Biofuels'),
    
    ('10_losses_and_own_use$10_01_own_use$x$x', '02_coal_products$x'): ('1.A.1 - Energy Industries', 'Coking Coal'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '03_peat$x'): ('1.A.1 - Energy Industries', 'Peat'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '04_peat_products$x'): ('1.A.1 - Energy Industries', 'Peat'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '06_crude_oil_and_ngl$06_01_crude_oil'): ('1.A.1 - Energy Industries', 'Crude Oil'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '06_crude_oil_and_ngl$06_02_natural_gas_liquids'): ('1.A.1 - Energy Industries', 'Natural Gas Liquids (NGLs)'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '06_crude_oil_and_ngl$x'): ('1.A.1 - Energy Industries', 'Crude Oil'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '07_petroleum_products$07_01_motor_gasoline'): ('1.A.1 - Energy Industries', 'Motor Gasoline'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '07_petroleum_products$07_02_aviation_gasoline'): ('1.A.1 - Energy Industries', 'Aviation Gasoline'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '07_petroleum_products$07_03_naphtha'): ('1.A.1 - Energy Industries', 'Naphtha'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '07_petroleum_products$07_06_kerosene'): ('1.A.1 - Energy Industries', 'Jet Kerosene'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '07_petroleum_products$07_07_gas_diesel_oil'): ('1.A.1 - Energy Industries', 'Diesel Oil'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '07_petroleum_products$07_08_fuel_oil'): ('1.A.1 - Energy Industries', 'Residual Fuel Oil'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '07_petroleum_products$07_09_lpg'): ('1.A.1 - Energy Industries', 'Liquefied Petroleum Gases'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '07_petroleum_products$07_10_refinery_gas_not_liquefied'): ('1.A.1 - Energy Industries', 'Refinery Gas'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '07_petroleum_products$07_x_other_petroleum_products'): ('1.A.1 - Energy Industries', 'Other Petroleum Products'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '07_petroleum_products$x'): ('1.A.1 - Energy Industries', 'Other Petroleum Products'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '08_gas$08_01_natural_gas'): ('1.A.1 - Energy Industries', 'Natural Gas'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '08_gas$08_02_lng'): ('1.A.1 - Energy Industries', 'Natural Gas'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '08_gas$08_03_gas_works_gas'): ('1.A.1 - Energy Industries', 'Gas Works Gas'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '08_gas$x'): ('1.A.1 - Energy Industries', 'Natural Gas'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '15_solid_biomass$15_05_other_biomass'): ('1.A.1 - Energy Industries', 'Other Primary Solid Biomass'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '15_solid_biomass$x'): ('1.A.1 - Energy Industries', 'Other Primary Solid Biomass'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '16_others$16_01_biogas'): ('1.A.1 - Energy Industries', 'Other Biogas'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '16_others$16_02_industrial_waste'): ('1.A.1 - Energy Industries', 'Industrial Wastes'),
    ('10_losses_and_own_use$10_01_own_use$x$x', '16_others$16_06_biodiesel'): ('1.A.1 - Energy Industries', 'Biodiesels'),
    ('10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x', '02_coal_products$x'): ('1.A.1 - Energy Industries', 'Coke Oven Coke and Lignite Coke'),
    ('10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x', '06_crude_oil_and_ngl$06_01_crude_oil'): ('1.A.1 - Energy Industries', 'Crude Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x', '06_crude_oil_and_ngl$06_02_natural_gas_liquids'): ('1.A.1 - Energy Industries', 'Natural Gas Liquids (NGLs)'),
    ('10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x', '06_crude_oil_and_ngl$x'): ('1.A.1 - Energy Industries', 'Crude Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x', '07_petroleum_products$07_01_motor_gasoline'): ('1.A.1 - Energy Industries', 'Motor Gasoline'),
    ('10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x', '07_petroleum_products$07_06_kerosene'): ('1.A.1 - Energy Industries', 'Jet Kerosene'),
    ('10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x', '07_petroleum_products$07_07_gas_diesel_oil'): ('1.A.1 - Energy Industries', 'Diesel Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x', '07_petroleum_products$07_08_fuel_oil'): ('1.A.1 - Energy Industries', 'Residual Fuel Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x', '07_petroleum_products$07_09_lpg'): ('1.A.1 - Energy Industries', 'Liquefied Petroleum Gases'),
    ('10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x', '07_petroleum_products$07_10_refinery_gas_not_liquefied'): ('1.A.1 - Energy Industries', 'Refinery Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x', '07_petroleum_products$07_x_other_petroleum_products'): ('1.A.1 - Energy Industries', 'Other Petroleum Products'),
    ('10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x', '07_petroleum_products$x'): ('1.A.1 - Energy Industries', 'Other Petroleum Products'),
    ('10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x', '08_gas$08_01_natural_gas'): ('1.A.1 - Energy Industries', 'Natural Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x', '08_gas$08_03_gas_works_gas'): ('1.A.1 - Energy Industries', 'Gas Works Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x', '08_gas$x'): ('1.A.1 - Energy Industries', 'Natural Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x', '06_crude_oil_and_ngl$06_01_crude_oil'): ('1.A.1 - Energy Industries', 'Crude Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x', '06_crude_oil_and_ngl$x'): ('1.A.1 - Energy Industries', 'Crude Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x', '07_petroleum_products$07_01_motor_gasoline'): ('1.A.1 - Energy Industries', 'Motor Gasoline'),
    ('10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x', '07_petroleum_products$07_06_kerosene'): ('1.A.1 - Energy Industries', 'Jet Kerosene'),
    ('10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x', '07_petroleum_products$07_07_gas_diesel_oil'): ('1.A.1 - Energy Industries', 'Diesel Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x', '07_petroleum_products$07_08_fuel_oil'): ('1.A.1 - Energy Industries', 'Residual Fuel Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x', '07_petroleum_products$07_09_lpg'): ('1.A.1 - Energy Industries', 'Liquefied Petroleum Gases'),
    ('10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x', '07_petroleum_products$07_x_other_petroleum_products'): ('1.A.1 - Energy Industries', 'Other Petroleum Products'),
    ('10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x', '07_petroleum_products$x'): ('1.A.1 - Energy Industries', 'Other Petroleum Products'),
    ('10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x', '08_gas$08_01_natural_gas'): ('1.A.1 - Energy Industries', 'Natural Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x', '08_gas$x'): ('1.A.1 - Energy Industries', 'Natural Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x', '07_petroleum_products$07_09_lpg'): ('1.B.2 - Oil and Natural Gas', 'Liquefied Petroleum Gases'),
    ('10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x', '07_petroleum_products$07_x_other_petroleum_products'): ('1.B.2 - Oil and Natural Gas', 'Other Petroleum Products'),
    ('10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x', '07_petroleum_products$x'): ('1.B.2 - Oil and Natural Gas', 'Other Petroleum Products'),
    ('10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x', '08_gas$08_01_natural_gas'): ('1.B.2 - Oil and Natural Gas', 'Natural Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x', '08_gas$x'): ('1.B.2 - Oil and Natural Gas', 'Natural Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x', '07_petroleum_products$07_01_motor_gasoline'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Motor Gasoline'),
    ('10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x', '07_petroleum_products$07_06_kerosene'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Other Kerosene'),
    ('10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x', '07_petroleum_products$07_07_gas_diesel_oil'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Diesel Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x', '07_petroleum_products$07_08_fuel_oil'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Residual Fuel Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x', '07_petroleum_products$07_09_lpg'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Liquefied Petroleum Gases'),
    ('10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x', '07_petroleum_products$07_x_other_petroleum_products'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Other Petroleum Products'),
    ('10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x', '07_petroleum_products$x'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Other Petroleum Products'),
    ('10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x', '08_gas$08_01_natural_gas'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Natural Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x', '08_gas$08_03_gas_works_gas'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Gas Works Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x', '08_gas$x'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Natural Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x', '02_coal_products$x'): ('1.B.1 - Solid Fuel Transformation', 'Coke Oven Coke and Lignite Coke'),
    ('10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x', '06_crude_oil_and_ngl$06_01_crude_oil'): ('1.B.1 - Solid Fuel Transformation', 'Crude Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x', '06_crude_oil_and_ngl$x'): ('1.B.1 - Solid Fuel Transformation', 'Crude Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x', '07_petroleum_products$07_01_motor_gasoline'): ('1.B.1 - Solid Fuel Transformation', 'Motor Gasoline'),
    ('10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x', '07_petroleum_products$07_06_kerosene'): ('1.B.1 - Solid Fuel Transformation', 'Other Kerosene'),
    ('10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x', '07_petroleum_products$07_07_gas_diesel_oil'): ('1.B.1 - Solid Fuel Transformation', 'Diesel Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x', '07_petroleum_products$07_08_fuel_oil'): ('1.B.1 - Solid Fuel Transformation', 'Residual Fuel Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x', '07_petroleum_products$07_09_lpg'): ('1.B.1 - Solid Fuel Transformation', 'Liquefied Petroleum Gases'),
    ('10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x', '07_petroleum_products$07_10_refinery_gas_not_liquefied'): ('1.B.1 - Solid Fuel Transformation', 'Refinery Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x', '07_petroleum_products$07_x_other_petroleum_products'): ('1.B.1 - Solid Fuel Transformation', 'Other Petroleum Products'),
    ('10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x', '07_petroleum_products$x'): ('1.B.1 - Solid Fuel Transformation', 'Other Petroleum Products'),
    ('10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x', '08_gas$08_01_natural_gas'): ('1.B.1 - Solid Fuel Transformation', 'Natural Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x', '08_gas$08_03_gas_works_gas'): ('1.B.1 - Solid Fuel Transformation', 'Gas Works Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x', '08_gas$x'): ('1.B.1 - Solid Fuel Transformation', 'Natural Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_10_blast_furnaces$x', '02_coal_products$x'): ('1.A.2.a - Iron and Steel', 'Coke Oven Coke and Lignite Coke'),
    ('10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x', '07_petroleum_products$07_07_gas_diesel_oil'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Diesel Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x', '07_petroleum_products$07_08_fuel_oil'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Residual Fuel Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x', '07_petroleum_products$07_09_lpg'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Liquefied Petroleum Gases'),
    ('10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x', '07_petroleum_products$07_10_refinery_gas_not_liquefied'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Refinery Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x', '07_petroleum_products$07_x_other_petroleum_products'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Other Petroleum Products'),
    ('10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x', '07_petroleum_products$x'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Other Petroleum Products'),
    ('10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x', '08_gas$08_01_natural_gas'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Natural Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x', '08_gas$x'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Natural Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x', '06_crude_oil_and_ngl$06_02_natural_gas_liquids'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Natural Gas Liquids (NGLs)'),
    ('10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x', '06_crude_oil_and_ngl$x'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Crude Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x', '07_petroleum_products$07_01_motor_gasoline'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Motor Gasoline'),
    ('10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x', '07_petroleum_products$07_07_gas_diesel_oil'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Diesel Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x', '07_petroleum_products$07_08_fuel_oil'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Residual Fuel Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x', '07_petroleum_products$07_09_lpg'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Liquefied Petroleum Gases'),
    ('10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x', '07_petroleum_products$07_x_other_petroleum_products'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Other Petroleum Products'),
    ('10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x', '07_petroleum_products$x'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Other Petroleum Products'),
    ('10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x', '08_gas$08_01_natural_gas'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Natural Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x', '08_gas$x'): ('1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries', 'Natural Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x', '06_crude_oil_and_ngl$06_01_crude_oil'): ('1.A.1.b - Petroleum Refining', 'Crude Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x', '06_crude_oil_and_ngl$06_02_natural_gas_liquids'): ('1.A.1.b - Petroleum Refining', 'Natural Gas Liquids (NGLs)'),
    ('10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x', '06_crude_oil_and_ngl$x'): ('1.A.1.b - Petroleum Refining', 'Crude Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x', '07_petroleum_products$07_01_motor_gasoline'): ('1.A.1.b - Petroleum Refining', 'Motor Gasoline'),
    ('10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x', '07_petroleum_products$07_03_naphtha'): ('1.A.1.b - Petroleum Refining', 'Naphtha'),
    ('10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x', '07_petroleum_products$07_06_kerosene'): ('1.A.1.b - Petroleum Refining', 'Other Kerosene'),
    ('10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x', '07_petroleum_products$07_08_fuel_oil'): ('1.A.1.b - Petroleum Refining', 'Residual Fuel Oil'),
    ('10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x', '07_petroleum_products$07_09_lpg'): ('1.A.1.b - Petroleum Refining', 'Liquefied Petroleum Gases'),
    ('10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x', '07_petroleum_products$07_10_refinery_gas_not_liquefied'): ('1.A.1.b - Petroleum Refining', 'Refinery Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x', '07_petroleum_products$07_x_other_petroleum_products'): ('1.A.1.b - Petroleum Refining', 'Other Petroleum Products'),
    ('10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x', '07_petroleum_products$x'): ('1.A.1.b - Petroleum Refining', 'Other Petroleum Products'),
    ('10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x', '08_gas$08_01_natural_gas'): ('1.A.1.b - Petroleum Refining', 'Natural Gas'),
    ('10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x', '08_gas$x'): ('1.A.1.b - Petroleum Refining', 'Natural Gas'),
    # Electricity, CHP, and Heat Plants Own Use
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "07_petroleum_products$07_01_motor_gasoline"):
        ("1.A.2.g - Other Manufacturing Industries", "Motor Gasoline"),
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.2.g - Other Manufacturing Industries", "Other Kerosene"),
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.2.g - Other Manufacturing Industries", "Gas/Diesel Oil"),
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.2.g - Other Manufacturing Industries", "Residual Fuel Oil"),
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "15_solid_biomass$15_05_other_biomass"):
        ("1.A.2.g - Other Manufacturing Industries", "Other Primary Solid Biomass"),
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "15_solid_biomass$x"):
        ("1.A.2.g - Other Manufacturing Industries", "Wood/Wood Waste"),
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "16_others$16_02_industrial_waste"):
        ("1.A.2.g - Other Manufacturing Industries", "Industrial Wastes"),
    
    # Gas Works Plants Own Use
    ("10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.2.g - Other Manufacturing Industries", "Liquefied Petroleum Gases"),
    ("10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x", "07_petroleum_products$x"):
        ("1.A.2.g - Other Manufacturing Industries", "Other Petroleum Products"),
    ("10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x", "08_gas$08_03_gas_works_gas"):
        ("1.A.2.g - Other Manufacturing Industries", "Gas Works Gas"),
    ("10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x", "08_gas$x"):
        ("1.A.2.g - Other Manufacturing Industries", "Natural Gas"),
    
    # Liquefaction/Regasification Plants Own Use
    ("10_losses_and_own_use$10_01_own_use$10_01_03_liquefaction_regasification_plants$x", "08_gas$08_01_natural_gas"):
        ("1.A.2.g - Other Manufacturing Industries", "Natural Gas"),
    ("10_losses_and_own_use$10_01_own_use$10_01_03_liquefaction_regasification_plants$x", "08_gas$x"):
        ("1.A.2.g - Other Manufacturing Industries", "Natural Gas"),
    
    # Gas to Liquids Plants Own Use
    ("10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x", "02_coal_products$x"):
        ("1.A.2.g - Other Manufacturing Industries", "Coke Oven Coke and Lignite Coke"),
    ("10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.2.g - Other Manufacturing Industries", "Residual Fuel Oil"),
    ("10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x", "07_petroleum_products$x"):
        ("1.A.2.g - Other Manufacturing Industries", "Other Petroleum Products"),
    ("10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x", "08_gas$08_01_natural_gas"):
        ("1.A.2.g - Other Manufacturing Industries", "Natural Gas"),
    
    # Gas Separation Own Use
    ("10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x", "01_coal$x"):
        ("1.A.2.g - Other Manufacturing Industries", "Other Bituminous Coal"),
    ("10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x", "02_coal_products$x"):
        ("1.A.2.g - Other Manufacturing Industries", "Coke Oven Coke and Lignite Coke"),
    ("10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.2.g - Other Manufacturing Industries", "Gas/Diesel Oil"),
    ("10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.2.g - Other Manufacturing Industries", "Residual Fuel Oil"),
    # Continue mapping all combinations in the same pattern...
    
    # Coke Ovens Own Use
    ("10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x", "01_coal$x"):
        ("1.A.2.a - Iron and Steel", "Other Bituminous Coal"),
    ("10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x", "02_coal_products$x"):
        ("1.A.2.a - Iron and Steel", "Coke Oven Coke and Lignite Coke"),
    ("10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x", "06_crude_oil_and_ngl$x"):
        ("1.A.2.a - Iron and Steel", "Crude Oil"),
    # Continue mapping...
    
    # Coal Mines Own Use
    ("10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x", "01_coal$x"):
        ("1.A.2.a - Iron and Steel", "Other Bituminous Coal"),
    # Continue mapping...
    
    # BKB/PB Plants Own Use
    ("10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x", "02_coal_products$x"):
        ("1.A.2.c - Chemicals", "Patent Fuel"),
    # Continue mapping...
    
    # Liquefaction Plants (Coal to Oil) Own Use
    ("10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x", "06_crude_oil_and_ngl$06_01_crude_oil"):
        ("1.A.2.g - Other Manufacturing Industries", "Crude Oil"),
    # Continue mapping...
    
    # Oil Refineries Own Use
    ("10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x", "01_coal$x"):
        ("1.A.2.b - Petroleum Refining", "Other Bituminous Coal"),
    # Continue mapping...
    
    # Oil and Gas Extraction Own Use
    ("10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x", "01_coal$x"):
        ("1.A.2.f - Mining (excluding fuels) and Quarrying", "Other Bituminous Coal"),
    # Continue mapping...
    
    # Non-specified Own Uses
    ("10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x", "02_coal_products$x"):
        ("1.A.2.g - Other Manufacturing Industries", "Coke Oven Coke and Lignite Coke"),
    # Continue mapping...
    
    # Own Use (Unspecified)
    ("10_losses_and_own_use$10_01_own_use$x$x", "01_coal$x"):
        ("1.A.2.g - Other Manufacturing Industries", "Other Bituminous Coal"),
    # Continue mapping...
    
    # Transmission and Distribution Losses
    ("10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x", "01_coal$x"):
        ("1.A.2.g - Other Manufacturing Industries", "Other Bituminous Coal"),
    # Continue mapping...
    
    # Losses and Own Use (Unspecified)
    ("10_losses_and_own_use$x$x$x", "01_coal$x"):
        ("1.A.2.g - Other Manufacturing Industries", "Other Bituminous Coal"),
    # Continue mapping...
    
    # Total Final Consumption
    ("12_total_final_consumption$x$x$x", "01_coal$x"):
        ("1.A.4 - Other Sectors", "Other Bituminous Coal"),
    # Continue mapping...
    
    # Total Final Energy Consumption
    ("13_total_final_energy_consumption$x$x$x", "01_coal$x"):
        ("1.A.4 - Other Sectors", "Other Bituminous Coal"),
    # Continue mapping...
    
    # Other Sector - Buildings
    ("16_other_sector$16_01_buildings$x$x", "01_coal$x"):
        ("1.A.4.b - Residential", "Other Bituminous Coal"),
    # Continue mapping...
    
    # Other Sector - Agriculture and Fishing
    ("16_other_sector$16_02_agriculture_and_fishing$x$x", "01_coal$x"):
        ("1.A.4.c - Agriculture/Forestry/Fishing", "Other Bituminous Coal"),
    # Continue mapping...
    
    # Other Sector - Non-specified Others
    ("16_other_sector$16_05_nonspecified_others$x$x", "01_coal$x"):
        ("1.A.4 - Other Sectors", "Other Bituminous Coal"),
    # Continue mapping...
    
    # Other Sector (Unspecified)
    ("16_other_sector$x$x$x", "01_coal$x"):
        ("1.A.4 - Other Sectors", "Other Bituminous Coal"),
    # Continue mapping...
    
    # Non-energy Use
    ("17_nonenergy_use$x$x$x", "01_coal$x"):
        ("1.A.2.g - Other Manufacturing Industries", "Other Bituminous Coal"),
    # Continue mapping...
    # Coking Coal Mappings
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "01_coal$01_01_coking_coal"):
        ("1.A.1 - Energy Industries", "Coking Coal"),
    ("10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x", "01_coal$01_01_coking_coal"):
        ("1.A.1 - Energy Industries", "Coking Coal"),
    ("10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x", "01_coal$01_01_coking_coal"):
        ("1.A.1 - Energy Industries", "Coking Coal"),
    ("10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x", "01_coal$01_01_coking_coal"):
        ("1.A.1 - Energy Industries", "Coking Coal"),
    ("10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x", "01_coal$01_01_coking_coal"):
        ("1.A.1 - Energy Industries", "Coking Coal"),
    ("10_losses_and_own_use$10_01_own_use$x$x", "01_coal$01_01_coking_coal"):
        ("1.A.1 - Energy Industries", "Coking Coal"),
    ("10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x", "01_coal$01_01_coking_coal"):
        ("1.A.1 - Energy Industries", "Coking Coal"),
    ("10_losses_and_own_use$x$x$x", "01_coal$01_01_coking_coal"):
        ("1.A.1 - Energy Industries", "Coking Coal"),
    ("12_total_final_consumption$x$x$x", "01_coal$01_01_coking_coal"):
        ("1.A - Fuel Combustion Activities", "Coking Coal"),
    ("13_total_final_energy_consumption$x$x$x", "01_coal$01_01_coking_coal"):
        ("1.A - Fuel Combustion Activities", "Coking Coal"),
    ("16_other_sector$16_01_buildings$x$x", "01_coal$01_01_coking_coal"):
        ("1.A.4 - Other Sectors", "Coking Coal"),
    ("16_other_sector$16_02_agriculture_and_fishing$x$x", "01_coal$01_01_coking_coal"):
        ("1.A.4 - Other Sectors", "Coking Coal"),
    ("16_other_sector$16_05_nonspecified_others$x$x", "01_coal$01_01_coking_coal"):
        ("1.A.4 - Other Sectors", "Coking Coal"),
    ("16_other_sector$x$x$x", "01_coal$01_01_coking_coal"):
        ("1.A.4 - Other Sectors", "Coking Coal"),
    ("17_nonenergy_use$x$x$x", "01_coal$01_01_coking_coal"):
        ("1.A.1 - Energy Industries", "Coking Coal"),
    
    # Lignite Mappings
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "01_coal$01_05_lignite"):
        ("1.A.1 - Energy Industries", "Lignite"),
    ("10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x", "01_coal$01_05_lignite"):
        ("1.A.1 - Energy Industries", "Lignite"),
    ("10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x", "01_coal$01_05_lignite"):
        ("1.A.1 - Energy Industries", "Lignite"),
    ("10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x", "01_coal$01_05_lignite"):
        ("1.A.1 - Energy Industries", "Lignite"),
    ("10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x", "01_coal$01_05_lignite"):
        ("1.A.1 - Energy Industries", "Lignite"),
    ("10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x", "01_coal$01_05_lignite"):
        ("1.A.1 - Energy Industries", "Lignite"),
    ("10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x", "01_coal$01_05_lignite"):
        ("1.A.1 - Energy Industries", "Lignite"),
    ("10_losses_and_own_use$10_01_own_use$x$x", "01_coal$01_05_lignite"):
        ("1.A.1 - Energy Industries", "Lignite"),
    ("10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x", "01_coal$01_05_lignite"):
        ("1.A.1 - Energy Industries", "Lignite"),
    ("10_losses_and_own_use$x$x$x", "01_coal$01_05_lignite"):
        ("1.A.1 - Energy Industries", "Lignite"),
    ("12_total_final_consumption$x$x$x", "01_coal$01_05_lignite"):
        ("1.A - Fuel Combustion Activities", "Lignite"),
    ("13_total_final_energy_consumption$x$x$x", "01_coal$01_05_lignite"):
        ("1.A - Fuel Combustion Activities", "Lignite"),
    ("16_other_sector$16_01_buildings$x$x", "01_coal$01_05_lignite"):
        ("1.A.4 - Other Sectors", "Lignite"),
    ("16_other_sector$16_02_agriculture_and_fishing$x$x", "01_coal$01_05_lignite"):
        ("1.A.4 - Other Sectors", "Lignite"),
    ("16_other_sector$16_05_nonspecified_others$x$x", "01_coal$01_05_lignite"):
        ("1.A.4 - Other Sectors", "Lignite"),
    ("16_other_sector$x$x$x", "01_coal$01_05_lignite"):
        ("1.A.4 - Other Sectors", "Lignite"),
    ("17_nonenergy_use$x$x$x", "01_coal$01_05_lignite"):
        ("1.A.1 - Energy Industries", "Lignite"),
    
    # Thermal Coal Mappings (Mapped to Other Bituminous Coal)
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    ("10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    ("10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    ("10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    ("10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    ("10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    ("10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    ("10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    ("10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    ("10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    ("10_losses_and_own_use$10_01_own_use$x$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    ("10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    ("10_losses_and_own_use$x$x$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    ("12_total_final_consumption$x$x$x", "01_coal$01_x_thermal_coal"):
        ("1.A - Fuel Combustion Activities", "Other Bituminous Coal"),
    ("13_total_final_energy_consumption$x$x$x", "01_coal$01_x_thermal_coal"):
        ("1.A - Fuel Combustion Activities", "Other Bituminous Coal"),
    ("16_other_sector$16_01_buildings$x$x", "01_coal$01_x_thermal_coal"):
        ("1.A.4 - Other Sectors", "Other Bituminous Coal"),
    ("16_other_sector$16_02_agriculture_and_fishing$x$x", "01_coal$01_x_thermal_coal"):
        ("1.A.4 - Other Sectors", "Other Bituminous Coal"),
    ("16_other_sector$16_05_nonspecified_others$x$x", "01_coal$01_x_thermal_coal"):
        ("1.A.4 - Other Sectors", "Other Bituminous Coal"),
    ("16_other_sector$x$x$x", "01_coal$01_x_thermal_coal"):
        ("1.A.4 - Other Sectors", "Other Bituminous Coal"),
    ("17_nonenergy_use$x$x$x", "01_coal$01_x_thermal_coal"):
        ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    
    # Unspecified Coal Mappings (Mapped to Other Bituminous Coal)
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "01_coal$x"):
        ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    ("10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x", "01_coal$x"):
        ("1.A.1 - Energy Industries", "Other Bituminous Coal"),
    # ... (Continue with the rest of the unspecified coal mappings)

    # Coal Products Mappings
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "02_coal_products$x"):
        ("1.A.1 - Energy Industries", "Coke Oven Coke and Lignite Coke"),
    # ... (Continue with the rest of the coal products mappings)

    # Peat Mappings
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "03_peat$x"):
        ("1.A.1 - Energy Industries", "Peat"),
    # ... (Continue with the rest of the peat mappings)

    # Peat Products Mappings (Mapped to Peat)
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "04_peat_products$x"):
        ("1.A.1 - Energy Industries", "Peat"),
    # ... (Continue with the rest of the peat products mappings)

    # Crude Oil Mappings
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "06_crude_oil_and_ngl$06_01_crude_oil"):
        ("1.A.1 - Energy Industries", "Crude Oil"),
    # ... (Continue with the rest of the crude oil mappings)

    # Natural Gas Liquids (NGLs) Mappings
    ("10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x", "06_crude_oil_and_ngl$06_02_natural_gas_liquids"):
        ("1.A.1 - Energy Industries", "Natural Gas Liquids (NGLs)"),
    # ... (Continue with the rest of the NGLs mappings)

    # Unspecified Crude Oil and NGLs Mappings (Mapped to Crude Oil)
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "06_crude_oil_and_ngl$x"):
        ("1.A.1 - Energy Industries", "Crude Oil"),
    # ... (Continue with the rest of the unspecified crude oil and NGLs mappings)

    # Motor Gasoline Mappings
    ("04_international_marine_bunkers$x$x$x", "07_petroleum_products$07_01_motor_gasoline"):
        ("1.A.3.d - International Water-Borne Navigation", "Motor Gasoline"),
    ("05_international_aviation_bunkers$x$x$x", "07_petroleum_products$07_01_motor_gasoline"):
        ("1.A.3.a - International Aviation", "Motor Gasoline"),
    # ... (Continue with the rest of the motor gasoline mappings)

    # Aviation Gasoline Mappings
    ("05_international_aviation_bunkers$x$x$x", "07_petroleum_products$07_02_aviation_gasoline"):
        ("1.A.3.a - International Aviation", "Aviation Gasoline"),
    # ... (Continue with the rest of the aviation gasoline mappings)

    # Naphtha Mappings
    ("10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x", "07_petroleum_products$07_03_naphtha"):
        ("1.A.1 - Energy Industries", "Naphtha"),
    # ... (Continue with the rest of the naphtha mappings)

    # Kerosene Mappings
    ("04_international_marine_bunkers$x$x$x", "07_petroleum_products$07_06_kerosene"):
        ("1.A.3.d - International Water-Borne Navigation", "Other Kerosene"),
    # ... (Continue with the rest of the kerosene mappings)

    # Gas/Diesel Oil Mappings
    ("04_international_marine_bunkers$x$x$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.3.d - International Water-Borne Navigation", "Gas Oil"),
    ("05_international_aviation_bunkers$x$x$x", "07_petroleum_products$07_07_gas_diesel_oil"):
        ("1.A.3.a - International Aviation", "Gas Oil"),
    # ... (Continue with the rest of the gas/diesel oil mappings)

    # Fuel Oil Mappings
    ("04_international_marine_bunkers$x$x$x", "07_petroleum_products$07_08_fuel_oil"):
        ("1.A.3.d - International Water-Borne Navigation", "Residual Fuel Oil"),
    # ... (Continue with the rest of the fuel oil mappings)

    # LPG Mappings
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "07_petroleum_products$07_09_lpg"):
        ("1.A.1 - Energy Industries", "Liquefied Petroleum Gases"),
    # ... (Continue with the rest of the LPG mappings)

    # Refinery Gas Mappings
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "07_petroleum_products$07_10_refinery_gas_not_liquefied"):
        ("1.A.1 - Energy Industries", "Refinery Gas"),
    # ... (Continue with the rest of the refinery gas mappings)

    # Natural Gas Mappings
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "08_gas$08_01_natural_gas"):
        ("1.A.1 - Energy Industries", "Natural Gas"),
#################

    # Ethane Mappings
    ("10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x", "07_petroleum_products$07_11_ethane"):
        ("1.A.1 - Energy Industries", "Ethane"),
    ("10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x", "07_petroleum_products$07_11_ethane"):
        ("1.A.1 - Energy Industries", "Ethane"),
    ("10_losses_and_own_use$10_01_own_use$x$x", "07_petroleum_products$07_11_ethane"):
        ("1.A.1 - Energy Industries", "Ethane"),
    ("10_losses_and_own_use$x$x$x", "07_petroleum_products$07_11_ethane"):
        ("1.A.1 - Energy Industries", "Ethane"),
    ("12_total_final_consumption$x$x$x", "07_petroleum_products$07_11_ethane"):
        ("1.A - Fuel Combustion Activities", "Ethane"),
    ("13_total_final_energy_consumption$x$x$x", "07_petroleum_products$07_11_ethane"):
        ("1.A - Fuel Combustion Activities", "Ethane"),
    ("17_nonenergy_use$x$x$x", "07_petroleum_products$07_11_ethane"):
        ("1.A.1 - Energy Industries", "Ethane"),
    
    # Jet Fuel Mappings (mapped to Jet Kerosene)
    ("04_international_marine_bunkers$x$x$x", "07_petroleum_products$07_x_jet_fuel"):
        ("1.A - Fuel Combustion Activities", "Jet Kerosene"),
    ("05_international_aviation_bunkers$x$x$x", "07_petroleum_products$07_x_jet_fuel"):
        ("1.A - Fuel Combustion Activities", "Jet Kerosene"),
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "07_petroleum_products$07_x_jet_fuel"):
        ("1.A.1 - Energy Industries", "Jet Kerosene"),
    ("10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x", "07_petroleum_products$07_x_jet_fuel"):
        ("1.A.1 - Energy Industries", "Jet Kerosene"),
    ("10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x", "07_petroleum_products$07_x_jet_fuel"):
        ("1.A.1 - Energy Industries", "Jet Kerosene"),
    ("10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x", "07_petroleum_products$07_x_jet_fuel"):
        ("1.A.1 - Energy Industries", "Jet Kerosene"),
    ("10_losses_and_own_use$10_01_own_use$x$x", "07_petroleum_products$07_x_jet_fuel"):
        ("1.A.1 - Energy Industries", "Jet Kerosene"),
    ("10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x", "07_petroleum_products$07_x_jet_fuel"):
        ("1.A.1 - Energy Industries", "Jet Kerosene"),
    ("10_losses_and_own_use$x$x$x", "07_petroleum_products$07_x_jet_fuel"):
        ("1.A.1 - Energy Industries", "Jet Kerosene"),
    ("12_total_final_consumption$x$x$x", "07_petroleum_products$07_x_jet_fuel"):
        ("1.A - Fuel Combustion Activities", "Jet Kerosene"),
    ("13_total_final_energy_consumption$x$x$x", "07_petroleum_products$07_x_jet_fuel"):
        ("1.A - Fuel Combustion Activities", "Jet Kerosene"),
    ("16_other_sector$16_01_buildings$x$x", "07_petroleum_products$07_x_jet_fuel"):
        ("1.A - Fuel Combustion Activities", "Jet Kerosene"),
    ("16_other_sector$16_05_nonspecified_others$x$x", "07_petroleum_products$07_x_jet_fuel"):
        ("1.A - Fuel Combustion Activities", "Jet Kerosene"),
    ("16_other_sector$x$x$x", "07_petroleum_products$07_x_jet_fuel"):
        ("1.A - Fuel Combustion Activities", "Jet Kerosene"),
    
    # Other Petroleum Products Mappings
    ("04_international_marine_bunkers$x$x$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A - Fuel Combustion Activities", "Other Petroleum Products"),
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.1 - Energy Industries", "Other Petroleum Products"),
    ("10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x", "07_petroleum_products$07_x_other_petroleum_products"):
        ("1.A.1 - Energy Industries", "Other Petroleum Products"),
    # ... (Continue mapping all other sectors with '07_petroleum_products$07_x_other_petroleum_products')
    
    # Unspecified Petroleum Products Mappings (mapped to Other Petroleum Products)
    ("04_international_marine_bunkers$x$x$x", "07_petroleum_products$x"):
        ("1.A - Fuel Combustion Activities", "Other Petroleum Products"),
    ("05_international_aviation_bunkers$x$x$x", "07_petroleum_products$x"):
        ("1.A - Fuel Combustion Activities", "Other Petroleum Products"),
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "07_petroleum_products$x"):
        ("1.A.1 - Energy Industries", "Other Petroleum Products"),
    # ... (Continue mapping all other sectors with '07_petroleum_products$x')
    
    # Natural Gas Mappings
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "08_gas$08_01_natural_gas"):
        ("1.A.1 - Energy Industries", "Natural Gas"),
    # ... (Continue mapping all other sectors with '08_gas$08_01_natural_gas')
    
    # LNG Mappings (mapped to Natural Gas)
    ("10_losses_and_own_use$10_01_own_use$10_01_03_liquefaction_regasification_plants$x", "08_gas$08_02_lng"):
        ("1.A.1 - Energy Industries", "Natural Gas"),
    # ... (Continue mapping all other sectors with '08_gas$08_02_lng')
    
    # Gas Works Gas Mappings
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "08_gas$08_03_gas_works_gas"):
        ("1.A.1 - Energy Industries", "Gas Works Gas"),
    # ... (Continue mapping all other sectors with '08_gas$08_03_gas_works_gas')
    
    # Unspecified Gas Mappings (mapped to Natural Gas)
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "08_gas$x"):
        ("1.A.1 - Energy Industries", "Natural Gas"),
    # ... (Continue mapping all other sectors with '08_gas$x')
    
    # Solid Biomass Mappings
    ("12_total_final_consumption$x$x$x", "15_solid_biomass$15_01_fuelwood_and_woodwaste"):
        ("1.A - Fuel Combustion Activities", "Wood/Wood Waste"),
    ("13_total_final_energy_consumption$x$x$x", "15_solid_biomass$15_01_fuelwood_and_woodwaste"):
        ("1.A - Fuel Combustion Activities", "Wood/Wood Waste"),
    ("16_other_sector$16_01_buildings$x$x", "15_solid_biomass$15_01_fuelwood_and_woodwaste"):
        ("1.A - Fuel Combustion Activities", "Wood/Wood Waste"),
    # ... (Continue mapping all other sectors with '15_solid_biomass$15_01_fuelwood_and_woodwaste')
    
    # Other Biomass Mappings
    ("12_total_final_consumption$x$x$x", "15_solid_biomass$15_02_bagasse"):
        ("1.A - Fuel Combustion Activities", "Other Primary Solid Biomass"),
    # ... (Continue mapping all other sectors with '15_solid_biomass$15_02_bagasse')
    
    # Biogas Mappings
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "16_others$16_01_biogas"):
        ("1.A.1 - Energy Industries", "Other Biogas"),
    # ... (Continue mapping all other sectors with '16_others$16_01_biogas')
    
    # Biodiesel Mappings
    ("04_international_marine_bunkers$x$x$x", "16_others$16_06_biodiesel"):
        ("1.A - Fuel Combustion Activities", "Biodiesels"),
    # ... (Continue mapping all other sectors with '16_others$16_06_biodiesel')
    
    # Other Liquid Biofuels Mappings
    ("12_total_final_consumption$x$x$x", "16_others$16_08_other_liquid_biofuels"):
        ("1.A - Fuel Combustion Activities", "Other Liquid Biofuels"),
    # ... (Continue mapping all other sectors with '16_others$16_08_other_liquid_biofuels')
}

#BELOW ARE THE PROMPTS I USED (USING CHATGPT O1):
#Please map the following aperc sector, fuel combinations to one of the following IPCC 2006 Source/Sink Category, Fuel 2006 combinations and put it in a python dict. ignore the row numbers. (for the IPCC sector categories tr to prioritise mapping using the transport realted sectors rather than the 1.A.1 - Energy Industries sector):
# APERC:
# 	aperc_sector	aperc_fuel
# 58	15_transport_sector$15_03_rail$x$x	01_coal$01_01_coking_coal
# 59	15_transport_sector$15_04_domestic_navigation$x$x	01_coal$01_01_coking_coal
# 60	15_transport_sector$x$x$x	01_coal$01_01_coking_coal
# 208	15_transport_sector$15_03_rail$x$x	01_coal$01_05_lignite
# 209	15_transport_sector$x$x$x	01_coal$01_05_lignite
# 458	15_transport_sector$15_03_rail$x$x	01_coal$01_x_thermal_coal
# 460	15_transport_sector$15_04_domestic_navigation$x$x	01_coal$01_x_thermal_coal
# 462	15_transport_sector$15_06_nonspecified_transport$x$x	01_coal$01_x_thermal_coal
# 464	15_transport_sector$x$x$x	01_coal$01_x_thermal_coal
# 816	15_transport_sector$15_03_rail$x$x	01_coal$x
# 822	15_transport_sector$15_04_domestic_navigation$x$x	01_coal$x
# 826	15_transport_sector$15_06_nonspecified_transport$x$x	01_coal$x
# 828	15_transport_sector$x$x$x	01_coal$x
# 1250	15_transport_sector$15_03_rail$x$x	02_coal_products$x
# 1253	15_transport_sector$15_04_domestic_navigation$x$x	02_coal_products$x
# 1256	15_transport_sector$x$x$x	02_coal_products$x
# 1970	15_transport_sector$15_05_pipeline_transport$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1971	15_transport_sector$15_06_nonspecified_transport$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1972	15_transport_sector$x$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 2084	15_transport_sector$15_02_road$x$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2085	15_transport_sector$x$x$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2450	15_transport_sector$15_02_road$x$x	06_crude_oil_and_ngl$x
# 2451	15_transport_sector$15_05_pipeline_transport$x$x	06_crude_oil_and_ngl$x
# 2452	15_transport_sector$15_06_nonspecified_transport$x$x	06_crude_oil_and_ngl$x
# 2453	15_transport_sector$x$x$x	06_crude_oil_and_ngl$x
# 2576	15_transport_sector$15_01_domestic_air_transport$x$x	07_petroleum_products$07_01_motor_gasoline
# 2588	15_transport_sector$15_02_road$x$x	07_petroleum_products$07_01_motor_gasoline
# 2591	15_transport_sector$15_03_rail$x$x	07_petroleum_products$07_01_motor_gasoline
# 2594	15_transport_sector$15_04_domestic_navigation$x$x	07_petroleum_products$07_01_motor_gasoline
# 2595	15_transport_sector$15_05_pipeline_transport$x$x	07_petroleum_products$07_01_motor_gasoline
# 2596	15_transport_sector$15_06_nonspecified_transport$x$x	07_petroleum_products$07_01_motor_gasoline
# 2597	15_transport_sector$x$x$x	07_petroleum_products$07_01_motor_gasoline
# 2715	15_transport_sector$15_01_domestic_air_transport$x$x	07_petroleum_products$07_02_aviation_gasoline
# 2735	15_transport_sector$15_06_nonspecified_transport$x$x	07_petroleum_products$07_02_aviation_gasoline
# 2736	15_transport_sector$x$x$x	07_petroleum_products$07_02_aviation_gasoline
# 3044	15_transport_sector$15_01_domestic_air_transport$x$x	07_petroleum_products$07_06_kerosene
# 3068	15_transport_sector$15_02_road$x$x	07_petroleum_products$07_06_kerosene
# 3074	15_transport_sector$15_03_rail$x$x	07_petroleum_products$07_06_kerosene
# 3080	15_transport_sector$15_04_domestic_navigation$x$x	07_petroleum_products$07_06_kerosene
# 3082	15_transport_sector$15_05_pipeline_transport$x$x	07_petroleum_products$07_06_kerosene
# 3084	15_transport_sector$15_06_nonspecified_transport$x$x	07_petroleum_products$07_06_kerosene
# 3086	15_transport_sector$x$x$x	07_petroleum_products$07_06_kerosene
# 3412	15_transport_sector$15_01_domestic_air_transport$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3436	15_transport_sector$15_02_road$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3442	15_transport_sector$15_03_rail$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3448	15_transport_sector$15_04_domestic_navigation$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3450	15_transport_sector$15_05_pipeline_transport$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3452	15_transport_sector$15_06_nonspecified_transport$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3454	15_transport_sector$x$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3681	15_transport_sector$15_01_domestic_air_transport$x$x	07_petroleum_products$07_08_fuel_oil
# 3693	15_transport_sector$15_02_road$x$x	07_petroleum_products$07_08_fuel_oil
# 3696	15_transport_sector$15_03_rail$x$x	07_petroleum_products$07_08_fuel_oil
# 3699	15_transport_sector$15_04_domestic_navigation$x$x	07_petroleum_products$07_08_fuel_oil
# 3700	15_transport_sector$15_05_pipeline_transport$x$x	07_petroleum_products$07_08_fuel_oil
# 3701	15_transport_sector$15_06_nonspecified_transport$x$x	07_petroleum_products$07_08_fuel_oil
# 3702	15_transport_sector$x$x$x	07_petroleum_products$07_08_fuel_oil
# 3831	15_transport_sector$15_01_domestic_air_transport$x$x	07_petroleum_products$07_09_lpg
# 3843	15_transport_sector$15_02_road$x$x	07_petroleum_products$07_09_lpg
# 3846	15_transport_sector$15_03_rail$x$x	07_petroleum_products$07_09_lpg
# 3849	15_transport_sector$15_04_domestic_navigation$x$x	07_petroleum_products$07_09_lpg
# 3850	15_transport_sector$15_05_pipeline_transport$x$x	07_petroleum_products$07_09_lpg
# 3851	15_transport_sector$15_06_nonspecified_transport$x$x	07_petroleum_products$07_09_lpg
# 3852	15_transport_sector$x$x$x	07_petroleum_products$07_09_lpg
# 4203	15_transport_sector$15_01_domestic_air_transport$x$x	07_petroleum_products$07_x_jet_fuel
# 4223	15_transport_sector$15_06_nonspecified_transport$x$x	07_petroleum_products$07_x_jet_fuel
# 4224	15_transport_sector$x$x$x	07_petroleum_products$07_x_jet_fuel
# 4855	15_transport_sector$15_02_road$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4870	15_transport_sector$15_03_rail$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4885	15_transport_sector$15_04_domestic_navigation$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4895	15_transport_sector$15_06_nonspecified_transport$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4900	15_transport_sector$x$x$x	07_petroleum_products$07_x_other_petroleum_products
# 5305	15_transport_sector$15_01_domestic_air_transport$x$x	07_petroleum_products$x
# 5317	15_transport_sector$15_02_road$x$x	07_petroleum_products$x
# 5320	15_transport_sector$15_03_rail$x$x	07_petroleum_products$x
# 5323	15_transport_sector$15_04_domestic_navigation$x$x	07_petroleum_products$x
# 5324	15_transport_sector$15_05_pipeline_transport$x$x	07_petroleum_products$x
# 5325	15_transport_sector$15_06_nonspecified_transport$x$x	07_petroleum_products$x
# 5326	15_transport_sector$x$x$x	07_petroleum_products$x
# 5501	15_transport_sector$15_02_road$x$x	08_gas$08_01_natural_gas
# 5504	15_transport_sector$15_03_rail$x$x	08_gas$08_01_natural_gas
# 5508	15_transport_sector$15_05_pipeline_transport$x$x	08_gas$08_01_natural_gas
# 5509	15_transport_sector$15_06_nonspecified_transport$x$x	08_gas$08_01_natural_gas
# 5510	15_transport_sector$x$x$x	08_gas$08_01_natural_gas
# 5731	15_transport_sector$15_03_rail$x$x	08_gas$08_03_gas_works_gas
# 5732	15_transport_sector$x$x$x	08_gas$08_03_gas_works_gas
# 5905	15_transport_sector$15_02_road$x$x	08_gas$x
# 5908	15_transport_sector$15_03_rail$x$x	08_gas$x
# 5912	15_transport_sector$15_05_pipeline_transport$x$x	08_gas$x
# 5913	15_transport_sector$15_06_nonspecified_transport$x$x	08_gas$x
# 5914	15_transport_sector$x$x$x	08_gas$x
# 8590	15_transport_sector$15_02_road$x$x	16_others$16_05_biogasoline
# 8599	15_transport_sector$x$x$x	16_others$16_05_biogasoline
# 8726	15_transport_sector$15_02_road$x$x	16_others$16_06_biodiesel
# 8729	15_transport_sector$15_03_rail$x$x	16_others$16_06_biodiesel
# 8732	15_transport_sector$15_04_domestic_navigation$x$x	16_others$16_06_biodiesel
# 8734	15_transport_sector$15_06_nonspecified_transport$x$x	16_others$16_06_biodiesel
# 8735	15_transport_sector$x$x$x	16_others$16_06_biodiesel


# 	IPCC 2006 Source/Sink Category	Fuel 2006
# 2680	1.A.3.b - Road Transportation	Motor Gasoline
# 2683	1.A.3.b - Road Transportation	Gas Oil
# 2684	1.A.3.b - Road Transportation	Diesel Oil
# 2685	1.A.3.b - Road Transportation	Natural Gas
# 2686	1.A.3.b - Road Transportation	Liquefied Petroleum Gases
# 2687	1.A.3.b - Road Transportation	Biogasoline
# 3083	1.A.3.c - Railways	Diesel Oil
# 3085	1.A.3.c - Railways	Sub-Bituminous Coal
# 3097	1.A.3.d - Water-borne Navigation	Diesel Oil
# 3099	1.A.3.a - Civil Aviation	Aviation Gasoline
# 3100	1.A.3.a - Civil Aviation	Jet Kerosene
# 3101	1.A.3.a - Civil Aviation	Jet Gasoline


# IPCC categories:
# 	IPCC 2006 Source/Sink Category	Fuel 2006
# 1855	1.A.1 - Energy Industries	Crude Oil
# 1856	1.A.1 - Energy Industries	Orimulsion
# 1857	1.A.1 - Energy Industries	"Natural Gas Liquids
# (NGLs)"
# 1858	1.A.1 - Energy Industries	Motor Gasoline
# 1859	1.A.1 - Energy Industries	Aviation Gasoline
# 1860	1.A.1 - Energy Industries	Jet Gasoline
# 1861	1.A.1 - Energy Industries	Jet Kerosene
# 1862	1.A.1 - Energy Industries	Other Kerosene
# 1863	1.A.1 - Energy Industries	Shale Oil
# 1864	1.A.1 - Energy Industries	Gas Oil
# 1865	1.A.1 - Energy Industries	Diesel Oil
# 1866	1.A.1 - Energy Industries	Residual Fuel Oil
# 1867	1.A.1 - Energy Industries	Liquefied Petroleum Gases
# 1868	1.A.1 - Energy Industries	Ethane
# 1869	1.A.1 - Energy Industries	Naphtha
# 1870	1.A.1 - Energy Industries	Bitumen
# 1871	1.A.1 - Energy Industries	Lubricants
# 1872	1.A.1 - Energy Industries	Petroleum Coke
# 1873	1.A.1 - Energy Industries	Refinery Feedstocks
# 1874	1.A.1 - Energy Industries	Refinery Gas
# 1875	1.A.1 - Energy Industries	Waxes
# 1876	1.A.1 - Energy Industries	White Spirit & SBP
# 1877	1.A.1 - Energy Industries	Other Petroleum Products
# 1878	1.A.1 - Energy Industries	Anthracite
# 1879	1.A.1 - Energy Industries	Coking Coal
# 1880	1.A.1 - Energy Industries	Other Bituminous Coal
# 1881	1.A.1 - Energy Industries	Sub-Bituminous Coal
# 1882	1.A.1 - Energy Industries	Lignite
# 1883	1.A.1 - Energy Industries	Oil Shale and Tar Sands
# 1884	1.A.1 - Energy Industries	Brown Coal Briquettes
# 1885	1.A.1 - Energy Industries	Patent Fuel
# 1886	1.A.1 - Energy Industries	Coke Oven Coke and Lignite Coke
# 1887	1.A.1 - Energy Industries	Gas Coke
# 1888	1.A.1 - Energy Industries	Coal Tar
# 1889	1.A.1 - Energy Industries	Gas Works Gas
# 1890	1.A.1 - Energy Industries	Coke Oven Gas
# 1891	1.A.1 - Energy Industries	Blast Furnace Gas
# 1892	1.A.1 - Energy Industries	Oxygen Steel Furnace Gas
# 1893	1.A.1 - Energy Industries	Natural Gas
# 1894	1.A.1 - Energy Industries	Municipal Wastes (non-biomass fraction)
# 1895	1.A.1 - Energy Industries	Industrial Wastes
# 1896	1.A.1 - Energy Industries	Waste Oils
# 1897	1.A.1 - Energy Industries	Peat
# 1898	1.A.1 - Energy Industries	Wood/Wood Waste
# 1899	1.A.1 - Energy Industries	Sulphite Lyes (Black Liquor)
# 1900	1.A.1 - Energy Industries	Other Primary Solid Biomass
# 1901	1.A.1 - Energy Industries	Charcoal
# 1902	1.A.1 - Energy Industries	Biogasoline
# 1903	1.A.1 - Energy Industries	Biodiesels
# 1904	1.A.1 - Energy Industries	Other Liquid Biofuels
# 1905	1.A.1 - Energy Industries	Landfill Gas
# 1906	1.A.1 - Energy Industries	Sludge Gas
# 1907	1.A.1 - Energy Industries	Other Biogas
# 1908	1.A.1 - Energy Industries	Municipal Wastes (biomass fraction)

# 2680	1.A.3.b - Road Transportation	Motor Gasoline
# 2683	1.A.3.b - Road Transportation	Gas Oil
# 2684	1.A.3.b - Road Transportation	Diesel Oil
# 2685	1.A.3.b - Road Transportation	Natural Gas
# 2686	1.A.3.b - Road Transportation	Liquefied Petroleum Gases
# 2687	1.A.3.b - Road Transportation	Biogasoline
# # 3061	1.A.4.c.ii - Off-road Vehicles and Other Machinery	Diesel Oil
# # 3063	1.A.3.e.ii - Off-road	Diesel Oil
# # 3069	1.A.4.c.ii - Off-road Vehicles and Other Machinery	Motor Gasoline
# # 3070	1.A.3.e.ii - Off-road	Motor Gasoline
# 3083	1.A.3.c - Railways	Diesel Oil
# 3085	1.A.3.c - Railways	Sub-Bituminous Coal
# 3097	1.A.3.d - Water-borne Navigation	Diesel Oil
# 3099	1.A.3.a - Civil Aviation	Aviation Gasoline
# 3100	1.A.3.a - Civil Aviation	Jet Kerosene
# 3101	1.A.3.a - Civil Aviation	Jet Gasoline



#%%
# RESIDENTIAL
#Please map the following aperc sector, fuel combinations to one of the following IPCC 2006 Source/Sink Category, Fuel 2006 combinations and put it in a python dict. ignore the row numbers. (for the IPCC sector categories tr to prioritise mapping using the residential related sectors rather than the 1.A.1 - Energy Industries sector):
# APERC:

# 	aperc_sector	aperc_fuel
# 62	16_other_sector$16_01_buildings$16_01_02_residential$x	01_coal$01_01_coking_coal
# 211	16_other_sector$16_01_buildings$16_01_02_residential$x	01_coal$01_05_lignite
# 468	16_other_sector$16_01_buildings$16_01_02_residential$x	01_coal$01_x_thermal_coal
# 832	16_other_sector$16_01_buildings$16_01_02_residential$x	01_coal$x
# 1262	16_other_sector$16_01_buildings$16_01_02_residential$x	02_coal_products$x
# 1517	16_other_sector$16_01_buildings$16_01_02_residential$x	03_peat$x
# 1661	16_other_sector$16_01_buildings$16_01_02_residential$x	04_peat_products$x
# 2599	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_01_motor_gasoline
# 2738	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_02_aviation_gasoline
# 2853	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_03_naphtha
# 3090	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_06_kerosene
# 3458	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_07_gas_diesel_oil
# 3704	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_08_fuel_oil
# 3854	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_09_lpg
# 3979	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 4092	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_11_ethane
# 4226	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_x_jet_fuel
# 4910	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_x_other_petroleum_products
# 5328	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$x
# 5512	16_other_sector$16_01_buildings$16_01_02_residential$x	08_gas$08_01_natural_gas
# 5623	16_other_sector$16_01_buildings$16_01_02_residential$x	08_gas$08_02_lng
# 5734	16_other_sector$16_01_buildings$16_01_02_residential$x	08_gas$08_03_gas_works_gas
# 5916	16_other_sector$16_01_buildings$16_01_02_residential$x	08_gas$x
# 7123	16_other_sector$16_01_buildings$16_01_02_residential$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7232	16_other_sector$16_01_buildings$16_01_02_residential$x	15_solid_biomass$15_02_bagasse
# 7338	16_other_sector$16_01_buildings$16_01_02_residential$x	15_solid_biomass$15_03_charcoal
# 7447	16_other_sector$16_01_buildings$16_01_02_residential$x	15_solid_biomass$15_04_black_liquor
# 7556	16_other_sector$16_01_buildings$16_01_02_residential$x	15_solid_biomass$15_05_other_biomass
# 7712	16_other_sector$16_01_buildings$16_01_02_residential$x	15_solid_biomass$x
# 8024	16_other_sector$16_01_buildings$16_01_02_residential$x	16_others$16_01_biogas
# 8247	16_other_sector$16_01_buildings$16_01_02_residential$x	16_others$16_02_industrial_waste
# 8358	16_other_sector$16_01_buildings$16_01_02_residential$x	16_others$16_03_municipal_solid_waste_renewable
# 8469	16_other_sector$16_01_buildings$16_01_02_residential$x	16_others$16_04_municipal_solid_waste_nonrenewable
# 8601	16_other_sector$16_01_buildings$16_01_02_residential$x	16_others$16_05_biogasoline
# 8737	16_other_sector$16_01_buildings$16_01_02_residential$x	16_others$16_06_biodiesel
# 8946	16_other_sector$16_01_buildings$16_01_02_residential$x	16_others$16_07_bio_jet_kerosene
# 9101	16_other_sector$16_01_buildings$16_01_02_residential$x	16_others$16_08_other_liquid_biofuels

# 	IPCC 2006 Source/Sink Category	Fuel 2006
# 1855	1.A.1 - Energy Industries	Crude Oil
# 1856	1.A.1 - Energy Industries	Orimulsion
# 1857	1.A.1 - Energy Industries	"Natural Gas Liquids
# (NGLs)"
# 1858	1.A.1 - Energy Industries	Motor Gasoline
# 1859	1.A.1 - Energy Industries	Aviation Gasoline
# 1860	1.A.1 - Energy Industries	Jet Gasoline
# 1861	1.A.1 - Energy Industries	Jet Kerosene
# 1862	1.A.1 - Energy Industries	Other Kerosene
# 1863	1.A.1 - Energy Industries	Shale Oil
# 1864	1.A.1 - Energy Industries	Gas Oil
# 1865	1.A.1 - Energy Industries	Diesel Oil
# 1866	1.A.1 - Energy Industries	Residual Fuel Oil
# 1867	1.A.1 - Energy Industries	Liquefied Petroleum Gases
# 1868	1.A.1 - Energy Industries	Ethane
# 1869	1.A.1 - Energy Industries	Naphtha
# 1870	1.A.1 - Energy Industries	Bitumen
# 1871	1.A.1 - Energy Industries	Lubricants
# 1872	1.A.1 - Energy Industries	Petroleum Coke
# 1873	1.A.1 - Energy Industries	Refinery Feedstocks
# 1874	1.A.1 - Energy Industries	Refinery Gas
# 1875	1.A.1 - Energy Industries	Waxes
# 1876	1.A.1 - Energy Industries	White Spirit & SBP
# 1877	1.A.1 - Energy Industries	Other Petroleum Products
# 1878	1.A.1 - Energy Industries	Anthracite
# 1879	1.A.1 - Energy Industries	Coking Coal
# 1880	1.A.1 - Energy Industries	Other Bituminous Coal
# 1881	1.A.1 - Energy Industries	Sub-Bituminous Coal
# 1882	1.A.1 - Energy Industries	Lignite
# 1883	1.A.1 - Energy Industries	Oil Shale and Tar Sands
# 1884	1.A.1 - Energy Industries	Brown Coal Briquettes
# 1885	1.A.1 - Energy Industries	Patent Fuel
# 1886	1.A.1 - Energy Industries	Coke Oven Coke and Lignite Coke
# 1887	1.A.1 - Energy Industries	Gas Coke
# 1888	1.A.1 - Energy Industries	Coal Tar
# 1889	1.A.1 - Energy Industries	Gas Works Gas
# 1890	1.A.1 - Energy Industries	Coke Oven Gas
# 1891	1.A.1 - Energy Industries	Blast Furnace Gas
# 1892	1.A.1 - Energy Industries	Oxygen Steel Furnace Gas
# 1893	1.A.1 - Energy Industries	Natural Gas
# 1894	1.A.1 - Energy Industries	Municipal Wastes (non-biomass fraction)
# 1895	1.A.1 - Energy Industries	Industrial Wastes
# 1896	1.A.1 - Energy Industries	Waste Oils
# 1897	1.A.1 - Energy Industries	Peat
# 1898	1.A.1 - Energy Industries	Wood/Wood Waste
# 1899	1.A.1 - Energy Industries	Sulphite Lyes (Black Liquor)
# 1900	1.A.1 - Energy Industries	Other Primary Solid Biomass
# 1901	1.A.1 - Energy Industries	Charcoal
# 1902	1.A.1 - Energy Industries	Biogasoline
# 1903	1.A.1 - Energy Industries	Biodiesels
# 1904	1.A.1 - Energy Industries	Other Liquid Biofuels
# 1905	1.A.1 - Energy Industries	Landfill Gas
# 1906	1.A.1 - Energy Industries	Sludge Gas
# 1907	1.A.1 - Energy Industries	Other Biogas
# 1908	1.A.1 - Energy Industries	Municipal Wastes (biomass fraction)

# 2341	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Crude Oil
# 2342	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Orimulsion
# 2343	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	"Natural Gas Liquids
# (NGLs)"
# 2344	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Motor Gasoline
# 2345	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Aviation Gasoline
# 2346	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Jet Gasoline
# 2347	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Jet Kerosene
# 2348	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Other Kerosene
# 2349	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Shale Oil
# 2350	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Gas Oil
# 2351	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Diesel Oil
# 2352	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Residual Fuel Oil
# 2353	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Liquefied Petroleum Gases
# 2354	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Ethane
# 2355	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Naphtha
# 2356	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Bitumen
# 2357	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Lubricants
# 2358	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Petroleum Coke
# 2359	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Refinery Feedstocks
# 2360	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Refinery Gas
# 2361	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Waxes
# 2362	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	White Spirit & SBP
# 2363	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Other Petroleum Products
# 2364	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Anthracite
# 2365	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Coking Coal
# 2366	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Other Bituminous Coal
# 2367	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Sub-Bituminous Coal
# 2368	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Lignite
# 2369	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Oil Shale and Tar Sands
# 2370	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Brown Coal Briquettes
# 2371	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Patent Fuel
# 2372	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Coke Oven Coke and Lignite Coke
# 2373	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Gas Coke
# 2374	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Coal Tar
# 2375	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Gas Works Gas
# 2376	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Coke Oven Gas
# 2377	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Blast Furnace Gas
# 2378	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Oxygen Steel Furnace Gas
# 2379	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Natural Gas
# 2380	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Municipal Wastes (non-biomass fraction)
# 2381	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Industrial Wastes
# 2382	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Waste Oils
# 2383	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Peat
# 2384	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Wood/Wood Waste
# 2385	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Sulphite Lyes (Black Liquor)
# 2386	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Other Primary Solid Biomass
# 2387	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Charcoal
# 2388	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Biogasoline
# 2389	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Biodiesels
# 2390	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Other Liquid Biofuels
# 2391	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Landfill Gas
# 2392	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Sludge Gas
# 2393	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Other Biogas
# 2394	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Municipal Wastes (biomass fraction)









# INDUSTRIAL
#Please map the following aperc sector, fuel combinations to one of the following IPCC 2006 Source/Sink Category, Fuel 2006 combinations and put it in a python dict. ignore the row numbers. (for the IPCC sector categories tr to prioritise mapping using the industrial related sectors rather than the 1.A.1 - Energy Industries sector):
# APERC:

# 	IPCC 2006 Source/Sink Category	Fuel 2006
# 1855	1.A.1 - Energy Industries	Crude Oil
# 1856	1.A.1 - Energy Industries	Orimulsion
# 1857	1.A.1 - Energy Industries	"Natural Gas Liquids
# (NGLs)"
# 1858	1.A.1 - Energy Industries	Motor Gasoline
# 1859	1.A.1 - Energy Industries	Aviation Gasoline
# 1860	1.A.1 - Energy Industries	Jet Gasoline
# 1861	1.A.1 - Energy Industries	Jet Kerosene
# 1862	1.A.1 - Energy Industries	Other Kerosene
# 1863	1.A.1 - Energy Industries	Shale Oil
# 1864	1.A.1 - Energy Industries	Gas Oil
# 1865	1.A.1 - Energy Industries	Diesel Oil
# 1866	1.A.1 - Energy Industries	Residual Fuel Oil
# 1867	1.A.1 - Energy Industries	Liquefied Petroleum Gases
# 1868	1.A.1 - Energy Industries	Ethane
# 1869	1.A.1 - Energy Industries	Naphtha
# 1870	1.A.1 - Energy Industries	Bitumen
# 1871	1.A.1 - Energy Industries	Lubricants
# 1872	1.A.1 - Energy Industries	Petroleum Coke
# 1873	1.A.1 - Energy Industries	Refinery Feedstocks
# 1874	1.A.1 - Energy Industries	Refinery Gas
# 1875	1.A.1 - Energy Industries	Waxes
# 1876	1.A.1 - Energy Industries	White Spirit & SBP
# 1877	1.A.1 - Energy Industries	Other Petroleum Products
# 1878	1.A.1 - Energy Industries	Anthracite
# 1879	1.A.1 - Energy Industries	Coking Coal
# 1880	1.A.1 - Energy Industries	Other Bituminous Coal
# 1881	1.A.1 - Energy Industries	Sub-Bituminous Coal
# 1882	1.A.1 - Energy Industries	Lignite
# 1883	1.A.1 - Energy Industries	Oil Shale and Tar Sands
# 1884	1.A.1 - Energy Industries	Brown Coal Briquettes
# 1885	1.A.1 - Energy Industries	Patent Fuel
# 1886	1.A.1 - Energy Industries	Coke Oven Coke and Lignite Coke
# 1887	1.A.1 - Energy Industries	Gas Coke
# 1888	1.A.1 - Energy Industries	Coal Tar
# 1889	1.A.1 - Energy Industries	Gas Works Gas
# 1890	1.A.1 - Energy Industries	Coke Oven Gas
# 1891	1.A.1 - Energy Industries	Blast Furnace Gas
# 1892	1.A.1 - Energy Industries	Oxygen Steel Furnace Gas
# 1893	1.A.1 - Energy Industries	Natural Gas
# 1894	1.A.1 - Energy Industries	Municipal Wastes (non-biomass fraction)
# 1895	1.A.1 - Energy Industries	Industrial Wastes
# 1896	1.A.1 - Energy Industries	Waste Oils
# 1897	1.A.1 - Energy Industries	Peat
# 1898	1.A.1 - Energy Industries	Wood/Wood Waste
# 1899	1.A.1 - Energy Industries	Sulphite Lyes (Black Liquor)
# 1900	1.A.1 - Energy Industries	Other Primary Solid Biomass
# 1901	1.A.1 - Energy Industries	Charcoal
# 1902	1.A.1 - Energy Industries	Biogasoline
# 1903	1.A.1 - Energy Industries	Biodiesels
# 1904	1.A.1 - Energy Industries	Other Liquid Biofuels
# 1905	1.A.1 - Energy Industries	Landfill Gas
# 1906	1.A.1 - Energy Industries	Sludge Gas
# 1907	1.A.1 - Energy Industries	Other Biogas
# 1908	1.A.1 - Energy Industries	Municipal Wastes (biomass fraction)
# 2017	1.A.2 - Manufacturing Industries and Construction	Crude Oil
# 2018	1.A.2 - Manufacturing Industries and Construction	Orimulsion
# 2019	1.A.2 - Manufacturing Industries and Construction	"Natural Gas Liquids
# (NGLs)"
# 2020	1.A.2 - Manufacturing Industries and Construction	Motor Gasoline
# 2021	1.A.2 - Manufacturing Industries and Construction	Aviation Gasoline
# 2022	1.A.2 - Manufacturing Industries and Construction	Jet Gasoline
# 2023	1.A.2 - Manufacturing Industries and Construction	Jet Kerosene
# 2024	1.A.2 - Manufacturing Industries and Construction	Other Kerosene
# 2025	1.A.2 - Manufacturing Industries and Construction	Shale Oil
# 2026	1.A.2 - Manufacturing Industries and Construction	Gas Oil
# 2027	1.A.2 - Manufacturing Industries and Construction	Diesel Oil
# 2028	1.A.2 - Manufacturing Industries and Construction	Residual Fuel Oil
# 2029	1.A.2 - Manufacturing Industries and Construction	Liquefied Petroleum Gases
# 2030	1.A.2 - Manufacturing Industries and Construction	Ethane
# 2031	1.A.2 - Manufacturing Industries and Construction	Naphtha
# 2032	1.A.2 - Manufacturing Industries and Construction	Bitumen
# 2033	1.A.2 - Manufacturing Industries and Construction	Lubricants
# 2034	1.A.2 - Manufacturing Industries and Construction	Petroleum Coke
# 2035	1.A.2 - Manufacturing Industries and Construction	Refinery Feedstocks
# 2036	1.A.2 - Manufacturing Industries and Construction	Refinery Gas
# 2037	1.A.2 - Manufacturing Industries and Construction	Waxes
# 2038	1.A.2 - Manufacturing Industries and Construction	White Spirit & SBP
# 2039	1.A.2 - Manufacturing Industries and Construction	Other Petroleum Products
# 2040	1.A.2 - Manufacturing Industries and Construction	Anthracite
# 2041	1.A.2 - Manufacturing Industries and Construction	Coking Coal
# 2042	1.A.2 - Manufacturing Industries and Construction	Other Bituminous Coal
# 2043	1.A.2 - Manufacturing Industries and Construction	Sub-Bituminous Coal
# 2044	1.A.2 - Manufacturing Industries and Construction	Lignite
# 2045	1.A.2 - Manufacturing Industries and Construction	Oil Shale and Tar Sands
# 2046	1.A.2 - Manufacturing Industries and Construction	Brown Coal Briquettes
# 2047	1.A.2 - Manufacturing Industries and Construction	Patent Fuel
# 2048	1.A.2 - Manufacturing Industries and Construction	Coke Oven Coke and Lignite Coke
# 2049	1.A.2 - Manufacturing Industries and Construction	Gas Coke
# 2050	1.A.2 - Manufacturing Industries and Construction	Coal Tar
# 2051	1.A.2 - Manufacturing Industries and Construction	Gas Works Gas
# 2052	1.A.2 - Manufacturing Industries and Construction	Coke Oven Gas
# 2053	1.A.2 - Manufacturing Industries and Construction	Blast Furnace Gas
# 2054	1.A.2 - Manufacturing Industries and Construction	Oxygen Steel Furnace Gas
# 2055	1.A.2 - Manufacturing Industries and Construction	Natural Gas
# 2056	1.A.2 - Manufacturing Industries and Construction	Municipal Wastes (non-biomass fraction)
# 2057	1.A.2 - Manufacturing Industries and Construction	Industrial Wastes
# 2058	1.A.2 - Manufacturing Industries and Construction	Waste Oils
# 2059	1.A.2 - Manufacturing Industries and Construction	Peat
# 2060	1.A.2 - Manufacturing Industries and Construction	Wood/Wood Waste
# 2061	1.A.2 - Manufacturing Industries and Construction	Sulphite Lyes (Black Liquor)
# 2062	1.A.2 - Manufacturing Industries and Construction	Other Primary Solid Biomass
# 2063	1.A.2 - Manufacturing Industries and Construction	Charcoal
# 2064	1.A.2 - Manufacturing Industries and Construction	Biogasoline
# 2065	1.A.2 - Manufacturing Industries and Construction	Biodiesels
# 2066	1.A.2 - Manufacturing Industries and Construction	Other Liquid Biofuels
# 2067	1.A.2 - Manufacturing Industries and Construction	Landfill Gas
# 2068	1.A.2 - Manufacturing Industries and Construction	Sludge Gas
# 2069	1.A.2 - Manufacturing Industries and Construction	Other Biogas
# 2070	1.A.2 - Manufacturing Industries and Construction	Municipal Wastes (biomass fraction)

# APERC:
#     	aperc_sector	aperc_fuel
# 34	14_industry_sector$14_01_mining_and_quarrying$x$x	01_coal$01_01_coking_coal
# 35	14_industry_sector$14_02_construction$x$x	01_coal$01_01_coking_coal
# 41	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	01_coal$01_01_coking_coal
# 44	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	01_coal$01_01_coking_coal
# 45	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	01_coal$01_01_coking_coal
# 48	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	01_coal$01_01_coking_coal
# 49	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	01_coal$01_01_coking_coal
# 50	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	01_coal$01_01_coking_coal
# 51	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	01_coal$01_01_coking_coal
# 52	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	01_coal$01_01_coking_coal
# 53	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	01_coal$01_01_coking_coal
# 54	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	01_coal$01_01_coking_coal
# 55	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	01_coal$01_01_coking_coal
# 56	14_industry_sector$14_03_manufacturing$x$x	01_coal$01_01_coking_coal
# 57	14_industry_sector$x$x$x	01_coal$01_01_coking_coal
# 184	14_industry_sector$14_01_mining_and_quarrying$x$x	01_coal$01_05_lignite
# 185	14_industry_sector$14_02_construction$x$x	01_coal$01_05_lignite
# 191	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	01_coal$01_05_lignite
# 194	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	01_coal$01_05_lignite
# 195	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	01_coal$01_05_lignite
# 198	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	01_coal$01_05_lignite
# 199	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	01_coal$01_05_lignite
# 200	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	01_coal$01_05_lignite
# 201	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	01_coal$01_05_lignite
# 202	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	01_coal$01_05_lignite
# 203	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	01_coal$01_05_lignite
# 204	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	01_coal$01_05_lignite
# 205	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	01_coal$01_05_lignite
# 206	14_industry_sector$14_03_manufacturing$x$x	01_coal$01_05_lignite
# 207	14_industry_sector$x$x$x	01_coal$01_05_lignite
# 410	14_industry_sector$14_01_mining_and_quarrying$x$x	01_coal$01_x_thermal_coal
# 412	14_industry_sector$14_02_construction$x$x	01_coal$01_x_thermal_coal
# 424	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	01_coal$01_x_thermal_coal
# 430	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	01_coal$01_x_thermal_coal
# 432	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	01_coal$01_x_thermal_coal
# 438	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	01_coal$01_x_thermal_coal
# 440	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	01_coal$01_x_thermal_coal
# 442	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	01_coal$01_x_thermal_coal
# 444	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	01_coal$01_x_thermal_coal
# 446	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	01_coal$01_x_thermal_coal
# 448	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	01_coal$01_x_thermal_coal
# 450	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	01_coal$01_x_thermal_coal
# 452	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	01_coal$01_x_thermal_coal
# 454	14_industry_sector$14_03_manufacturing$x$x	01_coal$01_x_thermal_coal
# 456	14_industry_sector$x$x$x	01_coal$01_x_thermal_coal
# 734	14_industry_sector$14_01_mining_and_quarrying$x$x	01_coal$x
# 736	14_industry_sector$14_02_construction$x$x	01_coal$x
# 748	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	01_coal$x
# 754	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	01_coal$x
# 756	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	01_coal$x
# 762	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	01_coal$x
# 764	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	01_coal$x
# 766	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	01_coal$x
# 768	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	01_coal$x
# 770	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	01_coal$x
# 772	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	01_coal$x
# 774	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	01_coal$x
# 776	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	01_coal$x
# 778	14_industry_sector$14_03_manufacturing$x$x	01_coal$x
# 780	14_industry_sector$x$x$x	01_coal$x
# 1178	14_industry_sector$14_01_mining_and_quarrying$x$x	02_coal_products$x
# 1181	14_industry_sector$14_02_construction$x$x	02_coal_products$x
# 1199	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	02_coal_products$x
# 1208	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	02_coal_products$x
# 1211	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	02_coal_products$x
# 1220	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	02_coal_products$x
# 1223	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	02_coal_products$x
# 1226	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	02_coal_products$x
# 1229	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	02_coal_products$x
# 1232	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	02_coal_products$x
# 1235	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	02_coal_products$x
# 1238	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	02_coal_products$x
# 1241	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	02_coal_products$x
# 1244	14_industry_sector$14_03_manufacturing$x$x	02_coal_products$x
# 1247	14_industry_sector$x$x$x	02_coal_products$x
# 1493	14_industry_sector$14_02_construction$x$x	03_peat$x
# 1502	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	03_peat$x
# 1503	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	03_peat$x
# 1506	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	03_peat$x
# 1508	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	03_peat$x
# 1511	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	03_peat$x
# 1512	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	03_peat$x
# 1513	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	03_peat$x
# 1514	14_industry_sector$14_03_manufacturing$x$x	03_peat$x
# 1515	14_industry_sector$x$x$x	03_peat$x
# 1643	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	04_peat_products$x
# 1647	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	04_peat_products$x
# 1652	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	04_peat_products$x
# 1655	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	04_peat_products$x
# 1657	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	04_peat_products$x
# 1658	14_industry_sector$14_03_manufacturing$x$x	04_peat_products$x
# 1659	14_industry_sector$x$x$x	04_peat_products$x
# 1946	14_industry_sector$14_01_mining_and_quarrying$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1947	14_industry_sector$14_02_construction$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1953	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1956	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1957	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1960	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1961	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1962	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1963	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1964	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1965	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1966	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1967	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1968	14_industry_sector$14_03_manufacturing$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1969	14_industry_sector$x$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 2060	14_industry_sector$14_01_mining_and_quarrying$x$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2067	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2070	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2071	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2074	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2075	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2076	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2077	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2078	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2079	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2080	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2081	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2082	14_industry_sector$14_03_manufacturing$x$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2083	14_industry_sector$x$x$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2426	14_industry_sector$14_01_mining_and_quarrying$x$x	06_crude_oil_and_ngl$x
# 2427	14_industry_sector$14_02_construction$x$x	06_crude_oil_and_ngl$x
# 2433	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	06_crude_oil_and_ngl$x
# 2436	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	06_crude_oil_and_ngl$x
# 2437	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	06_crude_oil_and_ngl$x
# 2440	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	06_crude_oil_and_ngl$x
# 2441	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	06_crude_oil_and_ngl$x
# 2442	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	06_crude_oil_and_ngl$x
# 2443	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	06_crude_oil_and_ngl$x
# 2444	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	06_crude_oil_and_ngl$x
# 2445	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	06_crude_oil_and_ngl$x
# 2446	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	06_crude_oil_and_ngl$x
# 2447	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	06_crude_oil_and_ngl$x
# 2448	14_industry_sector$14_03_manufacturing$x$x	06_crude_oil_and_ngl$x
# 2449	14_industry_sector$x$x$x	06_crude_oil_and_ngl$x
# 2550	14_industry_sector$14_01_mining_and_quarrying$x$x	07_petroleum_products$07_01_motor_gasoline
# 2551	14_industry_sector$14_02_construction$x$x	07_petroleum_products$07_01_motor_gasoline
# 2557	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	07_petroleum_products$07_01_motor_gasoline
# 2560	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	07_petroleum_products$07_01_motor_gasoline
# 2561	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	07_petroleum_products$07_01_motor_gasoline
# 2564	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	07_petroleum_products$07_01_motor_gasoline
# 2565	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	07_petroleum_products$07_01_motor_gasoline
# 2566	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	07_petroleum_products$07_01_motor_gasoline
# 2567	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	07_petroleum_products$07_01_motor_gasoline
# 2568	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	07_petroleum_products$07_01_motor_gasoline
# 2569	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	07_petroleum_products$07_01_motor_gasoline
# 2570	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	07_petroleum_products$07_01_motor_gasoline
# 2571	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	07_petroleum_products$07_01_motor_gasoline
# 2572	14_industry_sector$14_03_manufacturing$x$x	07_petroleum_products$07_01_motor_gasoline
# 2573	14_industry_sector$x$x$x	07_petroleum_products$07_01_motor_gasoline
# 2710	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	07_petroleum_products$07_02_aviation_gasoline
# 2711	14_industry_sector$14_03_manufacturing$x$x	07_petroleum_products$07_02_aviation_gasoline
# 2712	14_industry_sector$x$x$x	07_petroleum_products$07_02_aviation_gasoline
# 2828	14_industry_sector$14_01_mining_and_quarrying$x$x	07_petroleum_products$07_03_naphtha
# 2829	14_industry_sector$14_02_construction$x$x	07_petroleum_products$07_03_naphtha
# 2838	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	07_petroleum_products$07_03_naphtha
# 2839	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	07_petroleum_products$07_03_naphtha
# 2842	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	07_petroleum_products$07_03_naphtha
# 2843	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	07_petroleum_products$07_03_naphtha
# 2844	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	07_petroleum_products$07_03_naphtha
# 2845	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	07_petroleum_products$07_03_naphtha
# 2846	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	07_petroleum_products$07_03_naphtha
# 2848	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	07_petroleum_products$07_03_naphtha
# 2849	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	07_petroleum_products$07_03_naphtha
# 2850	14_industry_sector$14_03_manufacturing$x$x	07_petroleum_products$07_03_naphtha
# 2851	14_industry_sector$x$x$x	07_petroleum_products$07_03_naphtha
# 2992	14_industry_sector$14_01_mining_and_quarrying$x$x	07_petroleum_products$07_06_kerosene
# 2994	14_industry_sector$14_02_construction$x$x	07_petroleum_products$07_06_kerosene
# 3006	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	07_petroleum_products$07_06_kerosene
# 3012	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	07_petroleum_products$07_06_kerosene
# 3014	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	07_petroleum_products$07_06_kerosene
# 3020	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	07_petroleum_products$07_06_kerosene
# 3022	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	07_petroleum_products$07_06_kerosene
# 3024	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	07_petroleum_products$07_06_kerosene
# 3026	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	07_petroleum_products$07_06_kerosene
# 3028	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	07_petroleum_products$07_06_kerosene
# 3030	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	07_petroleum_products$07_06_kerosene
# 3032	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	07_petroleum_products$07_06_kerosene
# 3034	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	07_petroleum_products$07_06_kerosene
# 3036	14_industry_sector$14_03_manufacturing$x$x	07_petroleum_products$07_06_kerosene
# 3038	14_industry_sector$x$x$x	07_petroleum_products$07_06_kerosene
# 3360	14_industry_sector$14_01_mining_and_quarrying$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3362	14_industry_sector$14_02_construction$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3374	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	07_petroleum_products$07_07_gas_diesel_oil
# 3380	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	07_petroleum_products$07_07_gas_diesel_oil
# 3382	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	07_petroleum_products$07_07_gas_diesel_oil
# 3388	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	07_petroleum_products$07_07_gas_diesel_oil
# 3390	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	07_petroleum_products$07_07_gas_diesel_oil
# 3392	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	07_petroleum_products$07_07_gas_diesel_oil
# 3394	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	07_petroleum_products$07_07_gas_diesel_oil
# 3396	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	07_petroleum_products$07_07_gas_diesel_oil
# 3398	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	07_petroleum_products$07_07_gas_diesel_oil
# 3400	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	07_petroleum_products$07_07_gas_diesel_oil
# 3402	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	07_petroleum_products$07_07_gas_diesel_oil
# 3404	14_industry_sector$14_03_manufacturing$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3406	14_industry_sector$x$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3655	14_industry_sector$14_01_mining_and_quarrying$x$x	07_petroleum_products$07_08_fuel_oil
# 3656	14_industry_sector$14_02_construction$x$x	07_petroleum_products$07_08_fuel_oil
# 3662	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	07_petroleum_products$07_08_fuel_oil
# 3665	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	07_petroleum_products$07_08_fuel_oil
# 3666	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	07_petroleum_products$07_08_fuel_oil
# 3669	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	07_petroleum_products$07_08_fuel_oil
# 3670	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	07_petroleum_products$07_08_fuel_oil
# 3671	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	07_petroleum_products$07_08_fuel_oil
# 3672	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	07_petroleum_products$07_08_fuel_oil
# 3673	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	07_petroleum_products$07_08_fuel_oil
# 3674	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	07_petroleum_products$07_08_fuel_oil
# 3675	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	07_petroleum_products$07_08_fuel_oil
# 3676	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	07_petroleum_products$07_08_fuel_oil
# 3677	14_industry_sector$14_03_manufacturing$x$x	07_petroleum_products$07_08_fuel_oil
# 3678	14_industry_sector$x$x$x	07_petroleum_products$07_08_fuel_oil
# 3805	14_industry_sector$14_01_mining_and_quarrying$x$x	07_petroleum_products$07_09_lpg
# 3806	14_industry_sector$14_02_construction$x$x	07_petroleum_products$07_09_lpg
# 3812	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	07_petroleum_products$07_09_lpg
# 3815	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	07_petroleum_products$07_09_lpg
# 3816	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	07_petroleum_products$07_09_lpg
# 3819	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	07_petroleum_products$07_09_lpg
# 3820	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	07_petroleum_products$07_09_lpg
# 3821	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	07_petroleum_products$07_09_lpg
# 3822	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	07_petroleum_products$07_09_lpg
# 3823	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	07_petroleum_products$07_09_lpg
# 3824	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	07_petroleum_products$07_09_lpg
# 3825	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	07_petroleum_products$07_09_lpg
# 3826	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	07_petroleum_products$07_09_lpg
# 3827	14_industry_sector$14_03_manufacturing$x$x	07_petroleum_products$07_09_lpg
# 3828	14_industry_sector$x$x$x	07_petroleum_products$07_09_lpg
# 3954	14_industry_sector$14_01_mining_and_quarrying$x$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3955	14_industry_sector$14_02_construction$x$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3961	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3964	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3965	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3968	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3969	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3970	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3971	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3972	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3974	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3975	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3976	14_industry_sector$14_03_manufacturing$x$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3977	14_industry_sector$x$x$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 4077	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	07_petroleum_products$07_11_ethane
# 4088	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	07_petroleum_products$07_11_ethane
# 4089	14_industry_sector$14_03_manufacturing$x$x	07_petroleum_products$07_11_ethane
# 4090	14_industry_sector$x$x$x	07_petroleum_products$07_11_ethane
# 4177	14_industry_sector$14_01_mining_and_quarrying$x$x	07_petroleum_products$07_x_jet_fuel
# 4187	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	07_petroleum_products$07_x_jet_fuel
# 4192	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	07_petroleum_products$07_x_jet_fuel
# 4198	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	07_petroleum_products$07_x_jet_fuel
# 4199	14_industry_sector$14_03_manufacturing$x$x	07_petroleum_products$07_x_jet_fuel
# 4200	14_industry_sector$x$x$x	07_petroleum_products$07_x_jet_fuel
# 4665	14_industry_sector$14_01_mining_and_quarrying$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4670	14_industry_sector$14_02_construction$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4700	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	07_petroleum_products$07_x_other_petroleum_products
# 4715	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	07_petroleum_products$07_x_other_petroleum_products
# 4720	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	07_petroleum_products$07_x_other_petroleum_products
# 4735	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	07_petroleum_products$07_x_other_petroleum_products
# 4740	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	07_petroleum_products$07_x_other_petroleum_products
# 4745	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	07_petroleum_products$07_x_other_petroleum_products
# 4750	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	07_petroleum_products$07_x_other_petroleum_products
# 4755	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	07_petroleum_products$07_x_other_petroleum_products
# 4760	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	07_petroleum_products$07_x_other_petroleum_products
# 4765	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	07_petroleum_products$07_x_other_petroleum_products
# 4770	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	07_petroleum_products$07_x_other_petroleum_products
# 4775	14_industry_sector$14_03_manufacturing$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4780	14_industry_sector$x$x$x	07_petroleum_products$07_x_other_petroleum_products
# 5279	14_industry_sector$14_01_mining_and_quarrying$x$x	07_petroleum_products$x
# 5280	14_industry_sector$14_02_construction$x$x	07_petroleum_products$x
# 5286	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	07_petroleum_products$x
# 5289	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	07_petroleum_products$x
# 5290	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	07_petroleum_products$x
# 5293	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	07_petroleum_products$x
# 5294	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	07_petroleum_products$x
# 5295	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	07_petroleum_products$x
# 5296	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	07_petroleum_products$x
# 5297	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	07_petroleum_products$x
# 5298	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	07_petroleum_products$x
# 5299	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	07_petroleum_products$x
# 5300	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	07_petroleum_products$x
# 5301	14_industry_sector$14_03_manufacturing$x$x	07_petroleum_products$x
# 5302	14_industry_sector$x$x$x	07_petroleum_products$x
# 5463	14_industry_sector$14_01_mining_and_quarrying$x$x	08_gas$08_01_natural_gas
# 5464	14_industry_sector$14_02_construction$x$x	08_gas$08_01_natural_gas
# 5470	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	08_gas$08_01_natural_gas
# 5473	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	08_gas$08_01_natural_gas
# 5474	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	08_gas$08_01_natural_gas
# 5477	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	08_gas$08_01_natural_gas
# 5478	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	08_gas$08_01_natural_gas
# 5479	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	08_gas$08_01_natural_gas
# 5480	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	08_gas$08_01_natural_gas
# 5481	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	08_gas$08_01_natural_gas
# 5482	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	08_gas$08_01_natural_gas
# 5483	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	08_gas$08_01_natural_gas
# 5484	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	08_gas$08_01_natural_gas
# 5485	14_industry_sector$14_03_manufacturing$x$x	08_gas$08_01_natural_gas
# 5486	14_industry_sector$x$x$x	08_gas$08_01_natural_gas
# 5707	14_industry_sector$14_01_mining_and_quarrying$x$x	08_gas$08_03_gas_works_gas
# 5708	14_industry_sector$14_02_construction$x$x	08_gas$08_03_gas_works_gas
# 5714	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	08_gas$08_03_gas_works_gas
# 5717	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	08_gas$08_03_gas_works_gas
# 5718	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	08_gas$08_03_gas_works_gas
# 5721	

#%%


# INDUSTRY 2:


# INDUSTRIAL
#Please map the following aperc sector, fuel combinations to one of the following IPCC 2006 Source/Sink Category, Fuel 2006 combinations and put it in a python dict. ignore the row numbers. (for the IPCC sector categories tr to prioritise mapping using the industrial related sectors rather than the 1.A.1 - Energy Industries sector):
# APERC:

# 	IPCC 2006 Source/Sink Category	Fuel 2006
# 1855	1.A.1 - Energy Industries	Crude Oil
# 1856	1.A.1 - Energy Industries	Orimulsion
# 1857	1.A.1 - Energy Industries	"Natural Gas Liquids
# (NGLs)"
# 1858	1.A.1 - Energy Industries	Motor Gasoline
# 1859	1.A.1 - Energy Industries	Aviation Gasoline
# 1860	1.A.1 - Energy Industries	Jet Gasoline
# 1861	1.A.1 - Energy Industries	Jet Kerosene
# 1862	1.A.1 - Energy Industries	Other Kerosene
# 1863	1.A.1 - Energy Industries	Shale Oil
# 1864	1.A.1 - Energy Industries	Gas Oil
# 1865	1.A.1 - Energy Industries	Diesel Oil
# 1866	1.A.1 - Energy Industries	Residual Fuel Oil
# 1867	1.A.1 - Energy Industries	Liquefied Petroleum Gases
# 1868	1.A.1 - Energy Industries	Ethane
# 1869	1.A.1 - Energy Industries	Naphtha
# 1870	1.A.1 - Energy Industries	Bitumen
# 1871	1.A.1 - Energy Industries	Lubricants
# 1872	1.A.1 - Energy Industries	Petroleum Coke
# 1873	1.A.1 - Energy Industries	Refinery Feedstocks
# 1874	1.A.1 - Energy Industries	Refinery Gas
# 1875	1.A.1 - Energy Industries	Waxes
# 1876	1.A.1 - Energy Industries	White Spirit & SBP
# 1877	1.A.1 - Energy Industries	Other Petroleum Products
# 1878	1.A.1 - Energy Industries	Anthracite
# 1879	1.A.1 - Energy Industries	Coking Coal
# 1880	1.A.1 - Energy Industries	Other Bituminous Coal
# 1881	1.A.1 - Energy Industries	Sub-Bituminous Coal
# 1882	1.A.1 - Energy Industries	Lignite
# 1883	1.A.1 - Energy Industries	Oil Shale and Tar Sands
# 1884	1.A.1 - Energy Industries	Brown Coal Briquettes
# 1885	1.A.1 - Energy Industries	Patent Fuel
# 1886	1.A.1 - Energy Industries	Coke Oven Coke and Lignite Coke
# 1887	1.A.1 - Energy Industries	Gas Coke
# 1888	1.A.1 - Energy Industries	Coal Tar
# 1889	1.A.1 - Energy Industries	Gas Works Gas
# 1890	1.A.1 - Energy Industries	Coke Oven Gas
# 1891	1.A.1 - Energy Industries	Blast Furnace Gas
# 1892	1.A.1 - Energy Industries	Oxygen Steel Furnace Gas
# 1893	1.A.1 - Energy Industries	Natural Gas
# 1894	1.A.1 - Energy Industries	Municipal Wastes (non-biomass fraction)
# 1895	1.A.1 - Energy Industries	Industrial Wastes
# 1896	1.A.1 - Energy Industries	Waste Oils
# 1897	1.A.1 - Energy Industries	Peat
# 1898	1.A.1 - Energy Industries	Wood/Wood Waste
# 1899	1.A.1 - Energy Industries	Sulphite Lyes (Black Liquor)
# 1900	1.A.1 - Energy Industries	Other Primary Solid Biomass
# 1901	1.A.1 - Energy Industries	Charcoal
# 1902	1.A.1 - Energy Industries	Biogasoline
# 1903	1.A.1 - Energy Industries	Biodiesels
# 1904	1.A.1 - Energy Industries	Other Liquid Biofuels
# 1905	1.A.1 - Energy Industries	Landfill Gas
# 1906	1.A.1 - Energy Industries	Sludge Gas
# 1907	1.A.1 - Energy Industries	Other Biogas
# 1908	1.A.1 - Energy Industries	Municipal Wastes (biomass fraction)
# 2017	1.A.2 - Manufacturing Industries and Construction	Crude Oil
# 2018	1.A.2 - Manufacturing Industries and Construction	Orimulsion
# 2019	1.A.2 - Manufacturing Industries and Construction	"Natural Gas Liquids
# (NGLs)"
# 2020	1.A.2 - Manufacturing Industries and Construction	Motor Gasoline
# 2021	1.A.2 - Manufacturing Industries and Construction	Aviation Gasoline
# 2022	1.A.2 - Manufacturing Industries and Construction	Jet Gasoline
# 2023	1.A.2 - Manufacturing Industries and Construction	Jet Kerosene
# 2024	1.A.2 - Manufacturing Industries and Construction	Other Kerosene
# 2025	1.A.2 - Manufacturing Industries and Construction	Shale Oil
# 2026	1.A.2 - Manufacturing Industries and Construction	Gas Oil
# 2027	1.A.2 - Manufacturing Industries and Construction	Diesel Oil
# 2028	1.A.2 - Manufacturing Industries and Construction	Residual Fuel Oil
# 2029	1.A.2 - Manufacturing Industries and Construction	Liquefied Petroleum Gases
# 2030	1.A.2 - Manufacturing Industries and Construction	Ethane
# 2031	1.A.2 - Manufacturing Industries and Construction	Naphtha
# 2032	1.A.2 - Manufacturing Industries and Construction	Bitumen
# 2033	1.A.2 - Manufacturing Industries and Construction	Lubricants
# 2034	1.A.2 - Manufacturing Industries and Construction	Petroleum Coke
# 2035	1.A.2 - Manufacturing Industries and Construction	Refinery Feedstocks
# 2036	1.A.2 - Manufacturing Industries and Construction	Refinery Gas
# 2037	1.A.2 - Manufacturing Industries and Construction	Waxes
# 2038	1.A.2 - Manufacturing Industries and Construction	White Spirit & SBP
# 2039	1.A.2 - Manufacturing Industries and Construction	Other Petroleum Products
# 2040	1.A.2 - Manufacturing Industries and Construction	Anthracite
# 2041	1.A.2 - Manufacturing Industries and Construction	Coking Coal
# 2042	1.A.2 - Manufacturing Industries and Construction	Other Bituminous Coal
# 2043	1.A.2 - Manufacturing Industries and Construction	Sub-Bituminous Coal
# 2044	1.A.2 - Manufacturing Industries and Construction	Lignite
# 2045	1.A.2 - Manufacturing Industries and Construction	Oil Shale and Tar Sands
# 2046	1.A.2 - Manufacturing Industries and Construction	Brown Coal Briquettes
# 2047	1.A.2 - Manufacturing Industries and Construction	Patent Fuel
# 2048	1.A.2 - Manufacturing Industries and Construction	Coke Oven Coke and Lignite Coke
# 2049	1.A.2 - Manufacturing Industries and Construction	Gas Coke
# 2050	1.A.2 - Manufacturing Industries and Construction	Coal Tar
# 2051	1.A.2 - Manufacturing Industries and Construction	Gas Works Gas
# 2052	1.A.2 - Manufacturing Industries and Construction	Coke Oven Gas
# 2053	1.A.2 - Manufacturing Industries and Construction	Blast Furnace Gas
# 2054	1.A.2 - Manufacturing Industries and Construction	Oxygen Steel Furnace Gas
# 2055	1.A.2 - Manufacturing Industries and Construction	Natural Gas
# 2056	1.A.2 - Manufacturing Industries and Construction	Municipal Wastes (non-biomass fraction)
# 2057	1.A.2 - Manufacturing Industries and Construction	Industrial Wastes
# 2058	1.A.2 - Manufacturing Industries and Construction	Waste Oils
# 2059	1.A.2 - Manufacturing Industries and Construction	Peat
# 2060	1.A.2 - Manufacturing Industries and Construction	Wood/Wood Waste
# 2061	1.A.2 - Manufacturing Industries and Construction	Sulphite Lyes (Black Liquor)
# 2062	1.A.2 - Manufacturing Industries and Construction	Other Primary Solid Biomass
# 2063	1.A.2 - Manufacturing Industries and Construction	Charcoal
# 2064	1.A.2 - Manufacturing Industries and Construction	Biogasoline
# 2065	1.A.2 - Manufacturing Industries and Construction	Biodiesels
# 2066	1.A.2 - Manufacturing Industries and Construction	Other Liquid Biofuels
# 2067	1.A.2 - Manufacturing Industries and Construction	Landfill Gas
# 2068	1.A.2 - Manufacturing Industries and Construction	Sludge Gas
# 2069	1.A.2 - Manufacturing Industries and Construction	Other Biogas
# 2070	1.A.2 - Manufacturing Industries and Construction	Municipal Wastes (biomass fraction)


#APERC
# 14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	08_gas$08_03_gas_works_gas
# 5722	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	08_gas$08_03_gas_works_gas
# 5723	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	08_gas$08_03_gas_works_gas
# 5724	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	08_gas$08_03_gas_works_gas
# 5725	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	08_gas$08_03_gas_works_gas
# 5726	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	08_gas$08_03_gas_works_gas
# 5727	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	08_gas$08_03_gas_works_gas
# 5728	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	08_gas$08_03_gas_works_gas
# 5729	14_industry_sector$14_03_manufacturing$x$x	08_gas$08_03_gas_works_gas
# 5730	14_industry_sector$x$x$x	08_gas$08_03_gas_works_gas
# 5867	14_industry_sector$14_01_mining_and_quarrying$x$x	08_gas$x
# 5868	14_industry_sector$14_02_construction$x$x	08_gas$x
# 5874	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	08_gas$x
# 5877	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	08_gas$x
# 5878	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	08_gas$x
# 5881	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	08_gas$x
# 5882	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	08_gas$x
# 5883	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	08_gas$x
# 5884	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	08_gas$x
# 5885	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	08_gas$x
# 5886	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	08_gas$x
# 5887	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	08_gas$x
# 5888	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	08_gas$x
# 5889	14_industry_sector$14_03_manufacturing$x$x	08_gas$x
# 5890	14_industry_sector$x$x$x	08_gas$x
# 7098	14_industry_sector$14_01_mining_and_quarrying$x$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7105	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7108	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7112	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7115	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7116	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7117	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7118	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7119	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7120	14_industry_sector$14_03_manufacturing$x$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7121	14_industry_sector$x$x$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7217	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	15_solid_biomass$15_02_bagasse
# 7224	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	15_solid_biomass$15_02_bagasse
# 7228	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	15_solid_biomass$15_02_bagasse
# 7229	14_industry_sector$14_03_manufacturing$x$x	15_solid_biomass$15_02_bagasse
# 7230	14_industry_sector$x$x$x	15_solid_biomass$15_02_bagasse
# 7313	14_industry_sector$14_01_mining_and_quarrying$x$x	15_solid_biomass$15_03_charcoal
# 7323	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	15_solid_biomass$15_03_charcoal
# 7327	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	15_solid_biomass$15_03_charcoal
# 7330	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	15_solid_biomass$15_03_charcoal
# 7334	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	15_solid_biomass$15_03_charcoal
# 7335	14_industry_sector$14_03_manufacturing$x$x	15_solid_biomass$15_03_charcoal
# 7336	14_industry_sector$x$x$x	15_solid_biomass$15_03_charcoal
# 7432	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	15_solid_biomass$15_04_black_liquor
# 7440	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	15_solid_biomass$15_04_black_liquor
# 7444	14_industry_sector$14_03_manufacturing$x$x	15_solid_biomass$15_04_black_liquor
# 7445	14_industry_sector$x$x$x	15_solid_biomass$15_04_black_liquor
# 7531	14_industry_sector$14_01_mining_and_quarrying$x$x	15_solid_biomass$15_05_other_biomass
# 7532	14_industry_sector$14_02_construction$x$x	15_solid_biomass$15_05_other_biomass
# 7538	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	15_solid_biomass$15_05_other_biomass
# 7541	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	15_solid_biomass$15_05_other_biomass
# 7542	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	15_solid_biomass$15_05_other_biomass
# 7545	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	15_solid_biomass$15_05_other_biomass
# 7546	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	15_solid_biomass$15_05_other_biomass
# 7547	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	15_solid_biomass$15_05_other_biomass
# 7548	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	15_solid_biomass$15_05_other_biomass
# 7549	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	15_solid_biomass$15_05_other_biomass
# 7550	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	15_solid_biomass$15_05_other_biomass
# 7551	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	15_solid_biomass$15_05_other_biomass
# 7552	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	15_solid_biomass$15_05_other_biomass
# 7553	14_industry_sector$14_03_manufacturing$x$x	15_solid_biomass$15_05_other_biomass
# 7554	14_industry_sector$x$x$x	15_solid_biomass$15_05_other_biomass
# 7687	14_industry_sector$14_01_mining_and_quarrying$x$x	15_solid_biomass$x
# 7688	14_industry_sector$14_02_construction$x$x	15_solid_biomass$x
# 7694	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	15_solid_biomass$x
# 7697	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	15_solid_biomass$x
# 7698	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	15_solid_biomass$x
# 7701	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	15_solid_biomass$x
# 7702	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	15_solid_biomass$x
# 7703	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	15_solid_biomass$x
# 7704	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	15_solid_biomass$x
# 7705	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	15_solid_biomass$x
# 7706	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	15_solid_biomass$x
# 7707	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	15_solid_biomass$x
# 7708	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	15_solid_biomass$x
# 7709	14_industry_sector$14_03_manufacturing$x$x	15_solid_biomass$x
# 7710	14_industry_sector$x$x$x	15_solid_biomass$x
# 7898	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	16_others$16_01_biogas
# 7907	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	16_others$16_01_biogas
# 7919	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	16_others$16_01_biogas
# 7922	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	16_others$16_01_biogas
# 7928	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	16_others$16_01_biogas
# 7931	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	16_others$16_01_biogas
# 7937	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	16_others$16_01_biogas
# 7940	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	16_others$16_01_biogas
# 7943	14_industry_sector$14_03_manufacturing$x$x	16_others$16_01_biogas
# 7946	14_industry_sector$x$x$x	16_others$16_01_biogas
# 8222	14_industry_sector$14_01_mining_and_quarrying$x$x	16_others$16_02_industrial_waste
# 8223	14_industry_sector$14_02_construction$x$x	16_others$16_02_industrial_waste
# 8229	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	16_others$16_02_industrial_waste
# 8232	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	16_others$16_02_industrial_waste
# 8233	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	16_others$16_02_industrial_waste
# 8236	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	16_others$16_02_industrial_waste
# 8237	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	16_others$16_02_industrial_waste
# 8238	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	16_others$16_02_industrial_waste
# 8239	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	16_others$16_02_industrial_waste
# 8240	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	16_others$16_02_industrial_waste
# 8241	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	16_others$16_02_industrial_waste
# 8242	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	16_others$16_02_industrial_waste
# 8243	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	16_others$16_02_industrial_waste
# 8244	14_industry_sector$14_03_manufacturing$x$x	16_others$16_02_industrial_waste
# 8245	14_industry_sector$x$x$x	16_others$16_02_industrial_waste
# 8334	14_industry_sector$14_02_construction$x$x	16_others$16_03_municipal_solid_waste_renewable
# 8343	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	16_others$16_03_municipal_solid_waste_renewable
# 8347	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	16_others$16_03_municipal_solid_waste_renewable
# 8351	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	16_others$16_03_municipal_solid_waste_renewable
# 8353	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	16_others$16_03_municipal_solid_waste_renewable
# 8354	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	16_others$16_03_municipal_solid_waste_renewable
# 8355	14_industry_sector$14_03_manufacturing$x$x	16_others$16_03_municipal_solid_waste_renewable
# 8356	14_industry_sector$x$x$x	16_others$16_03_municipal_solid_waste_renewable
# 8445	14_industry_sector$14_02_construction$x$x	16_others$16_04_municipal_solid_waste_nonrenewable
# 8454	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	16_others$16_04_municipal_solid_waste_nonrenewable
# 8462	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	16_others$16_04_municipal_solid_waste_nonrenewable
# 8464	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	16_others$16_04_municipal_solid_waste_nonrenewable
# 8465	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	16_others$16_04_municipal_solid_waste_nonrenewable
# 8466	14_industry_sector$14_03_manufacturing$x$x	16_others$16_04_municipal_solid_waste_nonrenewable
# 8467	14_industry_sector$x$x$x	16_others$16_04_municipal_solid_waste_nonrenewable
# 8552	14_industry_sector$14_01_mining_and_quarrying$x$x	16_others$16_05_biogasoline
# 8573	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	16_others$16_05_biogasoline
# 8574	14_industry_sector$14_03_manufacturing$x$x	16_others$16_05_biogasoline
# 8575	14_industry_sector$x$x$x	16_others$16_05_biogasoline
# 8688	14_industry_sector$14_01_mining_and_quarrying$x$x	16_others$16_06_biodiesel
# 8689	14_industry_sector$14_02_construction$x$x	16_others$16_06_biodiesel
# 8695	14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x	16_others$16_06_biodiesel
# 8698	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	16_others$16_06_biodiesel
# 8699	14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x	16_others$16_06_biodiesel
# 8702	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	16_others$16_06_biodiesel
# 8703	14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x	16_others$16_06_biodiesel
# 8704	14_industry_sector$14_03_manufacturing$14_03_06_machinery$x	16_others$16_06_biodiesel
# 8705	14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x	16_others$16_06_biodiesel
# 8706	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	16_others$16_06_biodiesel
# 8707	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	16_others$16_06_biodiesel
# 8708	14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x	16_others$16_06_biodiesel
# 8709	14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x	16_others$16_06_biodiesel
# 8710	14_industry_sector$14_03_manufacturing$x$x	16_others$16_06_biodiesel
# 8711	14_industry_sector$x$x$x	16_others$16_06_biodiesel
# 9086	14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x	16_others$16_08_other_liquid_biofuels
# 9090	14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x	16_others$16_08_other_liquid_biofuels
# 9094	14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x	16_others$16_08_other_liquid_biofuels
# 9095	14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x	16_others$16_08_other_liquid_biofuels
# 9098	14_industry_sector$14_03_manufacturing$x$x	16_others$16_08_other_liquid_biofuels
# 9099	14_industry_sector$x$x$x	16_others$16_08_other_liquid_biofuels















#%%
#SERVICES
#Please map the following aperc sector, fuel combinations to one of the following IPCC 2006 Source/Sink Category, Fuel 2006 combinations and put it in a python dict. ignore the row numbers. (for the IPCC sector categories tr to prioritise mapping using the SERVICES related sectors rather than the 1.A.1 - Energy Industries sector):
# APERC:

# 	IPCC 2006 Source/Sink Category	Fuel 2006
# 1855	1.A.1 - Energy Industries	Crude Oil
# 1856	1.A.1 - Energy Industries	Orimulsion
# 1857	1.A.1 - Energy Industries	Natural Gas Liquids (NGLs)
# 1858	1.A.1 - Energy Industries	Motor Gasoline
# 1859	1.A.1 - Energy Industries	Aviation Gasoline
# 1860	1.A.1 - Energy Industries	Jet Gasoline
# 1861	1.A.1 - Energy Industries	Jet Kerosene
# 1862	1.A.1 - Energy Industries	Other Kerosene
# 1863	1.A.1 - Energy Industries	Shale Oil
# 1864	1.A.1 - Energy Industries	Gas Oil
# 1865	1.A.1 - Energy Industries	Diesel Oil
# 1866	1.A.1 - Energy Industries	Residual Fuel Oil
# 1867	1.A.1 - Energy Industries	Liquefied Petroleum Gases
# 1868	1.A.1 - Energy Industries	Ethane
# 1869	1.A.1 - Energy Industries	Naphtha
# 1870	1.A.1 - Energy Industries	Bitumen
# 1871	1.A.1 - Energy Industries	Lubricants
# 1872	1.A.1 - Energy Industries	Petroleum Coke
# 1873	1.A.1 - Energy Industries	Refinery Feedstocks
# 1874	1.A.1 - Energy Industries	Refinery Gas
# 1875	1.A.1 - Energy Industries	Waxes
# 1876	1.A.1 - Energy Industries	White Spirit & SBP
# 1877	1.A.1 - Energy Industries	Other Petroleum Products
# 1878	1.A.1 - Energy Industries	Anthracite
# 1879	1.A.1 - Energy Industries	Coking Coal
# 1880	1.A.1 - Energy Industries	Other Bituminous Coal
# 1881	1.A.1 - Energy Industries	Sub-Bituminous Coal
# 1882	1.A.1 - Energy Industries	Lignite
# 1883	1.A.1 - Energy Industries	Oil Shale and Tar Sands
# 1884	1.A.1 - Energy Industries	Brown Coal Briquettes
# 1885	1.A.1 - Energy Industries	Patent Fuel
# 1886	1.A.1 - Energy Industries	Coke Oven Coke and Lignite Coke
# 1887	1.A.1 - Energy Industries	Gas Coke
# 1888	1.A.1 - Energy Industries	Coal Tar
# 1889	1.A.1 - Energy Industries	Gas Works Gas
# 1890	1.A.1 - Energy Industries	Coke Oven Gas
# 1891	1.A.1 - Energy Industries	Blast Furnace Gas
# 1892	1.A.1 - Energy Industries	Oxygen Steel Furnace Gas
# 1893	1.A.1 - Energy Industries	Natural Gas
# 1894	1.A.1 - Energy Industries	Municipal Wastes (non-biomass fraction)
# 1895	1.A.1 - Energy Industries	Industrial Wastes
# 1896	1.A.1 - Energy Industries	Waste Oils
# 1897	1.A.1 - Energy Industries	Peat
# 1898	1.A.1 - Energy Industries	Wood/Wood Waste
# 1899	1.A.1 - Energy Industries	Sulphite Lyes (Black Liquor)
# 1900	1.A.1 - Energy Industries	Other Primary Solid Biomass
# 1901	1.A.1 - Energy Industries	Charcoal
# 1902	1.A.1 - Energy Industries	Biogasoline
# 1903	1.A.1 - Energy Industries	Biodiesels
# 1904	1.A.1 - Energy Industries	Other Liquid Biofuels
# 1905	1.A.1 - Energy Industries	Landfill Gas
# 1906	1.A.1 - Energy Industries	Sludge Gas
# 1907	1.A.1 - Energy Industries	Other Biogas
# 1908	1.A.1 - Energy Industries	Municipal Wastes (biomass fraction)
# 2179	1.A.4.a - Commercial/Institutional	Crude Oil
# 2180	1.A.4.a - Commercial/Institutional	Orimulsion
# 2181	1.A.4.a - Commercial/Institutional	Natural Gas Liquids (NGLs)
# 2182	1.A.4.a - Commercial/Institutional	Motor Gasoline
# 2183	1.A.4.a - Commercial/Institutional	Aviation Gasoline
# 2184	1.A.4.a - Commercial/Institutional	Jet Gasoline
# 2185	1.A.4.a - Commercial/Institutional	Jet Kerosene
# 2186	1.A.4.a - Commercial/Institutional	Other Kerosene
# 2187	1.A.4.a - Commercial/Institutional	Shale Oil
# 2188	1.A.4.a - Commercial/Institutional	Gas Oil
# 2189	1.A.4.a - Commercial/Institutional	Diesel Oil
# 2190	1.A.4.a - Commercial/Institutional	Residual Fuel Oil
# 2191	1.A.4.a - Commercial/Institutional	Liquefied Petroleum Gases
# 2192	1.A.4.a - Commercial/Institutional	Ethane
# 2193	1.A.4.a - Commercial/Institutional	Naphtha
# 2194	1.A.4.a - Commercial/Institutional	Bitumen
# 2195	1.A.4.a - Commercial/Institutional	Lubricants
# 2196	1.A.4.a - Commercial/Institutional	Petroleum Coke
# 2197	1.A.4.a - Commercial/Institutional	Refinery Feedstocks
# 2198	1.A.4.a - Commercial/Institutional	Refinery Gas
# 2199	1.A.4.a - Commercial/Institutional	Waxes
# 2200	1.A.4.a - Commercial/Institutional	White Spirit & SBP
# 2201	1.A.4.a - Commercial/Institutional	Other Petroleum Products
# 2202	1.A.4.a - Commercial/Institutional	Anthracite
# 2203	1.A.4.a - Commercial/Institutional	Coking Coal
# 2204	1.A.4.a - Commercial/Institutional	Other Bituminous Coal
# 2205	1.A.4.a - Commercial/Institutional	Sub-Bituminous Coal
# 2206	1.A.4.a - Commercial/Institutional	Lignite
# 2207	1.A.4.a - Commercial/Institutional	Oil Shale and Tar Sands
# 2208	1.A.4.a - Commercial/Institutional	Brown Coal Briquettes
# 2209	1.A.4.a - Commercial/Institutional	Patent Fuel
# 2210	1.A.4.a - Commercial/Institutional	Coke Oven Coke and Lignite Coke
# 2211	1.A.4.a - Commercial/Institutional	Gas Coke
# 2212	1.A.4.a - Commercial/Institutional	Coal Tar
# 2213	1.A.4.a - Commercial/Institutional	Gas Works Gas
# 2214	1.A.4.a - Commercial/Institutional	Coke Oven Gas
# 2215	1.A.4.a - Commercial/Institutional	Blast Furnace Gas
# 2216	1.A.4.a - Commercial/Institutional	Oxygen Steel Furnace Gas
# 2217	1.A.4.a - Commercial/Institutional	Natural Gas
# 2218	1.A.4.a - Commercial/Institutional	Municipal Wastes (non-biomass fraction)
# 2219	1.A.4.a - Commercial/Institutional	Industrial Wastes
# 2220	1.A.4.a - Commercial/Institutional	Waste Oils
# 2221	1.A.4.a - Commercial/Institutional	Peat
# 2222	1.A.4.a - Commercial/Institutional	Wood/Wood Waste
# 2223	1.A.4.a - Commercial/Institutional	Sulphite Lyes (Black Liquor)
# 2224	1.A.4.a - Commercial/Institutional	Other Primary Solid Biomass
# 2225	1.A.4.a - Commercial/Institutional	Charcoal
# 2226	1.A.4.a - Commercial/Institutional	Biogasoline
# 2227	1.A.4.a - Commercial/Institutional	Biodiesels
# 2228	1.A.4.a - Commercial/Institutional	Other Liquid Biofuels
# 2229	1.A.4.a - Commercial/Institutional	Landfill Gas
# 2230	1.A.4.a - Commercial/Institutional	Sludge Gas
# 2231	1.A.4.a - Commercial/Institutional	Other Biogas
# 2232	1.A.4.a - Commercial/Institutional	Municipal Wastes (biomass fraction)

# APERC:
#     	aperc_sector	aperc_fuel
# 61	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	01_coal$01_01_coking_coal
# 210	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	01_coal$01_05_lignite
# 466	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	01_coal$01_x_thermal_coal
# 830	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	01_coal$x
# 1259	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	02_coal_products$x
# 1516	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	03_peat$x
# 1660	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	04_peat_products$x
# 2598	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	07_petroleum_products$07_01_motor_gasoline
# 2737	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	07_petroleum_products$07_02_aviation_gasoline
# 2852	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	07_petroleum_products$07_03_naphtha
# 3088	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	07_petroleum_products$07_06_kerosene
# 3456	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	07_petroleum_products$07_07_gas_diesel_oil
# 3703	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	07_petroleum_products$07_08_fuel_oil
# 3853	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	07_petroleum_products$07_09_lpg
# 3978	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 4091	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	07_petroleum_products$07_11_ethane
# 4225	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	07_petroleum_products$07_x_jet_fuel
# 4905	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	07_petroleum_products$07_x_other_petroleum_products
# 5327	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	07_petroleum_products$x
# 5511	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	08_gas$08_01_natural_gas
# 5622	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	08_gas$08_02_lng
# 5733	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	08_gas$08_03_gas_works_gas
# 5915	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	08_gas$x
# 7122	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7231	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	15_solid_biomass$15_02_bagasse
# 7337	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	15_solid_biomass$15_03_charcoal
# 7446	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	15_solid_biomass$15_04_black_liquor
# 7555	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	15_solid_biomass$15_05_other_biomass
# 7711	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	15_solid_biomass$x
# 8021	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	16_others$16_01_biogas
# 8246	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	16_others$16_02_industrial_waste
# 8357	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	16_others$16_03_municipal_solid_waste_renewable
# 8468	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	16_others$16_04_municipal_solid_waste_nonrenewable
# 8600	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	16_others$16_05_biogasoline
# 8736	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	16_others$16_06_biodiesel
# 8944	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	16_others$16_07_bio_jet_kerosene
# 9100	16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x	16_others$16_08_other_liquid_biofuels




#%%
# TRANSPORFAMTION
#Please map the following aperc sector, fuel combinations to one of the following IPCC 2006 Source/Sink Category, Fuel 2006 combinations and put it in a python dict. ignore the row numbers. (for the IPCC sector categories tr to prioritise mapping using the  1.A.1 - Energy Industries sector):

# 	IPCC 2006 Source/Sink Category	Fuel 2006
# 1855	1.A.1 - Energy Industries	Crude Oil
# 1856	1.A.1 - Energy Industries	Orimulsion
# 1857	1.A.1 - Energy Industries	Natural Gas Liquids (NGLs)
# 1858	1.A.1 - Energy Industries	Motor Gasoline
# 1859	1.A.1 - Energy Industries	Aviation Gasoline
# 1860	1.A.1 - Energy Industries	Jet Gasoline
# 1861	1.A.1 - Energy Industries	Jet Kerosene
# 1862	1.A.1 - Energy Industries	Other Kerosene
# 1863	1.A.1 - Energy Industries	Shale Oil
# 1864	1.A.1 - Energy Industries	Gas Oil
# 1865	1.A.1 - Energy Industries	Diesel Oil
# 1866	1.A.1 - Energy Industries	Residual Fuel Oil
# 1867	1.A.1 - Energy Industries	Liquefied Petroleum Gases
# 1868	1.A.1 - Energy Industries	Ethane
# 1869	1.A.1 - Energy Industries	Naphtha
# 1870	1.A.1 - Energy Industries	Bitumen
# 1871	1.A.1 - Energy Industries	Lubricants
# 1872	1.A.1 - Energy Industries	Petroleum Coke
# 1873	1.A.1 - Energy Industries	Refinery Feedstocks
# 1874	1.A.1 - Energy Industries	Refinery Gas
# 1875	1.A.1 - Energy Industries	Waxes
# 1876	1.A.1 - Energy Industries	White Spirit & SBP
# 1877	1.A.1 - Energy Industries	Other Petroleum Products
# 1878	1.A.1 - Energy Industries	Anthracite
# 1879	1.A.1 - Energy Industries	Coking Coal
# 1880	1.A.1 - Energy Industries	Other Bituminous Coal
# 1881	1.A.1 - Energy Industries	Sub-Bituminous Coal
# 1882	1.A.1 - Energy Industries	Lignite
# 1883	1.A.1 - Energy Industries	Oil Shale and Tar Sands
# 1884	1.A.1 - Energy Industries	Brown Coal Briquettes
# 1885	1.A.1 - Energy Industries	Patent Fuel
# 1886	1.A.1 - Energy Industries	Coke Oven Coke and Lignite Coke
# 1887	1.A.1 - Energy Industries	Gas Coke
# 1888	1.A.1 - Energy Industries	Coal Tar
# 1889	1.A.1 - Energy Industries	Gas Works Gas
# 1890	1.A.1 - Energy Industries	Coke Oven Gas
# 1891	1.A.1 - Energy Industries	Blast Furnace Gas
# 1892	1.A.1 - Energy Industries	Oxygen Steel Furnace Gas
# 1893	1.A.1 - Energy Industries	Natural Gas
# 1894	1.A.1 - Energy Industries	Municipal Wastes (non-biomass fraction)
# 1895	1.A.1 - Energy Industries	Industrial Wastes
# 1896	1.A.1 - Energy Industries	Waste Oils
# 1897	1.A.1 - Energy Industries	Peat
# 1898	1.A.1 - Energy Industries	Wood/Wood Waste
# 1899	1.A.1 - Energy Industries	Sulphite Lyes (Black Liquor)
# 1900	1.A.1 - Energy Industries	Other Primary Solid Biomass
# 1901	1.A.1 - Energy Industries	Charcoal
# 1902	1.A.1 - Energy Industries	Biogasoline
# 1903	1.A.1 - Energy Industries	Biodiesels
# 1904	1.A.1 - Energy Industries	Other Liquid Biofuels
# 1905	1.A.1 - Energy Industries	Landfill Gas
# 1906	1.A.1 - Energy Industries	Sludge Gas
# 1907	1.A.1 - Energy Industries	Other Biogas
# 1908	1.A.1 - Energy Industries	Municipal Wastes (biomass fraction)
# 2503	1.A - Fuel Combustion Activities	Residual Fuel Oil
# 2504	1.A - Fuel Combustion Activities	Shale Oil
# 2507	1.A - Fuel Combustion Activities	Gas Oil
# 2508	1.A - Fuel Combustion Activities	Diesel Oil
# 2512	1.A - Fuel Combustion Activities	Other Bituminous Coal
# 2519	1.A - Fuel Combustion Activities	Natural Gas
# 2523	1.A - Fuel Combustion Activities	Peat
# 2525	1.A - Fuel Combustion Activities	Wood/Wood Waste
# 2542	1.A - Fuel Combustion Activities	Lignite



# APERC:
# 	aperc_sector	aperc_fuel
# 5	09_total_transformation_sector$09_01_electricity_plants$x$x	01_coal$01_01_coking_coal
# 6	09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x	01_coal$01_01_coking_coal
# 7	09_total_transformation_sector$09_06_gas_processing_plants$x$x	01_coal$01_01_coking_coal
# 8	09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x	01_coal$01_01_coking_coal
# 9	09_total_transformation_sector$09_08_coal_transformation$09_08_02_blast_furnaces$x	01_coal$01_01_coking_coal
# 10	09_total_transformation_sector$09_08_coal_transformation$09_08_03_patent_fuel_plants$x	01_coal$01_01_coking_coal
# 11	09_total_transformation_sector$09_08_coal_transformation$09_08_04_bkb_pb_plants$x	01_coal$01_01_coking_coal
# 12	09_total_transformation_sector$09_08_coal_transformation$09_08_05_liquefaction_coal_to_oil$x	01_coal$01_01_coking_coal
# 13	09_total_transformation_sector$09_08_coal_transformation$x$x	01_coal$01_01_coking_coal
# 15	09_total_transformation_sector$09_x_heat_plants$x$x	01_coal$01_01_coking_coal
# 16	09_total_transformation_sector$x$x$x	01_coal$01_01_coking_coal
# 145	09_total_transformation_sector$09_01_electricity_plants$x$x	01_coal$01_05_lignite
# 150	09_total_transformation_sector$09_02_chp_plants$x$x	01_coal$01_05_lignite
# 151	09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x	01_coal$01_05_lignite
# 152	09_total_transformation_sector$09_06_gas_processing_plants$x$x	01_coal$01_05_lignite
# 153	09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x	01_coal$01_05_lignite
# 156	09_total_transformation_sector$09_08_coal_transformation$09_08_04_bkb_pb_plants$x	01_coal$01_05_lignite
# 157	09_total_transformation_sector$09_08_coal_transformation$09_08_05_liquefaction_coal_to_oil$x	01_coal$01_05_lignite
# 158	09_total_transformation_sector$09_08_coal_transformation$x$x	01_coal$01_05_lignite
# 164	09_total_transformation_sector$09_x_heat_plants$x$x	01_coal$01_05_lignite
# 165	09_total_transformation_sector$x$x$x	01_coal$01_05_lignite
# 328	09_total_transformation_sector$09_01_electricity_plants$x$x	01_coal$01_x_thermal_coal
# 338	09_total_transformation_sector$09_02_chp_plants$x$x	01_coal$01_x_thermal_coal
# 340	09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x	01_coal$01_x_thermal_coal
# 342	09_total_transformation_sector$09_06_gas_processing_plants$x$x	01_coal$01_x_thermal_coal
# 344	09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x	01_coal$01_x_thermal_coal
# 346	09_total_transformation_sector$09_08_coal_transformation$09_08_02_blast_furnaces$x	01_coal$01_x_thermal_coal
# 348	09_total_transformation_sector$09_08_coal_transformation$09_08_03_patent_fuel_plants$x	01_coal$01_x_thermal_coal
# 350	09_total_transformation_sector$09_08_coal_transformation$09_08_04_bkb_pb_plants$x	01_coal$01_x_thermal_coal
# 352	09_total_transformation_sector$09_08_coal_transformation$09_08_05_liquefaction_coal_to_oil$x	01_coal$01_x_thermal_coal
# 354	09_total_transformation_sector$09_08_coal_transformation$x$x	01_coal$01_x_thermal_coal
# 366	09_total_transformation_sector$09_x_heat_plants$x$x	01_coal$01_x_thermal_coal
# 368	09_total_transformation_sector$x$x$x	01_coal$01_x_thermal_coal
# 638	09_total_transformation_sector$09_01_electricity_plants$x$x	01_coal$x
# 648	09_total_transformation_sector$09_02_chp_plants$x$x	01_coal$x
# 650	09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x	01_coal$x
# 652	09_total_transformation_sector$09_06_gas_processing_plants$x$x	01_coal$x
# 654	09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x	01_coal$x
# 656	09_total_transformation_sector$09_08_coal_transformation$09_08_02_blast_furnaces$x	01_coal$x
# 658	09_total_transformation_sector$09_08_coal_transformation$09_08_03_patent_fuel_plants$x	01_coal$x
# 660	09_total_transformation_sector$09_08_coal_transformation$09_08_04_bkb_pb_plants$x	01_coal$x
# 662	09_total_transformation_sector$09_08_coal_transformation$09_08_05_liquefaction_coal_to_oil$x	01_coal$x
# 664	09_total_transformation_sector$09_08_coal_transformation$x$x	01_coal$x
# 690	09_total_transformation_sector$09_x_heat_plants$x$x	01_coal$x
# 692	09_total_transformation_sector$x$x$x	01_coal$x
# 1034	09_total_transformation_sector$09_01_electricity_plants$x$x	02_coal_products$x
# 1049	09_total_transformation_sector$09_02_chp_plants$x$x	02_coal_products$x
# 1052	09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x	02_coal_products$x
# 1055	09_total_transformation_sector$09_06_gas_processing_plants$x$x	02_coal_products$x
# 1058	09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x	02_coal_products$x
# 1061	09_total_transformation_sector$09_08_coal_transformation$09_08_02_blast_furnaces$x	02_coal_products$x
# 1064	09_total_transformation_sector$09_08_coal_transformation$09_08_03_patent_fuel_plants$x	02_coal_products$x
# 1067	09_total_transformation_sector$09_08_coal_transformation$09_08_04_bkb_pb_plants$x	02_coal_products$x
# 1070	09_total_transformation_sector$09_08_coal_transformation$09_08_05_liquefaction_coal_to_oil$x	02_coal_products$x
# 1073	09_total_transformation_sector$09_08_coal_transformation$x$x	02_coal_products$x
# 1112	09_total_transformation_sector$09_x_heat_plants$x$x	02_coal_products$x
# 1115	09_total_transformation_sector$x$x$x	02_coal_products$x
# 1421	09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x	02_coal_products$x
# 1456	09_total_transformation_sector$09_01_electricity_plants$x$x	03_peat$x
# 1461	09_total_transformation_sector$09_02_chp_plants$x$x	03_peat$x
# 1465	09_total_transformation_sector$09_08_coal_transformation$09_08_04_bkb_pb_plants$x	03_peat$x
# 1467	09_total_transformation_sector$09_08_coal_transformation$x$x	03_peat$x
# 1473	09_total_transformation_sector$09_x_heat_plants$x$x	03_peat$x
# 1474	09_total_transformation_sector$x$x$x	03_peat$x
# 1607	09_total_transformation_sector$09_02_chp_plants$x$x	04_peat_products$x
# 1611	09_total_transformation_sector$09_08_coal_transformation$09_08_04_bkb_pb_plants$x	04_peat_products$x
# 1613	09_total_transformation_sector$09_08_coal_transformation$x$x	04_peat_products$x
# 1619	09_total_transformation_sector$09_x_heat_plants$x$x	04_peat_products$x
# 1620	09_total_transformation_sector$x$x$x	04_peat_products$x
# 1916	09_total_transformation_sector$09_01_electricity_plants$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1917	09_total_transformation_sector$09_02_chp_plants$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1918	09_total_transformation_sector$09_07_oil_refineries$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1926	09_total_transformation_sector$09_x_heat_plants$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1927	09_total_transformation_sector$x$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 2031	09_total_transformation_sector$09_01_electricity_plants$x$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2032	09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2033	09_total_transformation_sector$09_06_gas_processing_plants$x$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2034	09_total_transformation_sector$09_07_oil_refineries$x$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2042	09_total_transformation_sector$09_12_nonspecified_transformation$x$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2043	09_total_transformation_sector$x$x$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2148	09_total_transformation_sector$09_01_electricity_plants$x$x	06_crude_oil_and_ngl$06_x_other_hydrocarbons
# 2150	09_total_transformation_sector$09_06_gas_processing_plants$x$x	06_crude_oil_and_ngl$06_x_other_hydrocarbons
# 2152	09_total_transformation_sector$09_07_oil_refineries$x$x	06_crude_oil_and_ngl$06_x_other_hydrocarbons
# 2168	09_total_transformation_sector$09_12_nonspecified_transformation$x$x	06_crude_oil_and_ngl$06_x_other_hydrocarbons
# 2170	09_total_transformation_sector$x$x$x	06_crude_oil_and_ngl$06_x_other_hydrocarbons
# 2348	09_total_transformation_sector$09_09_petrochemical_industry$x$x	06_crude_oil_and_ngl$06_x_other_hydrocarbons
# 2350	09_total_transformation_sector$09_06_gas_processing_plants$09_06_04_gastoliquids_plants$x	06_crude_oil_and_ngl$06_x_other_hydrocarbons
# 2385	09_total_transformation_sector$09_01_electricity_plants$x$x	06_crude_oil_and_ngl$x
# 2390	09_total_transformation_sector$09_02_chp_plants$x$x	06_crude_oil_and_ngl$x
# 2391	09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x	06_crude_oil_and_ngl$x
# 2392	09_total_transformation_sector$09_06_gas_processing_plants$x$x	06_crude_oil_and_ngl$x
# 2393	09_total_transformation_sector$09_07_oil_refineries$x$x	06_crude_oil_and_ngl$x
# 2401	09_total_transformation_sector$09_12_nonspecified_transformation$x$x	06_crude_oil_and_ngl$x
# 2406	09_total_transformation_sector$09_x_heat_plants$x$x	06_crude_oil_and_ngl$x
# 2407	09_total_transformation_sector$x$x$x	06_crude_oil_and_ngl$x
# 2508	09_total_transformation_sector$09_09_petrochemical_industry$x$x	06_crude_oil_and_ngl$x
# 2509	09_total_transformation_sector$09_06_gas_processing_plants$09_06_04_gastoliquids_plants$x	06_crude_oil_and_ngl$x
# 2518	09_total_transformation_sector$09_01_electricity_plants$x$x	07_petroleum_products$07_01_motor_gasoline
# 2519	09_total_transformation_sector$09_06_gas_processing_plants$x$x	07_petroleum_products$07_01_motor_gasoline
# 2520	09_total_transformation_sector$09_07_oil_refineries$x$x	07_petroleum_products$07_01_motor_gasoline
# 2528	09_total_transformation_sector$09_x_heat_plants$x$x	07_petroleum_products$07_01_motor_gasoline
# 2529	09_total_transformation_sector$x$x$x	07_petroleum_products$07_01_motor_gasoline
# 2654	09_total_transformation_sector$09_06_gas_processing_plants$09_06_02_liquefaction_regasification_plants$x	07_petroleum_products$07_01_motor_gasoline
# 2664	09_total_transformation_sector$09_07_oil_refineries$x$x	07_petroleum_products$07_02_aviation_gasoline
# 2672	09_total_transformation_sector$x$x$x	07_petroleum_products$07_02_aviation_gasoline
# 2797	09_total_transformation_sector$09_01_electricity_plants$x$x	07_petroleum_products$07_03_naphtha
# 2798	09_total_transformation_sector$09_02_chp_plants$x$x	07_petroleum_products$07_03_naphtha
# 2799	09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x	07_petroleum_products$07_03_naphtha
# 2800	09_total_transformation_sector$09_06_gas_processing_plants$x$x	07_petroleum_products$07_03_naphtha
# 2801	09_total_transformation_sector$09_07_oil_refineries$x$x	07_petroleum_products$07_03_naphtha
# 2809	09_total_transformation_sector$09_x_heat_plants$x$x	07_petroleum_products$07_03_naphtha
# 2810	09_total_transformation_sector$x$x$x	07_petroleum_products$07_03_naphtha
# 2905	09_total_transformation_sector$09_06_gas_processing_plants$09_06_02_liquefaction_regasification_plants$x	07_petroleum_products$07_03_naphtha
# 2906	09_total_transformation_sector$09_09_petrochemical_industry$x$x	07_petroleum_products$07_03_naphtha
# 2907	09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x	07_petroleum_products$07_03_naphtha
# 2924	09_total_transformation_sector$09_01_electricity_plants$x$x	07_petroleum_products$07_06_kerosene
# 2926	09_total_transformation_sector$09_02_chp_plants$x$x	07_petroleum_products$07_06_kerosene
# 2928	09_total_transformation_sector$09_06_gas_processing_plants$x$x	07_petroleum_products$07_06_kerosene
# 2930	09_total_transformation_sector$09_07_oil_refineries$x$x	07_petroleum_products$07_06_kerosene
# 2946	09_total_transformation_sector$09_x_heat_plants$x$x	07_petroleum_products$07_06_kerosene
# 2948	09_total_transformation_sector$x$x$x	07_petroleum_products$07_06_kerosene
# 3198	09_total_transformation_sector$09_09_petrochemical_industry$x$x	07_petroleum_products$07_06_kerosene
# 3200	09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x	07_petroleum_products$07_06_kerosene
# 3202	09_total_transformation_sector$09_06_gas_processing_plants$09_06_04_gastoliquids_plants$x	07_petroleum_products$07_06_kerosene
# 3276	09_total_transformation_sector$09_01_electricity_plants$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3286	09_total_transformation_sector$09_02_chp_plants$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3288	09_total_transformation_sector$09_06_gas_processing_plants$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3290	09_total_transformation_sector$09_07_oil_refineries$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3292	09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x	07_petroleum_products$07_07_gas_diesel_oil
# 3302	09_total_transformation_sector$09_08_coal_transformation$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3314	09_total_transformation_sector$09_x_heat_plants$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3316	09_total_transformation_sector$x$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3568	09_total_transformation_sector$09_09_petrochemical_industry$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3570	09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x	07_petroleum_products$07_07_gas_diesel_oil
# 3572	09_total_transformation_sector$09_06_gas_processing_plants$09_06_04_gastoliquids_plants$x	07_petroleum_products$07_07_gas_diesel_oil
# 3611	09_total_transformation_sector$09_01_electricity_plants$x$x	07_petroleum_products$07_08_fuel_oil
# 3616	09_total_transformation_sector$09_02_chp_plants$x$x	07_petroleum_products$07_08_fuel_oil
# 3617	09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x	07_petroleum_products$07_08_fuel_oil
# 3618	09_total_transformation_sector$09_06_gas_processing_plants$x$x	07_petroleum_products$07_08_fuel_oil
# 3619	09_total_transformation_sector$09_07_oil_refineries$x$x	07_petroleum_products$07_08_fuel_oil
# 3620	09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x	07_petroleum_products$07_08_fuel_oil
# 3621	09_total_transformation_sector$09_08_coal_transformation$09_08_02_blast_furnaces$x	07_petroleum_products$07_08_fuel_oil
# 3625	09_total_transformation_sector$09_08_coal_transformation$x$x	07_petroleum_products$07_08_fuel_oil
# 3627	09_total_transformation_sector$09_12_nonspecified_transformation$x$x	07_petroleum_products$07_08_fuel_oil
# 3632	09_total_transformation_sector$09_x_heat_plants$x$x	07_petroleum_products$07_08_fuel_oil
# 3633	09_total_transformation_sector$x$x$x	07_petroleum_products$07_08_fuel_oil
# 3759	09_total_transformation_sector$09_09_petrochemical_industry$x$x	07_petroleum_products$07_08_fuel_oil
# 3769	09_total_transformation_sector$09_01_electricity_plants$x$x	07_petroleum_products$07_09_lpg
# 3770	09_total_transformation_sector$09_02_chp_plants$x$x	07_petroleum_products$07_09_lpg
# 3771	09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x	07_petroleum_products$07_09_lpg
# 3772	09_total_transformation_sector$09_06_gas_processing_plants$x$x	07_petroleum_products$07_09_lpg
# 3773	09_total_transformation_sector$09_07_oil_refineries$x$x	07_petroleum_products$07_09_lpg
# 3781	09_total_transformation_sector$09_12_nonspecified_transformation$x$x	07_petroleum_products$07_09_lpg
# 3782	09_total_transformation_sector$09_x_heat_plants$x$x	07_petroleum_products$07_09_lpg
# 3783	09_total_transformation_sector$x$x$x	07_petroleum_products$07_09_lpg
# 3909	09_total_transformation_sector$09_06_gas_processing_plants$09_06_02_liquefaction_regasification_plants$x	07_petroleum_products$07_09_lpg
# 3910	09_total_transformation_sector$09_09_petrochemical_industry$x$x	07_petroleum_products$07_09_lpg
# 3911	09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x	07_petroleum_products$07_09_lpg
# 3921	09_total_transformation_sector$09_01_electricity_plants$x$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3922	09_total_transformation_sector$09_02_chp_plants$x$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3923	09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3924	09_total_transformation_sector$09_06_gas_processing_plants$x$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3925	09_total_transformation_sector$09_07_oil_refineries$x$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3933	09_total_transformation_sector$09_x_heat_plants$x$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3934	09_total_transformation_sector$x$x$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 4029	09_total_transformation_sector$09_09_petrochemical_industry$x$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 4030	09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 4031	09_total_transformation_sector$09_06_gas_processing_plants$09_06_04_gastoliquids_plants$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 4040	09_total_transformation_sector$09_07_oil_refineries$x$x	07_petroleum_products$07_11_ethane
# 4048	09_total_transformation_sector$09_12_nonspecified_transformation$x$x	07_petroleum_products$07_11_ethane
# 4049	09_total_transformation_sector$x$x$x	07_petroleum_products$07_11_ethane
# 4149	09_total_transformation_sector$09_01_electricity_plants$x$x	07_petroleum_products$07_x_jet_fuel
# 4150	09_total_transformation_sector$09_02_chp_plants$x$x	07_petroleum_products$07_x_jet_fuel
# 4151	09_total_transformation_sector$09_07_oil_refineries$x$x	07_petroleum_products$07_x_jet_fuel
# 4159	09_total_transformation_sector$x$x$x	07_petroleum_products$07_x_jet_fuel
# 4455	09_total_transformation_sector$09_01_electricity_plants$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4480	09_total_transformation_sector$09_02_chp_plants$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4485	09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x	07_petroleum_products$07_x_other_petroleum_products
# 4490	09_total_transformation_sector$09_06_gas_processing_plants$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4495	09_total_transformation_sector$09_07_oil_refineries$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4500	09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x	07_petroleum_products$07_x_other_petroleum_products
# 4525	09_total_transformation_sector$09_08_coal_transformation$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4555	09_total_transformation_sector$09_x_heat_plants$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4560	09_total_transformation_sector$x$x$x	07_petroleum_products$07_x_other_petroleum_products
# 5185	09_total_transformation_sector$09_06_gas_processing_plants$09_06_02_liquefaction_regasification_plants$x	07_petroleum_products$07_x_other_petroleum_products
# 5190	09_total_transformation_sector$09_09_petrochemical_industry$x$x	07_petroleum_products$07_x_other_petroleum_products
# 5195	09_total_transformation_sector$09_06_gas_processing_plants$09_06_04_gastoliquids_plants$x	07_petroleum_products$07_x_other_petroleum_products
# 5235	09_total_transformation_sector$09_01_electricity_plants$x$x	07_petroleum_products$x
# 5240	09_total_transformation_sector$09_02_chp_plants$x$x	07_petroleum_products$x
# 5241	09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x	07_petroleum_products$x
# 5242	09_total_transformation_sector$09_06_gas_processing_plants$x$x	07_petroleum_products$x
# 5243	09_total_transformation_sector$09_07_oil_refineries$x$x	07_petroleum_products$x
# 5244	09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x	07_petroleum_products$x
# 5245	09_total_transformation_sector$09_08_coal_transformation$09_08_02_blast_furnaces$x	07_petroleum_products$x
# 5249	09_total_transformation_sector$09_08_coal_transformation$x$x	07_petroleum_products$x
# 5251	09_total_transformation_sector$09_12_nonspecified_transformation$x$x	07_petroleum_products$x
# 5256	09_total_transformation_sector$09_x_heat_plants$x$x	07_petroleum_products$x
# 5257	09_total_transformation_sector$x$x$x	07_petroleum_products$x
# 5383	09_total_transformation_sector$09_06_gas_processing_plants$09_06_02_liquefaction_regasification_plants$x	07_petroleum_products$x
# 5384	09_total_transformation_sector$09_09_petrochemical_industry$x$x	07_petroleum_products$x
# 5385	09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x	07_petroleum_products$x
# 5386	09_total_transformation_sector$09_06_gas_processing_plants$09_06_04_gastoliquids_plants$x	07_petroleum_products$x
# 5420	09_total_transformation_sector$09_01_electricity_plants$x$x	08_gas$08_01_natural_gas
# 5425	09_total_transformation_sector$09_02_chp_plants$x$x	08_gas$08_01_natural_gas
# 5426	09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x	08_gas$08_01_natural_gas
# 5427	09_total_transformation_sector$09_06_gas_processing_plants$x$x	08_gas$08_01_natural_gas
# 5428	09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x	08_gas$08_01_natural_gas
# 5429	09_total_transformation_sector$09_08_coal_transformation$09_08_02_blast_furnaces$x	08_gas$08_01_natural_gas
# 5433	09_total_transformation_sector$09_08_coal_transformation$x$x	08_gas$08_01_natural_gas
# 5435	09_total_transformation_sector$09_12_nonspecified_transformation$x$x	08_gas$08_01_natural_gas
# 5440	09_total_transformation_sector$09_x_heat_plants$x$x	08_gas$08_01_natural_gas
# 5441	09_total_transformation_sector$x$x$x	08_gas$08_01_natural_gas
# 5565	09_total_transformation_sector$09_06_gas_processing_plants$09_06_02_liquefaction_regasification_plants$x	08_gas$08_01_natural_gas
# 5566	09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x	08_gas$08_01_natural_gas
# 5567	09_total_transformation_sector$09_06_gas_processing_plants$09_06_04_gastoliquids_plants$x	08_gas$08_01_natural_gas
# 5574	09_total_transformation_sector$09_06_gas_processing_plants$x$x	08_gas$08_02_lng
# 5582	09_total_transformation_sector$x$x$x	08_gas$08_02_lng
# 5672	09_total_transformation_sector$09_06_gas_processing_plants$09_06_02_liquefaction_regasification_plants$x	08_gas$08_02_lng
# 5678	09_total_transformation_sector$09_01_electricity_plants$x$x	08_gas$08_03_gas_works_gas
# 5679	09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x	08_gas$08_03_gas_works_gas
# 5680	09_total_transformation_sector$09_06_gas_processing_plants$x$x	08_gas$08_03_gas_works_gas
# 5688	09_total_transformation_sector$09_x_heat_plants$x$x	08_gas$08_03_gas_works_gas
# 5689	09_total_transformation_sector$x$x$x	08_gas$08_03_gas_works_gas
# 5784	09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x	08_gas$08_03_gas_works_gas
# 5817	09_total_transformation_sector$09_01_electricity_plants$x$x	08_gas$x
# 5822	09_total_transformation_sector$09_02_chp_plants$x$x	08_gas$x
# 5823	09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x	08_gas$x
# 5824	09_total_transformation_sector$09_06_gas_processing_plants$x$x	08_gas$x
# 5825	09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x	08_gas$x
# 5826	09_total_transformation_sector$09_08_coal_transformation$09_08_02_blast_furnaces$x	08_gas$x
# 5830	09_total_transformation_sector$09_08_coal_transformation$x$x	08_gas$x
# 5832	09_total_transformation_sector$09_12_nonspecified_transformation$x$x	08_gas$x
# 5844	09_total_transformation_sector$09_x_heat_plants$x$x	08_gas$x
# 5845	09_total_transformation_sector$x$x$x	08_gas$x
# 5969	09_total_transformation_sector$09_06_gas_processing_plants$09_06_02_liquefaction_regasification_plants$x	08_gas$x
# 5970	09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x	08_gas$x
# 5971	09_total_transformation_sector$09_06_gas_processing_plants$09_06_04_gastoliquids_plants$x	08_gas$x
# 7073	09_total_transformation_sector$09_01_electricity_plants$x$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7074	09_total_transformation_sector$09_02_chp_plants$x$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7082	09_total_transformation_sector$x$x$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7176	09_total_transformation_sector$09_11_charcoal_processing$x$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7182	09_total_transformation_sector$09_01_electricity_plants$x$x	15_solid_biomass$15_02_bagasse
# 7183	09_total_transformation_sector$09_02_chp_plants$x$x	15_solid_biomass$15_02_bagasse
# 7191	09_total_transformation_sector$x$x$x	15_solid_biomass$15_02_bagasse
# 7297	09_total_transformation_sector$x$x$x	15_solid_biomass$15_03_charcoal
# 7391	09_total_transformation_sector$09_11_charcoal_processing$x$x	15_solid_biomass$15_03_charcoal
# 7397	09_total_transformation_sector$09_01_electricity_plants$x$x	15_solid_biomass$15_04_black_liquor
# 7398	09_total_transformation_sector$09_02_chp_plants$x$x	15_solid_biomass$15_04_black_liquor
# 7406	09_total_transformation_sector$x$x$x	15_solid_biomass$15_04_black_liquor
# 7501	09_total_transformation_sector$09_01_electricity_plants$x$x	15_solid_biomass$15_05_other_biomass
# 7502	09_total_transformation_sector$09_02_chp_plants$x$x	15_solid_biomass$15_05_other_biomass
# 7510	09_total_transformation_sector$09_12_nonspecified_transformation$x$x	15_solid_biomass$15_05_other_biomass
# 7511	09_total_transformation_sector$09_x_heat_plants$x$x	15_solid_biomass$15_05_other_biomass
# 7512	09_total_transformation_sector$x$x$x	15_solid_biomass$15_05_other_biomass
# 7609	09_total_transformation_sector$09_11_charcoal_processing$x$x	15_solid_biomass$15_05_other_biomass
# 7642	09_total_transformation_sector$09_01_electricity_plants$x$x	15_solid_biomass$x
# 7647	09_total_transformation_sector$09_02_chp_plants$x$x	15_solid_biomass$x
# 7655	09_total_transformation_sector$09_12_nonspecified_transformation$x$x	15_solid_biomass$x
# 7667	09_total_transformation_sector$09_x_heat_plants$x$x	15_solid_biomass$x
# 7668	09_total_transformation_sector$x$x$x	15_solid_biomass$x
# 7765	09_total_transformation_sector$09_11_charcoal_processing$x$x	15_solid_biomass$x
# 7787	09_total_transformation_sector$09_01_electricity_plants$x$x	16_others$16_01_biogas
# 7790	09_total_transformation_sector$09_02_chp_plants$x$x	16_others$16_01_biogas
# 7793	09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x	16_others$16_01_biogas
# 7796	09_total_transformation_sector$09_06_gas_processing_plants$x$x	16_others$16_01_biogas
# 7820	09_total_transformation_sector$09_12_nonspecified_transformation$x$x	16_others$16_01_biogas
# 7823	09_total_transformation_sector$09_x_heat_plants$x$x	16_others$16_01_biogas
# 7826	09_total_transformation_sector$x$x$x	16_others$16_01_biogas
# 8183	09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x	16_others$16_01_biogas
# 8193	09_total_transformation_sector$09_01_electricity_plants$x$x	16_others$16_02_industrial_waste
# 8194	09_total_transformation_sector$09_02_chp_plants$x$x	16_others$16_02_industrial_waste
# 8195	09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x	16_others$16_02_industrial_waste
# 8200	09_total_transformation_sector$09_08_coal_transformation$x$x	16_others$16_02_industrial_waste
# 8202	09_total_transformation_sector$09_12_nonspecified_transformation$x$x	16_others$16_02_industrial_waste
# 8203	09_total_transformation_sector$09_x_heat_plants$x$x	16_others$16_02_industrial_waste
# 8204	09_total_transformation_sector$x$x$x	16_others$16_02_industrial_waste
# 8307	09_total_transformation_sector$09_01_electricity_plants$x$x	16_others$16_03_municipal_solid_waste_renewable
# 8308	09_total_transformation_sector$09_02_chp_plants$x$x	16_others$16_03_municipal_solid_waste_renewable
# 8316	09_total_transformation_sector$09_x_heat_plants$x$x	16_others$16_03_municipal_solid_waste_renewable
# 8317	09_total_transformation_sector$x$x$x	16_others$16_03_municipal_solid_waste_renewable
# 8418	09_total_transformation_sector$09_01_electricity_plants$x$x	16_others$16_04_municipal_solid_waste_nonrenewable
# 8419	09_total_transformation_sector$09_02_chp_plants$x$x	16_others$16_04_municipal_solid_waste_nonrenewable
# 8427	09_total_transformation_sector$09_x_heat_plants$x$x	16_others$16_04_municipal_solid_waste_nonrenewable
# 8428	09_total_transformation_sector$x$x$x	16_others$16_04_municipal_solid_waste_nonrenewable
# 8661	09_total_transformation_sector$09_01_electricity_plants$x$x	16_others$16_06_biodiesel
# 8662	09_total_transformation_sector$09_02_chp_plants$x$x	16_others$16_06_biodiesel
# 8670	09_total_transformation_sector$x$x$x	16_others$16_06_biodiesel
# 9051	09_total_transformation_sector$09_01_electricity_plants$x$x	16_others$16_08_other_liquid_biofuels
# 9052	09_total_transformation_sector$09_02_chp_plants$x$x	16_others$16_08_other_liquid_biofuels
# 9060	09_total_transformation_sector$x$x$x	16_others$16_08_other_liquid_biofuels





#%%

# OTHER:

#Please map the following aperc sector, fuel combinations to one of the following IPCC 2006 Source/Sink Category, Fuel 2006 combinations and put it in a python dict. ignore the row numbers.


# 	IPCC 2006 Source/Sink Category	Fuel 2006
# 1855	1.A.1 - Energy Industries	Crude Oil
# 1856	1.A.1 - Energy Industries	Orimulsion
# 1857	1.A.1 - Energy Industries	Natural Gas Liquids (NGLs)
# 1858	1.A.1 - Energy Industries	Motor Gasoline
# 1859	1.A.1 - Energy Industries	Aviation Gasoline
# 1860	1.A.1 - Energy Industries	Jet Gasoline
# 1861	1.A.1 - Energy Industries	Jet Kerosene
# 1862	1.A.1 - Energy Industries	Other Kerosene
# 1863	1.A.1 - Energy Industries	Shale Oil
# 1864	1.A.1 - Energy Industries	Gas Oil
# 1865	1.A.1 - Energy Industries	Diesel Oil
# 1866	1.A.1 - Energy Industries	Residual Fuel Oil
# 1867	1.A.1 - Energy Industries	Liquefied Petroleum Gases
# 1868	1.A.1 - Energy Industries	Ethane
# 1869	1.A.1 - Energy Industries	Naphtha
# 1870	1.A.1 - Energy Industries	Bitumen
# 1871	1.A.1 - Energy Industries	Lubricants
# 1872	1.A.1 - Energy Industries	Petroleum Coke
# 1873	1.A.1 - Energy Industries	Refinery Feedstocks
# 1874	1.A.1 - Energy Industries	Refinery Gas
# 1875	1.A.1 - Energy Industries	Waxes
# 1876	1.A.1 - Energy Industries	White Spirit & SBP
# 1877	1.A.1 - Energy Industries	Other Petroleum Products
# 1878	1.A.1 - Energy Industries	Anthracite
# 1879	1.A.1 - Energy Industries	Coking Coal
# 1880	1.A.1 - Energy Industries	Other Bituminous Coal
# 1881	1.A.1 - Energy Industries	Sub-Bituminous Coal
# 1882	1.A.1 - Energy Industries	Lignite
# 1883	1.A.1 - Energy Industries	Oil Shale and Tar Sands
# 1884	1.A.1 - Energy Industries	Brown Coal Briquettes
# 1885	1.A.1 - Energy Industries	Patent Fuel
# 1886	1.A.1 - Energy Industries	Coke Oven Coke and Lignite Coke
# 1887	1.A.1 - Energy Industries	Gas Coke
# 1888	1.A.1 - Energy Industries	Coal Tar
# 1889	1.A.1 - Energy Industries	Gas Works Gas
# 1890	1.A.1 - Energy Industries	Coke Oven Gas
# 1891	1.A.1 - Energy Industries	Blast Furnace Gas
# 1892	1.A.1 - Energy Industries	Oxygen Steel Furnace Gas
# 1893	1.A.1 - Energy Industries	Natural Gas
# 1894	1.A.1 - Energy Industries	Municipal Wastes (non-biomass fraction)
# 1895	1.A.1 - Energy Industries	Industrial Wastes
# 1896	1.A.1 - Energy Industries	Waste Oils
# 1897	1.A.1 - Energy Industries	Peat
# 1898	1.A.1 - Energy Industries	Wood/Wood Waste
# 1899	1.A.1 - Energy Industries	Sulphite Lyes (Black Liquor)
# 1900	1.A.1 - Energy Industries	Other Primary Solid Biomass
# 1901	1.A.1 - Energy Industries	Charcoal
# 1902	1.A.1 - Energy Industries	Biogasoline
# 1903	1.A.1 - Energy Industries	Biodiesels
# 1904	1.A.1 - Energy Industries	Other Liquid Biofuels
# 1905	1.A.1 - Energy Industries	Landfill Gas
# 1906	1.A.1 - Energy Industries	Sludge Gas
# 1907	1.A.1 - Energy Industries	Other Biogas
# 1908	1.A.1 - Energy Industries	Municipal Wastes (biomass fraction)
# 2503	1.A - Fuel Combustion Activities	Residual Fuel Oil
# 2504	1.A - Fuel Combustion Activities	Shale Oil
# 2507	1.A - Fuel Combustion Activities	Gas Oil
# 2508	1.A - Fuel Combustion Activities	Diesel Oil
# 2512	1.A - Fuel Combustion Activities	Other Bituminous Coal
# 2519	1.A - Fuel Combustion Activities	Natural Gas
# 2523	1.A - Fuel Combustion Activities	Peat
# 2525	1.A - Fuel Combustion Activities	Wood/Wood Waste
# 2542	1.A - Fuel Combustion Activities	Lignite


#APERC
# 	aperc_sector	aperc_fuel
# 17	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	01_coal$01_01_coking_coal
# 18	10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x	01_coal$01_01_coking_coal
# 20	10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x	01_coal$01_01_coking_coal
# 21	10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x	01_coal$01_01_coking_coal
# 22	10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x	01_coal$01_01_coking_coal
# 28	10_losses_and_own_use$10_01_own_use$x$x	01_coal$01_01_coking_coal
# 29	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	01_coal$01_01_coking_coal
# 30	10_losses_and_own_use$x$x$x	01_coal$01_01_coking_coal
# 32	12_total_final_consumption$x$x$x	01_coal$01_01_coking_coal
# 33	13_total_final_energy_consumption$x$x$x	01_coal$01_01_coking_coal
# 63	16_other_sector$16_01_buildings$x$x	01_coal$01_01_coking_coal
# 64	16_other_sector$16_02_agriculture_and_fishing$x$x	01_coal$01_01_coking_coal
# 65	16_other_sector$16_05_nonspecified_others$x$x	01_coal$01_01_coking_coal
# 66	16_other_sector$x$x$x	01_coal$01_01_coking_coal
# 67	17_nonenergy_use$x$x$x	01_coal$01_01_coking_coal
# 166	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	01_coal$01_05_lignite
# 167	10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x	01_coal$01_05_lignite
# 169	10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x	01_coal$01_05_lignite
# 170	10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x	01_coal$01_05_lignite
# 171	10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x	01_coal$01_05_lignite
# 174	10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x	01_coal$01_05_lignite
# 176	10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x	01_coal$01_05_lignite
# 178	10_losses_and_own_use$10_01_own_use$x$x	01_coal$01_05_lignite
# 179	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	01_coal$01_05_lignite
# 180	10_losses_and_own_use$x$x$x	01_coal$01_05_lignite
# 182	12_total_final_consumption$x$x$x	01_coal$01_05_lignite
# 183	13_total_final_energy_consumption$x$x$x	01_coal$01_05_lignite
# 212	16_other_sector$16_01_buildings$x$x	01_coal$01_05_lignite
# 215	16_other_sector$16_02_agriculture_and_fishing$x$x	01_coal$01_05_lignite
# 216	16_other_sector$16_05_nonspecified_others$x$x	01_coal$01_05_lignite
# 217	16_other_sector$x$x$x	01_coal$01_05_lignite
# 218	17_nonenergy_use$x$x$x	01_coal$01_05_lignite
# 370	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	01_coal$01_x_thermal_coal
# 372	10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x	01_coal$01_x_thermal_coal
# 376	10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x	01_coal$01_x_thermal_coal
# 378	10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x	01_coal$01_x_thermal_coal
# 380	10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x	01_coal$01_x_thermal_coal
# 382	10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x	01_coal$01_x_thermal_coal
# 386	10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x	01_coal$01_x_thermal_coal
# 388	10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x	01_coal$01_x_thermal_coal
# 390	10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x	01_coal$01_x_thermal_coal
# 394	10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x	01_coal$01_x_thermal_coal
# 398	10_losses_and_own_use$10_01_own_use$x$x	01_coal$01_x_thermal_coal
# 400	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	01_coal$01_x_thermal_coal
# 402	10_losses_and_own_use$x$x$x	01_coal$01_x_thermal_coal
# 406	12_total_final_consumption$x$x$x	01_coal$01_x_thermal_coal
# 408	13_total_final_energy_consumption$x$x$x	01_coal$01_x_thermal_coal
# 470	16_other_sector$16_01_buildings$x$x	01_coal$01_x_thermal_coal
# 476	16_other_sector$16_02_agriculture_and_fishing$x$x	01_coal$01_x_thermal_coal
# 478	16_other_sector$16_05_nonspecified_others$x$x	01_coal$01_x_thermal_coal
# 480	16_other_sector$x$x$x	01_coal$01_x_thermal_coal
# 482	17_nonenergy_use$x$x$x	01_coal$01_x_thermal_coal
# 694	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	01_coal$x
# 696	10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x	01_coal$x
# 700	10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x	01_coal$x
# 702	10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x	01_coal$x
# 704	10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x	01_coal$x
# 706	10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x	01_coal$x
# 710	10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x	01_coal$x
# 712	10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x	01_coal$x
# 714	10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x	01_coal$x
# 718	10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x	01_coal$x
# 722	10_losses_and_own_use$10_01_own_use$x$x	01_coal$x
# 724	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	01_coal$x
# 726	10_losses_and_own_use$x$x$x	01_coal$x
# 730	12_total_final_consumption$x$x$x	01_coal$x
# 732	13_total_final_energy_consumption$x$x$x	01_coal$x
# 834	16_other_sector$16_01_buildings$x$x	01_coal$x
# 840	16_other_sector$16_02_agriculture_and_fishing$x$x	01_coal$x
# 842	16_other_sector$16_05_nonspecified_others$x$x	01_coal$x
# 844	16_other_sector$x$x$x	01_coal$x
# 846	17_nonenergy_use$x$x$x	01_coal$x
# 1118	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	02_coal_products$x
# 1121	10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x	02_coal_products$x
# 1127	10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x	02_coal_products$x
# 1130	10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x	02_coal_products$x
# 1133	10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x	02_coal_products$x
# 1136	10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x	02_coal_products$x
# 1139	10_losses_and_own_use$10_01_own_use$10_01_10_blast_furnaces$x	02_coal_products$x
# 1142	10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x	02_coal_products$x
# 1148	10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x	02_coal_products$x
# 1154	10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x	02_coal_products$x
# 1160	10_losses_and_own_use$10_01_own_use$x$x	02_coal_products$x
# 1163	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	02_coal_products$x
# 1166	10_losses_and_own_use$x$x$x	02_coal_products$x
# 1172	12_total_final_consumption$x$x$x	02_coal_products$x
# 1175	13_total_final_energy_consumption$x$x$x	02_coal_products$x
# 1265	16_other_sector$16_01_buildings$x$x	02_coal_products$x
# 1274	16_other_sector$16_02_agriculture_and_fishing$x$x	02_coal_products$x
# 1277	16_other_sector$16_05_nonspecified_others$x$x	02_coal_products$x
# 1280	16_other_sector$x$x$x	02_coal_products$x
# 1283	17_nonenergy_use$x$x$x	02_coal_products$x
# 1475	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	03_peat$x
# 1477	10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x	03_peat$x
# 1484	10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x	03_peat$x
# 1486	10_losses_and_own_use$10_01_own_use$x$x	03_peat$x
# 1487	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	03_peat$x
# 1488	10_losses_and_own_use$x$x$x	03_peat$x
# 1490	12_total_final_consumption$x$x$x	03_peat$x
# 1491	13_total_final_energy_consumption$x$x$x	03_peat$x
# 1518	16_other_sector$16_01_buildings$x$x	03_peat$x
# 1521	16_other_sector$16_02_agriculture_and_fishing$x$x	03_peat$x
# 1522	16_other_sector$16_05_nonspecified_others$x$x	03_peat$x
# 1523	16_other_sector$x$x$x	03_peat$x
# 1621	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	04_peat_products$x
# 1630	10_losses_and_own_use$10_01_own_use$x$x	04_peat_products$x
# 1632	10_losses_and_own_use$x$x$x	04_peat_products$x
# 1634	12_total_final_consumption$x$x$x	04_peat_products$x
# 1635	13_total_final_energy_consumption$x$x$x	04_peat_products$x
# 1662	16_other_sector$16_01_buildings$x$x	04_peat_products$x
# 1665	16_other_sector$16_02_agriculture_and_fishing$x$x	04_peat_products$x
# 1666	16_other_sector$16_05_nonspecified_others$x$x	04_peat_products$x
# 1667	16_other_sector$x$x$x	04_peat_products$x
# 1668	17_nonenergy_use$x$x$x	04_peat_products$x
# 1928	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1929	10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1932	10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1934	10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1935	10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1936	10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1938	10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1940	10_losses_and_own_use$10_01_own_use$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1941	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1942	10_losses_and_own_use$x$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1944	12_total_final_consumption$x$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1945	13_total_final_energy_consumption$x$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1973	16_other_sector$16_01_buildings$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1976	16_other_sector$16_02_agriculture_and_fishing$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1977	16_other_sector$16_05_nonspecified_others$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1978	16_other_sector$x$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 1979	17_nonenergy_use$x$x$x	06_crude_oil_and_ngl$06_01_crude_oil
# 2046	10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2049	10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2050	10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2051	10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2054	10_losses_and_own_use$10_01_own_use$x$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2056	10_losses_and_own_use$x$x$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2058	12_total_final_consumption$x$x$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2059	13_total_final_energy_consumption$x$x$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2086	16_other_sector$16_01_buildings$x$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2087	16_other_sector$16_02_agriculture_and_fishing$x$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2088	16_other_sector$x$x$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2089	17_nonenergy_use$x$x$x	06_crude_oil_and_ngl$06_02_natural_gas_liquids
# 2198	12_total_final_consumption$x$x$x	06_crude_oil_and_ngl$06_x_other_hydrocarbons
# 2252	17_nonenergy_use$x$x$x	06_crude_oil_and_ngl$06_x_other_hydrocarbons
# 2408	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	06_crude_oil_and_ngl$x
# 2409	10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x	06_crude_oil_and_ngl$x
# 2411	10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x	06_crude_oil_and_ngl$x
# 2412	10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x	06_crude_oil_and_ngl$x
# 2414	10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x	06_crude_oil_and_ngl$x
# 2415	10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x	06_crude_oil_and_ngl$x
# 2416	10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x	06_crude_oil_and_ngl$x
# 2418	10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x	06_crude_oil_and_ngl$x
# 2420	10_losses_and_own_use$10_01_own_use$x$x	06_crude_oil_and_ngl$x
# 2421	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	06_crude_oil_and_ngl$x
# 2422	10_losses_and_own_use$x$x$x	06_crude_oil_and_ngl$x
# 2424	12_total_final_consumption$x$x$x	06_crude_oil_and_ngl$x
# 2425	13_total_final_energy_consumption$x$x$x	06_crude_oil_and_ngl$x
# 2454	16_other_sector$16_01_buildings$x$x	06_crude_oil_and_ngl$x
# 2457	16_other_sector$16_02_agriculture_and_fishing$x$x	06_crude_oil_and_ngl$x
# 2458	16_other_sector$16_05_nonspecified_others$x$x	06_crude_oil_and_ngl$x
# 2459	16_other_sector$x$x$x	06_crude_oil_and_ngl$x
# 2460	17_nonenergy_use$x$x$x	06_crude_oil_and_ngl$x
# 2513	04_international_marine_bunkers$x$x$x	07_petroleum_products$07_01_motor_gasoline
# 2514	05_international_aviation_bunkers$x$x$x	07_petroleum_products$07_01_motor_gasoline
# 2530	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	07_petroleum_products$07_01_motor_gasoline
# 2531	10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x	07_petroleum_products$07_01_motor_gasoline
# 2533	10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x	07_petroleum_products$07_01_motor_gasoline
# 2534	10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x	07_petroleum_products$07_01_motor_gasoline
# 2535	10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x	07_petroleum_products$07_01_motor_gasoline
# 2537	10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x	07_petroleum_products$07_01_motor_gasoline
# 2538	10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x	07_petroleum_products$07_01_motor_gasoline
# 2539	10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x	07_petroleum_products$07_01_motor_gasoline
# 2540	10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x	07_petroleum_products$07_01_motor_gasoline
# 2542	10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x	07_petroleum_products$07_01_motor_gasoline
# 2544	10_losses_and_own_use$10_01_own_use$x$x	07_petroleum_products$07_01_motor_gasoline
# 2545	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	07_petroleum_products$07_01_motor_gasoline
# 2546	10_losses_and_own_use$x$x$x	07_petroleum_products$07_01_motor_gasoline
# 2548	12_total_final_consumption$x$x$x	07_petroleum_products$07_01_motor_gasoline
# 2549	13_total_final_energy_consumption$x$x$x	07_petroleum_products$07_01_motor_gasoline
# 2600	16_other_sector$16_01_buildings$x$x	07_petroleum_products$07_01_motor_gasoline
# 2603	16_other_sector$16_02_agriculture_and_fishing$x$x	07_petroleum_products$07_01_motor_gasoline
# 2604	16_other_sector$16_05_nonspecified_others$x$x	07_petroleum_products$07_01_motor_gasoline
# 2605	16_other_sector$x$x$x	07_petroleum_products$07_01_motor_gasoline
# 2606	17_nonenergy_use$x$x$x	07_petroleum_products$07_01_motor_gasoline
# 2655	10_losses_and_own_use$10_01_own_use$10_01_05_natural_gas_blending_plants$x	07_petroleum_products$07_01_motor_gasoline
# 2660	05_international_aviation_bunkers$x$x$x	07_petroleum_products$07_02_aviation_gasoline
# 2678	10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x	07_petroleum_products$07_02_aviation_gasoline
# 2683	10_losses_and_own_use$10_01_own_use$x$x	07_petroleum_products$07_02_aviation_gasoline
# 2685	10_losses_and_own_use$x$x$x	07_petroleum_products$07_02_aviation_gasoline
# 2687	12_total_final_consumption$x$x$x	07_petroleum_products$07_02_aviation_gasoline
# 2688	13_total_final_energy_consumption$x$x$x	07_petroleum_products$07_02_aviation_gasoline
# 2739	16_other_sector$16_01_buildings$x$x	07_petroleum_products$07_02_aviation_gasoline
# 2740	16_other_sector$16_05_nonspecified_others$x$x	07_petroleum_products$07_02_aviation_gasoline
# 2741	16_other_sector$x$x$x	07_petroleum_products$07_02_aviation_gasoline
# 2814	10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x	07_petroleum_products$07_03_naphtha
# 2816	10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x	07_petroleum_products$07_03_naphtha
# 2817	10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x	07_petroleum_products$07_03_naphtha
# 2818	10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x	07_petroleum_products$07_03_naphtha
# 2822	10_losses_and_own_use$10_01_own_use$x$x	07_petroleum_products$07_03_naphtha
# 2823	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	07_petroleum_products$07_03_naphtha
# 2824	10_losses_and_own_use$x$x$x	07_petroleum_products$07_03_naphtha
# 2826	12_total_final_consumption$x$x$x	07_petroleum_products$07_03_naphtha
# 2827	13_total_final_energy_consumption$x$x$x	07_petroleum_products$07_03_naphtha
# 2854	16_other_sector$16_01_buildings$x$x	07_petroleum_products$07_03_naphtha
# 2855	16_other_sector$16_05_nonspecified_others$x$x	07_petroleum_products$07_03_naphtha
# 2856	16_other_sector$x$x$x	07_petroleum_products$07_03_naphtha
# 2857	17_nonenergy_use$x$x$x	07_petroleum_products$07_03_naphtha
# 2914	04_international_marine_bunkers$x$x$x	07_petroleum_products$07_06_kerosene
# 2950	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	07_petroleum_products$07_06_kerosene
# 2952	10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x	07_petroleum_products$07_06_kerosene
# 2956	10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x	07_petroleum_products$07_06_kerosene
# 2958	10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x	07_petroleum_products$07_06_kerosene
# 2960	10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x	07_petroleum_products$07_06_kerosene
# 2962	10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x	07_petroleum_products$07_06_kerosene
# 2966	10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x	07_petroleum_products$07_06_kerosene
# 2968	10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x	07_petroleum_products$07_06_kerosene
# 2970	10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x	07_petroleum_products$07_06_kerosene
# 2972	10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x	07_petroleum_products$07_06_kerosene
# 2976	10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x	07_petroleum_products$07_06_kerosene
# 2980	10_losses_and_own_use$10_01_own_use$x$x	07_petroleum_products$07_06_kerosene
# 2982	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	07_petroleum_products$07_06_kerosene
# 2984	10_losses_and_own_use$x$x$x	07_petroleum_products$07_06_kerosene
# 2988	12_total_final_consumption$x$x$x	07_petroleum_products$07_06_kerosene
# 2990	13_total_final_energy_consumption$x$x$x	07_petroleum_products$07_06_kerosene
# 3092	16_other_sector$16_01_buildings$x$x	07_petroleum_products$07_06_kerosene
# 3098	16_other_sector$16_02_agriculture_and_fishing$x$x	07_petroleum_products$07_06_kerosene
# 3100	16_other_sector$16_05_nonspecified_others$x$x	07_petroleum_products$07_06_kerosene
# 3102	16_other_sector$x$x$x	07_petroleum_products$07_06_kerosene
# 3104	17_nonenergy_use$x$x$x	07_petroleum_products$07_06_kerosene
# 3204	10_losses_and_own_use$10_01_own_use$10_01_05_natural_gas_blending_plants$x	07_petroleum_products$07_06_kerosene
# 3212	04_international_marine_bunkers$x$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3214	05_international_aviation_bunkers$x$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3318	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	07_petroleum_products$07_07_gas_diesel_oil
# 3320	10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x	07_petroleum_products$07_07_gas_diesel_oil
# 3324	10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x	07_petroleum_products$07_07_gas_diesel_oil
# 3326	10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x	07_petroleum_products$07_07_gas_diesel_oil
# 3328	10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x	07_petroleum_products$07_07_gas_diesel_oil
# 3330	10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x	07_petroleum_products$07_07_gas_diesel_oil
# 3334	10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x	07_petroleum_products$07_07_gas_diesel_oil
# 3336	10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x	07_petroleum_products$07_07_gas_diesel_oil
# 3340	10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x	07_petroleum_products$07_07_gas_diesel_oil
# 3344	10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x	07_petroleum_products$07_07_gas_diesel_oil
# 3348	10_losses_and_own_use$10_01_own_use$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3350	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3352	10_losses_and_own_use$x$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3356	12_total_final_consumption$x$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3358	13_total_final_energy_consumption$x$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3460	16_other_sector$16_01_buildings$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3466	16_other_sector$16_02_agriculture_and_fishing$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3468	16_other_sector$16_05_nonspecified_others$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3470	16_other_sector$x$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3472	17_nonenergy_use$x$x$x	07_petroleum_products$07_07_gas_diesel_oil
# 3574	10_losses_and_own_use$10_01_own_use$10_01_05_natural_gas_blending_plants$x	07_petroleum_products$07_07_gas_diesel_oil
# 3579	04_international_marine_bunkers$x$x$x	07_petroleum_products$07_08_fuel_oil
# 3634	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	07_petroleum_products$07_08_fuel_oil
# 3635	10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x	07_petroleum_products$07_08_fuel_oil
# 3637	10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x	07_petroleum_products$07_08_fuel_oil
# 3638	10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x	07_petroleum_products$07_08_fuel_oil
# 3639	10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x	07_petroleum_products$07_08_fuel_oil
# 3640	10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x	07_petroleum_products$07_08_fuel_oil
# 3642	10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x	07_petroleum_products$07_08_fuel_oil
# 3643	10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x	07_petroleum_products$07_08_fuel_oil
# 3644	10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x	07_petroleum_products$07_08_fuel_oil
# 3645	10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x	07_petroleum_products$07_08_fuel_oil
# 3647	10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x	07_petroleum_products$07_08_fuel_oil
# 3649	10_losses_and_own_use$10_01_own_use$x$x	07_petroleum_products$07_08_fuel_oil
# 3650	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	07_petroleum_products$07_08_fuel_oil
# 3651	10_losses_and_own_use$x$x$x	07_petroleum_products$07_08_fuel_oil
# 3653	12_total_final_consumption$x$x$x	07_petroleum_products$07_08_fuel_oil
# 3654	13_total_final_energy_consumption$x$x$x	07_petroleum_products$07_08_fuel_oil
# 3705	16_other_sector$16_01_buildings$x$x	07_petroleum_products$07_08_fuel_oil
# 3708	16_other_sector$16_02_agriculture_and_fishing$x$x	07_petroleum_products$07_08_fuel_oil
# 3709	16_other_sector$16_05_nonspecified_others$x$x	07_petroleum_products$07_08_fuel_oil
# 3710	16_other_sector$x$x$x	07_petroleum_products$07_08_fuel_oil
# 3711	17_nonenergy_use$x$x$x	07_petroleum_products$07_08_fuel_oil
# 3760	10_losses_and_own_use$10_01_own_use$10_01_05_natural_gas_blending_plants$x	07_petroleum_products$07_08_fuel_oil
# 3784	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	07_petroleum_products$07_09_lpg
# 3785	10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x	07_petroleum_products$07_09_lpg
# 3787	10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x	07_petroleum_products$07_09_lpg
# 3788	10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x	07_petroleum_products$07_09_lpg
# 3789	10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x	07_petroleum_products$07_09_lpg
# 3790	10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x	07_petroleum_products$07_09_lpg
# 3792	10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x	07_petroleum_products$07_09_lpg
# 3793	10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x	07_petroleum_products$07_09_lpg
# 3794	10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x	07_petroleum_products$07_09_lpg
# 3795	10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x	07_petroleum_products$07_09_lpg
# 3797	10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x	07_petroleum_products$07_09_lpg
# 3799	10_losses_and_own_use$10_01_own_use$x$x	07_petroleum_products$07_09_lpg
# 3800	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	07_petroleum_products$07_09_lpg
# 3801	10_losses_and_own_use$x$x$x	07_petroleum_products$07_09_lpg
# 3803	12_total_final_consumption$x$x$x	07_petroleum_products$07_09_lpg
# 3804	13_total_final_energy_consumption$x$x$x	07_petroleum_products$07_09_lpg
# 3855	16_other_sector$16_01_buildings$x$x	07_petroleum_products$07_09_lpg
# 3858	16_other_sector$16_02_agriculture_and_fishing$x$x	07_petroleum_products$07_09_lpg
# 3859	16_other_sector$16_05_nonspecified_others$x$x	07_petroleum_products$07_09_lpg
# 3860	16_other_sector$x$x$x	07_petroleum_products$07_09_lpg
# 3861	17_nonenergy_use$x$x$x	07_petroleum_products$07_09_lpg
# 3912	10_losses_and_own_use$10_01_own_use$10_01_05_natural_gas_blending_plants$x	07_petroleum_products$07_09_lpg
# 3935	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3936	10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3939	10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3941	10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3942	10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3943	10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3944	10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3946	10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3948	10_losses_and_own_use$10_01_own_use$x$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3949	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3950	10_losses_and_own_use$x$x$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3952	12_total_final_consumption$x$x$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3953	13_total_final_energy_consumption$x$x$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3980	16_other_sector$16_01_buildings$x$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3981	16_other_sector$x$x$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 3982	17_nonenergy_use$x$x$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
# 4055	













# Other 2:
#Please map the following aperc sector, fuel combinations to one of the following IPCC 2006 Source/Sink Category, Fuel 2006 combinations and put it in a python dict. ignore the row numbers.


# 	IPCC 2006 Source/Sink Category	Fuel 2006
# 1855	1.A.1 - Energy Industries	Crude Oil
# 1856	1.A.1 - Energy Industries	Orimulsion
# 1857	1.A.1 - Energy Industries	Natural Gas Liquids (NGLs)
# 1858	1.A.1 - Energy Industries	Motor Gasoline
# 1859	1.A.1 - Energy Industries	Aviation Gasoline
# 1860	1.A.1 - Energy Industries	Jet Gasoline
# 1861	1.A.1 - Energy Industries	Jet Kerosene
# 1862	1.A.1 - Energy Industries	Other Kerosene
# 1863	1.A.1 - Energy Industries	Shale Oil
# 1864	1.A.1 - Energy Industries	Gas Oil
# 1865	1.A.1 - Energy Industries	Diesel Oil
# 1866	1.A.1 - Energy Industries	Residual Fuel Oil
# 1867	1.A.1 - Energy Industries	Liquefied Petroleum Gases
# 1868	1.A.1 - Energy Industries	Ethane
# 1869	1.A.1 - Energy Industries	Naphtha
# 1870	1.A.1 - Energy Industries	Bitumen
# 1871	1.A.1 - Energy Industries	Lubricants
# 1872	1.A.1 - Energy Industries	Petroleum Coke
# 1873	1.A.1 - Energy Industries	Refinery Feedstocks
# 1874	1.A.1 - Energy Industries	Refinery Gas
# 1875	1.A.1 - Energy Industries	Waxes
# 1876	1.A.1 - Energy Industries	White Spirit & SBP
# 1877	1.A.1 - Energy Industries	Other Petroleum Products
# 1878	1.A.1 - Energy Industries	Anthracite
# 1879	1.A.1 - Energy Industries	Coking Coal
# 1880	1.A.1 - Energy Industries	Other Bituminous Coal
# 1881	1.A.1 - Energy Industries	Sub-Bituminous Coal
# 1882	1.A.1 - Energy Industries	Lignite
# 1883	1.A.1 - Energy Industries	Oil Shale and Tar Sands
# 1884	1.A.1 - Energy Industries	Brown Coal Briquettes
# 1885	1.A.1 - Energy Industries	Patent Fuel
# 1886	1.A.1 - Energy Industries	Coke Oven Coke and Lignite Coke
# 1887	1.A.1 - Energy Industries	Gas Coke
# 1888	1.A.1 - Energy Industries	Coal Tar
# 1889	1.A.1 - Energy Industries	Gas Works Gas
# 1890	1.A.1 - Energy Industries	Coke Oven Gas
# 1891	1.A.1 - Energy Industries	Blast Furnace Gas
# 1892	1.A.1 - Energy Industries	Oxygen Steel Furnace Gas
# 1893	1.A.1 - Energy Industries	Natural Gas
# 1894	1.A.1 - Energy Industries	Municipal Wastes (non-biomass fraction)
# 1895	1.A.1 - Energy Industries	Industrial Wastes
# 1896	1.A.1 - Energy Industries	Waste Oils
# 1897	1.A.1 - Energy Industries	Peat
# 1898	1.A.1 - Energy Industries	Wood/Wood Waste
# 1899	1.A.1 - Energy Industries	Sulphite Lyes (Black Liquor)
# 1900	1.A.1 - Energy Industries	Other Primary Solid Biomass
# 1901	1.A.1 - Energy Industries	Charcoal
# 1902	1.A.1 - Energy Industries	Biogasoline
# 1903	1.A.1 - Energy Industries	Biodiesels
# 1904	1.A.1 - Energy Industries	Other Liquid Biofuels
# 1905	1.A.1 - Energy Industries	Landfill Gas
# 1906	1.A.1 - Energy Industries	Sludge Gas
# 1907	1.A.1 - Energy Industries	Other Biogas
# 1908	1.A.1 - Energy Industries	Municipal Wastes (biomass fraction)
# 2503	1.A - Fuel Combustion Activities	Residual Fuel Oil
# 2504	1.A - Fuel Combustion Activities	Shale Oil
# 2507	1.A - Fuel Combustion Activities	Gas Oil
# 2508	1.A - Fuel Combustion Activities	Diesel Oil
# 2512	1.A - Fuel Combustion Activities	Other Bituminous Coal
# 2519	1.A - Fuel Combustion Activities	Natural Gas
# 2523	1.A - Fuel Combustion Activities	Peat
# 2525	1.A - Fuel Combustion Activities	Wood/Wood Waste
# 2542	1.A - Fuel Combustion Activities	Lignite


# APERC
# 10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x	07_petroleum_products$07_11_ethane
# 4056	10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x	07_petroleum_products$07_11_ethane
# 4061	10_losses_and_own_use$10_01_own_use$x$x	07_petroleum_products$07_11_ethane
# 4063	10_losses_and_own_use$x$x$x	07_petroleum_products$07_11_ethane
# 4065	12_total_final_consumption$x$x$x	07_petroleum_products$07_11_ethane
# 4066	13_total_final_energy_consumption$x$x$x	07_petroleum_products$07_11_ethane
# 4095	17_nonenergy_use$x$x$x	07_petroleum_products$07_11_ethane
# 4144	04_international_marine_bunkers$x$x$x	07_petroleum_products$07_x_jet_fuel
# 4145	05_international_aviation_bunkers$x$x$x	07_petroleum_products$07_x_jet_fuel
# 4160	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	07_petroleum_products$07_x_jet_fuel
# 4165	10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x	07_petroleum_products$07_x_jet_fuel
# 4166	10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x	07_petroleum_products$07_x_jet_fuel
# 4167	10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x	07_petroleum_products$07_x_jet_fuel
# 4171	10_losses_and_own_use$10_01_own_use$x$x	07_petroleum_products$07_x_jet_fuel
# 4172	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	07_petroleum_products$07_x_jet_fuel
# 4173	10_losses_and_own_use$x$x$x	07_petroleum_products$07_x_jet_fuel
# 4175	12_total_final_consumption$x$x$x	07_petroleum_products$07_x_jet_fuel
# 4176	13_total_final_energy_consumption$x$x$x	07_petroleum_products$07_x_jet_fuel
# 4227	16_other_sector$16_01_buildings$x$x	07_petroleum_products$07_x_jet_fuel
# 4231	16_other_sector$16_05_nonspecified_others$x$x	07_petroleum_products$07_x_jet_fuel
# 4232	16_other_sector$x$x$x	07_petroleum_products$07_x_jet_fuel
# 4295	04_international_marine_bunkers$x$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4565	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	07_petroleum_products$07_x_other_petroleum_products
# 4570	10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x	07_petroleum_products$07_x_other_petroleum_products
# 4580	10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x	07_petroleum_products$07_x_other_petroleum_products
# 4585	10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x	07_petroleum_products$07_x_other_petroleum_products
# 4590	10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x	07_petroleum_products$07_x_other_petroleum_products
# 4600	10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x	07_petroleum_products$07_x_other_petroleum_products
# 4605	10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x	07_petroleum_products$07_x_other_petroleum_products
# 4610	10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x	07_petroleum_products$07_x_other_petroleum_products
# 4615	10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x	07_petroleum_products$07_x_other_petroleum_products
# 4625	10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x	07_petroleum_products$07_x_other_petroleum_products
# 4635	10_losses_and_own_use$10_01_own_use$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4640	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4645	10_losses_and_own_use$x$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4655	12_total_final_consumption$x$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4660	13_total_final_energy_consumption$x$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4915	16_other_sector$16_01_buildings$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4930	16_other_sector$16_02_agriculture_and_fishing$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4935	16_other_sector$16_05_nonspecified_others$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4940	16_other_sector$x$x$x	07_petroleum_products$07_x_other_petroleum_products
# 4945	17_nonenergy_use$x$x$x	07_petroleum_products$07_x_other_petroleum_products
# 5203	04_international_marine_bunkers$x$x$x	07_petroleum_products$x
# 5204	05_international_aviation_bunkers$x$x$x	07_petroleum_products$x
# 5258	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	07_petroleum_products$x
# 5259	10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x	07_petroleum_products$x
# 5261	10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x	07_petroleum_products$x
# 5262	10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x	07_petroleum_products$x
# 5263	10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x	07_petroleum_products$x
# 5264	10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x	07_petroleum_products$x
# 5266	10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x	07_petroleum_products$x
# 5267	10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x	07_petroleum_products$x
# 5268	10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x	07_petroleum_products$x
# 5269	10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x	07_petroleum_products$x
# 5271	10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x	07_petroleum_products$x
# 5273	10_losses_and_own_use$10_01_own_use$x$x	07_petroleum_products$x
# 5274	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	07_petroleum_products$x
# 5275	10_losses_and_own_use$x$x$x	07_petroleum_products$x
# 5277	12_total_final_consumption$x$x$x	07_petroleum_products$x
# 5278	13_total_final_energy_consumption$x$x$x	07_petroleum_products$x
# 5329	16_other_sector$16_01_buildings$x$x	07_petroleum_products$x
# 5332	16_other_sector$16_02_agriculture_and_fishing$x$x	07_petroleum_products$x
# 5333	16_other_sector$16_05_nonspecified_others$x$x	07_petroleum_products$x
# 5334	16_other_sector$x$x$x	07_petroleum_products$x
# 5335	17_nonenergy_use$x$x$x	07_petroleum_products$x
# 5387	10_losses_and_own_use$10_01_own_use$10_01_05_natural_gas_blending_plants$x	07_petroleum_products$x
# 5442	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	08_gas$08_01_natural_gas
# 5443	10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x	08_gas$08_01_natural_gas
# 5444	10_losses_and_own_use$10_01_own_use$10_01_03_liquefaction_regasification_plants$x	08_gas$08_01_natural_gas
# 5445	10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x	08_gas$08_01_natural_gas
# 5446	10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x	08_gas$08_01_natural_gas
# 5447	10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x	08_gas$08_01_natural_gas
# 5448	10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x	08_gas$08_01_natural_gas
# 5450	10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x	08_gas$08_01_natural_gas
# 5451	10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x	08_gas$08_01_natural_gas
# 5452	10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x	08_gas$08_01_natural_gas
# 5453	10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x	08_gas$08_01_natural_gas
# 5455	10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x	08_gas$08_01_natural_gas
# 5457	10_losses_and_own_use$10_01_own_use$x$x	08_gas$08_01_natural_gas
# 5458	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	08_gas$08_01_natural_gas
# 5459	10_losses_and_own_use$x$x$x	08_gas$08_01_natural_gas
# 5461	12_total_final_consumption$x$x$x	08_gas$08_01_natural_gas
# 5462	13_total_final_energy_consumption$x$x$x	08_gas$08_01_natural_gas
# 5513	16_other_sector$16_01_buildings$x$x	08_gas$08_01_natural_gas
# 5516	16_other_sector$16_02_agriculture_and_fishing$x$x	08_gas$08_01_natural_gas
# 5517	16_other_sector$16_05_nonspecified_others$x$x	08_gas$08_01_natural_gas
# 5518	16_other_sector$x$x$x	08_gas$08_01_natural_gas
# 5519	17_nonenergy_use$x$x$x	08_gas$08_01_natural_gas
# 5568	10_losses_and_own_use$10_01_own_use$10_01_05_natural_gas_blending_plants$x	08_gas$08_01_natural_gas
# 5584	10_losses_and_own_use$10_01_own_use$10_01_03_liquefaction_regasification_plants$x	08_gas$08_02_lng
# 5592	10_losses_and_own_use$10_01_own_use$x$x	08_gas$08_02_lng
# 5594	10_losses_and_own_use$x$x$x	08_gas$08_02_lng
# 5690	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	08_gas$08_03_gas_works_gas
# 5691	10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x	08_gas$08_03_gas_works_gas
# 5693	10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x	08_gas$08_03_gas_works_gas
# 5694	10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x	08_gas$08_03_gas_works_gas
# 5696	10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x	08_gas$08_03_gas_works_gas
# 5698	10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x	08_gas$08_03_gas_works_gas
# 5701	10_losses_and_own_use$10_01_own_use$x$x	08_gas$08_03_gas_works_gas
# 5702	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	08_gas$08_03_gas_works_gas
# 5703	10_losses_and_own_use$x$x$x	08_gas$08_03_gas_works_gas
# 5705	12_total_final_consumption$x$x$x	08_gas$08_03_gas_works_gas
# 5706	13_total_final_energy_consumption$x$x$x	08_gas$08_03_gas_works_gas
# 5735	16_other_sector$16_01_buildings$x$x	08_gas$08_03_gas_works_gas
# 5736	16_other_sector$16_05_nonspecified_others$x$x	08_gas$08_03_gas_works_gas
# 5737	16_other_sector$x$x$x	08_gas$08_03_gas_works_gas
# 5846	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	08_gas$x
# 5847	10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x	08_gas$x
# 5848	10_losses_and_own_use$10_01_own_use$10_01_03_liquefaction_regasification_plants$x	08_gas$x
# 5849	10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x	08_gas$x
# 5850	10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x	08_gas$x
# 5851	10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x	08_gas$x
# 5852	10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x	08_gas$x
# 5854	10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x	08_gas$x
# 5855	10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x	08_gas$x
# 5856	10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x	08_gas$x
# 5857	10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x	08_gas$x
# 5859	10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x	08_gas$x
# 5861	10_losses_and_own_use$10_01_own_use$x$x	08_gas$x
# 5862	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	08_gas$x
# 5863	10_losses_and_own_use$x$x$x	08_gas$x
# 5865	12_total_final_consumption$x$x$x	08_gas$x
# 5866	13_total_final_energy_consumption$x$x$x	08_gas$x
# 5917	16_other_sector$16_01_buildings$x$x	08_gas$x
# 5920	16_other_sector$16_02_agriculture_and_fishing$x$x	08_gas$x
# 5921	16_other_sector$16_05_nonspecified_others$x$x	08_gas$x
# 5922	16_other_sector$x$x$x	08_gas$x
# 5923	17_nonenergy_use$x$x$x	08_gas$x
# 5972	10_losses_and_own_use$10_01_own_use$10_01_05_natural_gas_blending_plants$x	08_gas$x
# 7096	12_total_final_consumption$x$x$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7097	13_total_final_energy_consumption$x$x$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7124	16_other_sector$16_01_buildings$x$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7127	16_other_sector$16_02_agriculture_and_fishing$x$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7129	16_other_sector$x$x$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
# 7205	12_total_final_consumption$x$x$x	15_solid_biomass$15_02_bagasse
# 7206	13_total_final_energy_consumption$x$x$x	15_solid_biomass$15_02_bagasse
# 7233	16_other_sector$16_01_buildings$x$x	15_solid_biomass$15_02_bagasse
# 7236	16_other_sector$16_02_agriculture_and_fishing$x$x	15_solid_biomass$15_02_bagasse
# 7238	16_other_sector$x$x$x	15_solid_biomass$15_02_bagasse
# 7311	12_total_final_consumption$x$x$x	15_solid_biomass$15_03_charcoal
# 7312	13_total_final_energy_consumption$x$x$x	15_solid_biomass$15_03_charcoal
# 7339	16_other_sector$16_01_buildings$x$x	15_solid_biomass$15_03_charcoal
# 7342	16_other_sector$16_02_agriculture_and_fishing$x$x	15_solid_biomass$15_03_charcoal
# 7344	16_other_sector$x$x$x	15_solid_biomass$15_03_charcoal
# 7420	12_total_final_consumption$x$x$x	15_solid_biomass$15_04_black_liquor
# 7421	13_total_final_energy_consumption$x$x$x	15_solid_biomass$15_04_black_liquor
# 7513	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	15_solid_biomass$15_05_other_biomass
# 7515	10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x	15_solid_biomass$15_05_other_biomass
# 7519	10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x	15_solid_biomass$15_05_other_biomass
# 7523	10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x	15_solid_biomass$15_05_other_biomass
# 7525	10_losses_and_own_use$10_01_own_use$x$x	15_solid_biomass$15_05_other_biomass
# 7526	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	15_solid_biomass$15_05_other_biomass
# 7527	10_losses_and_own_use$x$x$x	15_solid_biomass$15_05_other_biomass
# 7529	12_total_final_consumption$x$x$x	15_solid_biomass$15_05_other_biomass
# 7530	13_total_final_energy_consumption$x$x$x	15_solid_biomass$15_05_other_biomass
# 7557	16_other_sector$16_01_buildings$x$x	15_solid_biomass$15_05_other_biomass
# 7560	16_other_sector$16_02_agriculture_and_fishing$x$x	15_solid_biomass$15_05_other_biomass
# 7561	16_other_sector$16_05_nonspecified_others$x$x	15_solid_biomass$15_05_other_biomass
# 7562	16_other_sector$x$x$x	15_solid_biomass$15_05_other_biomass
# 7669	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	15_solid_biomass$x
# 7671	10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x	15_solid_biomass$x
# 7675	10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x	15_solid_biomass$x
# 7679	10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x	15_solid_biomass$x
# 7681	10_losses_and_own_use$10_01_own_use$x$x	15_solid_biomass$x
# 7682	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	15_solid_biomass$x
# 7683	10_losses_and_own_use$x$x$x	15_solid_biomass$x
# 7685	12_total_final_consumption$x$x$x	15_solid_biomass$x
# 7686	13_total_final_energy_consumption$x$x$x	15_solid_biomass$x
# 7713	16_other_sector$16_01_buildings$x$x	15_solid_biomass$x
# 7716	16_other_sector$16_02_agriculture_and_fishing$x$x	15_solid_biomass$x
# 7717	16_other_sector$16_05_nonspecified_others$x$x	15_solid_biomass$x
# 7718	16_other_sector$x$x$x	15_solid_biomass$x
# 7829	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	16_others$16_01_biogas
# 7853	10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x	16_others$16_01_biogas
# 7859	10_losses_and_own_use$10_01_own_use$x$x	16_others$16_01_biogas
# 7862	10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x	16_others$16_01_biogas
# 7865	10_losses_and_own_use$x$x$x	16_others$16_01_biogas
# 7871	12_total_final_consumption$x$x$x	16_others$16_01_biogas
# 7874	13_total_final_energy_consumption$x$x$x	16_others$16_01_biogas
# 8027	16_other_sector$16_01_buildings$x$x	16_others$16_01_biogas
# 8036	16_other_sector$16_02_agriculture_and_fishing$x$x	16_others$16_01_biogas
# 8039	16_other_sector$16_05_nonspecified_others$x$x	16_others$16_01_biogas
# 8042	16_other_sector$x$x$x	16_others$16_01_biogas
# 8205	10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x	16_others$16_02_industrial_waste
# 8207	10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x	16_others$16_02_industrial_waste
# 8211	10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x	16_others$16_02_industrial_waste
# 8216	10_losses_and_own_use$10_01_own_use$x$x	16_others$16_02_industrial_waste
# 8218	10_losses_and_own_use$x$x$x	16_others$16_02_industrial_waste
# 8220	12_total_final_consumption$x$x$x	16_others$16_02_industrial_waste
# 8221	13_total_final_energy_consumption$x$x$x	16_others$16_02_industrial_waste
# 8248	16_other_sector$16_01_buildings$x$x	16_others$16_02_industrial_waste
# 8251	16_other_sector$16_02_agriculture_and_fishing$x$x	16_others$16_02_industrial_waste
# 8252	16_other_sector$16_05_nonspecified_others$x$x	16_others$16_02_industrial_waste
# 8253	16_other_sector$x$x$x	16_others$16_02_industrial_waste
# 8331	12_total_final_consumption$x$x$x	16_others$16_03_municipal_solid_waste_renewable
# 8332	13_total_final_energy_consumption$x$x$x	16_others$16_03_municipal_solid_waste_renewable
# 8359	16_other_sector$16_01_buildings$x$x	16_others$16_03_municipal_solid_waste_renewable
# 8363	16_other_sector$16_05_nonspecified_others$x$x	16_others$16_03_municipal_solid_waste_renewable
# 8364	16_other_sector$x$x$x	16_others$16_03_municipal_solid_waste_renewable
# 8442	12_total_final_consumption$x$x$x	16_others$16_04_municipal_solid_waste_nonrenewable
# 8443	13_total_final_energy_consumption$x$x$x	16_others$16_04_municipal_solid_waste_nonrenewable
# 8470	16_other_sector$16_01_buildings$x$x	16_others$16_04_municipal_solid_waste_nonrenewable
# 8473	16_other_sector$16_02_agriculture_and_fishing$x$x	16_others$16_04_municipal_solid_waste_nonrenewable
# 8474	16_other_sector$16_05_nonspecified_others$x$x	16_others$16_04_municipal_solid_waste_nonrenewable
# 8475	16_other_sector$x$x$x	16_others$16_04_municipal_solid_waste_nonrenewable
# 8550	12_total_final_consumption$x$x$x	16_others$16_05_biogasoline
# 8551	13_total_final_energy_consumption$x$x$x	16_others$16_05_biogasoline
# 8602	16_other_sector$16_01_buildings$x$x	16_others$16_05_biogasoline
# 8605	16_other_sector$16_02_agriculture_and_fishing$x$x	16_others$16_05_biogasoline
# 8607	16_other_sector$x$x$x	16_others$16_05_biogasoline
# 8657	04_international_marine_bunkers$x$x$x	16_others$16_06_biodiesel
# 8673	10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x	16_others$16_06_biodiesel
# 8677	10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x	16_others$16_06_biodiesel
# 8682	10_losses_and_own_use$10_01_own_use$x$x	16_others$16_06_biodiesel
# 8684	10_losses_and_own_use$x$x$x	16_others$16_06_biodiesel
# 8686	12_total_final_consumption$x$x$x	16_others$16_06_biodiesel
# 8687	13_total_final_energy_consumption$x$x$x	16_others$16_06_biodiesel
# 8738	16_other_sector$16_01_buildings$x$x	16_others$16_06_biodiesel
# 8741	16_other_sector$16_02_agriculture_and_fishing$x$x	16_others$16_06_biodiesel
# 8742	16_other_sector$16_05_nonspecified_others$x$x	16_others$16_06_biodiesel
# 8743	16_other_sector$x$x$x	16_others$16_06_biodiesel
# 9074	12_total_final_consumption$x$x$x	16_others$16_08_other_liquid_biofuels
# 9075	13_total_final_energy_consumption$x$x$x	16_others$16_08_other_liquid_biofuels
# 9102	16_other_sector$16_01_buildings$x$x	16_others$16_08_other_liquid_biofuels
# 9103	16_other_sector$x$x$x	16_others$16_08_other_liquid_biofuels

