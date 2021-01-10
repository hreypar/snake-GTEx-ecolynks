samples_filename = "GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt"

# declare dictionary
tissues_dict = {}

#Read lines of file
with open(samples_filename,'r') as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        if row[5] not in tissues_dict:
            tissues_dict[row[5]] = row[0]


# declare dictionary

# open the file
# detect which columns are SAMPID and SMTS
# for each row
#   if the key doesnt exist, add new key and value
# append value to key
