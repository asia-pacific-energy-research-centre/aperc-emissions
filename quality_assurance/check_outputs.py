#use to double check outputs using set of tests

#%%

#this test will compare output against previous output.
import numpy as np
import pandas as pd
SAVE = True
LATEST_EGEDA_YEAR = 2018
Latet_ouput_file = 'EGEDA_{}_CO2_Emissions'.format(LATEST_EGEDA_YEAR)
Previous_output_file = 'EGEDA_FC_CO2_Emissions_years_2018_HUGH_COPY'#change me as you need. note, no .csv at the end
#LOAD
#this tst will require you set the keys for the dataframe to be the same as the keys in the previous output.
index_keys = ['economy', 'fuel_code', 'item_code_new', 'Unit']#set this if it needs to change
Latest_output = pd.read_csv("../output_data/{}.csv".format(Latet_ouput_file), index_col=index_keys)
Previous_output = pd.read_csv("../output_data/{}.csv".format(Previous_output_file), index_col=index_keys)

#first round all to 1 dp to avoid insignificant differences
Latest_output = Latest_output.round(decimals=1)
Previous_output = Previous_output.round(decimals=1)

#compare outputs
diff = Latest_output.compare(Previous_output, keep_shape=False, keep_equal=False)
print('there are at least', diff.shape[1], 'differences between the two dfs (this number is the number of rows in the dataframe so if there are more than 1 diff per row, then there are more differences)')

#option to save if you want
if SAVE == True:
    diff.to_csv("../quality_assurance/DIFF_{}_VS_{}.csv".format(Latet_ouput_file, Previous_output_file))
#%%