# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd
import yaml


# %%

with open('./config.yml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    data = yaml.load(file, Loader=yaml.FullLoader)


# %%
data_sheets = data['FilePaths']

# %% [markdown]
# #### Read in emissions data and mapping file and format

# %%
# Read in emissions data


# %%
IPCC_Emission = pd.read_excel(data['Maping_File'], sheet_name = "Emission Factors", header=0,index_col="Fuel type ")


# %%
# Read in emissions sheet


# %%
# Read in maping sheet sheet


# %%
IPCC_map = pd.read_excel(data['Maping_File'] , sheet_name = "MAP", header=1,index_col="Fuel type ")


# %%
#Select only the columns that are going to be used In the emissions file. 


# %%
IPCC_Emission = IPCC_Emission[["Default Carbon content2\n(kg/GJ)"]]


# %%
IPCC_Emission.columns = ["Carbon content(kg/GJ)"]


# %%
Emission_egeda = IPCC_map.join(IPCC_Emission,on="Fuel type ")


# %%
Emission_egeda = Emission_egeda.dropna()


# %%
Emission_egeda= Emission_egeda.set_index(['Fuel ','Account'])


# %%
Emission_egeda.loc[pd.IndexSlice[:,"LULUCF"],:] = 0


# %%
Emission_egeda = Emission_egeda.droplevel(level = 1, axis =0)


# %%
start_cols = ['REGION','TECHNOLOGY','EMISSION','MODE_OF_OPERATION','UNITS','NOTES']


# %%
end_cols =  [*range(2017,2051)]


# %%
all_cols = start_cols + end_cols


# %%
def demand_emissions(df_data_sheet,Emission_map):
    df_EmissionActivityRatio = df_data_sheet.merge(right = Emission_map, left_on= "FUEL", right_index=True)

    df_EmissionActivityRatio.iloc[:,6:-1] = df_EmissionActivityRatio.iloc[:,6:-1].mul(df_EmissionActivityRatio.loc[:,"Carbon content(kg/GJ)"],axis =0 ) *1000

    df_EmissionActivityRatio = df_EmissionActivityRatio.set_index("REGION","TECHNOLOGY","FUEL").groupby(["REGION","TECHNOLOGY"]).sum()

    df_EmissionActivityRatio = df_EmissionActivityRatio.reset_index()
    df_EmissionActivityRatio["MODE_OF_OPERATION"] = 1
    df_EmissionActivityRatio["UNITS"] = np.nan
    df_EmissionActivityRatio["NOTES"] = np.nan
    df_EmissionActivityRatio["EMISSION"] = "CO2"
    
    return df_EmissionActivityRatio


# %%



# %%
for paths in data_sheets:
    input_activity = pd.read_excel(data_sheets[paths], sheet_name = "InputActivityRatio", header=0)
    print ("reading " + f'{paths} at {data_sheets[paths]}')
    EmissionActivityRatio = demand_emissions(input_activity,Emission_egeda)
    EmissionActivityRatio[all_cols]
    EmissionActivityRatio.to_excel(data['Output_location']+ "EmissionActivityRatio" + paths+".xlsx" ,index= False)
    print ( f' Saved to {data_sheets[paths]}')
    



