






















#%%
# # Define acceptable units
# accepted_units = ['TJ/Gg', 'kg/GJ', 'TJ/kt', 'tC/TJ']#'kg/GJ', 'kg/TJ', 'KG/TJ', 'tC/TJ', 't CO2/TJ', 'gC/MJ', 'g/MJ', 'CO2 kg/GJ']

# # Select emission factors with these units
# ef_selected = model_df_wide_simplified_ipcc_merged_new[
#     model_df_wide_simplified_ipcc_merged_new['Unit'].isin(accepted_units)
# ].copy()

# # Check what gases are present
# print('Gases present in selected emission factors:', ef_selected['Gas'].unique())

# #%%
# # Function to standardize emission factors to kg CO2eq/TJ
# def standardize_emission_factor(row):
#     ef = row['EF']  # Emission factor value
#     unit = row['Unit']
#     gas = row['Gas']
#     if pd.isnull(ef):
#         return None  # Can't process missing values

#     # Initialize standardized emission factor (kg CO2eq/TJ)
#     ef_kg_TJ = None

#     # Standardize units to kg/TJ
#     if unit in ['kg/GJ', 'CO2 kg/GJ']:
#         # Multiply by 1000 to convert kg/GJ to kg/TJ
#         ef_kg_TJ = ef * 1000
#     elif unit in ['kg/TJ', 'KG/TJ']:
#         ef_kg_TJ = ef
#     elif unit == 'tC/TJ':
#         # Convert tC/TJ to kgC/TJ (multiply by 1000), then to kgCO2/TJ
#         ef_kg_TJ = ef * 1000 * 3.664
#     elif unit == 't CO2/TJ':
#         # Convert t CO2/TJ to kg CO2/TJ (multiply by 1000)
#         ef_kg_TJ = ef * 1000
#     elif unit == 'gC/MJ':
#         # Convert gC/MJ to kgC/TJ (multiply by 1e6), then to kgCO2/TJ
#         ef_kg_TJ = ef * 1e6 * 3.664
#     elif unit == 'g/MJ':
#         # Convert g/MJ to kg/TJ (multiply by 1e6)
#         ef_kg_TJ = ef * 1e6
#     else:
#         # Unit not recognized, cannot process
#         return None

#     # Apply GWP factors for CH4 and N2O
#     if gas == 'CO2':
#         GWP = 1
#     elif gas == 'CH4':
#         GWP = 28  # AR5 GWP100 value
#     elif gas == 'N2O':
#         GWP = 265  # AR5 GWP100 value
#     else:
#         # For other gases, we might need to look up GWP, but for now, skip
#         GWP = None

#     if GWP is not None:
#         ef_kg_TJ_CO2eq = ef_kg_TJ * GWP
#         return ef_kg_TJ_CO2eq
#     else:
#         return None

# # Apply the function to the dataframe
# ef_selected['EF_kg_TJ_CO2eq'] = ef_selected.apply(standardize_emission_factor, axis=1)

# #%%
# # Filter out rows with null EF_kg_TJ_CO2eq
# valid_efs = ef_selected[ef_selected['EF_kg_TJ_CO2eq'].notnull()]
# print(f"Number of valid emission factors: {valid_efs.shape[0]}")

# # Sum the emission factors for different gases
# ef_total = valid_efs.groupby(['aperc_sector', 'aperc_fuel'])['EF_kg_TJ_CO2eq'].sum().reset_index()

# #%%
# # Prepare energy data
# energy_data = model_df_wide_original.copy()

# # Create 'aperc_sector' and 'aperc_fuel' in energy data
# energy_data['aperc_sector'] = energy_data['sectors'] + '$' + energy_data['sub1sectors'] + '$' + energy_data['sub2sectors'] + '$' + energy_data['sub3sectors']
# energy_data['aperc_fuel'] = energy_data['fuels'] + '$' + energy_data['subfuels']

# # Melt the data to long format
# years = [col for col in energy_data.columns if col.isdigit()]
# energy_long = energy_data.melt(
#     id_vars=['economy', 'scenarios', 'aperc_sector', 'aperc_fuel', 'is_subtotal'],
#     value_vars=years,
#     var_name='year',
#     value_name='energy_PJ'
# )

# # Remove subtotals and zeros
# energy_long = energy_long[
#     (energy_long['is_subtotal'] == False) &
#     (energy_long['energy_PJ'].notnull()) &
#     (energy_long['energy_PJ'] != 0)
# ]

# #%%
# # Merge the emission factors with the energy data
# energy_emissions = energy_long.merge(ef_total, on=['aperc_sector', 'aperc_fuel'], how='left')

# # Check for missing emission factors
# missing_efs = energy_emissions[energy_emissions['EF_kg_TJ_CO2eq'].isnull()]
# print(f"Number of energy rows without emission factors: {missing_efs.shape[0]}")

# # Remove rows without emission factors
# energy_emissions = energy_emissions[energy_emissions['EF_kg_TJ_CO2eq'].notnull()]

# #%%
# # Calculate emissions
# # Emissions (Mt CO2eq) = Energy (PJ) * Emission Factor (kg CO2eq/TJ) * 1e-6
# energy_emissions['emissions_MtCO2eq'] = energy_emissions['energy_PJ'] * energy_emissions['EF_kg_TJ_CO2eq'] * 1e-6

# #%%
# # Aggregate emissions by economy, scenario, sector, and year
# emissions_aggregated = energy_emissions.groupby(
#     ['economy', 'scenarios', 'aperc_sector', 'year']
# )['emissions_MtCO2eq'].sum().reset_index()

# # Save the emissions data
# emissions_aggregated.to_csv('emissions_aggregated.csv', index=False)

# # Output a message indicating completion
# print("Emissions calculation completed and saved to 'emissions_aggregated.csv'.")
#%%







#%%
# #create anotehr sample and check it out:"
# # Extract the first 5000 rows
# first_1000 = model_df_wide_sample.head(1000)
# last_1000 = model_df_wide_sample.tail(1000)

# sample_df = pd.concat([first_1000, last_1000])
# sample_df.to_csv('model_df_wide_sample_cleaned.csv', index=False)

# #










































#process where i decided to remov3e regional specifications:
#%%
# #lets see what happens if we remove the regions that arent na. we can compare it to the df with regions that arent na, and see if we are missing any combinations of aperc_sector	aperc_fuel

# no_regions = model_df_wide_simplified_ipcc_merged_clean.loc[model_df_wide_simplified_ipcc_merged_clean['Region / Regional Conditions'].isna()][['aperc_sector', 'aperc_fuel', 'ipcc_sector', 'ipcc_fuel']].drop_duplicates()
# regions = model_df_wide_simplified_ipcc_merged_clean.loc[model_df_wide_simplified_ipcc_merged_clean['Region / Regional Conditions'].notna()][['aperc_sector', 'aperc_fuel', 'ipcc_sector', 'ipcc_fuel']].drop_duplicates()

# #fiund missing values
# missing_values = no_regions.merge(regions, on=['aperc_sector', 'aperc_fuel', 'ipcc_sector', 'ipcc_fuel'], how='outer', indicator=True)

# #rename indicator to something more clear
# missing_values = missing_values.rename(columns={'_merge': 'missing_region'})
# #where its left_only write 'missing from data with regions' and where its right_only write 'missing from data without regions'
# missing_values['missing_region'] = missing_values['missing_region'].map({'left_only': 'missing from data with regions', 'right_only': 'missing from data without regions'})
# #save to csv
# missing_values.to_csv('missing_values.csv', index=False)
# #%%
# #extract the right only data so we can see what rows we ahve otherwsie:
# missing_values_right_only = missing_values[missing_values['missing_region'] == 'missing from data without regions']
# #join that to the model_df_wide_simplified_ipcc_merged_clean to see what we are missing:
# missing_values_right_only = missing_values_right_only.merge(model_df_wide_simplified_ipcc_merged_clean, on=['aperc_sector', 'aperc_fuel', 'ipcc_sector', 'ipcc_fuel'], how='inner')
# #%%


# #it seems risky to map to a specific region? one thing we think we know is that there is a  mapping for every fuel if we map it to the sector '1.A - Fuel Combustion Activities' so there are no specific regions. so maybe for these, try chbange their ipcc_sector to '1.A - Fuel Combustion Activities' and see if we can map them to a where the region is not na. if we can, then we can map them to that region. if we cant, then we can map them to the default region. if we cant map them to the default region, then we can drop them.

# missing_values_right_only['new_ipcc_sector'] = '1.A - Fuel Combustion Activities'
# alt_emissions_factors_ipcc =emissions_factors_ipcc.loc[emissions_factors_ipcc['IPCC 2006 Source/Sink Category'] == '1.A - Fuel Combustion Activities']
# missing_values_right_only = pd.merge(missing_values_right_only, emissions_factors_ipcc, left_on=['new_ipcc_sector', 'ipcc_fuel'], right_on=['IPCC 2006 Source/Sink Category', 'Fuel 2006'], how='left')
# model_df_wide_simplified_ipcc_merged_clean


























and now do it for these:

# RESIDENTIAL
#Please map the following aperc sector, fuel combinations to one of the following IPCC 2006 Source/Sink Category, Fuel 2006 combinations and put it in a python dict. ignore the row numbers. (for the IPCC sector categories tr to prioritise mapping using the residential related sectors rather than the 1.A.1 - Energy Industries sector):
# APERC:

	aperc_sector	aperc_fuel
62	16_other_sector$16_01_buildings$16_01_02_residential$x	01_coal$01_01_coking_coal
211	16_other_sector$16_01_buildings$16_01_02_residential$x	01_coal$01_05_lignite
468	16_other_sector$16_01_buildings$16_01_02_residential$x	01_coal$01_x_thermal_coal
832	16_other_sector$16_01_buildings$16_01_02_residential$x	01_coal$x
1262	16_other_sector$16_01_buildings$16_01_02_residential$x	02_coal_products$x
1517	16_other_sector$16_01_buildings$16_01_02_residential$x	03_peat$x
1661	16_other_sector$16_01_buildings$16_01_02_residential$x	04_peat_products$x
2599	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_01_motor_gasoline
2738	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_02_aviation_gasoline
2853	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_03_naphtha
3090	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_06_kerosene
3458	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_07_gas_diesel_oil
3704	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_08_fuel_oil
3854	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_09_lpg
3979	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_10_refinery_gas_not_liquefied
4092	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_11_ethane
4226	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_x_jet_fuel
4910	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$07_x_other_petroleum_products
5328	16_other_sector$16_01_buildings$16_01_02_residential$x	07_petroleum_products$x
5512	16_other_sector$16_01_buildings$16_01_02_residential$x	08_gas$08_01_natural_gas
5623	16_other_sector$16_01_buildings$16_01_02_residential$x	08_gas$08_02_lng
5734	16_other_sector$16_01_buildings$16_01_02_residential$x	08_gas$08_03_gas_works_gas
5916	16_other_sector$16_01_buildings$16_01_02_residential$x	08_gas$x
7123	16_other_sector$16_01_buildings$16_01_02_residential$x	15_solid_biomass$15_01_fuelwood_and_woodwaste
7232	16_other_sector$16_01_buildings$16_01_02_residential$x	15_solid_biomass$15_02_bagasse
7338	16_other_sector$16_01_buildings$16_01_02_residential$x	15_solid_biomass$15_03_charcoal
7447	16_other_sector$16_01_buildings$16_01_02_residential$x	15_solid_biomass$15_04_black_liquor
7556	16_other_sector$16_01_buildings$16_01_02_residential$x	15_solid_biomass$15_05_other_biomass
7712	16_other_sector$16_01_buildings$16_01_02_residential$x	15_solid_biomass$x
8024	16_other_sector$16_01_buildings$16_01_02_residential$x	16_others$16_01_biogas
8247	16_other_sector$16_01_buildings$16_01_02_residential$x	16_others$16_02_industrial_waste
8358	16_other_sector$16_01_buildings$16_01_02_residential$x	16_others$16_03_municipal_solid_waste_renewable
8469	16_other_sector$16_01_buildings$16_01_02_residential$x	16_others$16_04_municipal_solid_waste_nonrenewable
8601	16_other_sector$16_01_buildings$16_01_02_residential$x	16_others$16_05_biogasoline
8737	16_other_sector$16_01_buildings$16_01_02_residential$x	16_others$16_06_biodiesel
8946	16_other_sector$16_01_buildings$16_01_02_residential$x	16_others$16_07_bio_jet_kerosene
9101	16_other_sector$16_01_buildings$16_01_02_residential$x	16_others$16_08_other_liquid_biofuels


IPCC:


# 	IPCC 2006 Source/Sink Category	Fuel 2006
# 1855	1.A.1 - Energy Industries	Crude Oil
# 1856	1.A.1 - Energy Industries	Orimulsion
# 1857	1.A.1 - Energy Industries	"Natural Gas Liquids
# (NGLs)"
# 1858	1.A.1 - Energy Industries	Motor Gasoline
# 1859	1.A.1 - Energy Industries	Aviation Gasoline
# 1860	1.A.1 - Energy Industries	Jet Gasoline
# 1861	1.A.1 - Energy Industries	Jet Kerosene
# 1862	1.A.1 - Energy Industries	Other Kerosene
# 1863	1.A.1 - Energy Industries	Shale Oil
# 1864	1.A.1 - Energy Industries	Gas Oil
# 1865	1.A.1 - Energy Industries	Diesel Oil
# 1866	1.A.1 - Energy Industries	Residual Fuel Oil
# 1867	1.A.1 - Energy Industries	Liquefied Petroleum Gases
# 1868	1.A.1 - Energy Industries	Ethane
# 1869	1.A.1 - Energy Industries	Naphtha
# 1870	1.A.1 - Energy Industries	Bitumen
# 1871	1.A.1 - Energy Industries	Lubricants
# 1872	1.A.1 - Energy Industries	Petroleum Coke
# 1873	1.A.1 - Energy Industries	Refinery Feedstocks
# 1874	1.A.1 - Energy Industries	Refinery Gas
# 1875	1.A.1 - Energy Industries	Waxes
# 1876	1.A.1 - Energy Industries	White Spirit & SBP
# 1877	1.A.1 - Energy Industries	Other Petroleum Products
# 1878	1.A.1 - Energy Industries	Anthracite
# 1879	1.A.1 - Energy Industries	Coking Coal
# 1880	1.A.1 - Energy Industries	Other Bituminous Coal
# 1881	1.A.1 - Energy Industries	Sub-Bituminous Coal
# 1882	1.A.1 - Energy Industries	Lignite
# 1883	1.A.1 - Energy Industries	Oil Shale and Tar Sands
# 1884	1.A.1 - Energy Industries	Brown Coal Briquettes
# 1885	1.A.1 - Energy Industries	Patent Fuel
# 1886	1.A.1 - Energy Industries	Coke Oven Coke and Lignite Coke
# 1887	1.A.1 - Energy Industries	Gas Coke
# 1888	1.A.1 - Energy Industries	Coal Tar
# 1889	1.A.1 - Energy Industries	Gas Works Gas
# 1890	1.A.1 - Energy Industries	Coke Oven Gas
# 1891	1.A.1 - Energy Industries	Blast Furnace Gas
# 1892	1.A.1 - Energy Industries	Oxygen Steel Furnace Gas
# 1893	1.A.1 - Energy Industries	Natural Gas
# 1894	1.A.1 - Energy Industries	Municipal Wastes (non-biomass fraction)
# 1895	1.A.1 - Energy Industries	Industrial Wastes
# 1896	1.A.1 - Energy Industries	Waste Oils
# 1897	1.A.1 - Energy Industries	Peat
# 1898	1.A.1 - Energy Industries	Wood/Wood Waste
# 1899	1.A.1 - Energy Industries	Sulphite Lyes (Black Liquor)
# 1900	1.A.1 - Energy Industries	Other Primary Solid Biomass
# 1901	1.A.1 - Energy Industries	Charcoal
# 1902	1.A.1 - Energy Industries	Biogasoline
# 1903	1.A.1 - Energy Industries	Biodiesels
# 1904	1.A.1 - Energy Industries	Other Liquid Biofuels
# 1905	1.A.1 - Energy Industries	Landfill Gas
# 1906	1.A.1 - Energy Industries	Sludge Gas
# 1907	1.A.1 - Energy Industries	Other Biogas
# 1908	1.A.1 - Energy Industries	Municipal Wastes (biomass fraction)

# 2341	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Crude Oil
# 2342	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Orimulsion
# 2343	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	"Natural Gas Liquids
# (NGLs)"
# 2344	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Motor Gasoline
# 2345	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Aviation Gasoline
# 2346	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Jet Gasoline
# 2347	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Jet Kerosene
# 2348	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Other Kerosene
# 2349	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Shale Oil
# 2350	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Gas Oil
# 2351	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Diesel Oil
# 2352	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Residual Fuel Oil
# 2353	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Liquefied Petroleum Gases
# 2354	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Ethane
# 2355	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Naphtha
# 2356	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Bitumen
# 2357	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Lubricants
# 2358	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Petroleum Coke
# 2359	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Refinery Feedstocks
# 2360	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Refinery Gas
# 2361	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Waxes
# 2362	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	White Spirit & SBP
# 2363	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Other Petroleum Products
# 2364	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Anthracite
# 2365	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Coking Coal
# 2366	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Other Bituminous Coal
# 2367	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Sub-Bituminous Coal
# 2368	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Lignite
# 2369	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Oil Shale and Tar Sands
# 2370	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Brown Coal Briquettes
# 2371	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Patent Fuel
# 2372	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Coke Oven Coke and Lignite Coke
# 2373	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Gas Coke
# 2374	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Coal Tar
# 2375	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Gas Works Gas
# 2376	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Coke Oven Gas
# 2377	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Blast Furnace Gas
# 2378	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Oxygen Steel Furnace Gas
# 2379	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Natural Gas
# 2380	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Municipal Wastes (non-biomass fraction)
# 2381	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Industrial Wastes
# 2382	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Waste Oils
# 2383	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Peat
# 2384	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Wood/Wood Waste
# 2385	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Sulphite Lyes (Black Liquor)
# 2386	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Other Primary Solid Biomass
# 2387	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Charcoal
# 2388	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Biogasoline
# 2389	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Biodiesels
# 2390	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Other Liquid Biofuels
# 2391	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Landfill Gas
# 2392	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Sludge Gas
# 2393	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Other Biogas
# 2394	"1.A.4.b - Residential
# 1.A.4.c.i - Stationary"	Municipal Wastes (biomass fraction)
