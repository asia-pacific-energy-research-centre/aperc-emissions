#intention is to create a system to calc emissions for elec generation. 
#However it is difficult to create a one size fits all system since the input energy data is going to have different categories. However we can creeate an easy to follow example for the user to replciate for their needs

#This example will take in the energy used to generate the electricity, as well as the total electricity geenrated. it will sum up the energy used to generate electricity and the total electricity generated and then calculate the emissions using emisisons_of_elec_gen / PJ_of_elec_gen.
#this example will also be done on the whole of the 00APEC file so it will calc gen emissions for historical data for all economys
#%%

execfile("../config/config.py")#usae this to load libraries and set variables. Feel free to edit that file as you need

#%%

#load electricity generation data
#note that this needs to be put in a format that is compatable with the emissions factors file. Basically a fuel_code column and a PJ column. #eg this is the origianl format of each sheet of the xlsx file we will load in
#Economy, Year, Fuel, PJ
# eg. 01_Aus, 2010, 17_electricity, 0.0  #this is the electricity output data
# eg. 01_Aus, 2011, 7_8_fuel_oil, 0.0  #this is the fuel oil input data

energy_data_file = '../../utility_data/00APEC_FUELSUMSREMOVED.xlsx'#CHANGE ME. 
emissions_factors_file = '00APEC_emissions_factors.csv'#CHANGE ME.
#%%
#LOAD
emissions_factors = pd.read_csv('{}/{}'.format(output_data_path, emissions_factors_file))
# energy_data = pd.read_excel('{}/{}'.format(input_data_path, energy_data_file))

#%%
#FORMAT
#rename fuel_code to Fuel
emissions_factors = emissions_factors.rename(columns={'fuel_code':'Fuel'})

#create example using eachh sheet of the 00_APEC data
generation_emissions_dtf = pd.DataFrame(columns=['Economy', 'Year','Emissions factor (MT/PJ)'])#create empty dtf. We will add all newly created emissions factors to it
for sheet in pd.ExcelFile(energy_data_file).sheet_names:
    APEC_data = pd.read_excel(energy_data_file, sheet_name=sheet)
    
    #make data tall 
    APEC_data = APEC_data.melt(id_vars=['Fuel', 'Sector'], var_name='Year', value_name='PJ')

    #filter for only the sectors that we want () #note that this excludes energy used in CHP to produce electricity and heat by autoproducers and main activity roducers. This is because we have no way to split the heat production from the electricity generation for CHP, and it seems more likely that the heat prdction will make up a majority of CHP input energy.
    APEC_input_energy_data = APEC_data[APEC_data['Sector'].isin(['9.1.1 Electricity plants', '9.2.1 Electricity plants'])]
    APEC_input_energy_data = APEC_input_energy_data[APEC_input_energy_data['Fuel']!='17 Electricity']#emissions will be set to 0 for this anyway, but best to be sure

    APEC_output_energy_data = APEC_data[APEC_data['Sector'].isin(['9. Total transformation sector'])]
    APEC_output_energy_data = APEC_output_energy_data[APEC_output_energy_data['Fuel'].isin(['17 Electricity'])]

    #sum data by Fuel type and year
    APEC_input_energy_data = APEC_input_energy_data.groupby(['Fuel', 'Year']).sum().reset_index()
    APEC_output_energy_data = APEC_output_energy_data.groupby(['Fuel', 'Year']).sum().reset_index()

    #convert input data to positives
    APEC_input_energy_data['PJ'] = APEC_input_energy_data['PJ'].abs()

    #%%
    #Check if there are any fuel codes are in the energy data set that arent in the emissions factors set:
    list_2 = emissions_factors['Fuel'].unique()
    list_1 = APEC_input_energy_data['Fuel'].unique()
    missing_codes_list = [x for set_1 in (set(list_2),) for x in list_1 if x not in set_1]
    if len(missing_codes_list)>0:
        print("These fuel codes are in the energy data set for sheet {} but arent in the emissions factors set. You will need to do somethig about them: ".format(sheet), missing_codes_list)

    #%%
    #merge input data with emission factors  
    APEC_input_energy_data = pd.merge(APEC_input_energy_data, emissions_factors, on='Fuel', how='left')
    #and then times them,
    APEC_input_energy_data['Emissions'] = APEC_input_energy_data['PJ'] * APEC_input_energy_data['Emissions factor (MT/PJ)']

    #sum the emissions per year
    APEC_input_energy_data_emissions_sum = APEC_input_energy_data[['Year', 'Emissions']].groupby(['Year']).sum().reset_index()

    #merge the emissions per year with the output electricity data
    APEC_output_energy_data = pd.merge(APEC_output_energy_data, APEC_input_energy_data_emissions_sum, on='Year', how='left')

    #divide the emissions by the pj to get emisisons factor MT/PJ of emissions for elec produciton in the year
    APEC_output_energy_data['Emissions factor (MT/PJ)'] = APEC_output_energy_data['Emissions'] / APEC_output_energy_data['PJ']

    #lastly make a column which specs what economy the generation data is from so that wen we look at the dtf of all emisison factors we can se what econmomy it is for
    APEC_output_energy_data['Economy'] = sheet
    APEC_output_energy_data['Fuel'] = '17 Electricity'
    APEC_output_energy_data = APEC_output_energy_data[['Economy', 'Year', 'Fuel', 'Emissions factor (MT/PJ)']]

    generation_emissions_dtf = pd.concat([generation_emissions_dtf, APEC_output_energy_data], axis=0)
    
#%%

#join emissions factors to the newly calculated generation data
#load
#create a copy of the emissions factors foir each economy and year in gen_factors (which is every economy year combination in the 00_APEC dataset) then concat the two dataframes. this will make it so we ahve a set of emission factors for each eocnomy and year in the apec data so we can calculate the emissions for each economy easily, given that the emissions factors for elec use is different wfor eadch economy.
dummy_df = generation_emissions_dtf[['Economy', 'Year']].drop_duplicates()

emissions_factors['dummy'] = 1
dummy_df['dummy'] = 1

apec_factors_2 = dummy_df.merge(emissions_factors, on='dummy')#

apec_factors_2.drop(['dummy'], axis=1, inplace=True)

#concatenate gen and emissionfactors
large_emissions_factors_df = pd.concat([generation_emissions_dtf, apec_factors_2], axis=0)


#%%
#SAVE
generation_emissions_dtf.to_csv('{}/egeda_generation_emissions_factors.csv'.format(output_data_path), index=False)

large_emissions_factors_df.to_csv('{}/egeda_all_emissions_factors.csv'.format(output_data_path), index=False)

#%%
#wish list, example using 8th edition data as inpt *would require using finns transport scripts that take in data from 8th edition charts outputs, change it to take in data from sheets for 'Power Fuel Consumption' and then format. 
# %%
