#this is the finalised version for extracting data from the ipcc full dataset on energy emission factors. We had a much more messy script before, but this is a bit nicer ..  although nothing that i would want to show off to anyone!
#chances are that the process is still valid - i dont see us changing the way we strucutre our outlook data, but we very likely will have new sectors and fuel combinations. So you will need to run this again and check the outputs so taht you can update the mappings. -  also update the gwp's and emissions factors inputs if this is a while aftr 10/17/2024 - they might have been updated.
#also please note that the gpt_prompts_extract_data_from_all_ipcc_data.py file is not really a script but an input for this script. it contains all the prompts and mappings that i used to get the data from chatgpt. i have left it in here so that you can see what i did, as wella s import and udpate the mappings when you need to.
#%%
import pandas as pd
import numpy as np
import os
model_df_wide_original = pd.read_csv('../input_data/model_df_wide_tgt_20241018.csv')
emissions_factors_ipcc = pd.read_csv('../input_data/EFDB_output (all unfcc energy sector emissions factors).csv')#this was downlaoded from here https://www.ipcc-nggip.iges.or.jp/EFDB/find_ef.php?ipcc_code=1&ipcc_level=0 < that is, the ipccc emissions factors database for the IPCC 2006 category: 1 - Energy.

gwp_dict = {'CO2': 1, 'CH4': 32, 'N2O': 298}# https://chatgpt.com/share/6710a2c2-50e0-8000-8234-70d171ee9ed4 - why i have these values
#then print all the unique values in the IPCC 2006 Source/Sink Category column and map them to all the unique vategories in the model_df_wide['sectors'] column < we might ahve to create a concat of all the subsectors columns in mdoel_df_wide to get more precise mappings
#%%
#%%
############################
#firrst set up the model_df_wide df to make it easier to work with:
############################
#we will concat all the column ['sectors', 'sub1sectors', 'sub2sectors', 'sub3sectors', 'sub4sectors'] to get a more precise mapping, using $ as a separator. Then we can print the list of unique values ready to be input to chatgpt. we will ask chat gpt to create a mapping of these to the most specific ipcc sectors in 1.A and 1.B, separately. Where there are multiple options of the same specificity, we will ask chatgpt to provide a list of the most likely options.
model_df_wide=model_df_wide_original.copy()
model_df_wide['aperc_sector'] = model_df_wide['sectors'] + '$' + model_df_wide['sub1sectors'] + '$' + model_df_wide['sub2sectors'] + '$' + model_df_wide['sub3sectors'] 

#we also dont need most  of the cols so lets drop them and any duplicates:
model_df_wide = model_df_wide[['sectors', 'sub1sectors', 'sub2sectors', 'sub3sectors', 'sub4sectors', 'fuels', 'subfuels', 'aperc_sector']].drop_duplicates()
        
#now we need to do the same but for fuels. We will get a list of the fuels in each df and then map them. we MIGHT have a few fuels on each side of the mapping that mathc up, thats ok. we might also be missing fuels depending on the sector. we will work that out later.
model_df_wide['aperc_fuel']=model_df_wide['fuels']+'$'+model_df_wide['subfuels']

model_df_wide_original_wide_copy = model_df_wide.copy()
#%%

# %%
#we also hvae a lot of instances where we have combinations of aperc_sectors and aperc_fuels that simply arent likely. So we will remove them by removing any where the sum of energy values across all years is 0:

model_df_wide_invalid_rows = model_df_wide_original.copy()

model_df_wide_invalid_rows['aperc_sector'] = model_df_wide_invalid_rows['sectors'] + '$' + model_df_wide_invalid_rows['sub1sectors'] + '$' + model_df_wide_invalid_rows['sub2sectors'] + '$' + model_df_wide_invalid_rows['sub3sectors']
model_df_wide_invalid_rows['aperc_fuel'] = model_df_wide_invalid_rows['fuels'] + '$' + model_df_wide_invalid_rows['subfuels']

model_df_wide_invalid_rows = model_df_wide_invalid_rows.drop(columns=['sectors', 'sub1sectors', 'sub2sectors', 'sub3sectors', 'fuels', 'subfuels', 'is_subtotal', 'sub4sectors', 'scenarios', 'economy'])

#melt 
model_df_wide_invalid_rows = model_df_wide_invalid_rows.melt(id_vars=['aperc_sector', 'aperc_fuel'], var_name='year', value_name='value')
#set all values that are na to 0:
model_df_wide_invalid_rows['value'] = model_df_wide_invalid_rows['value'].fillna(0)
#calc the sum of value
model_df_wide_invalid_rows['sum_value'] = model_df_wide_invalid_rows.groupby(['aperc_sector', 'aperc_fuel'])['value'].transform('sum')

model_df_wide_invalid_rows_copy = model_df_wide_invalid_rows.copy()
#%%
#keep only row where value is 0 
model_df_wide_invalid_rows = model_df_wide_invalid_rows[model_df_wide_invalid_rows['sum_value'] == 0]
valid_rows = model_df_wide_invalid_rows_copy[model_df_wide_invalid_rows_copy['sum_value'] != 0][['aperc_sector', 'aperc_fuel', 'sum_value']].drop_duplicates()
model_df_wide_invalid_rows=model_df_wide_invalid_rows[['aperc_sector', 'aperc_fuel']].drop_duplicates()

#for some reason we are missing data for all of '16_01_01_commercial_and_public_services', '16_01_02_residential'. we dont want to drop them so remove any rows which contain them in their aperc_sector col:
model_df_wide_invalid_rows = model_df_wide_invalid_rows.loc[~model_df_wide_invalid_rows.aperc_sector.str.contains('16_01_01_commercial_and_public_services')]
model_df_wide_invalid_rows = model_df_wide_invalid_rows.loc[~model_df_wide_invalid_rows.aperc_sector.str.contains('16_01_02_residential')]

#drop those from the model_df_wide_simplified df
model_df_wide_simplified_old = model_df_wide.copy()

model_df_wide_simplified = model_df_wide.merge(model_df_wide_invalid_rows, on=['aperc_sector', 'aperc_fuel'], how='left', indicator=True)
#drop rows where aperc_sector and	aperc_fuel is not na
#%%
previous_row_number=len(model_df_wide_simplified)
dropped_rows = model_df_wide_simplified[model_df_wide_simplified['_merge'] == 'both']

model_df_wide_simplified = model_df_wide_simplified[model_df_wide_simplified['_merge'] =='left_only']
print('dropped {} rows'.format(previous_row_number-len(model_df_wide_simplified)))
print('dropped rows: {}'.format(dropped_rows))
#%%

zero_emissions_fuels = [
    '09_nuclear$x',
    '10_hydro$x',
    '11_geothermal$x',
    '12_solar$12_01_of_which_photovoltaics',
    '12_solar$12_x_other_solar',
    '12_solar$x',
    '13_tide_wave_ocean$x',
    '14_wind$x',
    '16_others$16_09_other_sources',
    '16_others$16_x_ammonia',
    '16_others$16_x_efuel',
    '16_others$16_x_hydrogen',
    '16_others$x',
    '17_electricity$x',
    '18_heat$x',
    '19_total$x',
    '20_total_renewables$x',
    '21_modern_renewables$x'
]
not_applicable_sectors = [
    '01_production$x$x$x',
    '02_imports$x$x$x',
    '03_exports$x$x$x',
    '06_stock_changes$x$x$x',
    '07_total_primary_energy_supply$x$x$x',
    '08_transfers$x$x$x',
    '11_statistical_discrepancy$x$x$x',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_01_coal_power$18_01_01_01_subcritical',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_01_coal_power$18_01_01_02_superultracritical',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_01_coal_power$18_01_01_03_advultracritical',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_01_coal_power$18_01_01_04_ccs',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_02_gas_power$18_01_02_01_gasturbine',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_02_gas_power$18_01_02_02_combinedcycle',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_02_gas_power$18_01_02_03_ccs',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_03_oil$x',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_04_nuclear$x',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_05_hydro$18_01_05_01_large',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_05_hydro$18_01_05_02_mediumsmall',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_05_hydro$18_01_05_03_pump',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_06_biomass$x',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_07_geothermal$x',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_08_solar$18_01_08_01_utility',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_08_solar$18_01_08_02_rooftop',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_08_solar$18_01_08_03_csp',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_09_wind$18_01_09_01_onshore',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_09_wind$18_01_09_02_offshore',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_10_otherrenewable$x',
    '19_heat_output_in_pj$19_01_chp_plants$19_01_01_coal$x',
    '19_heat_output_in_pj$19_01_chp_plants$19_01_02_gas$x',
    '19_heat_output_in_pj$19_01_chp_plants$19_01_03_oil$x',
    '19_heat_output_in_pj$19_01_chp_plants$19_01_04_biomass$x',
    '19_heat_output_in_pj$19_02_heat_plants$19_02_01_coal$x',
    '19_heat_output_in_pj$19_02_heat_plants$19_02_02_gas$x',
    '19_heat_output_in_pj$19_02_heat_plants$19_02_03_oil$x',
    '19_heat_output_in_pj$19_02_heat_plants$19_02_04_biomass$x',
    '19_heat_output_in_pj$x$x$x',
    '08_transfers$08_02_interproduct_transfers$x$x',
    '08_transfers$08_03_products_transferred$x$x',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_01_coal_power$x',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_02_gas_power$x',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_05_hydro$x',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_08_solar$x',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_09_wind$x',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_11_otherfuel$x',
    '18_electricity_output_in_gwh$18_01_electricity_plants$18_01_12_storage$x',
    '18_electricity_output_in_gwh$18_01_electricity_plants$x$x',
    '18_electricity_output_in_gwh$18_02_chp_plants$18_02_01_coal$x',
    '18_electricity_output_in_gwh$18_02_chp_plants$18_02_02_gas$x',
    '18_electricity_output_in_gwh$18_02_chp_plants$18_02_03_oil$x',
    '18_electricity_output_in_gwh$18_02_chp_plants$18_02_04_biomass$x',
    '18_electricity_output_in_gwh$18_02_chp_plants$x$x',
    '18_electricity_output_in_gwh$x$x$x',
    '19_heat_output_in_pj$19_01_chp_plants$x$x',
    '19_heat_output_in_pj$19_02_heat_plants$x$x',
]

#%%
model_df_wide_copy = model_df_wide_simplified.copy()
#drop rows where the fuel is zero emissions
model_df_wide_simplified = model_df_wide_simplified[~model_df_wide_simplified['aperc_fuel'].isin([fuel for fuel in zero_emissions_fuels])]
model_df_wide_simplified = model_df_wide_simplified[~model_df_wide_simplified['aperc_sector'].isin([sector for sector in not_applicable_sectors])]
#%%

############################
#now format the emissions factors:
############################
#replace rows that contain Natural Gas Liquids\n(NGLs) with Natural Gas Liquids (NGLs)
emissions_factors_ipcc['Fuel 2006'] = emissions_factors_ipcc['Fuel 2006'].str.replace('Natural Gas Liquids\n(NGLs)', 'Natural Gas Liquids (NGLs)')
#and renaame 1.A.4.b - Residential\n1.A.4.c.i - Stationary to 1.A.4.b - Residential
emissions_factors_ipcc['IPCC 2006 Source/Sink Category'] = emissions_factors_ipcc['IPCC 2006 Source/Sink Category'].str.replace('1.A.4.b - Residential\n1.A.4.c.i - Stationary', '1.A.4.b - Residential')
#SHRINK THE SIZE OF BOTHJ DATAFRAMES TO MAKE IT EASIER TO WORK WITH:

#WE DECIDED EARLY ON THAT WE SHOULD REMOVE MAPPINGS TO ROWS WEHRE THE FACTOR WAS ONLY AVAILABLE FOR A CERTAIN REGION AND INSTEAD TAKE A LESS SPECIFIC SECTOR. THS JUST REDUCES COMPLEXITY.
emissions_factors_ipcc_no_regions = emissions_factors_ipcc[emissions_factors_ipcc['Region / Regional Conditions'].isna()]

#also we found that specifications by technology were not useful since we dont measure by technology. So we will remove those rows and keep only where Technologies / Practice is na
emissions_factors_ipcc_no_regions_no_technology = emissions_factors_ipcc_no_regions[emissions_factors_ipcc_no_regions['Technologies / Practices'].isna()]


#we will need to filter for the data which has the units KG/TJ > im pretty sure this will have all we need
emissions_factors_ipcc_no_regions_no_technology = emissions_factors_ipcc_no_regions_no_technology[emissions_factors_ipcc_no_regions_no_technology['Unit'] == 'kg/TJ']


#%%
############################
#NOW START PROCESSING
############################


#%%
#in the origanal dataset for emissions factors, reprint all the unique combninations of 'IPCC 2006 Source/Sink Category', 'Fuel 2006', 'Gas'
#maybe we can map them:


new_emissions_factors_ipcc = emissions_factors_ipcc_no_regions_no_technology.copy()
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

#please note that i put all the mappings below into a file called gpt_prompts.py to save space here.
#%%

aperc_sectors = model_df_wide['aperc_sector'].unique()

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
#please note that iu had a whole lot of cahtgpt prompts and mappings here but i moved them to gpt_prompts.py
import gpt_prompts_extract_data_from_all_ipcc_data as gpt_prompts
transport_mapping =gpt_prompts.transport_mapping
residential_mapping = gpt_prompts.residential_mapping
industry_mapping = gpt_prompts.industry_mapping
services_mappings = gpt_prompts.services_mappings
transformation_mappings = gpt_prompts.transformation_mappings
other_mappings = gpt_prompts.other_mappings

#%%
#create a df from the mapping and then check that it maps correctly to the model_df_wide_simplified and emissions factors:

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

    print('Remapping the following sectors to the default sector:')
    print(left_onlys[['aperc_sector', 'aperc_fuel']])
    
    # #find where ipcc sectpr is "1.A.3.a - International Aviation" and ipcc fuel is "Aviation Gasoline"
    # a = mapping_test.loc[(mapping_test['ipcc_sector'] == '1.A.3.a - International Aviation') & (mapping_test['ipcc_fuel'] == 'Aviation Gasoline')]
    # if len(a) > 0:
    #     breakpoint()
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
    if len(duplicates) > 0:
        print(f"Warning: {len(duplicates)} duplicates in the aperc_sector	aperc_fuel columns")
    
    left_onlys = mapping_test[mapping_test['_merge'] == 'left_only']
    if len(left_onlys) > 0:
        print(f"Warning: {len(left_onlys)} combinations are still missing from the emissions factors")
    return mapping_test, left_onlys
#%%
results_transport, left_onlys_transport = map_sectors(transport_mapping, new_emissions_factors_ipcc)
results_residential, left_onlys_residential = map_sectors(residential_mapping, new_emissions_factors_ipcc)
#%%
results_industry, left_onlys_industry = map_sectors(industry_mapping, new_emissions_factors_ipcc)

results_services, left_onlys_services = map_sectors(services_mappings, new_emissions_factors_ipcc)

results_transformation, left_onlys_transformation = map_sectors(transformation_mappings, new_emissions_factors_ipcc)
#%%
results_other, left_onlys_other = map_sectors(other_mappings, new_emissions_factors_ipcc)
#%%
#also create something that will check the mappings for missing sectors. i.e. check industry mapping for missing aperc_sector aperc_fuel combinations in industry_combinations_model
def check_missing_sectors(mapping_df, model_df, sector_col, fuel_col, sector):
    
    mapping_df = pd.DataFrame(mapping_df).T.reset_index()
    mapping_df.columns = ['aperc_sector', 'aperc_fuel', 'ipcc_sector', 'ipcc_fuel']
    mapping_sectors_fuel_combos = mapping_df[[sector_col, fuel_col]].drop_duplicates()
    model_sectors_fuel_combos = model_df[[sector_col, fuel_col]].drop_duplicates()
    # breakpoint()
    #merege them
    combos_merged = pd.merge(mapping_sectors_fuel_combos, model_sectors_fuel_combos, on=[sector_col, fuel_col], indicator=True, how='outer')
    #extract non both rows
    missing_from_mapping = combos_merged.loc[combos_merged['_merge']=='right_only']
    if len(missing_from_mapping) > 0:
        print(f"Warning: for {sector} {len(missing_from_mapping)} mapping combinations are still missing and need to be mapped\n")
    not_needed_in_mapping =  combos_merged.loc[combos_merged['_merge']=='left_only']
    if len(not_needed_in_mapping) > 0:
        print(f"Warning: for {sector} {len(not_needed_in_mapping)} mapping combinations are not in the model and need to be removed from the mapping\n")
    return missing_from_mapping, not_needed_in_mapping
    
missing_from_mapping_industry, not_needed_in_mapping_industry = check_missing_sectors(industry_mapping, industry_combinations_model, 'aperc_sector', 'aperc_fuel', 'industry')

missing_from_mapping_services, not_needed_in_mapping_services= check_missing_sectors(services_mappings, services_combinations_model, 'aperc_sector', 'aperc_fuel', 'services')

missing_from_mapping_transformation, not_needed_in_mapping_transformation= check_missing_sectors(transformation_mappings, transformation_combinations_model, 'aperc_sector', 'aperc_fuel', 'transformation')

missing_from_mapping_other, not_needed_in_mapping_other= check_missing_sectors(other_mappings, other_combinations_model, 'aperc_sector', 'aperc_fuel', 'other')


missing_from_mapping_residential, not_needed_in_mapping_residential= check_missing_sectors(residential_mapping, residential_combinations_model, 'aperc_sector', 'aperc_fuel', 'residential')

missing_from_mapping_transport, not_needed_in_mapping_transport= check_missing_sectors(transport_mapping, transport_combinations_model, 'aperc_sector', 'aperc_fuel', 'other')

# #create method to remove the not needed mappings from the mapping dictionary in gp_prompts.py:
# def remove_not_needed_mappings(mapping_df, not_needed_df):
#     #go into the gpt_prompts_extract_data_from_all_ipcc_data.py file and remove the not needed mappings by finding them by the aperc_sector and aperc_fuel with the kind of format ('16_other_sector$16_01_buildings$16_01_02_residential$x', '01_coal$01_01_coking_coal'): ('1.A.4.b - Residential', 'Coking Coal')

#     mapping_df = pd.DataFrame(mapping_df).T.reset_index()
#     mapping_df.columns = ['aperc_sector', 'aperc_fuel', 'ipcc_sector', 'ipcc_fuel']
#     not_needed_df = not_needed_df[[ 'aperc_sector', 'aperc_fuel']]
#     mapping_df = mapping_df.loc[~mapping_df[['aperc_sector', 'aperc_fuel']].isin(not_needed_df[['aperc_sector', 'aperc_fuel']])]
#     return mapping_df
#%%
#create a funciton that will create the prompt to send to chatgpt to get the missing sectors and fuels:
def create_missing_sectors_fuel_prompts(missing_sectors_df, sector_col, fuel_col, original_cominations_df, industry_tag):
    #this will create a short prompt at the beginnign and then list the missing sectors and fuels followed by the original combinations that it needs to be mapped to.
    prompt = "Please provide the most likely IPCC 2006 Source/Sink Category and Fuel 2006 combinations for the aperc_sector and aperc_fuel combinations and put it in a python dict with the aperc_sector and aperc_fuel combinations as the keys and the corresponding, most likely IPCC 2006 Source/Sink Category and Fuel 2006 combinations as the value. e.g.dict ={('16_other_sector$16_01_buildings$16_01_02_residential$x', '01_coal$01_01_coking_coal'): ('1.A.4.b - Residential', 'Coking Coal')}.\n"
    if industry_tag != 'transformation':
        prompt +="(for the IPCC sector categories try to prioritise mapping using the {0} related sectors rather than the 1.A.1 - Energy Industries sector):\n".format(industry_tag)
    else:
        prompt +=f"(for the IPCC sector categories try to prioritise mapping using the 1.A - Fuel Combustion Activities sector):\n"
    prompt += "Please dont skip any combinations, and if you do please tell me"
    prompt += "The following aperc_sector and aperc_fuel combinations are missing from the model:\n"
    
    prompt += missing_sectors_df[[sector_col, fuel_col]].to_string(index=False)
    
    prompt += "\n\nThese need to be mapped to the following IPCC 2006 Source/Sink Category and Fuel 2006 combinations:\n"
    prompt += original_cominations_df.to_string(index=False)
    
    return prompt
    
#%%
#basically just print these out individaully and input them to chatgpt then extract the dict output and put it in the mappings in the gpt_prompts.py file. no doubt chatgpt will miss ome so we will need to do this a few times and potentially fix some of the mappings manually.
if len(missing_from_mapping_industry) > 0:
    industry_prompt = create_missing_sectors_fuel_prompts(missing_from_mapping_industry, 'aperc_sector', 'aperc_fuel', industry_combinations, 'industry')
    print(industry_prompt)
    print('\n\n')
if len(missing_from_mapping_services) > 0:
    services_prompt = create_missing_sectors_fuel_prompts(missing_from_mapping_services, 'aperc_sector', 'aperc_fuel', services_combinations, 'services')
    print(services_prompt)
    print('\n\n')
if len(missing_from_mapping_transformation) > 0:
    transformation_prompt = create_missing_sectors_fuel_prompts(
    missing_from_mapping_transformation, 'aperc_sector', 'aperc_fuel', transformation, 'transformation')
    print(transformation_prompt)
    print('\n\n')
if len(missing_from_mapping_other) > 0:
    other_prompt = create_missing_sectors_fuel_prompts(missing_from_mapping_other, 'aperc_sector', 'aperc_fuel', other, 'other')
    print(other_prompt)
    print('\n\n')
if len(missing_from_mapping_residential) > 0:
    residential_prompt = create_missing_sectors_fuel_prompts(missing_from_mapping_residential, 'aperc_sector', 'aperc_fuel', residential_combinations, 'residential')
    print(residential_prompt)
    print('\n\n')
if len(missing_from_mapping_transport) > 0:
    transport_prompt = create_missing_sectors_fuel_prompts(missing_from_mapping_transport, 'aperc_sector', 'aperc_fuel', transport_combinations, 'transport')
    print(transport_prompt)
    print('\n\n')

#IN 17 OCT I GOT TOLDBY CHATGPT THAT I HAD 5 RESPONSES FROM 01PREVIEW REMAINING FOR 7 DAYS LOL
#%%

#merge them all together
all_results = pd.concat([results_industry, results_services, results_transformation, results_other, results_residential, results_transport])

all_results.drop(columns=['_merge'], inplace=True)
#%%
#check there are no duplicates in the aperc_sector	aperc_fuel columns
duplicates = all_results[['aperc_sector', 'aperc_fuel', 'Gas']].loc[all_results[['aperc_sector', 'aperc_fuel', 'Gas']].duplicated()]
if len(duplicates) > 0:
    print(f"Warning: {len(duplicates)} duplicates in the aperc_sector	aperc_fuel columns")

#%%
#check that the missing sectors and fuels are jsut the ones we expect. do this by joininig model_df_wide_copy to all_results, checking what is missing and then checking that the missing values are the ones we expect:
model_df_wide_copy_test = model_df_wide_copy[['aperc_sector', 'aperc_fuel']].drop_duplicates()
model_df_wide_copy_test = model_df_wide_copy_test.merge(all_results, on=['aperc_sector', 'aperc_fuel'], how='left', indicator=True)
missing_sectors_fuels = model_df_wide_copy_test.loc[model_df_wide_copy_test['_merge'] == 'left_only'][['aperc_sector', 'aperc_fuel']].drop_duplicates()
#%%
missing_rows = pd.DataFrame()
# zero_emissions_fuels = [not_applicable_sectors
for sector_fuel in missing_sectors_fuels.iterrows():
    
    if sector_fuel[1]['aperc_sector'] not in not_applicable_sectors and sector_fuel[1]['aperc_fuel'] not in zero_emissions_fuels:
        print('Warning: missing sector and fuel combination not in zero_emissions_fuels or not_applicable_sectors. They are probably missing from the mapping. The missing sector and fuel combination is: {}'.format(sector_fuel))
        missing_rows = pd.concat([missing_rows, sector_fuel[1]])

#%%
#now separate aperc_sector and aperc_fuel into separate columns and join on to teh other key columns in model_df_wide_simplified

# model_df_wide=model_df_wide_original.copy()
# model_df_wide['aperc_sector'] = model_df_wide['sectors'] + '$' + model_df_wide['sub1sectors'] + '$' + model_df_wide['sub2sectors'] + '$' + model_df_wide['sub3sectors'] 

# #we also dont need most  of the cols so lets drop them and any duplicates:
# model_df_wide = model_df_wide[['sectors', 'sub1sectors', 'sub2sectors', 'sub3sectors', 'sub4sectors', 'fuels', 'subfuels', 'aperc_sector']].drop_duplicates()
        
# #now we need to do the same but for fuels. We will get a list of the fuels in each df and then map them. we MIGHT have a few fuels on each side of the mapping that mathc up, thats ok. we might also be missing fuels depending on the sector. we will work that out later.
# model_df_wide['aperc_fuel']=model_df_wide['fuels']+'$'+model_df_wide['subfuels']


all_results['sectors'] = all_results['aperc_sector'].str.split('$').str[0]
all_results['sub1sectors'] = all_results['aperc_sector'].str.split('$').str[1]
all_results['sub2sectors'] = all_results['aperc_sector'].str.split('$').str[2]
all_results['sub3sectors'] = all_results['aperc_sector'].str.split('$').str[3]

all_results['fuels'] = all_results['aperc_fuel'].str.split('$').str[0]
all_results['subfuels'] = all_results['aperc_fuel'].str.split('$').str[1]

#join on sub4sectors as well as all other combinations of sectors and fuels. we will label where the sector or fuel is not applicable or no emissions as well as where the sector fuel combination does not have any energy use.
all_results = all_results.merge(model_df_wide_original_wide_copy[['sectors', 'sub1sectors', 'sub2sectors', 'sub3sectors','sub4sectors', 'fuels', 'subfuels', 'aperc_sector', 'aperc_fuel']].drop_duplicates(), on=['sectors', 'sub1sectors', 'sub2sectors', 'sub3sectors', 'fuels', 'subfuels','aperc_sector', 'aperc_fuel'], how='outer', indicator=True)

#create columns called 'Sector not applicable' and 'Fuel not applicable' and set to True or False based on the sector or fuel being in the not_applicable_sectors or zero_emissions_fuels lists.
#and also a column called 'No energy use' which is True if the value is in the invalid rows df

all_results['Sector not applicable'] = all_results['aperc_sector'].isin(not_applicable_sectors)
all_results['Fuel not applicable'] = all_results['aperc_fuel'].isin(zero_emissions_fuels)
all_results= all_results.drop(columns=['_merge'])
all_results = all_results.merge(model_df_wide_invalid_rows, on=['aperc_sector', 'aperc_fuel'], how='outer', indicator=True)
#%%
#if thereas any right_onlys then create error
if len(all_results.loc[all_results['_merge'] == 'right_only']) > 0:
    raise ValueError('Error: there are right_onlys in the merge of all_results and model_df_wide_invalid_rows')
#%%
#and where merge is both, set 'No expected energy use' to True
all_results['No expected energy use'] = False
all_results.loc[all_results['_merge'] == 'both', 'No expected energy use'] = True


#drop the merge col
all_results.drop(columns=['_merge'], inplace=True)

#%%
#convert everything to mt/pj (from kg/tj)
all_results['Value'] = all_results['Value'].astype(float)
all_results['Value'] = all_results['Value'] / 1000
all_results['Unit'] = 'Mt/PJ'
#create a column alled co2e emissions factor and set it to the value times the GWP based on the Gas column. then rename Value to Original emissions factor.
all_results['GWP'] = all_results['Gas'].map(gwp_dict)
all_results['CO2e emissions factor'] = all_results['Value'] * all_results['GWP']
all_results.rename(columns={'Value': 'Original emissions factor'}, inplace=True)

#%%
#drop the columns we dont need
all_results.drop(columns=['aperc_sector', 'aperc_fuel', 'ipcc_sector','ipcc_fuel'], inplace=True)

#%%
#save to csv
all_results.to_csv('../output_data/9th_edition_emissions_factors_all_gases_IPCC_details.csv', index=False)

#and then remove non-essential cols and save to csv as simplified
# 'EF ID', 'IPCC 1996 Source/Sink Category',
#        'IPCC 2006 Source/Sink Category', 'Gas', 'Fuel 1996', 'Fuel 2006',
#        'Type of parameter', 'Description', 'Technologies / Practices',
#        'Parameters / Conditions', 'Region / Regional Conditions',
#        'Abatement / Control Technologies', 'Other properties',
#        'Original emissions factor', 'Unit', 'Equation', 'IPCC Worksheet',
#        'Technical Reference', 'Source of data', 'Data provider', 'sectors',
#        'sub1sectors', 'sub2sectors', 'sub3sectors', 'fuels', 'subfuels',
#        'sub4sectors', 'Sector not applicable', 'Fuel not applicable',
#        'No expected energy use', 'GWP', 'CO2e emissions factor']
#keep the following:
#'Unit', Gas, 'CO2e emissions factor' 'sectors',
#        'sub1sectors', 'sub2sectors', 'sub3sectors', 'fuels', 'subfuels',
#        'sub4sectors', 'Sector not applicable', 'Fuel not applicable',
#        'No expected energy use',
all_results_simple = all_results[['Unit', 'Gas', 'CO2e emissions factor', 'sectors', 'sub1sectors', 'sub2sectors', 'sub3sectors', 'sub4sectors','fuels', 'subfuels', 'Sector not applicable', 'Fuel not applicable', 'No expected energy use']]

#chekc for udplicates
duplicates = all_results_simple.loc[all_results_simple.duplicated()]
if len(duplicates) > 0:
    print(f"Warning: {len(duplicates)} duplicates in the aperc_sector	aperc_fuel columns, {duplicates}")
all_results_simple.to_csv('../output_data/9th_edition_emissions_factors_all_gases_simplified.csv', index=False)
#%%

#%%

