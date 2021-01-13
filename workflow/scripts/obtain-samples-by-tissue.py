__author__ = "Helena Reyes Gopar"

# read in tissues tissues dictionary

# read in rna_seq_data file, remember it's gzipped

### skip two lines (gct format)

### keep the following columns
##### "Name", "Description" AND whichever values correspond to the key tissue_of_interest in the dictionary

# write out the resulting table using the tissue_of_interest in the name
