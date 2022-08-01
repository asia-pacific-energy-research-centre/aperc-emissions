
#Brief:
#This file takes in historical energy data from EGEDA 
#and uses IPCC emissions factors to calculate CO2 emissions from it

#please note that the emissions factors are calculated in the calc_emissions_factors.py file. but since they are unlikely to change often you can feel free to run this file without running the other first

#The code has been slimmed down a lot to simplify it, as well as a lot of comments to make it clear what is happening. Sure, the code could be written more simply, but it works.
#To do
#adjust all years so they are defined in variables so we dont need to manually change those later 
#%%
execfile("../config/config.py")#usae this to load libraries and set variables. Feel free to edit that file as you need

LATEST_EGEDA_YEAR = 2018
LATEST_EGEDA_DATA_YEAR = 2017 #normally this would be the LATEST_EGEDA_YEAR minus one since that is the latest year available in the latest availble egeda data

#%%
df_egada =  pd.read_csv("../input_data/EGEDA_{}_items.csv".format(LATEST_EGEDA_YEAR),index_col=["economy","fuel_code","year"])
IPCC_emissions_factors = pd.read_csv("../intermediate_data/IPCC_emissions_factors.csv",index_col=["fuel_code"])
#%%
#FORMAT
#make egeda energy long
df_egada = df_egada.stack().unstack(level = 2)

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
EGEDA_FC_CO2_Emissions = df_egada_Emission.copy()#its unclear what file between this and the df_egada_Emission.csv one is used so i will just save both

#%%

df_egada_Emission.to_csv("../intermediate_data/df_egada_Emission.csv",index = False)

EGEDA_FC_CO2_Emissions.to_csv("../output_data/EGEDA_{}_CO2_Emissions.csv".format(LATEST_EGEDA_YEAR),index = False)#just looking at this, there are a lot of zeros here. But this is not an issue because there are also a lot of non=zeros when you look for them!


#%%