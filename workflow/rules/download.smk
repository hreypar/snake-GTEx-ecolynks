import os
from snakemake.remote.HTTP import RemoteProvider as HTTPRemoteProvider

HTTP = HTTPRemoteProvider()

rule download_gtex:
    input:
        HTTP.remote("storage.googleapis.com/gtex_analysis_v8/rna_seq_data/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_tpm.gct.gz", keep_local=True)
        HTTP.remote("storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt", keep_local=True)
#    run:
#        outputName = os.path.basename(input[0])
#        shell("mv {input} {outputName}")
