#!/usr/bin/bash
##
## DESCRIPTION:
## download sample annotation file from GTEx

# directory to download
DIR=data

# wget download url
URL=https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt

# wget logfile
LOGFILE=gtex-download-sample-annotation-`date +"%Y%m%d"`.log

mkdir -p $DIR

# download sample annotation file
  wget \
    $URL \
    --directory-prefix $DIR \
    --output-file $DIR/$LOGFILE
