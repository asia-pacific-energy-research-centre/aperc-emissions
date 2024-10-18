## SETUP
There are two options for environments. They depend if you want to use jupyter or just the command line to run the model. I prefer to use jupyter but i know that it takes a lot of space/set-up-time.
 - config/env_jupyter.yml
 - config/env_no_jupyter.yml

run:
conda env create --prefix ./env_jupyter --file ./config/env_jupyter.yml

Then:
conda activate ./env_jupyter

Note that installing those libraries in the yml files will result in a few other dependencies also being installed.


# Few changes:
on 10/17/2024 i updated this to use a new method incorporating a direct downlaod form the unfcc website https://www.ipcc-nggip.iges.or.jp/EFDB/find_ef.php?ipcc_code=1&ipcc_level=0 and mapping all of the 9th edition sector/fuel combinations to the no2, ch4 and co2 emissions factors. This involved a lot of chatgpt assisted mapping. It is a big change. Imprves the quality of our mappings as well as providing a more comprehensive set of emissions factors. However it is now a little messy and involved. If you have new combaintions of fuels/sectors then you will have to learn how the new scripts worked, sorry!


<<<<<<< HEAD













=======
# Please note that the below info is partly irrelevant now *as in dont bother reading it*
>>>>>>> b7f7600486e81fc424c8e17a462d0e058e364ab4

## The tool is focused on helping you to map emission factors to new fuel types you may have.

- It does this by providing code to create emission factors for energy categories used in the main APERC energy dataset. This code is intended to be able to be replicated for other datasets. 
- If a new energy dataset uses different fuel type codes, then a space for creating the mapping between those fuel codes and the emissions factors is provided in config/emissions_to_energy_mappings.xlsx
- Emission factors can also be updated in config/emission_factors.xlsx. 
- There is also a file to create **generation emissions factors** from the egeda data. This can also be easily edited to make it work for your own dataset.

PLEASE NOTE
This is not intended to calcualte emissions for your dataset of energy use. You can do that yourself using merge once you have created the emissions factors in this tool. 

# **The key files used are:**
#### Config/:
- config/emission_factors.xlsx - this contains emissions factors. It can be added to by the user if need be.
- config/emissions_to_energy_mappings.xlsx - this contains mappings for a set of fuel codes in an energy dataset that need to be mapped to a set of fuel codes for an emissions factors dataset. So there will be one column for the fuel codes in the energy dataset, and one or many columns depending on how many datasets of emissions factors you want to use (nromally just the latest dataset would do)

#### Output_data/:
- output_data/00APEC_emissions_factors.csv
- output_data/egeda_generation_emissions_factors.csv
- output_data/egeda_all_emissions_factors.csv - a combination of the above two csv's

#### Input_data/:
- input_data/00APEC_FUELSUMSREMOVED.xlsx - used in calculating generation emissions factors

#### Config/Archive/:
- We have ccs_rates.csv which may be useful in the future?

#### Workflow/:
_Use or edit these files for the purpose you need. You can save the new files in ../single_use_code/_

- get_emissions_factors_for_egeda_data
- calc_elec_gen_emission_factors_for_egeda_data.py

### Quality_assurance/
There is a quality assurance folder that provides a space for you to test the output. Please use and update this with any tests you write so it can be better in the future.

## Improvements and queries
If you have any querys or improvements to suggest please feel free to contact the person in charge of this (probably the last person to make a commit), they will probably endeavour to help and make any improvements you suggest. The main issue is trying to work out how to make this library more useful rather than just more complex.

Examples of improvements that may be useful if you raise them:

- output of emissions factors fuel types in the Xth edition outlook (eg. one fuel type for gasoline and kerosene jet fuel, a 0 for hydrogen emissions etc)
- estimation of hydrogen emission factors
- ability to calculate emissions given an input energy dataset
- graphs
