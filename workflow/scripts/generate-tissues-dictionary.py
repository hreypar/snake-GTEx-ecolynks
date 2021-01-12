__author__ = "Helena Reyes Gopar"

import csv

samples_filename = snakemake.input[0]

# declare dictionary
tissues_dict = {}

# open the file and read line by line
with open(samples_filename,'r') as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        tissue = row[5]
        sample = row[0]
        if tissue not in tissues_dict:
            tissues_dict[tissue] = [sample] # make sure the value is a list
        else:
            tissues_dict[tissue].append(sample) # append to the list

# detect which columns are SAMPID and SMTS
# see the keys with dict.keys(tissues_dict)

# save the dictionary to a csv file
with open(snakemake.output[0], 'w') as f:
    writer = csv.writer(f)
    for key, value in tissues_dict.items():
        writer.writerow([key] + value)
