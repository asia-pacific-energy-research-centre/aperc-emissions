This will produce the emission factors for energy categories used in APERC energy datasets. 

If the user just wants emissions factors for the standard APEC set of fuel categories, they can just run 'emissions_factors_for_egeda_data.py' and use the output

It is also intended to provide an easy setup for someone to calcualte emissions factors if they have a different set of fuel categories than the standard APEC set. they would jsut create a copy of the emissions_factors_for_egeda_data.py file and variables in tehre, then in a new sheet in config/emissions_to_energy_mappings.xlsx create a mapping fromn the emissions factors in config/emission_factors.xlsx they want, and their unique fuel codes

There is also a file to create generation emissions factors from the egeda data. This can also be easily edited to make it work for your own situation.

**The key files used are:**

config/emission_factors.xlsx - this contains emissions factors. It can be added to by the user if need be.
config/emissions_to_energy_mappings.xlsx - this contains mappings for a set of fuel codes in an energy dataset that need to be mapped to a set of fuel codes for an emissions factors dataset. So there will be one column for the fuel codes in the energy dataset, and one or many columns depending on how many datasets of emissions factors you want to use (nromally just the latest dataset would do)

Output:
    output_data/00APEC_emissions_factors.csv
    output_data/egeda_generation_emissions_factors.csv

Input data:
     input_data/00APEC_FUELSUMSREMOVED.xlsx - used in calculating generation emissions factors

Config/Archive/:
    We have ccs_rates.csv which may be useful in the future?

Workflow:
    Use or edit these files for the purpose you need. You can save the new files in ../single_use_code/ :
    get_emissions_factors_for_egeda_data
    calc_elec_gen_emission_factors_for_egeda_data.py

There is a quality assurance folde rthat allows you to test the output. Please use and update this with any tests you write so it can be better in the future.

If you have any querys or improvements to suggest please feel free to contact the person in charge of this (probably the last person to make a commit), they will probably endeavour to help and make any improvements you suggest.
Examples of improvements that may be useful if you raise them:
-output of emissions factors fuel types in the Xth edition outlook (eg. one fuel type for gasoline and kerosene jet fuel, a 0 for hydrogen emissions etc)
