This will produce the emissions in the EGEDA energy data using emissions factors based on carbon content values from the IPCC (IPCC Methodology to EGEDA map.xlsx > sheet=Emissions Factors). The folder it will output is:

======================================================================

**Output:**
 
 "/output_data/EGEDA_{}_CO2_Emissions.csv".format(LATEST_EGEDA_YEAR) - So you will want to pick the output that suits the year of egeda data you to use. 

======================================================================

**Input data is:**

the latest EGEDA data, named like so: "../input_data/EGEDA_{}_items.csv".format(LATEST_EGEDA_YEAR)

======================================================================

**Config data is:**
   
**IPCC Methodology to EGEDA map.xlsx** sheets are as follows:


_**USED:**_

**emissions factors** = same as sheet above but in Default Carbon content(kg/GJ), so THIS IS USED IN THE MAIN PROCESS as "carbon content values from the IPCC"

**MAP**  = a mapping between IPCC and EGEDA categories


_**NOT USED:**_

**Default NCV** = Default net calorific values (NCVs) (TJ/Gg) and lower and upper limits of the 95% confidence interval (not used yet)
    
**Map_old** = not used
    
**EGEDA** = a mapping too (i think), but not used

_**Config/Archive/:**_

**Emissions_factors.csv** = We also have emissions factors in Emission Factor(Mt_CO2/PJ) here for all APEC economies and fuel types based on EGEDA fuel type categories. This isn;t used for anything yet but could be helpful perhaps
    
We also have **ccs_rates.csv** which may be useful in the future?

======================================================================

**Workflow**:

To run the process use aperc-emissions\workflow\Calculate_Emissions_factors_EGEDA_hist.py

The file aperc-emissions\workflow\Calculate_Emissions_factors_EGEDA_hist_part_2.py is the second half of Hughs original code for emissions factors calcualtion. 
I split this part out because it seemed that it was not essential. I have attempted to use comments to explain whats going on, or where i am unsruew. 
But it is not as well done as the first half of his code. I expect it should only be used if you have a hunch that you need it

======================================================================

There is a quality assurance folde rthat allows you to test the output. Please use and update this with any tests you write so it can be better in the future.

