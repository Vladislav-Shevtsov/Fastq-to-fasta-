# Fastq-to-fasta-
Fastq to fasta conversion 
Fastq_to_fasta.py README

### Dependencies ###

python3
python-dev (sudo apt-get install python-dev), 
seqtk (can be installed using conda - 
		
		 conda install -c bioconda/label/cf201901 seqtk
		
Alternatevely, can be installed locally by downloading the source code from: 
		
		 https://github.com/lh3/seqtk

### goal ###

Fastq_to_fasta.py is a bash script with use of python language designed to automate the process of converting pool of fastq files into fasta files useing sektq tool.

### input ###

input files should be in .fastq format 

example : file.fastq

### output ### 

output represents files(reads) with .fasta extension located in output folder.    

### command line examples ###

```python3 Fastq_to_fasta.py /path/to/input_dir /path/to/out_dir``` #This will generate bash file# 

 ```./convert_to_fasta_files.sh``` #This will run generated bash file 

#written by V.Shevtsov xatabadich(at)gmail.com
