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

LATEST_EGEDA_YEAR = 2018
LATEST_EGEDA_DATA_YEAR = 2017 #normally this would be the LATEST_EGEDA_YEAR minus one since that is the latest year available in the latest availble egeda data

#%%
#LOAD
df_egada =  pd.read_csv("../input_data/EGEDA_{}_items.csv".format(LATEST_EGEDA_YEAR),index_col=["economy","fuel_code","year"])
IPCC_map = pd.read_excel("../config/IPCC Methodology to EGEDA map.xlsx" , sheet_name = "MAP", header=1,usecols=["Account","Fuel type","Fuel"] 
)#this is the map between IPCC and EGEDA fuel names
IPCC_Emission = pd.read_excel("../config/IPCC Methodology to EGEDA map.xlsx", sheet_name = "Emission Factors", header=0,index_col="Fuel type ")#this is the carbon cntent of each fuel in IPCC fuel categories

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
IPCC_emissions_factors = IPCC_carbon_content.copy()

#multiply carbon content by 3.67 to get CO2 emissions factors (One ton of carbon equals 44/12 = 11/3 = 3.67 tons of carbon dioxide).
#NOTE i change dthis to be divided by 1000 because hugh normlly would divde by 1mill and then times by 1000 later for some reason.
IPCC_emissions_factors['Emissions factor (MT/PJ)'] = IPCC_emissions_factors*3.67/1000
IPCC_emissions_factors.drop(columns=['Default Carbon content(kg/GJ)'],inplace=True)
#%%
#FORMAT
#join the egeda energy data onto the IPCC data by Fuel_code
df_egada_and_emission_factors = df_egada.join(IPCC_emissions_factors, on = "fuel_code")

#%%
#OPERATION
#this block will calculate the CO2 emissions from the egeda energy data using the c02 emission factors we cacualted from the carbon content factors from IPCC
#it will do it for every year in egeda data.
df_egada_Emission = df_egada_and_emission_factors.mul(df_egada_and_emission_factors["Emissions factor (MT/PJ)"], axis =0).drop("Emissions factor (MT/PJ)",axis =1)

#%%
# FORMAT
#clean up the energy emissions dtf so we can export it to csv
df_egada_Emission.index.names = ['economy', 'fuel_code',"item_code_new"]#note that item_code is like the sector/and or use category of the fuel.
df_egada_Emission = df_egada_Emission.reset_index()
df_egada_Emission = df_egada_Emission.replace(np.nan,0)
df_egada_Emission.insert(3, 'Unit', "MT")
EGEDA_FC_CO2_Emissions = df_egada_Emission.copy()#creeate a copy to save so we can continue to use and edit original dtf #to do, rename to more undrstandable name when you kjnow what this actually contains

#%%
#SAVE
IPCC_emissions_factors.to_csv("../intermediate_data/IPCC_emissions_factors.csv")
df_egada_Emission.to_csv("../intermediate_data/df_egada_Emission.csv",index = False)
EGEDA_FC_CO2_Emissions.to_csv("../output_data/EGEDA_{}_CO2_Emissions.csv".format(LATEST_EGEDA_YEAR),index = False)#just looking at this, there are a lot of zeros here. But this is not an issue because there are also a lot of non=zeros when you look for them!

#%%