#%%
#this file is intended to calcualte emission factors for the 8th edition of the transport data as there are no emission factors for some 'general' fuel types:  ['1_x_coal_thermal', '16_x_hydrogen', '7_x_jet_fuel']. Although, in doing so, it was realised that there is very little effect of this long process, and probably wouldv been better to save the effort. oh well.

execfile("../config/config.py")#usae this to load libraries and set variables. Feel free to edit that file as you need

#%%
#load mapping for transport 8th (created manually)
transport_8th_mapping = pd.read_excel('{}/emissions_to_energy_mappings.xlsx'.format(config_folder_path), sheet_name ='transport_8th')

#laod energy datas from aperc_transport
energy = pd.read_csv('../../aperc_transport/intermediate_data/energy.csv'.format(intermediate_data_path))

apec_mapping = pd.read_excel('{}/emissions_to_energy_mappings.xlsx'.format(config_folder_path), sheet_name ='00APEC_map')

generation_emissions_dtf = pd.read_csv('{}/egeda_generation_emissions_factors.csv'.format(output_data_path))

emissions_factors = pd.read_csv('{}/{}'.format(output_data_path, '00APEC_emissions_factors.csv'))

transport_energy = pd.read_csv('../../aperc_transport/output_data/00APEC_transport.csv')

#%%
#first, get transport emisison factors from full set of emission factors. The process wil first complete the mapping to IPCC fuel names/codes, then use this to retrieve the emissions factors that are neeeded  

#to retrieve from emission factrors in the output apec datafra,me we need similar fuel codes. So we map to the apec fuel code mapping using transport 8th mapping then apec mapping to eventually get the emissions factrrors with the same fuel codes as are used in transport 8th
transport_8th_mapping = transport_8th_mapping.merge(apec_mapping, on = 'IPCC_emission_factors_2021_fuel', how = 'left')

transport_8th_mapping.rename(columns={'00_APEC_fuel_code': 'fuel_code'}, inplace=True)

#drop cols just to make easy
transport_8th_mapping_fuels = transport_8th_mapping[['fuel_code', 'Fuel_transport_8th']].drop_duplicates()

#filter for only the fuel types in factors df we want using left join
transport_emission_factors = transport_8th_mapping_fuels.merge(emissions_factors, how='left', on='fuel_code')

#remove the fuel code column
transport_emission_factors = transport_emission_factors.drop(columns=['fuel_code']).drop_duplicates()

#now we have the emission factors for the transport fuel types in 8th
#%%
#  calc avg of last X year of generation factors for aeach economy

X = 5#avg emission factors of latest X years.
latest_year = max(generation_emissions_dtf['Year'])

generation_emissions_dtf2 =generation_emissions_dtf.copy()

#filter for only latest X years
generation_emissions_dtf2 = generation_emissions_dtf2[generation_emissions_dtf2["Year"].isin(range(latest_year-X,latest_year))]
#calc
generation_emissions_dtf2_mean = generation_emissions_dtf2.groupby(['Economy']).mean().reset_index()

#grab economy and emissions factor only
generation_emissions_dtf2_mean = generation_emissions_dtf2_mean[['Economy', 'Emissions factor (MT/PJ)']]
#%%
#make orignal data have every economy
transport_emission_factors_all_econ = transport_emission_factors.copy()

generation_emissions_dtf2_mean_only_econ = generation_emissions_dtf2_mean[['Economy']].drop_duplicates()

transport_emission_factors_all_econ = transport_emission_factors_all_econ.merge(generation_emissions_dtf2_mean_only_econ, how='cross')

#now replace elec data in roginal with elec data from generation_emissions_dtf2_mean
generation_emissions_dtf2_mean['Fuel_transport_8th'] = '17_electricity'
transport_emission_factors_all_econ = transport_emission_factors_all_econ[transport_emission_factors_all_econ['Fuel_transport_8th'] != '17_electricity']
transport_emission_factors_all_econ = pd.concat([transport_emission_factors_all_econ, generation_emissions_dtf2_mean])

#%%
FUEL_TYPES_IN_QUESTION = ['1_x_coal_thermal', '16_x_hydrogen', '7_x_jet_fuel']
#Now we wnat to replacce the values that dont match the mappings with avgs of the last X years

#we are going to have to do this by finding the proportion of total for each fuel type that could be in these general fuel types (eg. coal_thermal) then times those proprtions by the emission factor for those fuel types, then sum them

#will specify the fuel ttypes in question manully to reduce complexity. We will concat these two dtfs later.
avg_fuel_types = transport_emission_factors_all_econ[transport_emission_factors_all_econ['Fuel_transport_8th'].isin(FUEL_TYPES_IN_QUESTION)]
not_avg_fuel_types = transport_emission_factors_all_econ[~transport_emission_factors_all_econ['Fuel_transport_8th'].isin(FUEL_TYPES_IN_QUESTION)]

#hydrogen is assumed to be 0
avg_fuel_types.loc[(avg_fuel_types['Fuel_transport_8th'] == '16_x_hydrogen'), 'Emissions factor (MT/PJ)'] = 0

#make hisotric transport energy long format and year as an int in preparation for next steps using this data
transport_energy_long = transport_energy.melt(id_vars=['Fuel', 'Sector', 'Economy'], var_name = 'Year', value_name = 'Energy')
transport_energy_long['Year'] = transport_energy_long['Year'].astype(int)


#%%
#first lets do jet fuel:

#for each of these fuel types we will find the similar fuel types in transport energy use then sum them for the last X years, and find sum of each individual fuel type as a proprtion of total
x_jet_fuel = transport_energy_long[transport_energy_long['Fuel'].isin(['7.02 Aviation gasoline', '7.04 Gasoline type jet fuel', '7.05 Kerosene type jet fuel'])]

#filter for only latest X years
x_jet_fuel = x_jet_fuel[x_jet_fuel["Year"].isin(range(latest_year-X,latest_year))]

#calc proportion
x_jet_fuel_sum = x_jet_fuel.groupby(['Economy', 'Fuel']).sum().reset_index()

x_jet_fuel_sum = x_jet_fuel_sum[['Economy', 'Fuel', 'Energy']]

x_jet_fuel_sum2 = x_jet_fuel_sum.groupby(['Economy']).sum().reset_index()

x_jet_fuel_sum2 = x_jet_fuel_sum2[['Economy', 'Energy']]

x_jet_fuel_sum_merge = x_jet_fuel_sum.merge(x_jet_fuel_sum2, how='left', on='Economy')

x_jet_fuel_prop= x_jet_fuel_sum_merge.copy()
x_jet_fuel_prop['Proportion'] = x_jet_fuel_prop['Energy_x']/x_jet_fuel_prop['Energy_y']

#now we have the proportion of each fuel type in the total for each economy we join that onto the emission factrors
x_jet_fuel_prop = x_jet_fuel_prop[['Economy', 'Fuel', 'Proportion']]
x_jet_fuel_prop.rename(columns={'Fuel': 'fuel_code'}, inplace=True)
x_jet_fuel_prop_merge = x_jet_fuel_prop.merge(emissions_factors, how='left', on='fuel_code')

x_jet_fuel_prop_merge['Emissions factor (MT/PJ)'] = x_jet_fuel_prop_merge['Proportion']*x_jet_fuel_prop_merge['Emissions factor (MT/PJ)']

x_jet_fuel_sum_ef = x_jet_fuel_prop_merge.groupby(['Economy']).sum().reset_index()

#give it the same fuel code as is used in 8th energy data  and remove unneccsary cols so we can join it onto central df
x_jet_fuel_sum_ef['Fuel_transport_8th'] = '7_x_jet_fuel'
x_jet_fuel_sum_ef = x_jet_fuel_sum_ef[['Economy', 'Fuel_transport_8th', 'Emissions factor (MT/PJ)']]

#we have an issue where some economys will now have emission factors of 0 for these fuel types because they dont use that fuel, yet. In this case we will replcae them, with the avg of all other, non-0, emission factors for that fuel type
non_zero_jet_fuel = x_jet_fuel_sum_ef[x_jet_fuel_sum_ef['Emissions factor (MT/PJ)']>0]
non_zero_jet_fuel_avg = np.mean(non_zero_jet_fuel['Emissions factor (MT/PJ)'])

x_jet_fuel_sum_ef['Emissions factor (MT/PJ)'].replace(0, non_zero_jet_fuel_avg, inplace=True)

#remove jet fuel from avg_fuel_types then concat new data
avg_fuel_types = avg_fuel_types[~avg_fuel_types['Fuel_transport_8th'].isin(['7_x_jet_fuel'])]

avg_fuel_types = pd.concat([avg_fuel_types, x_jet_fuel_sum_ef])
#%%
#now for coal thermal using same strategy:

#for each of these fuel types we will find the similar fuel types in transport energy use then sum them for the last X years, and find sum of each individual fuel type as a proprtion of total
x_coal_thermal = transport_energy_long[transport_energy_long['Fuel'].isin(['1.2 Other bituminous coal', '1.3 Sub-bituminous coal', '1.4 Anthracite', '1.5 Lignite'])]

#filter for only latest X years
x_coal_thermal = x_coal_thermal[x_coal_thermal["Year"].isin(range(latest_year-X,latest_year))]

#calc proportion
x_coal_thermal_sum = x_coal_thermal.groupby(['Economy', 'Fuel']).sum().reset_index()

x_coal_thermal_sum = x_coal_thermal_sum[['Economy', 'Fuel', 'Energy']]

x_coal_thermal_sum2 = x_coal_thermal_sum.groupby(['Economy']).sum().reset_index()

x_coal_thermal_sum2 = x_coal_thermal_sum2[['Economy', 'Energy']]

x_coal_thermal_sum_merge = x_coal_thermal_sum.merge(x_coal_thermal_sum2, how='left', on='Economy')

x_coal_thermal_prop= x_coal_thermal_sum_merge.copy()
x_coal_thermal_prop['Proportion'] = x_coal_thermal_prop['Energy_x']/x_coal_thermal_prop['Energy_y']

#now we have the proportion of each fuel type in the total for each economy we join that onto the emission factrors
x_coal_thermal_prop = x_coal_thermal_prop[['Economy', 'Fuel', 'Proportion']]
x_coal_thermal_prop.rename(columns={'Fuel': 'fuel_code'}, inplace=True)
x_coal_thermal_prop_merge = x_coal_thermal_prop.merge(emissions_factors, how='left', on='fuel_code')

x_coal_thermal_prop_merge['Emissions factor (MT/PJ)'] = x_coal_thermal_prop_merge['Proportion']*x_coal_thermal_prop_merge['Emissions factor (MT/PJ)']

x_coal_thermal_sum_ef = x_coal_thermal_prop_merge.groupby(['Economy']).sum().reset_index()

#give it the same fuel code as is used in 8th energy data  and remove unneccsary cols so we can join it onto central df
x_coal_thermal_sum_ef['Fuel_transport_8th'] = '1_x_coal_thermal'
x_coal_thermal_sum_ef = x_coal_thermal_sum_ef[['Economy', 'Fuel_transport_8th', 'Emissions factor (MT/PJ)']]

#we have an issue where some economys will now have emission factors of 0 for these fuel types because they dont use that fuel, yet. In this case we will replcae them, with the avg of all other, non-0, emission factors for that fuel type
non_zero_coal_thermal = x_coal_thermal_sum_ef[x_coal_thermal_sum_ef['Emissions factor (MT/PJ)']>0]
non_zero_coal_thermal_avg = np.mean(non_zero_coal_thermal['Emissions factor (MT/PJ)'])

x_coal_thermal_sum_ef['Emissions factor (MT/PJ)'].replace(0, non_zero_coal_thermal_avg, inplace=True)

#remove jet fuel from avg_fuel_types then concat new data
avg_fuel_types = avg_fuel_types[~avg_fuel_types['Fuel_transport_8th'].isin(['1_x_coal_thermal'])]

avg_fuel_types = pd.concat([avg_fuel_types, x_coal_thermal_sum_ef])
# %%
#now finally join all the fuel types together
emission_factors_for_8th_edition_transport = pd.concat([avg_fuel_types, not_avg_fuel_types])


#%%
#save and be done wiht this mess
emission_factors_for_8th_edition_transport.to_csv('../output_data/emission_factors_for_8th_edition_transport.csv', index=False)

#%%