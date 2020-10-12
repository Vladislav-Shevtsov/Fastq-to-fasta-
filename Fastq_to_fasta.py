import csv
import os

# determine tool directories
seqtktof = '/path_to/seqtk' #change to path to seqtk

# determine files directories
data_in_dir = '/path_to/input_dir' #change to input directory
data_out_dir = '/path_to/ou_dir' #change to output directory 

fastq_gz_row_list = sorted([os.path.join(data_in_dir, i) for i in os.listdir(data_in_dir) if i.endswith('.fastq')])
#generate the output nae suffix
def generate_bbduk_output_name(name, suffix = 'FAREADS'):
    a, b = os.path.splitext(name)
    new_name = a + '_' + suffix + b
    return new_name
#genetates bash file 
bash_file = 'convert_to_fasta.sh' # Name can be modified 
with open(bash_file, 'w') as f:
  f.write('#!/bin/bash \n')
  for sample in fastq_gz_row_list:
    name = os.path.basename(sample)
    
    out_sample = os.path.join(name)
    out_sample = generate_bbduk_output_name(out_sample + ".fasta")
    

    if not os.path.isfile(out_sample):
            f.write(f'{seqtktof} seq -a {sample} > {data_out_dir}/{out_sample} \n')
			
			
			#NOTE: 	GENERATED convert_to_fasta.sh FILE MUST BE EXECUTED OUTSIDE OF INPUT DIRECTORY!
