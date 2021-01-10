samples_filename = "GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt"

# declare dictionary
tissues_dict = {}

#Read lines of file
with open(samples_filename,'r') as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        tissue = row[5]
        sample = row[0]
        if tissue in tissues_dict:
            tissues_dict[tissue].append(sample) # append to the list
        else:
            tissues_dict[tissue] = [sample] # make sure the value is a list

# declare dictionary

# open the file
# detect which columns are SAMPID and SMTS
# for each row
#   if the key doesnt exist, add new key and value
# append value to key
