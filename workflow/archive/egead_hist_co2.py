#%%
#Brief:
# 1. This notebook takes in historical energy data from EGEDA 
#and uses IPCC emissions factors to calculate CO2 emissions from it

#input data:
# 1. 

#To do
#adjust all years so they are defined in variables so we dont need to manually change those later 
#%%
import numpy as np
import pandas as pd
# import yaml
# get_ipython().run_line_magic('config', 'Completer.use_jedi = False')

LATEST_EGEDA_YEAR = 2018
LATEST_EGEDA_DATA_YEAR = 2017 #normally this would be the LATEST_EGEDA_YEAR minus one since that is the latest year available in the latest availble egeda data

#%%
#LOAD
df_egada =  pd.read_csv("../data/EGEDA_{}_items.csv".format(LATEST_EGEDA_YEAR),index_col=["economy","fuel_code","year"])
IPCC_map = pd.read_excel("../config/IPCC Methodology to EGEDA map.xlsx" , sheet_name = "MAP", header=1,usecols=["Account","Fuel type","Fuel"] 
)#this is the map between IPCC and EGEDA fuel names
IPCC_Emission = pd.read_excel("../config/IPCC Methodology to EGEDA map.xlsx", sheet_name = "Emission Factors", header=0,index_col="Fuel type ")#this is the carbon cntent of each fuel in IPCC fuel categories

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
#FORMAT
#make egeda energy long
df_egada = df_egada.stack().unstack(level = 2)

#%%
#FORMAT
#this block will join carbon contents of different fuels with their respective Fuel names, as used in EGEDA and OSEMOSYS system (i.e 6_1_crude_oil) and then format so its clean
IPCC_Emission = IPCC_Emission[["Default Carbon content(kg/GJ)"]]
IPCC_carbon_content = IPCC_map.join(IPCC_Emission,on="Fuel type").dropna()
IPCC_carbon_content= IPCC_carbon_content.set_index(['Fuel','Account'])

IPCC_carbon_content.loc[pd.IndexSlice[:,"LULUCF"],:] = 0#Effectively rmeove LULUCF from df

IPCC_carbon_content = IPCC_carbon_content.droplevel(level = 'Account', axis =0)#Remove Account column
IPCC_carbon_content.index = IPCC_carbon_content.index.rename("fuel_code")
IPCC_carbon_content = IPCC_carbon_content[["Default Carbon content(kg/GJ)"]]#Remove all cols but carbon content (kg/GJ) column and fuel code column

#%%
#OPERATION
#multiply carbon content by 3.67 to get CO2 emissions factors (One ton of carbon equals 44/12 = 11/3 = 3.67 tons of carbon dioxide).
#but why divide by 1mil. Thought it could be to go from Gj to PJ? but then im pretty sure you times by 1million to get to KG/PJ
#and then notice that below there is also df_egada_Emission["Default Carbon content(kg/GJ)"]*1000, so it essentially ends up being *1000
IPCC_Emission_factors['Emissions factor (MT/PJ)'] = IPCC_carbon_content*3.67/1000000

#%%
#FORMAT
#join the egeda energy data onto the IPCC data by Fuel_code
df_egada_and_emission_factors = df_egada.join(IPCC_Emission_factors, on = "fuel_code")

#%%
#OPERATION
#this block will calculate the CO2 emissions from the egeda energy data using the c02 emission factors we cacualted from the carbon content factors from IPCC
#why are we multiplying by 1000 here?
#it will do it for every year in egeda data.
df_egada_Emission = df_egada_and_emission_factors.mul(df_egada_and_emission_factors["Emissions factor (MT/PJ)"]*1000, axis =0).drop("Emissions factor (MT/PJ)",axis =1)

#%%
# FORMAT
#clean up the energy emissions dtf so we can export it to csv
df_egada_Emission.index.names = ['economy', 'fuel_code',"item_code_new"]#note that item_code is like the sector/and or use category of the fuel.
df_egada_Emission = df_egada_Emission.reset_index()
df_egada_Emission = df_egada_Emission.replace(np.nan,0)
EGEDA_FC_CO2_Emissions = df_egada_Emission.copy()#creeate a copy to save so we can continue to use and edit original dtf #to do, rename to more undrstandable name when you kjnow what this actually contains

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
df_egada_Emission = df_egada_Emission.loc[pd.IndexSlice[:,:,:,LATEST_EGEDA_DATA_YEAR],:].droplevel(level =-1 )

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

#is this really what is done here, because it seems the same operation is done above on line 54#or is it the calculation of emission factors
#why are we multiplying by 1000 here?
#if this is really calcualtign emissions factors, what is the point when we had the, above? 
emmsion_factoers = df_egada_Emission['emissions']/(df_egada_latest_year[LATEST_EGEDA_DATA_YEAR]*1000)

#%%
#FORMAT
emmsion_factoers = emmsion_factoers.loc[pd.IndexSlice[:,'12_total_final_consumption',:]]
emmsion_factoers = emmsion_factoers.reset_index()

#%%
#join default carbon content dtf onto the emissions dtf then clean it up
emmsion_factoers = emmsion_factoers.join(IPCC_Emission_factors, on = "fuel_code").dropna(how ="all")
emmsion_factoers = emmsion_factoers.rename(columns = {0:"Primary Emissions factor (MT/PJ)"})

#%%
#fill missing values with the Emission factor we have calculated from the IPCC data
emmsion_factoers['Emissions factor (MT/PJ)'] = emmsion_factoers['Primary Emissions factor (MT/PJ)'].fillna(emmsion_factoers["Emissions factor (MT/PJ)"])
emmsion_factoers = emmsion_factoers.set_index(["economy","fuel_code"])
emmsion_factoers = emmsion_factoers[['Emissions factor (MT/PJ)']]#assumign this is the correct units for the emission factors because it is what is used throughout APERC
emmsion_factoers = emmsion_factoers.dropna()
# emmsion_factoers = emmsion_factoers.round(decimals=1)#removed this because rounding emissions factors will result in any that arent 0 or NA going to 0 since they are all so small (need about 5 decimal places)


#%%
#SAVE
EGEDA_FC_CO2_Emissions.to_csv("../intermediate_data/EGEDA_FC_CO2_Emissions.csv",index = False)
emmsion_factoers.to_csv("../intermediate_data/emmsion_factoers.csv")

#%% FORMAT
#this was previously done after saing emmsion_factoers.csv but it wasnt used for anything so ignore it for now
# emmsion_factoers.dropna(how='all').loc["APEC"][['12_total_final_consumption']].join(IPCC_Emission_factors, on = "fuel_code")

#%%
#NONE OF THIS IS USED FOR ANYTING
# ipcc_list =  IPCC_map.reset_index().dropna()["Fuel"].tolist()

# not_in_list  = [i for i in egada_list if i not in ipcc_list]


# IPCC_Emission_factors = IPCC_map.join(IPCC_Emission,on="Fuel type")

# egada_list = EGADA_names[2018].dropna().tolist()
