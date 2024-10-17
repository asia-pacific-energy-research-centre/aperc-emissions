#first lets tak in the sectors from mdoel_df_wide. We are going to use chatgpt to map them to the sectors in te emissions factors from ipccc, and try to develop a mapping. 
#%%
import pandas as pd
import numpy as np
import os
model_df_wide_original = pd.read_csv('single_use_inputs/model_df_wide_tgt_20231208.csv')
emissions_factors_ipcc = pd.read_csv('single_use_inputs/EFDB_output (1).csv')#this was downlaoded from here https://www.ipcc-nggip.iges.or.jp/EFDB/find_ef.php?ipcc_code=1&ipcc_level=0 < that is, the ipccc emissions factors database for the IPCC 2006 category: 1 - Energy.
#we will need to filter for the data which has the units KG/TJ > im pretty sure this will have all we need
#then print all the unique values in the IPCC 2006 Source/Sink Category column and map them to all the unique vategories in the model_df_wide['sectors'] column < we might ahve to create a concat of all the subsectors columns in mdoel_df_wide to get more precise mappings
#%%
#replace rows that contain Natural Gas Liquids\n(NGLs) with Natural Gas Liquids (NGLs)
emissions_factors_ipcc['Fuel 2006'] = emissions_factors_ipcc['Fuel 2006'].str.replace('Natural Gas Liquids\n(NGLs)', 'Natural Gas Liquids (NGLs)')
#and renaame 1.A.4.b - Residential\n1.A.4.c.i - Stationary to 1.A.4.b - Residential
emissions_factors_ipcc['IPCC 2006 Source/Sink Category'] = emissions_factors_ipcc['IPCC 2006 Source/Sink Category'].str.replace('1.A.4.b - Residential\n1.A.4.c.i - Stationary', '1.A.4.b - Residential')

# # emissions_factors_ipccc_filtered = emissions_factors_ipccc[emissions_factors_ipccc['Unit'] == 'KG/TJ']
# print(emissions_factors_ipccc['IPCC 2006 Source/Sink Category'].unique())
# ['1.A.1 - Energy Industries'
#  '1.A.2 - Manufacturing Industries and Construction' '1.A.3.c - Railways'
#  '1.A.3.d - Water-borne Navigation' '1.A.4.a - Commercial/Institutional'
#  '1.A.4.b - Residential' '1.A.4.c.i - Stationary'
#  '1.A.3.b - Road Transportation'
#  '1.A.4.c.ii - Off-road Vehicles and Other Machinery\n1.A.4.c.iii - Fishing (mobile combustion)'
#  '1.A.3.a - Civil Aviation'
#  '1.A.1 - Energy Industries\n1.A.1.a - Main Activity Electricity and Heat Production\n1.A.1.a.i - Electricity Generation\n1.A.1.a.ii - Combined Heat and Power Generation (CHP)\n1.A.1.a.iii - Heat Plants'
#  '1.A - Fuel Combustion Activities' '1.A.1.a.iii - Heat Plants'
#  '1.A - Fuel Combustion Activities\n1.A.3.b - Road Transportation'
#  '1.A.3.a - Civil Aviation\n1.A.3.a.i - International Aviation (International Bunkers)\n1.A.3.a.ii - Domestic Aviation'
#  '1.A.3.a - Civil Aviation\n1.A.3.a.ii - Domestic Aviation'
#  '1.A - Fuel Combustion Activities\n1.A.3.b - Road Transportation\n1.A.3.c - Railways\n1.A.3.d - Water-borne Navigation\n1.A.3.e.ii - Off-road'
#  '1.A - Fuel Combustion Activities\n1.A.3.d - Water-borne Navigation'
#  '1.A - Fuel Combustion Activities\n1.A.1.b - Petroleum Refining' nan]

#%%

#ok lets create a method that can be reused to map to the ipcc sectors if , say, we add more sectors to model_df_wide.
#we will concat all the column ['sectors', 'sub1sectors', 'sub2sectors', 'sub3sectors', 'sub4sectors'] to get a more precise mapping, using $ as a separator. Then we can print the list of unique values ready to be input to chatgpt. we will ask chat gpt to create a mapping of these to the most specific ipcc sectors in 1.A and 1.B, separately. Where there are multiple options of the same specificity, we will ask chatgpt to provide a list of the most likely options.
model_df_wide=model_df_wide_original.copy()
model_df_wide['concat_sectors'] = model_df_wide['sectors'] + '$' + model_df_wide['sub1sectors'] + '$' + model_df_wide['sub2sectors'] + '$' + model_df_wide['sub3sectors'] #+ '$' + model_df_wide['sub4sectors'] #ignore sub4sectors since they are currently just the engine types
# print(model_df_wide['concat_sectors'].unique())
#we also dont need most  of the cols so lets drop them and any duplicates:
model_df_wide = model_df_wide[['sectors', 'sub1sectors', 'sub2sectors', 'sub3sectors', 'sub4sectors', 'fuels', 'subfuels', 'concat_sectors']].drop_duplicates()

#%%

# # can u map these ipcc sectors 
# ipcc_sectors = ['1.A - Fuel Combustion Activities' '1.A.1 - Energy Industries'
#  '1.A.2 - Manufacturing Industries and Construction' '1.A.3.c - Railways'
#  '1.A.3.d - Water-borne Navigation' '1.A.4.a - Commercial/Institutional'
#  '1.A.4.b - Residential' '1.A.4.c.i - Stationary'
#  '1.A.3.b - Road Transportation'
#  '1.A.4.c.ii - Off-road Vehicles and Other Machinery\n1.A.4.c.iii - Fishing (mobile combustion)'
#  '1.A.3.a - Civil Aviation'
#  '1.A.1 - Energy Industries\n1.A.1.a - Main Activity Electricity and Heat Production\n1.A.1.a.i - Electricity Generation\n1.A.1.a.ii - Combined Heat and Power Generation (CHP)\n1.A.1.a.iii - Heat Plants'
#  '1.A.3.b - Road Transportation\n1.A.3.b.ii - Light-duty trucks\n1.A.3.b.iii - Heavy-duty trucks and buses'
#  '1.A.4.c.ii - Off-road Vehicles and Other Machinery'
#  '1.B.1.a - Coal mining and handling' '1.B.2.a - Oil'
#  '1.B.2.b - Natural Gas' '1.B.2 - Oil and Natural Gas'
#  '1.A.3.a.ii - Domestic Aviation'
#  '1.A.3.a.i - International Aviation (International Bunkers)'
#  '1.A.1.a.ii - Combined Heat and Power Generation (CHP)'
#  '1.A.1.b - Petroleum Refining'
#  '1.A.3.d.i - International water-borne navigation (International bunkers)'
#  '1.A.1.c.i - Manufacture of Solid Fuels'
#  '1.A.4.b - Residential\n1.A.4.c.i - Stationary' '1.A.3.b.i - Cars'
#  '1.A.3.b.ii - Light-duty trucks'
#  '1.A.3.b.iii - Heavy-duty trucks and buses' '1.A.3.b.iv - Motorcycles'
#  '1.A.3.e.ii - Off-road'
#  '1.A.3.a - Civil Aviation\n1.A.3.a.i - International Aviation (International Bunkers)\n1.A.3.a.ii - Domestic Aviation'
#  '1.B.1.a.i.1 - Mining' '1.B.1.a.i.2 - Post-mining seam gas emissions'
#  '1.B.1.a.ii.1 - Mining' '1.B.1.a.ii.2 - Post-mining seam gas emissions'
#  '1.B.1.a.i.3 - Abandoned underground mines'
#  '1.A.1.a.i - Electricity Generation'
#  '1.A.1 - Energy Industries\n1.A.2 - Manufacturing Industries and Construction'
#  '1.A.1.a - Main Activity Electricity and Heat Production\n1.A.1.a.i - Electricity Generation\n1.A.1.a.ii - Combined Heat and Power Generation (CHP)\n1.A.1.a.iii - Heat Plants'
#  '1.A.1 - Energy Industries\n1.A.4.a - Commercial/Institutional\n1.A.4.b - Residential\n1.A.4.c - Agriculture/Forestry/Fishing/Fish Farms\n1.A.4.c.i - Stationary'
#  '1.A.3.b.i.1 - Passenger cars with 3-way catalysts'
#  '1.B.1.a.i - Underground mines' '1.A.1.a.iii - Heat Plants'
#  '1.A.1.a - Main Activity Electricity and Heat Production'
#  '1.A.1.c - Manufacture of Solid Fuels and Other Energy Industries'
#  '1.A.1.c.ii - Other Energy Industries' '1.A.2.f - Non-Metallic Minerals'
#  '1.B.3 - Other emissions from Energy Production'
#  '1.A.2.d - Pulp, Paper and Print' nan '1.A.5.b - Mobile'
#  '1.A.2.a - Iron and Steel' '1.A.2.b - Non-Ferrous Metals'
#  '1.A.2.c - Chemicals' '1.A.2.e - Food Processing, Beverages and Tobacco'
#  '1.A.2.g - Transport Equipment' '1.A.2.h - Machinery'
#  '1.A.2.j - Wood and wood products' '1.A.2.l - Textile and Leather'
#  '1.B.1.a.ii - Surface mines' '1.A.3 - Transport' '1.A.4 - Other Sectors'
#  '1.A.2 - Manufacturing Industries and Construction\n1.A.4.a - Commercial/Institutional'
#  '1.A.2 - Manufacturing Industries and Construction\n1.A.4.a - Commercial/Institutional\n1.A.4.b - Residential\n1.A.4.c.ii - Off-road Vehicles and Other Machinery'
#  '1.A.3.b.i - Cars\n1.A.3.b.ii - Light-duty trucks'
#  '1.A.3.b - Road Transportation\n1.A.3.b.i - Cars'
#  '1.B.2.a.ii - Flaring\n1.B.2.b.ii - Flaring' '1.B.2.b.ii - Flaring'
#  '1.B.2.b.i - Venting' '1.B.2.a.i - Venting' '1.B.2.a.ii - Flaring'
#  '1.B.1.a.ii - Surface mines\n1.B.1.a.ii.1 - Mining'
#  '1.B.1.a.ii - Surface mines\n1.B.1.a.ii.2 - Post-mining seam gas emissions'
#  '1.A - Fuel Combustion Activities\n1.A.3.b - Road Transportation'
#  '1.A.3.a - Civil Aviation\n1.A.3.a.ii - Domestic Aviation'
#  '1.A - Fuel Combustion Activities\n1.A.3.b - Road Transportation\n1.A.3.c - Railways\n1.A.3.d - Water-borne Navigation\n1.A.3.e.ii - Off-road'
#  '1.A - Fuel Combustion Activities\n1.A.3.d - Water-borne Navigation'
#  '1.A - Fuel Combustion Activities\n1.A.1.b - Petroleum Refining'
#  '1 - Energy\n1.A - Fuel Combustion Activities\n1.A.1 - Energy Industries\n1.A.1.a - Main Activity Electricity and Heat Production\n1.A.1.a.i - Electricity Generation'
#  '1.A - Fuel Combustion Activities\n4.C.1 - Waste Incineration']

# To these sectors from our energy balacnes
#%%
aperc_sectors = model_df_wide['concat_sectors'].unique().tolist()
# aperc_sectors = ['01_production$x$x$x' '02_imports$x$x$x' '03_exports$x$x$x'
#  '04_international_marine_bunkers$x$x$x'
#  '05_international_aviation_bunkers$x$x$x' '06_stock_changes$x$x$x'
#  '07_total_primary_energy_supply$x$x$x' '08_transfers$x$x$x'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_01_coal_power$09_01_01_01_subcritical'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_01_coal_power$09_01_01_02_superultracritical'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_01_coal_power$09_01_01_03_advultracritical'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_01_coal_power$09_01_01_04_ccs'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_01_coal_power$x'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_02_gas_power$09_01_02_01_gasturbine'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_02_gas_power$09_01_02_02_combinedcycle'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_02_gas_power$09_01_02_03_ccs'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_02_gas_power$x'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_03_oil$x'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_04_nuclear$x'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_05_hydro$09_01_05_01_large'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_05_hydro$09_01_05_02_mediumsmall'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_05_hydro$09_01_05_03_pump'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_05_hydro$x'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_06_biomass$x'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_07_geothermal$x'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_08_solar$09_01_08_01_utility'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_08_solar$09_01_08_02_rooftop'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_08_solar$09_01_08_03_csp'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_08_solar$x'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_09_wind$09_01_09_01_onshore'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_09_wind$09_01_09_02_offshore'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_09_wind$x'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_10_otherrenewable$x'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_11_otherfuel$x'
#  '09_total_transformation_sector$09_01_electricity_plants$09_01_12_storage$x'
#  '09_total_transformation_sector$09_01_electricity_plants$x$x'
#  '09_total_transformation_sector$09_02_chp_plants$09_02_01_coal$x'
#  '09_total_transformation_sector$09_02_chp_plants$09_02_02_gas$x'
#  '09_total_transformation_sector$09_02_chp_plants$09_02_03_oil$x'
#  '09_total_transformation_sector$09_02_chp_plants$09_02_04_biomass$x'
#  '09_total_transformation_sector$09_02_chp_plants$x$x'
#  '09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x'
#  '09_total_transformation_sector$09_06_gas_processing_plants$x$x'
#  '09_total_transformation_sector$09_07_oil_refineries$x$x'
#  '09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x'
#  '09_total_transformation_sector$09_08_coal_transformation$09_08_02_blast_furnaces$x'
#  '09_total_transformation_sector$09_08_coal_transformation$09_08_03_patent_fuel_plants$x'
#  '09_total_transformation_sector$09_08_coal_transformation$09_08_04_bkb_pb_plants$x'
#  '09_total_transformation_sector$09_08_coal_transformation$09_08_05_liquefaction_coal_to_oil$x'
#  '09_total_transformation_sector$09_08_coal_transformation$x$x'
#  '09_total_transformation_sector$09_10_biofuels_processing$x$x'
#  '09_total_transformation_sector$09_12_nonspecified_transformation$x$x'
#  '09_total_transformation_sector$09_13_hydrogen_transformation$09_13_01_electrolysers$x'
#  '09_total_transformation_sector$09_13_hydrogen_transformation$09_13_02_smr_wo_ccs$x'
#  '09_total_transformation_sector$09_13_hydrogen_transformation$09_13_03_smr_w_ccs$x'
#  '09_total_transformation_sector$09_13_hydrogen_transformation$09_13_04_coal_wo_ccs$x'
#  '09_total_transformation_sector$09_13_hydrogen_transformation$09_13_05_coal_w_ccs$x'
#  '09_total_transformation_sector$09_13_hydrogen_transformation$09_13_06_others$x'
#  '09_total_transformation_sector$09_13_hydrogen_transformation$x$x'
#  '09_total_transformation_sector$09_x_heat_plants$09_x_01_coal$x'
#  '09_total_transformation_sector$09_x_heat_plants$09_x_02_gas$x'
#  '09_total_transformation_sector$09_x_heat_plants$09_x_03_oil$x'
#  '09_total_transformation_sector$09_x_heat_plants$09_x_04_biomass$x'
#  '09_total_transformation_sector$09_x_heat_plants$x$x'
#  '09_total_transformation_sector$x$x$x'
#  '10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x'
#  '10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x'
#  '10_losses_and_own_use$10_01_own_use$10_01_03_liquefaction_regasification_plants$x'
#  '10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x'
#  '10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x'
#  '10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x'
#  '10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x'
#  '10_losses_and_own_use$10_01_own_use$10_01_10_blast_furnaces$x'
#  '10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x'
#  '10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x'
#  '10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x'
#  '10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x'
#  '10_losses_and_own_use$10_01_own_use$10_01_16_biofuels_processing$x'
#  '10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x'
#  '10_losses_and_own_use$10_01_own_use$10_01_19_ccs$x'
#  '10_losses_and_own_use$10_01_own_use$x$x'
#  '10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x'
#  '10_losses_and_own_use$x$x$x' '11_statistical_discrepancy$x$x$x'
#  '12_total_final_consumption$x$x$x'
#  '13_total_final_energy_consumption$x$x$x'
#  '14_industry_sector$14_01_mining_and_quarrying$x$x'
#  '14_industry_sector$14_02_construction$x$x'
#  '14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$14_03_01_01_fs'
#  '14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$14_03_01_02_eaf'
#  '14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$14_03_01_03_ccs'
#  '14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$14_03_01_04_bfbof'
#  '14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$14_03_01_05_hydrogen'
#  '14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x'
#  '14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$14_03_02_01_fs'
#  '14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$14_03_02_02_ccs'
#  '14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x'
#  '14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x'
#  '14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$14_03_04_01_ccs'
#  '14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$14_03_04_02_nonccs'
#  '14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x'
#  '14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x'
#  '14_industry_sector$14_03_manufacturing$14_03_06_machinery$x'
#  '14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x'
#  '14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x'
#  '14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x'
#  '14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x'
#  '14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x'
#  '14_industry_sector$14_03_manufacturing$x$x'
#  '14_industry_sector$x$x$x'
#  '15_transport_sector$15_01_domestic_air_transport$15_01_01_passenger$x'
#  '15_transport_sector$15_01_domestic_air_transport$15_01_02_freight$x'
#  '15_transport_sector$15_01_domestic_air_transport$x$x'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_01_two_wheeler$15_02_01_01_01_diesel_engine'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_01_two_wheeler$15_02_01_01_02_gasoline_engine'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_01_two_wheeler$15_02_01_01_03_battery_ev'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_01_two_wheeler$15_02_01_01_04_compressed_natual_gas'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_01_two_wheeler$15_02_01_01_05_plugin_hybrid_ev_gasoline'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_01_two_wheeler$15_02_01_01_06_plugin_hybrid_ev_diesel'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_01_two_wheeler$15_02_01_01_07_liquified_petroleum_gas'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_01_two_wheeler$15_02_01_01_08_fuel_cell_ev'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_01_two_wheeler'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_02_car$15_02_01_02_01_diesel_engine'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_02_car$15_02_01_02_02_gasoline_engine'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_02_car$15_02_01_02_03_battery_ev'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_02_car$15_02_01_02_04_compressed_natual_gas'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_02_car$15_02_01_02_05_plugin_hybrid_ev_gasoline'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_02_car$15_02_01_02_06_plugin_hybrid_ev_diesel'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_02_car$15_02_01_02_07_liquified_petroleum_gas'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_02_car$15_02_01_02_08_fuel_cell_ev'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_02_car'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_03_sports_utility_vehicle$15_02_01_03_01_diesel_engine'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_03_sports_utility_vehicle$15_02_01_03_02_gasoline_engine'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_03_sports_utility_vehicle$15_02_01_03_03_battery_ev'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_03_sports_utility_vehicle$15_02_01_03_04_compressed_natual_gas'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_03_sports_utility_vehicle$15_02_01_03_05_plugin_hybrid_ev_gasoline'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_03_sports_utility_vehicle$15_02_01_03_06_plugin_hybrid_ev_diesel'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_03_sports_utility_vehicle$15_02_01_03_07_liquified_petroleum_gas'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_03_sports_utility_vehicle$15_02_01_03_08_fuel_cell_ev'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_03_sports_utility_vehicle'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_04_light_truck$15_02_01_04_01_diesel_engine'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_04_light_truck$15_02_01_04_02_gasoline_engine'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_04_light_truck$15_02_01_04_03_battery_ev'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_04_light_truck$15_02_01_04_04_compressed_natual_gas'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_04_light_truck$15_02_01_04_05_plugin_hybrid_ev_gasoline'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_04_light_truck$15_02_01_04_06_plugin_hybrid_ev_diesel'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_04_light_truck$15_02_01_04_07_liquified_petroleum_gas'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_04_light_truck$15_02_01_04_08_fuel_cell_ev'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_04_light_truck'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_05_bus$15_02_01_05_01_diesel_engine'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_05_bus$15_02_01_05_02_gasoline_engine'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_05_bus$15_02_01_05_03_battery_ev'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_05_bus$15_02_01_05_04_compressed_natual_gas'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_05_bus$15_02_01_05_05_plugin_hybrid_ev_gasoline'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_05_bus$15_02_01_05_06_plugin_hybrid_ev_diesel'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_05_bus$15_02_01_05_07_liquified_petroleum_gas'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_05_bus$15_02_01_05_08_fuel_cell_ev'
#  '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_05_bus'
#  '15_transport_sector$15_02_road$15_02_01_passenger$x'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_01_two_wheeler_freight$15_02_02_01_01_diesel_engine'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_01_two_wheeler_freight$15_02_02_01_02_gasoline_engine'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_01_two_wheeler_freight$15_02_02_01_03_battery_ev'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_01_two_wheeler_freight$15_02_02_01_04_compressed_natual_gas'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_01_two_wheeler_freight$15_02_02_01_05_plugin_hybrid_ev_gasoline'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_01_two_wheeler_freight$15_02_02_01_06_plugin_hybrid_ev_diesel'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_01_two_wheeler_freight$15_02_02_01_07_liquified_petroleum_gas'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_01_two_wheeler_freight$15_02_02_01_08_fuel_cell_ev'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_01_two_wheeler_freight'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_02_light_commercial_vehicle$15_02_02_02_01_diesel_engine'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_02_light_commercial_vehicle$15_02_02_02_02_gasoline_engine'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_02_light_commercial_vehicle$15_02_02_02_03_battery_ev'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_02_light_commercial_vehicle$15_02_02_02_04_compressed_natual_gas'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_02_light_commercial_vehicle$15_02_02_02_05_plugin_hybrid_ev_gasoline'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_02_light_commercial_vehicle$15_02_02_02_06_plugin_hybrid_ev_diesel'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_02_light_commercial_vehicle$15_02_02_02_07_liquified_petroleum_gas'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_02_light_commercial_vehicle$15_02_02_02_08_fuel_cell_ev'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_02_light_commercial_vehicle'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_03_medium_truck$15_02_02_03_01_diesel_engine'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_03_medium_truck$15_02_02_03_02_gasoline_engine'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_03_medium_truck$15_02_02_03_03_battery_ev'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_03_medium_truck$15_02_02_03_04_compressed_natual_gas'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_03_medium_truck$15_02_02_03_05_plugin_hybrid_ev_gasoline'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_03_medium_truck$15_02_02_03_06_plugin_hybrid_ev_diesel'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_03_medium_truck$15_02_02_03_07_liquified_petroleum_gas'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_03_medium_truck$15_02_02_03_08_fuel_cell_ev'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_03_medium_truck'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_04_heavy_truck$15_02_02_04_01_diesel_engine'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_04_heavy_truck$15_02_02_04_02_gasoline_engine'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_04_heavy_truck$15_02_02_04_03_battery_ev'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_04_heavy_truck$15_02_02_04_04_compressed_natual_gas'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_04_heavy_truck$15_02_02_04_05_plugin_hybrid_ev_gasoline'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_04_heavy_truck$15_02_02_04_06_plugin_hybrid_ev_diesel'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_04_heavy_truck$15_02_02_04_07_liquified_petroleum_gas'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_04_heavy_truck$15_02_02_04_08_fuel_cell_ev'
#  '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_04_heavy_truck'
#  '15_transport_sector$15_02_road$15_02_02_freight$x'
#  '15_transport_sector$15_02_road$x$x'
#  '15_transport_sector$15_03_rail$15_03_01_passenger$x'
#  '15_transport_sector$15_03_rail$15_03_02_freight$x'
#  '15_transport_sector$15_03_rail$x$x'
#  '15_transport_sector$15_04_domestic_navigation$15_04_01_passenger$x'
#  '15_transport_sector$15_04_domestic_navigation$15_04_02_freight$x'
#  '15_transport_sector$15_04_domestic_navigation$x$x'
#  '15_transport_sector$15_05_pipeline_transport$x$x'
#  '15_transport_sector$15_06_nonspecified_transport$x$x'
#  '15_transport_sector$x$x$x'
#  '16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x'
#  '16_other_sector$16_01_buildings$16_01_02_residential$x'
#  '16_other_sector$16_01_buildings$x$x'
#  '16_other_sector$16_02_agriculture_and_fishing$16_02_03_agriculture$x'
#  '16_other_sector$16_02_agriculture_and_fishing$16_02_04_fishing$x'
#  '16_other_sector$16_02_agriculture_and_fishing$x$x'
#  '16_other_sector$16_05_nonspecified_others$x$x'
#  '16_other_sector$x$x$x' '17_nonenergy_use$x$x$x'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_01_coal_power$18_01_01_01_subcritical'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_01_coal_power$18_01_01_02_superultracritical'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_01_coal_power$18_01_01_03_advultracritical'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_01_coal_power$18_01_01_04_ccs'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_01_coal_power$x'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_02_gas_power$18_01_02_01_gasturbine'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_02_gas_power$18_01_02_02_combinedcycle'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_02_gas_power$18_01_02_03_ccs'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_02_gas_power$x'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_03_oil$x'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_04_nuclear$x'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_05_hydro$18_01_05_01_large'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_05_hydro$18_01_05_02_mediumsmall'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_05_hydro$18_01_05_03_pump'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_05_hydro$x'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_06_biomass$x'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_07_geothermal$x'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_08_solar$18_01_08_01_utility'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_08_solar$18_01_08_02_rooftop'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_08_solar$18_01_08_03_csp'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_08_solar$x'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_09_wind$18_01_09_01_onshore'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_09_wind$18_01_09_02_offshore'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_09_wind$x'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_10_otherrenewable$x'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_11_otherfuel$x'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_12_storage$x'
#  '18_electricity_output_in_gwh$18_01_electricity_plants$x$x'
#  '18_electricity_output_in_gwh$18_02_chp_plants$18_02_01_coal$x'
#  '18_electricity_output_in_gwh$18_02_chp_plants$18_02_02_gas$x'
#  '18_electricity_output_in_gwh$18_02_chp_plants$18_02_03_oil$x'
#  '18_electricity_output_in_gwh$18_02_chp_plants$18_02_04_biomass$x'
#  '18_electricity_output_in_gwh$18_02_chp_plants$x$x'
#  '18_electricity_output_in_gwh$x$x$x'
#  '19_heat_output_in_pj$19_01_chp_plants$19_01_01_coal$x'
#  '19_heat_output_in_pj$19_01_chp_plants$19_01_02_gas$x'
#  '19_heat_output_in_pj$19_01_chp_plants$19_01_03_oil$x'
#  '19_heat_output_in_pj$19_01_chp_plants$19_01_04_biomass$x'
#  '19_heat_output_in_pj$19_01_chp_plants$x$x'
#  '19_heat_output_in_pj$19_02_heat_plants$19_02_01_coal$x'
#  '19_heat_output_in_pj$19_02_heat_plants$19_02_02_gas$x'
#  '19_heat_output_in_pj$19_02_heat_plants$19_02_03_oil$x'
#  '19_heat_output_in_pj$19_02_heat_plants$19_02_04_biomass$x'
#  '19_heat_output_in_pj$19_02_heat_plants$x$x'
#  '19_heat_output_in_pj$x$x$x'
#  '08_transfers$08_02_interproduct_transfers$x$x'
#  '08_transfers$08_03_products_transferred$x$x'
#  '09_total_transformation_sector$09_06_gas_processing_plants$09_06_02_liquefaction_regasification_plants$x'
#  '09_total_transformation_sector$09_09_petrochemical_industry$x$x'
#  '09_total_transformation_sector$09_05_chemical_heat_for_electricity_production$x$x'
#  '09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x'
#  '09_total_transformation_sector$09_11_charcoal_processing$x$x'
#  '09_total_transformation_sector$09_06_gas_processing_plants$09_06_04_gastoliquids_plants$x'
#  '10_losses_and_own_use$10_01_own_use$10_01_05_natural_gas_blending_plants$x'
#  '09_total_transformation_sector$09_04_electric_boilers$x$x']

# CHATGPT:
# Please provide it as a mapping from the energy blaance sector to the ipcc sector. Provide the most specific mapping (i.e.1.A.3.a is more precise than 1.A) , but where there are multiple options of the same specificity, please provide provide a list of the most likely options.

# If you cant provide all the mappings in one message, please write all you can and then when i say to keep going, writethe rest, but dont rewrite what you had previously

#%%
energy_to_ipcc_mapping = {
    '01_production$x$x$x': ['Not Applicable'],
    '02_imports$x$x$x': ['Not Applicable'],
    '03_exports$x$x$x': ['Not Applicable'],
    '04_international_marine_bunkers$x$x$x': ['1.A.3.d.i - International water-borne navigation (International bunkers)'],
    '05_international_aviation_bunkers$x$x$x': ['1.A.3.a.i - International Aviation (International Bunkers)'],
    '06_stock_changes$x$x$x': ['Not Applicable'],
    '07_total_primary_energy_supply$x$x$x': ['Not Applicable'],
    '08_transfers$x$x$x': ['Not Applicable'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_01_coal_power$09_01_01_01_subcritical': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_01_coal_power$09_01_01_02_superultracritical': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_01_coal_power$09_01_01_03_advultracritical': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_01_coal_power$09_01_01_04_ccs': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_01_coal_power$x': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_02_gas_power$09_01_02_01_gasturbine': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_02_gas_power$09_01_02_02_combinedcycle': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_02_gas_power$09_01_02_03_ccs': ['1.A.1.a.i - Electricity Generation'],#this one a bit tricky but since we dont know what degree of carbon capture and storage is used, we will assume it is the same as the other gas power plants and remove the carbon after calculating the emissions
    '09_total_transformation_sector$09_01_electricity_plants$09_01_02_gas_power$x': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_03_oil$x': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_04_nuclear$x': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_05_hydro$09_01_05_01_large': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_05_hydro$09_01_05_02_mediumsmall': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_05_hydro$09_01_05_03_pump': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_06_biomass$x': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_07_geothermal$x': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_08_solar$09_01_08_01_utility': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_08_solar$09_01_08_02_rooftop': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_08_solar$09_01_08_03_csp': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_09_wind$09_01_09_01_onshore': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_09_wind$09_01_09_02_offshore': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_10_otherrenewable$x': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_11_otherfuel$x': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_12_storage$x': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_02_chp_plants$09_02_01_coal$x': ['1.A.1.a.ii - Combined Heat and Power Generation (CHP)'],
    '09_total_transformation_sector$09_02_chp_plants$09_02_02_gas$x': ['1.A.1.a.ii - Combined Heat and Power Generation (CHP)'],
    '09_total_transformation_sector$09_02_chp_plants$09_02_03_oil$x': ['1.A.1.a.ii - Combined Heat and Power Generation (CHP)'],
    '09_total_transformation_sector$09_02_chp_plants$09_02_04_biomass$x': ['1.A.1.a.ii - Combined Heat and Power Generation (CHP)'],
    '09_total_transformation_sector$09_06_gas_processing_plants$09_06_01_gas_works_plants$x': ['1.A - Fuel Combustion Activities'],
    '09_total_transformation_sector$09_07_oil_refineries$x$x': ['1.A.1.b - Petroleum Refining'],
    '09_total_transformation_sector$09_08_coal_transformation$09_08_01_coke_ovens$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '09_total_transformation_sector$09_08_coal_transformation$09_08_02_blast_furnaces$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '09_total_transformation_sector$09_08_coal_transformation$09_08_03_patent_fuel_plants$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '09_total_transformation_sector$09_08_coal_transformation$09_08_04_bkb_pb_plants$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '09_total_transformation_sector$09_10_biofuels_processing$x$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '09_total_transformation_sector$09_13_hydrogen_transformation$09_13_01_electrolysers$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '09_total_transformation_sector$09_13_hydrogen_transformation$09_13_02_smr_wo_ccs$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '09_total_transformation_sector$09_13_hydrogen_transformation$09_13_03_smr_w_ccs$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    ########################################
    '09_total_transformation_sector$09_13_hydrogen_transformation$09_13_04_coal_wo_ccs$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '09_total_transformation_sector$09_13_hydrogen_transformation$09_13_05_coal_w_ccs$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '09_total_transformation_sector$09_13_hydrogen_transformation$09_13_06_others$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '09_total_transformation_sector$09_x_heat_plants$09_x_01_coal$x': ['1.A.1.a.iii - Heat Plants'],
    '09_total_transformation_sector$09_x_heat_plants$09_x_02_gas$x': ['1.A.1.a.iii - Heat Plants'],
    '09_total_transformation_sector$09_x_heat_plants$09_x_03_oil$x': ['1.A.1.a.iii - Heat Plants'],
    '09_total_transformation_sector$09_x_heat_plants$09_x_04_biomass$x': ['1.A.1.a.iii - Heat Plants'],
    '10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x': ['1.A.1.a.ii - Combined Heat and Power Generation (CHP)'],
    '10_losses_and_own_use$10_01_own_use$10_01_02_gas_works_plants$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '10_losses_and_own_use$10_01_own_use$10_01_03_liquefaction_regasification_plants$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '10_losses_and_own_use$10_01_own_use$10_01_06_gastoliquids_plants$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '10_losses_and_own_use$10_01_own_use$10_01_07_gas_separation$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '10_losses_and_own_use$10_01_own_use$10_01_08_coke_ovens$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '10_losses_and_own_use$10_01_own_use$10_01_09_coal_mines$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '10_losses_and_own_use$10_01_own_use$10_01_10_blast_furnaces$x': ['1.A.2.a - Iron and Steel'],
    '10_losses_and_own_use$10_01_own_use$10_01_14_oil_refineries$x': ['1.A.1.b - Petroleum Refining'],
    '10_losses_and_own_use$10_01_own_use$10_01_15_oil_and_gas_extraction$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '10_losses_and_own_use$10_01_own_use$10_01_16_biofuels_processing$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '10_losses_and_own_use$10_02_transmision_and_distribution_losses$x$x': ['1.A.1.a - Main Activity Electricity and Heat Production'],#seems vague?
    '11_statistical_discrepancy$x$x$x': ['Not Applicable'],
    '12_total_final_consumption$x$x$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '13_total_final_energy_consumption$x$x$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '14_industry_sector$14_01_mining_and_quarrying$x$x': ['1.A.2 - Manufacturing Industries and Construction'],#seems vague?
    '14_industry_sector$14_02_construction$x$x': ['1.A.2 - Manufacturing Industries and Construction'],#seems vague?
    '14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$14_03_01_01_fs': ['1.A.2.a - Iron and Steel'],
    '14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$14_03_01_02_eaf': ['1.A.2.a - Iron and Steel'],
    '14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$14_03_02_01_fs': ['1.A.2.c - Chemicals'],
    '14_industry_sector$14_03_manufacturing$14_03_03_non_ferrous_metals$x': ['1.A.2.b - Non-Ferrous Metals'],
    '14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$14_03_04_01_ccs': ['1.A.2.f - Non-Metallic Minerals'],
    '14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$x': ['1.A.2.f - Non-Metallic Minerals'],
    '14_industry_sector$14_03_manufacturing$14_03_05_transportation_equipment$x': ['1.A.2.g - Transport Equipment'],
    '14_industry_sector$14_03_manufacturing$14_03_06_machinery$x': ['1.A.2.h - Machinery'],
    '14_industry_sector$14_03_manufacturing$14_03_07_food_beverages_and_tobacco$x': ['1.A.2.e - Food Processing, Beverages and Tobacco'],
    '14_industry_sector$14_03_manufacturing$14_03_08_pulp_paper_and_printing$x': ['1.A.2.d - Pulp, Paper and Print'],
    '14_industry_sector$14_03_manufacturing$14_03_09_wood_and_wood_products$x': ['1.A.2.j - Wood and wood products'],
    '14_industry_sector$14_03_manufacturing$14_03_10_textiles_and_leather$x': ['1.A.2.l - Textile and Leather'],
    '15_transport_sector$15_01_domestic_air_transport$15_01_01_passenger$x': ['1.A.3.a.ii - Domestic Aviation'],
    '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_02_car': ['1.A.3.b.i - Cars'],
    '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_04_light_truck': ['1.A.3.b.ii - Light-duty trucks'],
    '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_03_medium_truck': ['1.A.3.b.iii - Heavy-duty trucks and buses'],
    '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_04_heavy_truck': ['1.A.3.b.iii - Heavy-duty trucks and buses'],
    '15_transport_sector$15_03_rail$15_03_01_passenger$x': ['1.A.3.c - Railways'],
    '15_transport_sector$15_04_domestic_navigation$15_04_01_passenger$x': ['1.A.3.d - Water-borne Navigation'],
    '16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x': ['1.A.4.a - Commercial/Institutional'],
    '16_other_sector$16_01_buildings$16_01_02_residential$x': ['1.A.4.b - Residential'],
    '16_other_sector$16_02_agriculture_and_fishing$16_02_03_agriculture$x': ['1.A.4.c - Agriculture/Forestry/Fishing/Fish Farms'],
    '16_other_sector$16_02_agriculture_and_fishing$16_02_04_fishing$x': ['1.A.4.c - Agriculture/Forestry/Fishing/Fish Farms'],
    ##############################
    '15_transport_sector$15_01_domestic_air_transport$15_01_02_freight$x': ['1.A.3.a.ii - Domestic Aviation'],
    '15_transport_sector$15_01_domestic_air_transport$x$x': ['1.A.3.a - Civil Aviation'],
    '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_01_two_wheeler': ['1.A.3.b.iv - Motorcycles'],
    '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_02_car': ['1.A.3.b.i - Cars'],
    '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_01_two_wheeler_freight': ['1.A.3.b.iv - Motorcycles'],#seems wrong?
    '15_transport_sector$15_02_road$15_02_02_freight$x': ['1.A.3.b - Road Transportation'],
    '15_transport_sector$15_02_road$x$x': ['1.A.3.b - Road Transportation'],
    '15_transport_sector$15_03_rail$x$x': ['1.A.3.c - Railways'],
    '15_transport_sector$15_04_domestic_navigation$15_04_02_freight$x': ['1.A.3.d - Water-borne Navigation'],
    '15_transport_sector$15_04_domestic_navigation$x$x': ['1.A.3.d - Water-borne Navigation'],
    '15_transport_sector$15_05_pipeline_transport$x$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '15_transport_sector$15_06_nonspecified_transport$x$x': ['1.A.3 - Transport'],
    '16_other_sector$16_02_agriculture_and_fishing$x$x': ['1.A.4.c - Agriculture/Forestry/Fishing/Fish Farms'],
    '16_other_sector$16_05_nonspecified_others$x$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '17_nonenergy_use$x$x$x': ['1.A - Fuel Combustion Activities'],#seems wrong?
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_01_coal_power$18_01_01_01_subcritical': ['Not Applicable'],
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_01_coal_power$18_01_01_02_superultracritical': ['Not Applicable'],
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_01_coal_power$18_01_01_03_advultracritical': ['Not Applicable'],
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_01_coal_power$18_01_01_04_ccs': ['Not Applicable'],
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_02_gas_power$18_01_02_01_gasturbine': ['Not Applicable'],
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_02_gas_power$18_01_02_02_combinedcycle': ['Not Applicable'],
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_02_gas_power$18_01_02_03_ccs': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_03_oil$x': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_04_nuclear$x': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_05_hydro$18_01_05_01_large': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_05_hydro$18_01_05_02_mediumsmall': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_05_hydro$18_01_05_03_pump': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_06_biomass$x': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_07_geothermal$x': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_08_solar$18_01_08_01_utility': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_08_solar$18_01_08_02_rooftop': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_08_solar$18_01_08_03_csp': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_09_wind$18_01_09_01_onshore': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_09_wind$18_01_09_02_offshore': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_10_otherrenewable$x': ['Not Applicable'],#electricity output is not measured by input fuel
    '19_heat_output_in_pj$19_01_chp_plants$19_01_01_coal$x': ['Not Applicable'],
    '19_heat_output_in_pj$19_01_chp_plants$19_01_02_gas$x': ['Not Applicable'],
    '19_heat_output_in_pj$19_01_chp_plants$19_01_03_oil$x': ['Not Applicable'],
    '19_heat_output_in_pj$19_01_chp_plants$19_01_04_biomass$x': ['Not Applicable'],
    '19_heat_output_in_pj$19_02_heat_plants$19_02_01_coal$x': ['Not Applicable'],
    '19_heat_output_in_pj$19_02_heat_plants$19_02_02_gas$x': ['Not Applicable'],
    '19_heat_output_in_pj$19_02_heat_plants$19_02_03_oil$x': ['Not Applicable'],
    '19_heat_output_in_pj$19_02_heat_plants$19_02_04_biomass$x': ['Not Applicable'],
    '19_heat_output_in_pj$x$x$x': ['Not Applicable'],
    '08_transfers$08_02_interproduct_transfers$x$x': ['Not Applicable'],
    '08_transfers$08_03_products_transferred$x$x': ['Not Applicable'],
    '09_total_transformation_sector$09_06_gas_processing_plants$09_06_02_liquefaction_regasification_plants$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '09_total_transformation_sector$09_09_petrochemical_industry$x$x': ['1.A.1.b - Petroleum Refining'],#seems like it will be missing methane?
    '09_total_transformation_sector$09_05_chemical_heat_for_electricity_production$x$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '09_total_transformation_sector$09_06_gas_processing_plants$09_06_03_natural_gas_blending_plants$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '09_total_transformation_sector$09_11_charcoal_processing$x$x': ['1.A.1.c.i - Manufacture of Solid Fuels'],
    '09_total_transformation_sector$09_06_gas_processing_plants$09_06_04_gastoliquids_plants$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '10_losses_and_own_use$10_01_own_use$10_01_05_natural_gas_blending_plants$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '09_total_transformation_sector$09_04_electric_boilers$x$x': ['1.A.1.a - Main Activity Electricity and Heat Production'],#seems wrong?
    ########################################
    '09_total_transformation_sector$09_01_electricity_plants$09_01_05_hydro$x': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_08_solar$x': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$09_01_09_wind$x': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_01_electricity_plants$x$x': ['1.A.1.a.i - Electricity Generation'],
    '09_total_transformation_sector$09_02_chp_plants$x$x': ['1.A.1.a.ii - Combined Heat and Power Generation (CHP)'],
    '09_total_transformation_sector$09_06_gas_processing_plants$x$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '09_total_transformation_sector$09_08_coal_transformation$09_08_05_liquefaction_coal_to_oil$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '09_total_transformation_sector$09_08_coal_transformation$x$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '09_total_transformation_sector$09_12_nonspecified_transformation$x$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '09_total_transformation_sector$09_13_hydrogen_transformation$x$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '09_total_transformation_sector$09_x_heat_plants$x$x': ['1.A.1.a.iii - Heat Plants'],
    '09_total_transformation_sector$x$x$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '10_losses_and_own_use$10_01_own_use$10_01_12_bkb_pb_plants$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '10_losses_and_own_use$10_01_own_use$10_01_13_liquefaction_plants_coal_to_oil$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '10_losses_and_own_use$10_01_own_use$10_01_18_nonspecified_own_uses$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '10_losses_and_own_use$10_01_own_use$10_01_19_ccs$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '10_losses_and_own_use$10_01_own_use$x$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '10_losses_and_own_use$x$x$x': ['1.A - Fuel Combustion Activities'],#seems vague?
    '14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$14_03_01_03_ccs': ['1.A.2.a - Iron and Steel'],
    '14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$14_03_01_04_bfbof': ['1.A.2.a - Iron and Steel'],
    '14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$14_03_01_05_hydrogen': ['1.A.2.a - Iron and Steel'],
    '14_industry_sector$14_03_manufacturing$14_03_01_iron_and_steel$x': ['1.A.2.a - Iron and Steel'],
    '14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$14_03_02_02_ccs': ['1.A.2.c - Chemicals'],
    '14_industry_sector$14_03_manufacturing$14_03_02_chemical_incl_petrochemical$x': ['1.A.2.c - Chemicals'],
    '14_industry_sector$14_03_manufacturing$14_03_04_nonmetallic_mineral_products$14_03_04_02_nonccs': ['1.A.2.f - Non-Metallic Minerals'],
    '14_industry_sector$14_03_manufacturing$14_03_11_nonspecified_industry$x': ['1.A.2 - Manufacturing Industries and Construction'],#seems vague?
    '14_industry_sector$14_03_manufacturing$x$x': ['1.A.2 - Manufacturing Industries and Construction'],#seems vague?
    '14_industry_sector$x$x$x': ['1.A.2 - Manufacturing Industries and Construction'],#seems vague?
    '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_03_sports_utility_vehicle': ['1.A.3.b.i - Cars'],\
    '15_transport_sector$15_02_road$15_02_01_passenger$15_02_01_05_bus': ['1.A.3.b.iii - Heavy-duty trucks and buses'],
    '15_transport_sector$15_02_road$15_02_01_passenger$x': ['1.A.3.b - Road Transportation'],
    '15_transport_sector$15_02_road$15_02_02_freight$15_02_02_02_light_commercial_vehicle': ['1.A.3.b.ii - Light-duty trucks'],
    '15_transport_sector$15_03_rail$15_03_02_freight$x': ['1.A.3.c - Railways'],
    '15_transport_sector$x$x$x': ['1.A.3 - Transport'],
    '16_other_sector$16_01_buildings$x$x': ['1.A.4 - Other Sectors'],#seems vague?
    '16_other_sector$x$x$x': ['1.A.4 - Other Sectors'],#seems vague?
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_01_coal_power$x': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_02_gas_power$x': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_05_hydro$x': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_08_solar$x': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_09_wind$x': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_11_otherfuel$x': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_12_storage$x': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_01_electricity_plants$x$x': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_02_chp_plants$18_02_01_coal$x':['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_02_chp_plants$18_02_02_gas$x': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_02_chp_plants$18_02_03_oil$x': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_02_chp_plants$18_02_04_biomass$x':['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$18_02_chp_plants$x$x': ['Not Applicable'],#electricity output is not measured by input fuel
    '18_electricity_output_in_gwh$x$x$x':['Not Applicable'],#electricity output is not measured by input fuel
    '19_heat_output_in_pj$19_01_chp_plants$x$x': ['Not Applicable'],#electricity output is not measured by input fuel
    '19_heat_output_in_pj$19_02_heat_plants$x$x': ['Not Applicable']#electricity output is not measured by input fuel
}
#%%
#check that all of teh aperc sectors are in the mapping above:
for sector in aperc_sectors:
    if sector not in energy_to_ipcc_mapping.keys():
        breakpoint()
        print(sector + ' not in mapping')
        
#check if there are any sectors in the mapping that arent in the aperc sectors:
for sector in energy_to_ipcc_mapping.keys():
    if sector not in aperc_sectors:
        breakpoint()
        print(sector + ' not in aperc sectors')


        
#%%
#create a df from the mapping. if there are multiple sectors in the list, then create multiple rows and set DUPLICATED to True
energy_to_ipcc_mapping_df = pd.DataFrame(columns=['aperc_sector', 'ipcc_sector', 'DUPLICATED'])
for sector in energy_to_ipcc_mapping.keys():
    for ipcc_sector in energy_to_ipcc_mapping[sector]:
        new_row = pd.DataFrame([{'aperc_sector': sector, 'ipcc_sector': ipcc_sector, 'DUPLICATED': False}])
        energy_to_ipcc_mapping_df = pd.concat([energy_to_ipcc_mapping_df, new_row], ignore_index=True)
    if len(energy_to_ipcc_mapping[sector]) > 1:
        energy_to_ipcc_mapping_df.loc[energy_to_ipcc_mapping_df['aperc_sector'] == sector, 'DUPLICATED'] = True
        
#%%
#now join the rows with these sectors together using an outer join
model_df_wide_sectors_mapped = model_df_wide.merge(energy_to_ipcc_mapping_df, left_on='concat_sectors', right_on='aperc_sector', how='outer')


#%%



#now we need to do the same but for fuels. We will get a list of the fuels in each df and then map them. we MIGHT have a few fuels on each side of the mapping that mathc up, thats ok. we might also be missing fuels depending on the sector. we will work that out later.

#but first check how many unique fuels there are:
emissions_factors_ipcc['Fuel 2006'].unique()

# array(['Crude Oil', 'Other Bituminous Coal', 'Lignite', 'Patent Fuel',
#        'Natural Gas Liquids\n(NGLs)', 'Gas Coke', 'Undifferentiated Coal',
#        'Refinery Feedstocks', 'Coking Coal', 'Sub-Bituminous Coal',
#        'Aviation Gasoline', 'Motor Gasoline', 'Other Kerosene',
#        'Shale Oil', 'Diesel Oil', 'Gas Oil', 'Residual Fuel Oil',
#        'Liquefied Petroleum Gases', 'Ethane', 'Naphtha', 'Bitumen',
#        'Lubricants', 'Petroleum Coke', 'Refinery Gas',
#        'Other Petroleum Products', 'Coal Tar', 'Oil Shale and Tar Sands',
#        'Orimulsion', 'Anthracite', 'Peat', 'Natural Gas',
#        'Wood/Wood Waste', 'Charcoal', 'Bio-Alcohol',
#        'Other Primary Solid Biomass', 'Coke Oven Coke and Lignite Coke',
#        nan, 'Jet Kerosene', 'Coke Oven Gas', 'Blast Furnace Gas',
#        'Other Liquid Biofuels', 'Other Biogas', 'Brown Coal Briquettes',
#        'Gas Works Gas', 'Oxygen Steel Furnace Gas', 'Jet Gasoline',
#        'Waxes', 'White Spirit & SBP',
#        'Municipal Wastes (non-biomass fraction)', 'Waste Oils',
#        'Sulphite Lyes (Black Liquor)', 'Biogasoline', 'Biodiesels',
#        'Landfill Gas', 'Sludge Gas',
#        'Municipal Wastes (biomass fraction)', 'Industrial Wastes',
#        'Fuel mixtures (fossil and biomass)', '(Unspecified)',
#        'Sewage Sludge'], dtype=object)

model_df_wide_sectors_mapped['concat_fuels']=model_df_wide_sectors_mapped['fuels']+'$'+model_df_wide_sectors_mapped['subfuels']
model_df_wide_sectors_mapped['concat_fuels'].unique()
# array(['01_coal01_01_coking_coal', '01_coal01_05_lignite',
#        '01_coal01_x_thermal_coal', '01_coalx', '02_coal_productsx',
#        '03_peatx', '04_peat_productsx', '05_oil_shale_and_oil_sandsx',
#        '06_crude_oil_and_ngl06_01_crude_oil',
#        '06_crude_oil_and_ngl06_02_natural_gas_liquids',
#        '06_crude_oil_and_ngl06_x_other_hydrocarbons',
#        '06_crude_oil_and_nglx',
#        '07_petroleum_products07_01_motor_gasoline',
#        '07_petroleum_products07_02_aviation_gasoline',
#        '07_petroleum_products07_03_naphtha',
#        '07_petroleum_products07_06_kerosene',
#        '07_petroleum_products07_07_gas_diesel_oil',
#        '07_petroleum_products07_08_fuel_oil',
#        '07_petroleum_products07_09_lpg',
#        '07_petroleum_products07_10_refinery_gas_not_liquefied',
#        '07_petroleum_products07_11_ethane',
#        '07_petroleum_products07_x_jet_fuel',
#        '07_petroleum_products07_x_other_petroleum_products',
#        '07_petroleum_productsx', '08_gas08_01_natural_gas',
#        '08_gas08_02_lng', '08_gas08_03_gas_works_gas', '08_gasx',
#        '09_nuclearx', '10_hydrox', '11_geothermalx',
#        '12_solar12_01_of_which_photovoltaics', '12_solar12_x_other_solar',
#        '12_solarx', '13_tide_wave_oceanx', '14_windx',
#        '15_solid_biomass15_01_fuelwood_and_woodwaste',
#        '15_solid_biomass15_02_bagasse', '15_solid_biomass15_03_charcoal',
#        '15_solid_biomass15_04_black_liquor',
#        '15_solid_biomass15_05_other_biomass', '15_solid_biomassx',
#        '16_others16_01_biogas', '16_others16_02_industrial_waste',
#        '16_others16_03_municipal_solid_waste_renewable',
#        '16_others16_04_municipal_solid_waste_nonrenewable',
#        '16_others16_05_biogasoline', '16_others16_06_biodiesel',
#        '16_others16_07_bio_jet_kerosene',
#        '16_others16_08_other_liquid_biofuels',
#        '16_others16_09_other_sources', '16_others16_x_ammonia',
#        '16_others16_x_efuel', '16_others16_x_hydrogen', '16_othersx',
#        '17_electricityx', '18_heatx', '19_totalx', '20_total_renewablesx',
#        '21_modern_renewablesx', nan], dtype=object)
#%%

fuel_mapping_updated = {
    '01_coal$01_01_coking_coal': ['Coking Coal'],
    '01_coal$01_05_lignite': ['Lignite'],
    '01_coal$01_x_thermal_coal': ['Other Bituminous Coal', 'Sub-Bituminous Coal'],
    '01_coal$x': ['Anthracite', 'Undifferentiated Coal'],
    '02_coal_products$x': ['Patent Fuel', 'Brown Coal Briquettes', 'Coke Oven Coke and Lignite Coke'],
    '03_peat$x': ['Peat'],
    '04_peat_products$x': ['Peat'],
    '05_oil_shale_and_oil_sands$x': ['Oil Shale and Tar Sands', 'Shale Oil'],
    '06_crude_oil_and_ngl$06_01_crude_oil': ['Crude Oil'],
    '06_crude_oil_and_ngl$06_02_natural_gas_liquids': ['Natural Gas Liquids\n(NGLs)'],
    '06_crude_oil_and_ngl$06_x_other_hydrocarbons': ['Other Petroleum Products', 'Refinery Feedstocks'],
    '06_crude_oil_and_ngl$x': ['Other Petroleum Products'],
    '07_petroleum_products$07_01_motor_gasoline': ['Motor Gasoline'],
    '07_petroleum_products$07_02_aviation_gasoline': ['Aviation Gasoline'],
    '07_petroleum_products$07_03_naphtha': ['Naphtha'],
    '07_petroleum_products$07_06_kerosene': ['Jet Kerosene', 'Other Kerosene'],
    '07_petroleum_products$07_07_gas_diesel_oil': ['Diesel Oil', 'Gas Oil'],
    '07_petroleum_products$07_08_fuel_oil': ['Residual Fuel Oil'],
    '07_petroleum_products$07_09_lpg': ['Liquefied Petroleum Gases'],
    '07_petroleum_products$07_10_refinery_gas_not_liquefied': ['Refinery Gas'],
    '07_petroleum_products$07_11_ethane': ['Ethane'],
    '07_petroleum_products$07_x_jet_fuel': ['Jet Gasoline'],
    '07_petroleum_products$07_x_other_petroleum_products': ['Bitumen', 'Lubricants', 'Petroleum Coke', 'Other Petroleum Products', 'Orimulsion'],
    '07_petroleum_products$x': ['Other Petroleum Products'],
    '08_gas$08_01_natural_gas': ['Natural Gas'],
    '08_gas$08_02_lng': ['Natural Gas'],
    '08_gas$08_03_gas_works_gas': ['Gas Works Gas'],
    '08_gas$x': ['Natural Gas'],
    '09_nuclear$x': ['zero emissions'],
    '10_hydro$x': ['zero emissions'],
    '11_geothermal$x': ['zero emissions'],
    '12_solar$12_01_of_which_photovoltaics': ['zero emissions'],
    '12_solar$12_x_other_solar': ['zero emissions'],
    '12_solar$x': ['zero emissions'],
    '13_tide_wave_ocean$x': ['zero emissions'],
    '14_wind$x': ['zero emissions'],
    '15_solid_biomass$15_01_fuelwood_and_woodwaste': ['Wood/Wood Waste'],
    '15_solid_biomass$15_02_bagasse': ['Other Primary Solid Biomass'],
    '15_solid_biomass$15_03_charcoal': ['Charcoal'],
    '15_solid_biomass$15_04_black_liquor': ['Sulphite Lyes (Black Liquor)'],
    '15_solid_biomass$15_05_other_biomass': ['Other Primary Solid Biomass'],
    '15_solid_biomass$x': ['Other Primary Solid Biomass'],
    '16_others$16_01_biogas': ['Sludge Gas', 'Other Biogas', 'Landfill Gas'],
    '16_others$16_02_industrial_waste': ['Industrial Wastes'],
    '16_others$16_03_municipal_solid_waste_renewable': ['Municipal Wastes (biomass fraction)'],
    '16_others$16_04_municipal_solid_waste_nonrenewable': ['Municipal Wastes (non-biomass fraction)'],
    '16_others$16_05_biogasoline': ['Biogasoline'],
    '16_others$16_06_biodiesel': ['Biodiesels'],
    '16_others$16_07_bio_jet_kerosene': ['Other Liquid Biofuels', 'Jet Kerosene'],
    '16_others$16_08_other_liquid_biofuels': ['Other Liquid Biofuels'],
    '16_others$16_09_other_sources': ['zero emissions'],
    '16_others$16_x_ammonia': ['zero emissions'],
    '16_others$16_x_efuel': ['zero emissions'],
    '16_others$16_x_hydrogen': ['zero emissions'],
    '16_others$x': ['zero emissions'],
    '17_electricity$x': ['zero emissions'],
    '18_heat$x': ['zero emissions'],
    '19_total$x': ['zero emissions'],
    '20_total_renewables$x': ['zero emissions'],
    '21_modern_renewables$x': ['zero emissions']
}
#%%
#map these to the model_df_wide_sectors_mapped and then merge with the sectors mapping. that way we can find where we are missing fuels and sectors:
fuel_mapping_df = pd.DataFrame(columns=['aperc_fuel', 'ipcc_fuel', 'DUPLICATED'])
for fuel in fuel_mapping_updated.keys():
    for ipcc_fuel in fuel_mapping_updated[fuel]:
        new_row = pd.DataFrame([{'aperc_fuel': fuel, 'ipcc_fuel': ipcc_fuel, 'DUPLICATED': False}])
        fuel_mapping_df = pd.concat([fuel_mapping_df, new_row], ignore_index=True)
    if len(fuel_mapping_updated[fuel]) > 1:
        fuel_mapping_df.loc[fuel_mapping_df['aperc_fuel'] == fuel, 'DUPLICATED'] = True

#now join the rows with these sectors together using an outer join
model_df_wide_fuels_sectors_mapped = model_df_wide_sectors_mapped.merge(fuel_mapping_df, left_on='concat_fuels', right_on='aperc_fuel', how='outer')
#%%
# model_df_wide_sectors_mapped.columns
# Index(['sectors', 'sub1sectors', 'sub2sectors', 'sub3sectors', 'sub4sectors',
#        'fuels', 'subfuels', 'concat_sectors', 'aperc_sector', 'ipcc_sector',
#        'DUPLICATED_x', 'concat_fuels', 'aperc_fuel', 'ipcc_fuel',
#        'DUPLICATED_y'],
#       dtype='object')

model_df_wide_simplified = model_df_wide_fuels_sectors_mapped[['aperc_sector', 'ipcc_sector', 'ipcc_fuel', 'aperc_fuel', 'DUPLICATED_x', 'DUPLICATED_y']].drop_duplicates()

#rename duplicated_x to duplicated_sector and duplicated_y to duplicated_fuel
model_df_wide_simplified = model_df_wide_simplified.rename(columns={'DUPLICATED_x': 'DUPLICATED_sector', 'DUPLICATED_y': 'DUPLICATED_fuel'})

#this is all of the combinations of sectors and fuels mapped to all the possible emissions factors. however some of these combinations of sector/fuel's from the ipcc emissions factors dont exist, so we need to find if they are essential or not, and if they are essential find an alternative.
#there also might be multiple rows in the ipcc factors that match to each fuel/sector combination. this is good, and we should thin them down later:
# %%
############################
#SHRINK THE SIZE OF BOTHJ DATAFRAMES TO MAKE IT EASIER TO WORK WITH:

#WE DECIDED EARLY ON THAT WE SHOULD REMOVE MAPPINGS TO ROWS WEHRE THE FACTOR WAS ONLY AVAILABLE FOR A CERTAIN REGION AND INSTEAD TAKE A LESS SPECIFIC SECTOR. THS JUST REDUCES COMPLEXITY.
emissions_factors_ipcc_no_regions = emissions_factors_ipcc[emissions_factors_ipcc['Region / Regional Conditions'].isna()]

#also we found that specifications by technology were not useful since we dont measure by technology. So we will remove those rows and keep only where Technologies / Practice is na
emissions_factors_ipcc_no_regions_no_technology = emissions_factors_ipcc_no_regions[emissions_factors_ipcc_no_regions['Technologies / Practices'].isna()]
#%%
#we also hvae a lot of instances where we have combinations of aperc_sectors and aperc_fuels that simply arent likely. So we will remove them by removing any where the sum of energy values across all years is 0:

model_df_wide_invalid_rows = model_df_wide_original.copy()

model_df_wide_invalid_rows['concat_sectors'] = model_df_wide_invalid_rows['sectors'] + '$' + model_df_wide_invalid_rows['sub1sectors'] + '$' + model_df_wide_invalid_rows['sub2sectors'] + '$' + model_df_wide_invalid_rows['sub3sectors']
model_df_wide_invalid_rows['concat_fuels'] = model_df_wide_invalid_rows['fuels'] + '$' + model_df_wide_invalid_rows['subfuels']

model_df_wide_invalid_rows = model_df_wide_invalid_rows.drop(columns=['sectors', 'sub1sectors', 'sub2sectors', 'sub3sectors', 'fuels', 'subfuels', 'is_subtotal', 'sub4sectors', 'scenarios', 'economy'])

#melt 
model_df_wide_invalid_rows = model_df_wide_invalid_rows.melt(id_vars=['concat_sectors', 'concat_fuels'], var_name='year', value_name='value')
#set all values that are na to 0:
model_df_wide_invalid_rows['value'] = model_df_wide_invalid_rows['value'].fillna(0)
#calc the sum of value
model_df_wide_invalid_rows['sum_value'] = model_df_wide_invalid_rows.groupby(['concat_sectors', 'concat_fuels'])['value'].transform('sum')

model_df_wide_invalid_rows_copy = model_df_wide_invalid_rows.copy()
#%%
#keep only row where value is 0 
model_df_wide_invalid_rows = model_df_wide_invalid_rows[model_df_wide_invalid_rows['sum_value'] == 0]
valid_rows = model_df_wide_invalid_rows_copy[model_df_wide_invalid_rows_copy['sum_value'] != 0][['concat_sectors', 'concat_fuels', 'sum_value']].drop_duplicates()
model_df_wide_invalid_rows=model_df_wide_invalid_rows[['concat_sectors', 'concat_fuels']].drop_duplicates()

#for some reason we are missing data for all of '16_01_01_commercial_and_public_services', '16_01_02_residential'. we dont want to drop them so remove any rows which contain them in their concat_sectors col:
model_df_wide_invalid_rows = model_df_wide_invalid_rows.loc[~model_df_wide_invalid_rows.concat_sectors.str.contains('16_01_01_commercial_and_public_services')]
model_df_wide_invalid_rows = model_df_wide_invalid_rows.loc[~model_df_wide_invalid_rows.concat_sectors.str.contains('16_01_02_residential')]

#drop those from the model_df_wide_simplified df
model_df_wide_simplified_old = model_df_wide_simplified.copy()

model_df_wide_simplified = model_df_wide_simplified.merge(model_df_wide_invalid_rows, right_on=['concat_sectors', 'concat_fuels'], left_on=['aperc_sector', 'aperc_fuel'], how='left', indicator=True)
#drop rows where concat_sectors and	concat_fuels is not na
#%%
previous_row_number=len(model_df_wide_simplified)
dropped_rows = model_df_wide_simplified[model_df_wide_simplified['_merge'] == 'both']

model_df_wide_simplified = model_df_wide_simplified[model_df_wide_simplified['_merge'] =='left_only']
print('dropped {} rows'.format(previous_row_number-len(model_df_wide_simplified)))
print('dropped rows: {}'.format(dropped_rows))
#%%
#AND REMOVE ROWS WHERE THE SECTOR IS NOT APPLICABLE OR THE FUEL IS ZERO EMISSIONS:
model_df_wide_simplified = model_df_wide_simplified[model_df_wide_simplified['ipcc_sector'] != 'Not Applicable']
#and where ipcc_fuel is Not Applicable
model_df_wide_simplified = model_df_wide_simplified[model_df_wide_simplified['ipcc_fuel'] != 'zero emissions']
############################


#%%
#START THE JOINING PROCESS:
#and then join the emissions_factors_ipccc to the model_df_wide
model_df_wide_simplified.drop(columns=['_merge'], inplace=True)

model_df_wide_simplified_ipcc_merged = model_df_wide_simplified.merge(emissions_factors_ipcc_no_regions_no_technology, left_on=['ipcc_sector', 'ipcc_fuel'], right_on=['IPCC 2006 Source/Sink Category', 'Fuel 2006'], how='outer', indicator=True)
#since we did an outer join we need to filter out the rows which dont match anythin from the right side, i.e. the rirhgt_only values, which is where we dont need the rows from the ipcc data
# model_df_wide_simplified_ipcc_merged = model_df_wide_simplified_ipcc_merged[model_df_wide_simplified_ipcc_merged['aperc_sector'].notna() & model_df_wide_simplified_ipcc_merged['ipcc_sector'].notna() & model_df_wide_simplified_ipcc_merged['ipcc_fuel'].notna() & model_df_wide_simplified_ipcc_merged['aperc_fuel'].notna()]
nas=model_df_wide_simplified_ipcc_merged[model_df_wide_simplified_ipcc_merged['_merge'] == 'right_only']
model_df_wide_simplified_ipcc_merged = model_df_wide_simplified_ipcc_merged[model_df_wide_simplified_ipcc_merged['_merge'] != 'right_only']
# model_df_wide_simplified_ipcc_merged = model_df_wide_simplified_ipcc_merged.drop(columns=['_merge'])
#save to csv
model_df_wide_simplified_ipcc_merged.to_csv('model_df_wide_sectors_fuels_mapped.csv')
#%%
#create a smaller, easier to read df:
#ddrop where ipcc_sector is Not Applicable
model_df_wide_sample = model_df_wide_simplified_ipcc_merged[model_df_wide_simplified_ipcc_merged['ipcc_sector'] != 'Not Applicable']
#and where ipcc_fuel is Not Applicable
model_df_wide_sample = model_df_wide_sample[model_df_wide_sample['ipcc_fuel'] != 'zero emissions']
# Extract the first 5000 rows
first_1000 = model_df_wide_sample.head(1000)

# Extract the last 5000 rows
last_1000 = model_df_wide_sample.tail(1000)

# Concatenate the two DataFrames
sample_df = pd.concat([first_1000, last_1000])

# Save to CSV
sample_df.to_csv('model_df_wide_sample.csv', index=False)
#%%

#where we are missing a mapping, trry mapping to where sector is 1A - Fuel Combustion Activities. there might be a few sectors where this will work:
missing_rows = model_df_wide_simplified_ipcc_merged.loc[model_df_wide_simplified_ipcc_merged['_merge'] == 'left_only']
print('missing rows: {}'.format(missing_rows))
#set their ipcc_sector to '1.A - Fuel Combustion Activities' then redo the merge:
missing_rows['ipcc_sector'] = '1.A - Fuel Combustion Activities'
missing_rows = missing_rows[['aperc_sector', 'aperc_fuel', 'ipcc_sector', 'ipcc_fuel']].drop_duplicates()

missing_rows = missing_rows.merge(emissions_factors_ipcc_no_regions_no_technology, left_on=['ipcc_sector', 'ipcc_fuel'], right_on=['IPCC 2006 Source/Sink Category', 'Fuel 2006'], how='outer', indicator=True)
#drop right only values
missing_rows = missing_rows[missing_rows['_merge'] != 'right_only']
#print the stil missing rows
print('missing rows after mapping to 1.A - Fuel Combustion Activities: {}'.format(missing_rows))
#show which rows were filled in 
print('rows filled in: {}'.format(missing_rows.loc[missing_rows['_merge'] == 'both']))
#add the filled in rows back to the model_df_wide_simplified_ipcc_merged
#drop the missing rows from original df and then add them again with some now filled in, buit not all, neccesarily
model_df_wide_simplified_ipcc_merged = model_df_wide_simplified_ipcc_merged[model_df_wide_simplified_ipcc_merged['_merge'] != 'left_only']
model_df_wide_simplified_ipcc_merged = pd.concat([model_df_wide_simplified_ipcc_merged, missing_rows], ignore_index=True)


#%%

#print the unique unit values in model_df_wide_simplified_ipcc_merged and see if we can remove some:
model_df_wide_simplified_ipcc_merged['Unit'].unique()
# array([nan, 'TJ/kt', 'tC/TJ', 'fraction', 'TJ/Gg', 'kg/GJ', 'CO2 kg/GJ',
#        'kg/TJ', 'KG/TJ', 't CO2/TJ', 'MJ/kg', 'gC/MJ', 'g/km',
#        'g/kg fuel', 'g/MJ', 'kg/LTO', 'dimensionless', 'g/tonne', 'mg/km'],
#%%
#where we alrady have other valeus, remove wherer unit is in ['fraction', 'dimensionless', 'g/km']
#we can do this by extracting the rows, joining them to the model_df_wide_simplified_ipcc_merged and then adding back any that are now not able to be joined:
model_df_wide_simplified_ipcc_merged_copy =model_df_wide_simplified_ipcc_merged.copy()
model_df_wide_simplified_ipcc_merged_copy = model_df_wide_simplified_ipcc_merged_copy.drop(columns=['_merge'])

bad_units = model_df_wide_simplified_ipcc_merged_copy[model_df_wide_simplified_ipcc_merged_copy['Unit'].isin(['fraction', 'dimensionless', 'g/km'])]
missing_units = model_df_wide_simplified_ipcc_merged_copy.merge(bad_units[['aperc_sector', 'aperc_fuel']].drop_duplicates(), on=['aperc_sector', 'aperc_fuel'], how='outer', indicator=True)
missing_units = missing_units[missing_units['_merge'] == 'right_only'].drop_duplicates()
model_df_wide_simplified_ipcc_merged_copy = model_df_wide_simplified_ipcc_merged_copy[~model_df_wide_simplified_ipcc_merged_copy['Unit'].isin(['fraction', 'dimensionless', 'g/km'])]
if missing_units.shape[0] > 0:
    missing_units = bad_units.merge(missing_units[['aperc_sector', 'aperc_fuel']].drop_duplicates(), on=['aperc_sector', 'aperc_fuel'], how='inner')
    model_df_wide_simplified_ipcc_merged_copy = pd.concat([model_df_wide_simplified_ipcc_merged_copy, missing_units], ignore_index=True)

    print('missing units added back, {}'.format(missing_units))

model_df_wide_simplified_ipcc_merged_new = model_df_wide_simplified_ipcc_merged_copy.copy()

#%%
#comapre the number of unique combinations of aperc_sector, aperc_fuel, to the number of rows for each unit:
unique_combinations = model_df_wide_simplified_ipcc_merged_new[['aperc_sector', 'aperc_fuel', 'Unit']].drop_duplicates()
unit_counts = unique_combinations.groupby(['Unit']).size().reset_index(name='counts')
n1 = unique_combinations[['aperc_sector', 'aperc_fuel']].drop_duplicates().shape[0]
print('number of emissions factors requried: {}'.format(n1))
print('number of emissions factors by unit: {}'.format(unit_counts))
#%%
#FOR SOME REASON THIS DIDNT WORK., SO KSIPPING FOR NOW:
DO_THIS = False
if DO_THIS:
    #order the unit counts and then one by one asdd them in by number of emission factors by unit. Once n1 == n2, then we have all the unique combinations of aperc_sector, aperc_fuel
    unit_counts = unit_counts.sort_values(by='counts', ascending=False)
    new_unique_combinations = pd.DataFrame(columns=['aperc_sector', 'aperc_fuel'])
    for unit in unit_counts['Unit']:
        added_unique_combinations = model_df_wide_simplified_ipcc_merged_new.loc[model_df_wide_simplified_ipcc_merged_new['Unit'] == unit][['aperc_sector', 'aperc_fuel']].drop_duplicates()
        if unit == 'TJ/kt':
            breakpoint()
        new_unique_combinations = pd.concat([new_unique_combinations, added_unique_combinations], ignore_index=True).drop_duplicates()
        n2 = new_unique_combinations.shape[0]
        if n1 == n2:
            break
        else:
            print(f'added {unit} to new_unique_combinations to achieve {n2} unique combinations. still need {n1-n2} more')

    remaining_combinations = new_unique_combinations.merge(unique_combinations[['aperc_sector', 'aperc_fuel']].drop_duplicates(), on=['aperc_sector', 'aperc_fuel'], how='outer', indicator=True)
    remaining_combinations = remaining_combinations[remaining_combinations['_merge'] == 'right_only']
#%%
# Group by 'Gas' and 'Unit' and count unique combinations
combinations_per_gas_unit = model_df_wide_simplified_ipcc_merged_new.groupby(['Gas', 'Unit']).apply(
    lambda df: df[['aperc_sector', 'aperc_fuel']].drop_duplicates().shape[0]
).reset_index(name='unique_combinations')

# Sort the results for better readability
combinations_per_gas_unit = combinations_per_gas_unit.sort_values(
    by='unique_combinations', ascending=False
)

# Display the results
print("Number of unique 'aperc_sector' and 'aperc_fuel' combinations per 'Gas' and 'Unit':")
print(combinations_per_gas_unit)
#maybe we could just use kg/TJ?























#%%
#in the origanal dataset for emissions factors, reprint all the unique combninations of 'IPCC 2006 Source/Sink Category', 'Fuel 2006', 'Gas'
#maybe we can map them:


new_emissions_factors_ipcc = emissions_factors_ipcc_no_regions_no_technology.copy()
new_emissions_factors_ipcc = new_emissions_factors_ipcc.loc[new_emissions_factors_ipcc['Unit'] == 'kg/TJ']
combinations = new_emissions_factors_ipcc[['IPCC 2006 Source/Sink Category', 'Fuel 2006', 'Gas']].drop_duplicates()
# print('unique combinations of IPCC 2006 Source/Sink Category, Fuel 2006, Gas:')
# print(combinations)
#ok yeah that is great!
#lets count the number of combinations of gases for each combiantion of IPCC 2006 Source/Sink Category, Fuel 2006
combinations_per_category_fuel = new_emissions_factors_ipcc.groupby(['IPCC 2006 Source/Sink Category', 'Fuel 2006']).apply(
    lambda df: df['Gas'].nunique()
).reset_index(name='unique_gases')

#seems that most of the combinations have all 3 gases. L<ets start off by trying to map each unique combo of aperc_sector, aperc_fuel to the unique combo of IPCC 2006 Source/Sink Category, Fuel 2006. then where we are missing a gas for a combo, we canm think about it:
combinations= new_emissions_factors_ipcc[['IPCC 2006 Source/Sink Category', 'Fuel 2006']].drop_duplicates()

#ok lets break it into pieces. first we'll start by crossing off the easy demand sectors (transport and residential). we will use  '1.A.1 - Energy Industries','1.A - Fuel Combustion Activities' as defaults where there is not a more szpecific sector to map to.

#%%

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
transport_combinations = new_emissions_factors_ipcc.loc[new_emissions_factors_ipcc['IPCC 2006 Source/Sink Category'].isin(['1.A.3.b - Road Transportation', '1.A.3.c - Railways', '1.A.3.d - Water-borne Navigation', '1.A.3.a - Civil Aviation',  '1.A.1 - Energy Industries','1.A - Fuel Combustion Activities'])][['IPCC 2006 Source/Sink Category', 'Fuel 2006']].drop_duplicates()
aperc_transport_combinations = [sector for sector in aperc_sectors if '15_transport_sector' in sector]

#now extract all the fuel sector combos from the model_df_wide_simplified that are in the transport_combinations    
transport_combinations_model = model_df_wide_simplified.loc[model_df_wide_simplified['aperc_sector'].isin(aperc_transport_combinations)][['aperc_sector', 'aperc_fuel']].drop_duplicates()

#    '16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x',
#    '16_other_sector$16_01_buildings$16_01_02_residential$x',
#And now same for residential:
residential_combinations = new_emissions_factors_ipcc.loc[new_emissions_factors_ipcc['IPCC 2006 Source/Sink Category'].isin(['1.A - Fuel Combustion Activities', '1.A.1 - Energy Industries', '1.A.4.a - Residential'])][['IPCC 2006 Source/Sink Category', 'Fuel 2006']].drop_duplicates()

residential_combinations_model = model_df_wide_simplified.loc[model_df_wide_simplified['aperc_sector'].isin(['16_other_sector$16_01_buildings$16_01_02_residential$x'])][['aperc_sector', 'aperc_fuel']].drop_duplicates()

aperc_industry_combinations = [sector for sector in aperc_sectors if '14_industry_sector' in sector]
services_sectors = ['16_other_sector$16_01_buildings$16_01_01_commercial_and_public_services$x']

industry_combinations = new_emissions_factors_ipcc.loc[new_emissions_factors_ipcc['IPCC 2006 Source/Sink Category'].isin(['1.A - Fuel Combustion Activities', '1.A.1 - Energy Industries', '1.A.2 - Manufacturing Industries and Construction'])][['IPCC 2006 Source/Sink Category', 'Fuel 2006']].drop_duplicates()

industry_combinations_model = model_df_wide_simplified.loc[model_df_wide_simplified['aperc_sector'].isin(aperc_industry_combinations)][['aperc_sector', 'aperc_fuel']].drop_duplicates()

services_combinations = new_emissions_factors_ipcc.loc[new_emissions_factors_ipcc['IPCC 2006 Source/Sink Category'].isin(['1.A.4.a - Commercial/Institutional', '1.A - Fuel Combustion Activities', '1.A.1 - Energy Industries'])][['IPCC 2006 Source/Sink Category', 'Fuel 2006']].drop_duplicates()
services_combinations_model = model_df_wide_simplified.loc[model_df_wide_simplified['aperc_sector'].isin(services_sectors)][['aperc_sector', 'aperc_fuel']].drop_duplicates()

aperc_transformation_combinations = [sector for sector in aperc_sectors if '09_total_transformation_sector' in sector]
transformation = new_emissions_factors_ipcc.loc[new_emissions_factors_ipcc['IPCC 2006 Source/Sink Category'].isin(['1.A - Fuel Combustion Activities', '1.A.1 - Energy Industries'])][['IPCC 2006 Source/Sink Category', 'Fuel 2006']].drop_duplicates()
transformation_combinations_model = model_df_wide_simplified.loc[model_df_wide_simplified['aperc_sector'].isin(aperc_transformation_combinations)][['aperc_sector', 'aperc_fuel']].drop_duplicates()

other = new_emissions_factors_ipcc.loc[new_emissions_factors_ipcc['IPCC 2006 Source/Sink Category'].isin(['1.A - Fuel Combustion Activities', '1.A.1 - Energy Industries', '1.A.5 - Other'])][['IPCC 2006 Source/Sink Category', 'Fuel 2006']].drop_duplicates()

completed_sectors =aperc_transformation_combinations + aperc_transport_combinations + ['16_other_sector$16_01_buildings$16_01_02_residential$x'] + aperc_industry_combinations + services_sectors
other_aperc_combinations = [sector for sector in aperc_sectors if sector not in completed_sectors]
other_combinations_model = model_df_wide_simplified.loc[model_df_wide_simplified['aperc_sector'].isin(other_aperc_combinations)][['aperc_sector', 'aperc_fuel']].drop_duplicates()
#%%
#print them out and chatgpt can help us map them:
#please note that iu had a whole lot of cahtgpt prompts but i moved them to gpt_prompts.py
#%%
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


other_mappings = {
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
    # ... (Continue with the rest of the natural gas mappings)

    # Wood/Wood Waste Mappings
    ("10_losses_and_own_use$10_01_own_use$10_01_01_electricity_chp_and_heat_plants$x", "15_solid_biomass$15_01_fuelwood_and_woodwaste"):
        ("1.A.1 - Energy Industries", "Wood/Wood Waste"),
    # ... (Continue with the rest of the wood/wood waste mappings)

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


#%%
#create a df from the mapping and then check that it maps correctly to the model_df_wide_simplified and emissions factors:
# new_transport_mapping = pd.DataFrame(transport_mapping).T.reset_index()
# new_transport_mapping.columns = [
# 'aperc_sector',	'aperc_fuel', 'ipcc_sector',	'ipcc_fuel']


# new_emissions_factors_ipcc['IPCC 2006 Source/Sink Category'].isin(['1.A.4.a - Residential'])][[

def map_sectors(mapping_df, emissions_factors_df, default_sector="1.A.1 - Energy Industries"):
    # Create a DataFrame from the mapping and then check that it maps correctly to the emissions factors
    new_mapping = pd.DataFrame(mapping_df).T.reset_index()
    new_mapping.columns = ['aperc_sector', 'aperc_fuel', 'ipcc_sector', 'ipcc_fuel']
    #check for duplicates
    duplicates = new_mapping.loc[new_mapping.duplicated()]
    if len(duplicates) > 0:
        print('Please remove these duplicates from the mapping: {}'.format(duplicates))
    # Join to emissions factor to check that these combinations do exist
    mapping_test = pd.merge(new_mapping, emissions_factors_df, how='left', 
                            left_on=['ipcc_sector', 'ipcc_fuel'], 
                            right_on=['IPCC 2006 Source/Sink Category', 'Fuel 2006'], 
                            indicator=True)
    # Identify any left_onlys
    left_onlys = mapping_test[mapping_test['_merge'] == 'left_only']

    # Try replace their sector with the default sector
    left_onlys['ipcc_sector'] = default_sector
    mapping_test = mapping_test.loc[mapping_test['_merge'] == 'both']

    mapping_test = pd.concat([mapping_test, left_onlys])
    
    # Keep only the original columns
    mapping_test = mapping_test[['aperc_sector', 'aperc_fuel', 'ipcc_sector', 'ipcc_fuel']].drop_duplicates()
    
    # Do the merge again and see how many missing values we have
    mapping_test = pd.merge(mapping_test, emissions_factors_df, how='left', 
                            left_on=['ipcc_sector', 'ipcc_fuel'], 
                            right_on=['IPCC 2006 Source/Sink Category', 'Fuel 2006'], 
                            indicator=True)
    
    #check for duplicates:
    duplicates = mapping_test.loc[mapping_test.duplicated()]
    
    left_onlys = mapping_test[mapping_test['_merge'] == 'left_only']
    if len(left_onlys) > 0:
        print(f"Warning: {len(left_onlys)} combinations are still missing from the emissions factors")
    return mapping_test, left_onlys
#%%
# Example usage:
# transport_mapping and new_emissions_factors_ipcc should be defined before calling this function
results_transport, left_onlys_transport = map_sectors(transport_mapping, new_emissions_factors_ipcc)
results_residential, left_onlys_residential = map_sectors(residential_mapping, new_emissions_factors_ipcc)
#%%
results_industry, left_onlys_industry = map_sectors(industry_mapping, new_emissions_factors_ipcc)

results_services, left_onlys_services = map_sectors(services_mappings, new_emissions_factors_ipcc)

results_transformation, left_onlys_transformation = map_sectors(transformation_mappings, new_emissions_factors_ipcc)

results_other, left_onlys_other = map_sectors(other_mappings, new_emissions_factors_ipcc)

#also create something that will check the mappings for missing sectors. i.e. check industry mapping for missing aperc_sector aperc_fuel combinations in industry_combinations_model
def check_missing_sectors(mapping_df, model_df, sector_col, fuel_col):
    
    mapping_df = pd.DataFrame(mapping_df).T.reset_index()
    mapping_df.columns = ['aperc_sector', 'aperc_fuel', 'ipcc_sector', 'ipcc_fuel']
    mapping_sectors_fuel_combos = mapping_df[[sector_col, fuel_col]].drop_duplicates()
    model_sectors_fuel_combos = model_df[[sector_col, fuel_col]].drop_duplicates()
    #merege them
    combos_merged = pd.merge(mapping_sectors_fuel_combos, model_sectors_fuel_combos, on=[sector_col, fuel_col], indicator=True)
    #extract non both rows
    combos_merged_missing = combos_merged.loc[combos_merged['_merge']!='both']
    print(f"Warning: {len(combos_merged_missing)} combinations are still missing from the model")
    return combos_merged_missing
    
combos_merged_missing_industry = missing_sectors_industry = check_missing_sectors(industry_mapping, industry_combinations_model, 'aperc_sector', 'aperc_fuel')

combos_merged_missing_services = missing_sectors_services = check_missing_sectors(services_mappings, services_combinations_model, 'aperc_sector', 'aperc_fuel')

combos_merged_missing_transformation = missing_sectors_transformation = check_missing_sectors(transformation_mappings, transformation_combinations_model, 'aperc_sector', 'aperc_fuel')

combos_merged_missing_other = missing_sectors_other = check_missing_sectors(other_mappings, other_combinations_model, 'aperc_sector', 'aperc_fuel')

combos_merged_missing_residential = missing_sectors_residential = check_missing_sectors(residential_mapping, residential_combinations_model, 'aperc_sector', 'aperc_fuel')

combos_merged_missing_transport = missing_sectors_transport = check_missing_sectors(transport_mapping, transport_combinations_model, 'aperc_sector', 'aperc_fuel')
#%%

#merge them all together
all_results = pd.concat([results_industry, results_services, results_transformation, results_other, results_residential, results_transport])
#%%
#check there are no duplicates in the aperc_sector	aperc_fuel columns
duplicates = all_results[['aperc_sector', 'aperc_fuel', 'Gas']].loc[all_results[['aperc_sector', 'aperc_fuel', 'Gas']].duplicated()]
if len(duplicates) > 0:
    print(f"Warning: {len(duplicates)} duplicates in the aperc_sector	aperc_fuel columns")

# print(duplicates)

#extrat those rows from duplicates within all_results:
duplicates_in_all_results1 = all_results.loc[all_results.duplicated()]
#extrat those rows from duplicates within all_results:
duplicates_in_all_results2 = all_results.loc[all_results[['aperc_sector', 'aperc_fuel', 'Gas']].duplicated()]#[['aperc_sector', 'aperc_fuel']]

# #we have a lot of unique Technologies / Practices in the duplicates_in_all_results2 - this si what is creating the duplicates. there are also some technolgoie swhich much higher emisisons, seemingly from differnt levels of combustion. Need to figure out how to differentiate between them.
# duplicates_in_all_results2['Technologies / Practices']

#%%




























# #join to emissions factor to check that these combinations do exist:
# new_transport_mapping_test = pd.merge(new_transport_mapping, new_emissions_factors_ipcc, how='left', left_on=['ipcc_sector', 'ipcc_fuel'], right_on=['IPCC 2006 Source/Sink Category', 'Fuel 2006'], indicator=True)
# #identify any left_onlys
# left_onlys = new_transport_mapping_test[new_transport_mapping_test['_merge'] == 'left_only']

# #try replace their sector with "1.A.1 - Energy Industries"
# left_onlys['ipcc_sector'] = "1.A.1 - Energy Industries"
# new_transport_mapping_test = new_transport_mapping_test.loc[new_transport_mapping_test['_merge'] == 'both']

# new_transport_mapping_test = pd.concat([new_transport_mapping_test, left_onlys])
# #keep only the original cols
# new_transport_mapping_test = new_transport_mapping_test[['aperc_sector', 'aperc_fuel', 'ipcc_sector', 'ipcc_fuel']]
# #do the merge again and see how many msising values we have:
# new_transport_mapping_test = pd.merge(new_transport_mapping_test, new_emissions_factors_ipcc, how='left', left_on=['ipcc_sector', 'ipcc_fuel'], right_on=['IPCC 2006 Source/Sink Category', 'Fuel 2006'], indicator=True)
# left_onlys = new_transport_mapping_test[new_transport_mapping_test['_merge'] == 'left_only']

