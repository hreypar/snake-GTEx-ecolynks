import os
from snakemake.remote.HTTP import RemoteProvider as HTTPRemoteProvider

#URL="storage.googleapis.com/gtex_analysis_v8/rna_seq_data/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_tpm.gct.gz"
URL="storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt"

HTTP = HTTPRemoteProvider()

rule download_gtex:
    input:
        HTTP.remote(URL, keep_local=True)
    run:
        outputName = os.path.basename(input[0])
        shell("mkdir -p resources")
        shell("mv {input} resources/{outputName}")

# I need to find a way to
## declare the URLs in a config file probably so the rule is generalised
## It would be good to understand what happens with http remote
