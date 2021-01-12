samples_filename = "GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt"

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
import csv

with open('filename', 'w') as f:
    c = csv.writer(f)

    for key, value in d.items():
        c.writerow([key] + value
