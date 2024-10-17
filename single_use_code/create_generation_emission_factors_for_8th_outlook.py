#since the output from the 8th edition outlook is in the format that osemosys uses it can be difficult to incroporate into the emisions system. This will just handle verything within that issue before calcualting gen emission factors

#MAIN EXPLANATION:
#it will create a emissions factrors set which contains generation factors for the outlook 8th edition 

#%%
import pandas as pd
import numpy as np
import os
#%%
#if single_use_code is in the cwd then move back one
if 'single_use_code' in os.getcwd():
    os.chdir('../')
    

#emissions factors to calculate emissions:
execfile("./config/config.py")#usae this to load libraries and set variables. Feel free to edit that file as you need

#improt the data
energy_ref = pd.read_excel('input_data/00_APEC_reference_results_2022-05-16-153419.xlsx', sheet_name='UseByTechnology')
energy_cn = pd.read_excel('input_data/00_APEC_net-zero_results_2022-05-16-153553.xlsx', sheet_name='UseByTechnology')

emissions_factors = pd.read_csv('./output_data/outlook_8th_emissions_factors.csv')

#%%
#join energy ref and cn, after creating a scenario column
energy_ref = energy_ref.assign(Scenario = 'Reference')
energy_cn = energy_cn.assign(Scenario = 'Carbon Neutral')
energy = pd.concat([energy_ref, energy_cn], axis=0, ignore_index=True)
#melt the data so we have a year and vlaue column
#drop somecols
energy_tall = energy.drop(['Unnamed: 58',	'Unnamed: 59', 'TIMESLICE'], axis=1)

energy_tall = pd.melt(energy_tall, id_vars=['Scenario', 'REGION', 'TECHNOLOGY', 'FUEL'], var_name='Year', value_name='Value')

#%%
#merge the technology column to easier to read values
sector_dict = {
'POW': 'Power',
'AGR': 'Agriculture',
'BLD': 'Building',
'BNK': 'Bunkers',
'HYD': 'Hydrogen',
'IND': 'Industry',
'NE_': 'Non-energy-use',
'OWN': 'Own-use',
'PIP': 'Pipeline',
'REF': 'Refining',
'TRN': 'Transport',
'NON': 'Non-specified'}

#for each value in the tech column, grab the first three characters and use them to look up the value in the dictionary. create a new column with the correspoding value
energy_tall = energy_tall.assign(Sector = energy_tall['TECHNOLOGY'].str[:3].map(sector_dict))

#rename REGION column to economy
energy_tall = energy_tall.rename(columns={'REGION': 'Economy'})
############################################################################
#now incorporate emissions and emissions factors
#%%
#merge the outlook fuels column to the emissions factors 
energy_tall_emissionms_factors = energy_tall.merge(emissions_factors, how='left', left_on='FUEL', right_on='fuel_code')  

#drop the fuel code column
energy_tall_emissionms_factors = energy_tall_emissionms_factors.drop(['fuel_code'], axis=1)


#%%
#calculate the emissions
energy_tall_emissionms_factors['Emissions'] = energy_tall_emissionms_factors['Value'] * energy_tall_emissionms_factors['Emissions factor (MT/PJ)']
#calculate average emissions factor for electricity use per year in each economy. We will do this by calculating the average emissions from the Power sector, and dividing by the average emergy use in the power sector. Theres a few assumptions here but i think its fine. 
#first we will filter the data to just the power sector
power_sector = energy_tall_emissionms_factors[energy_tall_emissionms_factors['Sector'] == 'Power']

#remove the POW_Transmission tech as this uses a lot of energy but is not used for electricity generation (i graphed it)
power_sector = power_sector[power_sector['TECHNOLOGY'] != 'POW_Transmission']

#now we will group by economy and year and calculate the average emissions
power_sector_emissions = power_sector.groupby(['Economy', 'Year', 'Scenario']).agg({'Emissions': 'mean', 'Value': 'mean'}).reset_index()

#now we will calculate the average emissions factor
power_sector_emissions['emissions_factor'] = power_sector_emissions['Emissions'] / power_sector_emissions['Value']

power_sector_emissions['FUEL'] = '17_electricity'

#create cop[ies of the dataframe for 17_electricity_import, 17_electricity_green and 17_electricity_h2
power_sector_emissions_import = power_sector_emissions.copy()
power_sector_emissions_import['FUEL'] = '17_electricity_import'
power_sector_emissions_green = power_sector_emissions.copy()
power_sector_emissions_green['FUEL'] = '17_electricity_green'
power_sector_emissions_h2 = power_sector_emissions.copy()
power_sector_emissions_h2['FUEL'] = '17_electricity_h2'

#concat all
power_sector_emissions = pd.concat([power_sector_emissions, power_sector_emissions_import, power_sector_emissions_green, power_sector_emissions_h2])

#%%
#now we will merge the power sector emissions factors back into the main data and recalcualte emissions
energy_tall_emissionms_factors_2 = energy_tall_emissionms_factors.merge(power_sector_emissions[['Economy', 'Year', 'FUEL','emissions_factor', 'Scenario']], how='left', on=['Economy', 'Year', 'FUEL', 'Scenario'])

#if we have dont have a nan in the emissions factor column, then replace the value in Emissions factor (MT/PJ) with the value in emissions factor column
energy_tall_emissionms_factors_2['Emissions factor (MT/PJ)'] = np.where(energy_tall_emissionms_factors_2['emissions_factor'].isnull(), energy_tall_emissionms_factors_2['Emissions factor (MT/PJ)'], energy_tall_emissionms_factors_2['emissions_factor'])

#now recalculate the emissions
energy_tall_emissionms_factors_2['Emissions'] = energy_tall_emissionms_factors_2['Value'] * energy_tall_emissionms_factors_2['Emissions factor (MT/PJ)']

#%%
#remove the emissions factor and Emissions factor (MT/PJ) and TECHNOLOGY column to create a final dataframe
energy_tall_emissionms_factors_3 = energy_tall_emissionms_factors_2.drop(['emissions_factor', 'Emissions factor (MT/PJ)', 'TECHNOLOGY'], axis=1)

#%%
#extract the Emissions factor (MT/PJ) column, remove duplicates and save it as outlook_emissions_factors_with_electricity
outlook_emissions_factors_with_electricity = energy_tall_emissionms_factors_2[['Economy', 'FUEL','Scenario','Year', 'Emissions factor (MT/PJ)']].drop_duplicates()
#rename FUEL to fuel_code
outlook_emissions_factors_with_electricity = outlook_emissions_factors_with_electricity.rename(columns={'FUEL': 'fuel_code'})
#save in output_data
outlook_emissions_factors_with_electricity.to_csv('./output_data/outlook_8th_emissions_factors_with_electricity.csv', index=False)
#%%

#plot outlook_emissions_factors_with_electricity using ploty
import plotly.express as px
fig = px.line(outlook_emissions_factors_with_electricity[outlook_emissions_factors_with_electricity.fuel_code=='17_electricity'], x="Year", y="Emissions factor (MT/PJ)", color='Economy', title='Emissions factor for electricity use in the 8th edition outlook', line_dash='Scenario')
#save to html
fig.write_html("./plotting_output/outlook_8th_emissions_factors_with_electricity.html")
# %%
