#!/usr/bin/bash
##
## DESCRIPTION:
## download RNA-seq Gene TPMs file from GTEx

# directory to download
DIR=data

# wget download url
URL=https://storage.googleapis.com/gtex_analysis_v8/rna_seq_data/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_tpm.gct.gz

# wget logfile
LOGFILE=gtex-download-tpm-`date +"%Y%m%d"`.log

mkdir -p $DIR

# download RNA-seq TPM file
wget \
  $URL \
  --directory-prefix $DIR \
  --output-file $DIR/$LOGFILE
