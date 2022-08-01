#craete mapping (temp)
#%%
execfile("../config/config.py")#usae this to load libraries and set variables. Feel free to edit that file as you need

#%%
energy_data_file = '00_APEC_example_energy_data.csv'#CHANGE ME. Make sure it is CSV. becausue by encouraging user to use csv, the user is encoruaged to make sure the formatting is correct too
energy_data = pd.read_csv("{}/{}".format(input_data_path, energy_data_file))

emissions_factors = pd.read_csv('{}/IPCC_emissions_factors.csv'.format(output_data_path))#note that these emissions factors have already been mapped for use in the 8th edition modelling. So this isnt exactly a mappiing from IPCC codes to EGEDA fuel codes.

#rename fuel_code to Fuel
emissions_factors = emissions_factors.rename(columns={'fuel_code':'Fuel'})

#%%
APEC_data = energy_data.copy()

# #create column titles for first two columns 
# APEC_data.columns.values[0] = 'Fuel'
# APEC_data.columns.values[1] = 'Sector'

#grab only the fuel code col
APEC_data = APEC_data[['Fuel']].drop_duplicates()
emissions_factors = emissions_factors[['Fuel']].drop_duplicates()
#%%

#format name for fuel codes, so we will replace spaces with _ and lowercase all, and replace .'s with _'s. this will sort out some mappings so we dont have to do them manually
APEC_data['00_APEC_fuel_code'] = APEC_data['Fuel']
APEC_data['Fuel'] = APEC_data['Fuel'].str.replace(' ', '_').str.lower().str.replace('.', '_').str.replace('/', '_').str.replace('(', '').str.replace(')', '').str.replace(':', '').str.replace(',', '').str.replace('-', '').str.replace('_0', '_').str.replace('&', 'and').str.replace('__', '_').str.replace('__', '_')

#create copy of col so it shows after the merge
emissions_factors['emissions_factors_fuel_code'] = emissions_factors['Fuel']

#merge input data with emission factors
APEC_input_energy_data = pd.merge(APEC_data, emissions_factors, on='Fuel', how='outer')

#Check iwhat fuel codes we are goign to have to manully map between the energy data set and the emissions factors set:
list_2 = emissions_factors['Fuel'].unique()
list_1 = APEC_data['Fuel'].unique()
missing_codes_list = [x for set_1 in (set(list_2),) for x in list_1 if x not in set_1]
print("These {} fuel codes are in the energy data set but arent in the emissions factors set. You will need to do somethig about them: \n\n".format(len(missing_codes_list)), missing_codes_list)

#%%
#SAVE data in input_data/archive
save = False
if save:
    APEC_input_energy_data.to_csv("{}/archive/APEC_to_IPCC_mappings.csv".format(input_data_path), index=False)#when looking at the output you want to use emissions_factors_fuel_code and 00_APEC_fuel_code as the columns for the mappings. there will be NA's in rows where only on fuel code is in a column. you will nbeed to manually work out what other fuerl code this mapos to in the column with the NA.

#%%
#Now thnat we ahve manually mapoped any mismatches between 00APEC and the IPCC emissions factors, we can see what fuels dont ahve corresponding value in each  column.
#It happens that some fuels are missing in the IPCC data set. This is because the IPCC data set is missing some fuel codes that arent in the energy data set.
#we should therefore manually map emissions factors found from reputable sources onto a new emissions factors data set, which will become the go to emissions factors datawset for APEC. This will also be the new data set for the 8th edition modelling (and perhaps even 9th edition)
#i did this using some missing factors in the ipcc e issions factors data set that hugh seemed to have missed. As well as using preexisting factors that hugh had used, but for imilar fuel types, eg. biofuels_other for bagasse
