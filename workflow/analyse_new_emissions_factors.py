
#load in 9th_edition_emissions_factors_PRE_CO2E_UPDATE.csv and compare the emisisons factors by fuel type to the new emissions factors. since there are a range of meisisons factors for each fuel we should probably just compare the mean and median of the emissions factors for each fuel type.
# %%

import pandas as pd
import numpy as np
import os
from datetime import datetime
import shutil
import utility_functions as utils

#load in the pre co2e update emissions factors
pre_co2e_update = pd.read_csv('../output_data/9th_edition_emissions_factors_PRE_CO2E_UPDATE.csv')
# %%
file = utils.find_most_recent_file_date_id('../output_data/', '9th_edition_emissions_factors_all_gases_simplified', RETURN_DATE_ID = False)
new_emissions_factors_ipcc = pd.read_csv(f'../output_data/{file}')

#%%
# And load in model_df_wide_original = pd.read_csv('../input_data/merged_file_energy_00_APEC_20241023.csv') to weight our new emissions factors by the energy use of each fuel type, so we can get a more accurate comparison of the emissions factors by fuel type.
model_df_wide_original = pd.read_csv('../input_data/merged_file_energy_00_APEC_20241101.csv')#'scenarios', 'economy', 'sectors', 'sub1sectors', 'sub2sectors',
#    'sub3sectors', 'sub4sectors', 'fuels', 'subfuels', 'subtotal_layout'
#drop where subtotal_layout is True
model_df_wide_original = model_df_wide_original.loc[model_df_wide_original['subtotal_layout'] == False]
#drop subtotal_results and subtoal_layout
model_df_wide_original = model_df_wide_original.drop(columns=['subtotal_layout', 'subtotal_results'])
model_df_wide_original_tall = model_df_wide_original.melt(id_vars=['scenarios', 'economy', 'sectors', 'sub1sectors', 'sub2sectors', 'sub3sectors', 'sub4sectors', 'fuels', 'subfuels'], var_name='Year', value_name='Value')

#drop year
model_df_wide_original_tall = model_df_wide_original_tall.drop(columns=['Year', 'scenarios','economy'])

#average out over all the years
model_df_wide_original_tall = model_df_wide_original_tall.groupby(['sectors', 'sub1sectors', 'sub2sectors', 'sub3sectors','sub4sectors', 'fuels', 'subfuels']).mean().reset_index()

#%%
# pre_co2e_update.columns
# Index(['fuel_code', 'Emissions factor (MT/PJ)'], dtype='object'
#%%
# new_emissions_factors_ipcc.columns
# Index(['Unit', 'Gas', 'CO2e emissions factor', 'sectors', 'sub1sectors',
#        'sub2sectors', 'sub3sectors', 'sub4sectors', 'fuels', 'subfuels',
#        'Sector not applicable', 'Fuel not applicable',
#        'No expected energy use'],
#       dtype='object')
#drop where CO2e emissions factor is na.
new_emissions_factors_ipcc = new_emissions_factors_ipcc.dropna(subset=['CO2e emissions factor'])
#and drop where woe of 'Sector not applicable', 'Fuel not applicable',
#        'No expected energy use' is True
new_emissions_factors_ipcc = new_emissions_factors_ipcc[new_emissions_factors_ipcc['Sector not applicable'] == False]
new_emissions_factors_ipcc = new_emissions_factors_ipcc[new_emissions_factors_ipcc['Fuel not applicable'] == False]
new_emissions_factors_ipcc = new_emissions_factors_ipcc[new_emissions_factors_ipcc['No expected energy use'] == False]

new_emissions_factors_ipcc_copy = new_emissions_factors_ipcc.copy()
#and get wher the Gas is CARBON DIOXIDE
new_emissions_factors_ipcc = new_emissions_factors_ipcc.loc[new_emissions_factors_ipcc['Gas'] == 'CARBON DIOXIDE']
#calcualte weighted average emissions factor by fuel type as well as the mean and median emissions factor by fuel type.
new_emissions_factors_ipcc_weighted = new_emissions_factors_ipcc.copy()
new_emissions_factors_ipcc_weighted = pd.merge(new_emissions_factors_ipcc_weighted, model_df_wide_original_tall, on=['sectors', 'sub1sectors', 'sub2sectors', 'sub3sectors','sub4sectors', 'fuels', 'subfuels'], how='left')

new_emissions_factors_ipcc_weighted['Weighted emissions factor'] = new_emissions_factors_ipcc_weighted['CO2e emissions factor'] * new_emissions_factors_ipcc_weighted['Value']
new_emissions_factors_ipcc_weighted = new_emissions_factors_ipcc_weighted.groupby(['fuels', 'subfuels']).agg({'Weighted emissions factor': 'sum', 'Value': 'sum'}).reset_index()
new_emissions_factors_ipcc_weighted['Weighted emissions factor'] = new_emissions_factors_ipcc_weighted['Weighted emissions factor'] / new_emissions_factors_ipcc_weighted['Value']
new_emissions_factors_ipcc_weighted = new_emissions_factors_ipcc_weighted.drop(columns=['Value'])
#now we ahve to melt subfuels into fuels col so that it can be compared to the pre_co2e_update df
new_emissions_factors_ipcc_weighted_melt = new_emissions_factors_ipcc_weighted.melt(id_vars=['Weighted emissions factor'], value_vars=['fuels', 'subfuels'], var_name='x', value_name='fuel')
#DROP x
new_emissions_factors_ipcc_weighted_melt = new_emissions_factors_ipcc_weighted_melt.drop(columns=['x'])
#average each fuel type
new_emissions_factors_ipcc_weighted_melt = new_emissions_factors_ipcc_weighted_melt.groupby('fuel').mean().reset_index()
#and drop where fuel =  x as well 
new_emissions_factors_ipcc_weighted_melt = new_emissions_factors_ipcc_weighted_melt.loc[new_emissions_factors_ipcc_weighted_melt['fuel'] != 'x']

#%%
######
#and calc the mean. we will first have to melt the subfuels into fuels so that we can compare it to the pre_co2e_update df
new_emissions_factors_ipcc_mean = new_emissions_factors_ipcc.copy()
new_emissions_factors_ipcc_mean = new_emissions_factors_ipcc_mean[['CO2e emissions factor', 'fuels', 'subfuels']]
#melt
new_emissions_factors_ipcc_mean = new_emissions_factors_ipcc_mean.melt(id_vars=['CO2e emissions factor'], value_vars=['fuels', 'subfuels'], var_name='x', value_name='fuel')
#drop x
new_emissions_factors_ipcc_mean = new_emissions_factors_ipcc_mean.drop(columns=['x'])
#average each fuel type
new_emissions_factors_ipcc_mean = new_emissions_factors_ipcc_mean.groupby(['fuel']).mean().reset_index()
#drop x
new_emissions_factors_ipcc_mean = new_emissions_factors_ipcc_mean.loc[new_emissions_factors_ipcc_mean['fuel'] != 'x']

##########
#and calc median
new_emissions_factors_ipcc_median = new_emissions_factors_ipcc.copy()
new_emissions_factors_ipcc_median = new_emissions_factors_ipcc_median[['CO2e emissions factor', 'fuels', 'subfuels']]
#melt
new_emissions_factors_ipcc_median = new_emissions_factors_ipcc_median.melt(id_vars=['CO2e emissions factor'], value_vars=['fuels', 'subfuels'], var_name='x', value_name='fuel')
#drop x
new_emissions_factors_ipcc_median = new_emissions_factors_ipcc_median.drop(columns=['x'])
#average each fuel type
new_emissions_factors_ipcc_median = new_emissions_factors_ipcc_median.groupby(['fuel']).median().reset_index()
#drop x
new_emissions_factors_ipcc_median = new_emissions_factors_ipcc_median.loc[new_emissions_factors_ipcc_median['fuel'] != 'x']
########
#rename value col in each df
new_emissions_factors_ipcc_median.rename(columns={'CO2e emissions factor': 'median'}, inplace=True)
new_emissions_factors_ipcc_mean.rename(columns={'CO2e emissions factor': 'mean'}, inplace=True)
new_emissions_factors_ipcc_weighted_melt.rename(columns={'Weighted emissions factor': 'weighted'}, inplace=True)
#merge them
new_emissions_factors_ipcc_comparison = pd.merge(new_emissions_factors_ipcc_mean, new_emissions_factors_ipcc_median, on='fuel', how='outer')
new_emissions_factors_ipcc_comparison = pd.merge(new_emissions_factors_ipcc_comparison, new_emissions_factors_ipcc_weighted_melt, on='fuel', how='outer')
# # %%
#%%
#rename pre_co2e_update value col to 'pre_co2e_update emissions factor'
pre_co2e_update.rename(columns={'Emissions factor (MT/PJ)': 'pre_co2e_update emissions factor'}, inplace=True)
#merge the two dataframes on fuel_code and fuel, and then fuel code and subfuels to get the emissions factors for the same fuel types.
merged_emissions_factors = pd.merge(pre_co2e_update, new_emissions_factors_ipcc_comparison, left_on='fuel_code', right_on='fuel', how='outer', indicator=True)

#identify number of new and old emissions factors
new_emissions_factors = merged_emissions_factors.loc[merged_emissions_factors['_merge'] == 'right_only']
old_emissions_factors = merged_emissions_factors.loc[merged_emissions_factors['_merge'] == 'left_only']
both_emissions_factors = merged_emissions_factors.loc[merged_emissions_factors['_merge'] == 'both']
print(f'There are {len(new_emissions_factors)} new emissions factors and {len(old_emissions_factors)} old emissions factors that dont match. There are {len(both_emissions_factors)} that are in both the new and old emissions factors fuels sets.')

#%%
#drop the merge col
merged_emissions_factors = merged_emissions_factors.drop(columns=['_merge'])
#now metl all values into one and then cahrt them using a column chart with x axis = fuel and y axis = emissions factor
#first, where fuel is na, replace with fuel_code:
merged_emissions_factors['fuel'] = merged_emissions_factors['fuel'].fillna(merged_emissions_factors['fuel_code'])
merged_emissions_factors.drop(columns=['fuel_code'], inplace=True)
merged_emissions_factors = merged_emissions_factors.melt(id_vars=['fuel'], var_name='emissions factor measure', value_name='emissions factor')

#order them by fuel 
merged_emissions_factors = merged_emissions_factors.sort_values(by='fuel')


# %%
#plot the emissions factors for each fuel type using plotly express
import plotly.express as px
#make teh bars side by side rather than stacked
fig = px.bar(merged_emissions_factors, x='fuel', y='emissions factor', color='emissions factor measure', title='Emissions factors by fuel type before and after CO2e update', barmode='group')
fig.write_html('../plotting_output/emissions_factors_by_fuel_type_before_and_after_CO2e_update.html')
#%%

#lets also plot the new eeissions factors for each gas. put them on a faceted plot with independent axes and use a strip plot to show how they are distributed.
new_emissions_factors_ipcc_gas = new_emissions_factors_ipcc_copy.copy()
new_emissions_factors_ipcc_gas = new_emissions_factors_ipcc_gas[['CO2e emissions factor','Gas', 'fuels', 'subfuels', 'sectors',	'sub1sectors', 'sub2sectors', 'sub3sectors', 'sub4sectors', 'GWP_type']]

#add together the sectors and subsectors
new_emissions_factors_ipcc_gas['_sectors'] = new_emissions_factors_ipcc_gas['sectors']
new_emissions_factors_ipcc_gas['sectors'] = new_emissions_factors_ipcc_gas['sectors'] + ' ' + new_emissions_factors_ipcc_gas['sub1sectors']
new_emissions_factors_ipcc_gas = new_emissions_factors_ipcc_gas.drop(columns=['sub1sectors'])
for GWP_type in new_emissions_factors_ipcc_gas['GWP_type'].unique():
    #create a unique plot for this fuel. we will add them all to one dashboard afterwards:
    data  = new_emissions_factors_ipcc_gas.loc[new_emissions_factors_ipcc_gas['GWP_type'] == GWP_type]
    fig = px.strip(data, x='fuels', y='CO2e emissions factor', facet_row='Gas', title=f'Emissions factors by gas and sector (GWP type: {GWP_type})', hover_data=['subfuels','sub2sectors', 'sub3sectors', 'sub4sectors'], color='_sectors')
    fig = fig.update_traces(marker=dict(size=4))
    fig = fig.update_layout(showlegend=False)
    fig.update_yaxes(matches=None)
    fig.for_each_yaxis(lambda yaxis: yaxis.update(showticklabels=True))
    fig.write_html(f'../plotting_output/emissions_factors_by_gas_and_sector_STRIP_{GWP_type}.html')
    
# fig = px.strip(new_emissions_factors_ipcc_gas, x='fuels', y='CO2e emissions factor', facet_row='Gas', title='Emissions factors by gas and sector', hover_data=['subfuels','sub2sectors', 'sub3sectors', 'sub4sectors'], color='_sectors')
#make the dots smaller
fig = fig.update_traces(marker=dict(size=4))
fig = fig.update_layout(showlegend=False)

fig.update_yaxes(matches=None)
fig.for_each_yaxis(lambda yaxis: yaxis.update(showticklabels=True))
fig.write_html('../plotting_output/emissions_factors_by_gas_and_sector_STRIP.html')

#%%
#and lastly to show the average emissions factor for each gas and gwp type, we will create a bar chart:

avg_emissions_factors_by_gas = new_emissions_factors_ipcc_gas.groupby(['Gas', 'fuels', 'GWP_type']).mean(numeric_only=True).reset_index()

fig = px.bar(avg_emissions_factors_by_gas, x='fuels', y='CO2e emissions factor', color='Gas', title='Average emissions factors by gas and fuel type \n(CO2e)', barmode='group', facet_row='GWP_type', facet_col_wrap=3)
fig.write_html('../plotting_output/average_emissions_factors_by_gas_GWP_and_fuel_type_BAR.html')

#%%

# #they all look pretty similar. so lets now create a set of boxplots where the fuel is the samebetween the two dataframes. we will use the original emissions factors and hsow all of the emissions factors for each fuel type in a boxplot, with the old ones highlighted in red and the new ones in blue.

# boxplot1 = pre_co2e_update.copy()
# boxplot1= boxplot1[boxplot1['pre_co2e_update emissions factor']!=0]

# boxplot2 = new_emissions_factors_ipcc.copy()
# #melt fuels and fuel while removing nonnecessary cols
# boxplot2 = boxplot2[['CO2e emissions factor', 'fuels', 'subfuels', 'sectors',	'sub1sectors']]
# boxplot2['sectors'] = boxplot2['sectors'] + ' ' + boxplot2['sub1sectors']
# boxplot2 = boxplot2.drop(columns=['sub1sectors'])
# boxplot2 = boxplot2.melt(id_vars=['CO2e emissions factor', 'sectors'], value_vars=['fuels', 'subfuels'], var_name='x', value_name='fuel')
# boxplot2 = boxplot2.drop(columns=['x'])
# boxplot2 = boxplot2.loc[boxplot2['fuel'] != 'x']
# boxplot2= boxplot2[boxplot2['CO2e emissions factor']!=0]
# #rename 
# boxplot2.rename(columns={'CO2e emissions factor': 'emissions factor'}, inplace=True)
# boxplot1.rename(columns={'pre_co2e_update emissions factor': 'emissions factor', 'fuel_code': 'fuel'}, inplace=True)
# #create measure col
# boxplot1['measure'] = 'old emissions factor'
# boxplot2['measure'] = 'new emissions factor'
# #merge the two dataframes
# boxplot_merged = pd.concat([boxplot1, boxplot2])

# #create a goruping of fuels so we can facet them by type:
# # array(['01_coal', '01_x_thermal_coal', '02_coal_products',
# #        '01_01_coking_coal', '01_05_lignite', '03_peat',
# #        '04_peat_products', '05_oil_shale_and_oil_sands',
# #        '06_crude_oil_and_ngl', '06_01_crude_oil',
# #        '06_02_natural_gas_liquids', '06_x_other_hydrocarbons',
# #        '07_petroleum_products', '07_x_other_petroleum_products',
# #        '07_01_motor_gasoline', '07_02_aviation_gasoline', '07_03_naphtha',
# #        '07_x_jet_fuel', '07_06_kerosene', '07_07_gas_diesel_oil',
# #        '07_08_fuel_oil', '07_09_lpg', '07_10_refinery_gas_not_liquefied',
# #        '07_11_ethane', '08_gas', '08_01_natural_gas', '08_02_lng',
# #        '08_03_gas_works_gas', '16_02_industrial_waste',
# #        '16_04_municipal_solid_waste_nonrenewable', '16_others',
# #        '15_solid_biomass', '17_x_green_electricity',
# #        '16_08_other_liquid_biofuels', '15_01_fuelwood_and_woodwaste',
# #        '15_02_bagasse', '15_03_charcoal', '15_05_other_biomass',
# #        '16_01_biogas', '16_03_municipal_solid_waste_renewable',
# #        '16_05_biogasoline', '16_06_biodiesel', '15_04_black_liquor',
# #        '16_07_bio_jet_kerosene'], dtype=object)
# #we will gorup them into things like coal, oil, gas, biomass, waste, other
# fuel_grouping = {'01_coal': 'coal', '01_x_thermal_coal': 'coal', '02_coal_products': 'coal', '01_01_coking_coal': 'coal', '01_05_lignite': 'coal', '03_peat': 'coal',
#         '04_peat_products': 'coal', '05_oil_shale_and_oil_sands': 'oil',
#         '06_crude_oil_and_ngl': 'oil', '06_01_crude_oil': 'oil',
#         '06_02_natural_gas_liquids': 'oil', '06_x_other_hydrocarbons': 'oil',
#         '07_petroleum_products': 'oil', '07_x_other_petroleum_products': 'oil',
#         '07_01_motor_gasoline': 'oil', '07_02_aviation_gasoline': 'oil', '07_03_naphtha': 'oil',
#         '07_x_jet_fuel': 'oil', '07_06_kerosene': 'oil', '07_07_gas_diesel_oil': 'oil',
#         '07_08_fuel_oil': 'oil', '07_09_lpg': 'oil', '07_10_refinery_gas_not_liquefied': 'oil',
#         '07_11_ethane': 'oil', '08_gas': 'gas', '08_01_natural_gas': 'gas', '08_02_lng': 'gas',
#         '08_03_gas_works_gas': 'gas', '16_02_industrial_waste': 'waste',
#         '16_04_municipal_solid_waste_nonrenewable': 'waste', '16_others': 'waste',
#         '15_solid_biomass': 'biomass', '17_x_green_electricity': 'other',
#         '16_08_other_liquid_biofuels': 'biomass', '15_01_fuelwood_and_woodwaste': 'biomass', '15_02_bagasse': 'biomass', '15_03_charcoal': 'biomass', '15_05_other_biomass': 'biomass', '16_01_biogas': 'biomass', '16_03_municipal_solid_waste_renewable': 'biomass', '16_05_biogasoline': 'biomass', '16_06_biodiesel': 'biomass', '15_04_black_liquor': 'biomass', '16_07_bio_jet_kerosene': 'biomass'} 
# #check fr any missing fuels
# missing_fuels = set(boxplot_merged['fuel']) - set(fuel_grouping.keys())
# if len(missing_fuels) > 0:
#     print(f'The following fuels are missing from the fuel grouping: {missing_fuels}')
# #apply the fuel grouping
# boxplot_merged['fuel_group'] = boxplot_merged['fuel'].map(fuel_grouping)

# #%%
# #create a dahsboard of many boxplots

# for fuel_group in fuel_grouping.values():
#     #create a unique plot for this fuel. we will add them all to one dashboard afterwards:
#     data  = boxplot_merged.loc[boxplot_merged['fuel_group'] == fuel_group]
#     fig = px.strip(data, x='fuel', y='emissions factor', color='measure', title=f'Emissions factors for {fuel_group}', hover_data=['fuel', 'sector', 'emissions factor'])
#     fig = fig.update_layout(showlegend=False)
#     fig.write_html(f'../plotting_output/emissions_factors_boxplot_{fuel_group}.html')
    

# %%