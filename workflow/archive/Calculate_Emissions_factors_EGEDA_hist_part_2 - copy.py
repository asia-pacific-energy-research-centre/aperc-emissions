#this is the second half of Hughs original code for emissions factors calcualtion. I split this part out because it seemed that it was not essential. 
#I have attempted to use comments to explain whats going on, or where i am unsruew. 
#but it is not as well done as the first half of his code. I expect it should only be used if you have a hunch that you need it

#%%
import numpy as np
import pandas as pd

#%%

#DONT FORGET TO SET THIS!!!! (Since there is no central config or integrate file)
LATEST_EGEDA_YEAR = 2018
LATEST_EGEDA_DATA_YEAR = 2017 #normally this would be the LATEST_EGEDA_YEAR minus one since that is the latest year available in the latest availble egeda data
#DONT FORGET TO SET THIS!!!!

#%%

#LOAD
df_egada_Emission = pd.read_csv("../intermediate_data/df_egada_Emission.csv")

df_egada =  pd.read_csv("../input_data/EGEDA_{}_items.csv".format(LATEST_EGEDA_YEAR),index_col=["economy","fuel_code","year"])

IPCC_emissions_factors = pd.read_csv("../intermediate_data/IPCC_emissions_factors.csv")

#Define a dtf of all the fuel types and their associated general categories. ie. coal_thermal, which represents all thermal coal use.
fuel_types_mappings = pd.DataFrame(zip(["1_2_other_bituminous_coal",
                "1_3_subbituminous_coal",
                "1_4_anthracite",
                "3_peat",
                "4_peat_products",
                "6_2_natural_gas_liquids",
                "6_3_refinery_feedstocks",
                "6_4_additives_oxygenates",
                "6_5_other_hydrocarbons",
                "7_12_white_spirit_sbp",
                "7_13_lubricants",
                "7_14_bitumen",
                "7_15_paraffin_waxes",
                "7_16_petroleum_coke",
                "7_17_other_products",
                "7_4_gasoline_type_jet_fuel",
                "7_5_kerosene_type_jet_fuel",
                "2_1_coke_oven_coke",
                "2_2_coke_oven_gas",
                "2_3_blast_furnace_gas",
                "2_4_other_recovered_gases",
                "2_5_patent_fuel",
                "2_6_coal_tar",
                "2_7_bkb_pb"
                ]
                      ,[
                    "1_x_coal_thermal",
                    "1_x_coal_thermal",
                    "1_x_coal_thermal",
                    "1_x_coal_thermal",
                    "1_x_coal_thermal",
                    "6_x_ngls",
                    "6_x_ngls",
                    "6_x_ngls",
                    "6_x_ngls",
                    "7_x_other_petroleum_products",
                    "7_x_other_petroleum_products",
                    "7_x_other_petroleum_products",
                    "7_x_other_petroleum_products",
                    "7_x_other_petroleum_products",
                    "7_x_other_petroleum_products",
                    "7_x_jet_fuel",
                    "7_x_jet_fuel",
                    "2_coal_products",
                    "2_coal_products",
                    "2_coal_products",
                    "2_coal_products",
                    "2_coal_products",
                    "2_coal_products",
                    "2_coal_products"
                      ]),
               columns =['fuel_code', 'new_code'])

#%%
emmsion_factoers.reset_index()['fuel_code'].unique()
'15_1_fuelwood_and_woodwaste', '15_3_charcoal',
       '15_4_black_liquor', '15_5_other_biomass', '16_1_biogas',
       '16_2_industrial_waste', '16_3_municipal_solid_waste_renewable',
       '16_4_municipal_solid_waste_nonrenewable', '16_5_biogasoline',
       '16_6_biodiesel', '16_8_other_liquid_biofuels', '1_1_coking_coal',
       '1_2_other_bituminous_coal', '1_3_subbituminous_coal',
       '1_4_anthracite', '1_5_lignite', '2_1_coke_oven_coke',
       '2_2_coke_oven_gas', '2_3_blast_furnace_gas',
       '2_4_other_recovered_gases', '2_5_patent_fuel', '2_6_coal_tar',
       '2_7_bkb_pb', '3_peat', '4_peat_products',
       '5_oil_shale_and_oil_sands', '6_1_crude_oil',
       '6_2_natural_gas_liquids', '6_3_refinery_feedstocks',
       '6_4_additives_oxygenates', '6_5_other_hydrocarbons',
       '7_10_refinery_gas_not_liquefied', '7_11_ethane',
       '7_12_white_spirit_sbp', '7_13_lubricants', '7_14_bitumen',
       '7_15_paraffin_waxes', '7_16_petroleum_coke',
       '7_17_other_products', '7_1_motor_gasoline',
       '7_2_aviation_gasoline', '7_3_naphtha',
       '7_4_gasoline_type_jet_fuel', '7_5_kerosene_type_jet_fuel',
       '7_6_kerosene', '7_7_gas_diesel_oil', '7_8_fuel_oil', '7_9_lpg',
       '8_1_natural_gas', '8_2_lng', '8_3_gas_works_gas'
#%%
#make egeda energy long
df_egada = df_egada.stack().unstack(level = 2)
#%%
#FORMAT
#set the index of the dtf to be the fuel_code so we can join the large fuel categories dtf manually defined at the beinning of this file onto the egeda emissions dtf 
#this is so that in the next block we can calculate the CO2 emissions for each general fuel category
fuel_types_mappings = fuel_types_mappings.set_index("fuel_code")
df_egada_Emission_agg = df_egada_Emission.join(fuel_types_mappings, on = "fuel_code")
df_egada_Emission_agg = df_egada_Emission_agg.dropna()
df_egada_Emission_agg = df_egada_Emission_agg.groupby(["economy",'new_code',"item_code_new"]).sum()#sum so we now have the total emissions for each fuel category
#note that we now have also dropped the fuel_code column and replaced it with new_code, which is essentially a less detailed version of the fuel_code (see fuel_types_mappings df)

#%%
#FORMAT
df_egada_Emission = df_egada_Emission_agg.rename_axis(index ={"new_code":"fuel_code"}).reset_index()#now rename new_code to be fuel_code
df_egada_Emission = df_egada_Emission.set_index(["economy","fuel_code","item_code_new"])
df_egada_Emission = df_egada_Emission.stack().reset_index()
df_egada_Emission.columns = ["economy","fuel_code","item_code_new","year",'emissions']#rename columns, again
df_egada_Emission = df_egada_Emission.set_index(["economy","item_code_new","fuel_code","year"])#.unstack("year")
df_egada_Emission = df_egada_Emission.loc[pd.IndexSlice[:,:,:,str(LATEST_EGEDA_DATA_YEAR)],:].droplevel(level =-1 )

#%%
#go back to the energy dataframe and edit it ready to use with the emissions 
df_egada_latest_year = df_egada.rename_axis(index = {None: "item_code_new"})
df_egada_latest_year = df_egada_latest_year.filter([LATEST_EGEDA_DATA_YEAR])#filter for only 2017 data
df_egada_latest_year = df_egada_latest_year.reorder_levels([0,2,1])

#%%
#OPERATION
#this block will calculate the CO2 emissions factors using from the egeda energy data using the c02 emission factors from IPCC
#it seems this has the advantage of calculating emsisions factors per economy adn fuel category, rather than just fuel category. This allows for more detail.
#but its still egeda energy converted using ipcc emissions factors, divide by egeda energy to get ?The same number?
emmsion_factoers = df_egada_Emission['emissions']/(df_egada_latest_year[LATEST_EGEDA_DATA_YEAR]*1000)

#%%
#FORMAT
emmsion_factoers = emmsion_factoers.loc[pd.IndexSlice[:,'12_total_final_consumption',:]]
emmsion_factoers = emmsion_factoers.reset_index()

#%%
#join default carbon content dtf onto the emissions dtf then clean it up
emmsion_factoers = emmsion_factoers.merge(IPCC_emissions_factors, on = "fuel_code").dropna(how ="all")
emmsion_factoers = emmsion_factoers.rename(columns = {0:"Primary Emissions factor (MT/PJ)"})

#%%
#fill missing values with the Emission factor we have calculated from the IPCC data
emmsion_factoers['Emissions factor (MT/PJ)'] = emmsion_factoers['Primary Emissions factor (MT/PJ)'].fillna(emmsion_factoers["Emissions factor (MT/PJ)"])
emmsion_factoers = emmsion_factoers.set_index(["economy","fuel_code"])
emmsion_factoers = emmsion_factoers[['Emissions factor (MT/PJ)']]#assumign this is the correct units for the emission factors because it is what is used throughout APERC
emmsion_factoers = emmsion_factoers.dropna()
# emmsion_factoers = emmsion_factoers.round(decimals=1)#removed this because rounding emissions factors will result in any that arent 0 or NA going to 0 since they are all so small (need about 5 decimal places)

#%%

emmsion_factoers.to_csv("../intermediate_data/emmsion_factoers.csv")

#%%