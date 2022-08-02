#%%

#this is used to create emissions factors for use in calculating emissions in other projects. The code in this file is written so taht its easy to understand so you can copy and edit it to create emissions factors for other fuel codes than the standard egeda set, as you need

#It uses a mappings file and an input emissiojns factors file. The mappings file will contain mappings for fuel codes between the input emissions factors file and a set of fuel codes for an energy data set (eg. egeda) that is being used within apec. 

#you can update the mappings and emissions factors files

#%%
execfile("../config/config.py")#usae this to load libraries and set variables. Feel free to edit that file as you need

#%%
#CHANGE ME ACCORDING TO WHAT EMISSIONS FACTORS AND MAPPINGS YOU WANT TO USE
mapping_sheet = "00APEC_map"

emission_factors_sheet ="IPCC Emission Factors 2021"

output_sheet = "00APEC_emissions_factors.csv"
#%%
#LOAD
#TRY TO KEEP THIS CELL THE SAME
mapping = pd.read_excel("../config/emissions_to_energy_mappings.xlsx" , sheet_name = mapping_sheet)#this is the map between emission factors and fuel names. It contains a few sheets sinnce there are different mappings depnding on the input data. 

emission_factors = pd.read_excel("../config/emission_factors.xlsx", sheet_name = emission_factors_sheet)#this is the carbon cntent of each fuel in IPCC fuel categories


#%%
#FORMAT
#FEEL FREE TO ADJUST THIS CELL TO YOUR NEEDS
#this block will join carbon contents of different fuels with their respective Fuel names, as used in EGEDA and OSEMOSYS system (i.e 6_1_crude_oil) and then format so its clean
emission_factors['IPCC_emission_factors_2021_fuel'] = emission_factors['Fuel type']

IPCC_carbon_content = mapping.merge(emission_factors, left_on="IPCC_emission_factors_2021_fuel", right_on="IPCC_emission_factors_2021_fuel", how='inner')

#filter only for the columns we want to use:
IPCC_carbon_content = IPCC_carbon_content[["00_APEC_fuel_code", "IPCC_emission_factors_2021_fuel", "Default Carbon content(kg/GJ)", "IPCC_Account"]]
#print rows with NA's in the data for user visibility of potential emission factor fuel types that are being missed out
print('Here are the fuel codes with missing mappings. You may want to sort them out if they are fuel codes from the energy data, missing fuel codes in the emission factors:\n\n', IPCC_carbon_content[IPCC_carbon_content.isnull().any(axis=1)])

#%%
#FORMAT
#FEEL FREE TO ADJUST THIS CELL TO YOUR NEEDS

#remove na's
IPCC_carbon_content = IPCC_carbon_content.dropna()

#set index
IPCC_carbon_content= IPCC_carbon_content.set_index(['00_APEC_fuel_code','IPCC_Account'])

IPCC_carbon_content.loc[pd.IndexSlice[:,"LULUCF"],:] = 0#set all LULUCF based emissions from df to 0 for simplicity. its arguable that these renewable fuel types have 0 emissions

#Remove Account column
IPCC_carbon_content = IPCC_carbon_content.droplevel(level = 'IPCC_Account', axis =0)

IPCC_carbon_content.index = IPCC_carbon_content.index.rename("fuel_code")
IPCC_carbon_content = IPCC_carbon_content[["Default Carbon content(kg/GJ)"]]#Remove all cols but carbon content (kg/GJ) column and fuel code column.

#%%
#OPERATION
#FEEL FREE TO ADJUST THIS CELL TO YOUR NEEDS
IPCC_emissions_factors = IPCC_carbon_content.copy()

#multiply carbon content by 3.67 to get CO2 emissions factors (One ton of carbon equals 44/12 = 11/3 = 3.67 tons of carbon dioxide).
#NOTE i change dthis to be divided by 1000 because hugh normlly would divde by 1mill and then times by 1000 later for some reason.
IPCC_emissions_factors['Emissions factor (MT/PJ)'] = IPCC_emissions_factors*3.67/1000

#in the above the conversion from kg/GJ to MT/PJ is essentially:
#convert kg to MT = kg/1000000000   #note that MT stands for million tons
#convert GJ to PJ = GJ/1000000
#therefore: convert kg/GJ to MT/PJ = (kg/1000000000)/(GJ/1000000) = X/1000
IPCC_emissions_factors.drop(columns=['Default Carbon content(kg/GJ)'],inplace=True)

#%%
#SAVE
#IDEALLY DONT CHANGE THIS
IPCC_emissions_factors.to_csv("../output_data/{}".format(output_sheet))
#%%
