# RNA_modification overlap other features
import glob
import os
from decimal import *
####################################################
RNA_mod_data = ''
QTL_result_dir = ''
QTL_data_list = glob.glob('')
GWAS_data = ''
GWAS_result_dir = ''
ClinVar_data = ''
ClinVar_result_dir = ''
COSMIC_data = ''
COSMIC_result_dir = ''
miRNA_data = ''
miRNA_result_dir = ''
RBP_data = ''
RBP_result_dir = ''
###################################################
# QTL
os.system('mkdir -p ' + QTL_result_dir)
for i in data_list:
    filename = os.path.basename(i)
    command = 'bedtools intersect -a %s -b %s -wa -wb   |sort |uniq > %s' % (
        RNA_mod_data, i, QTL_result_dir + filename)
    os.system(command)
# GWAS
os.system('mkdir -p ' + GWAS_result_dir)
filename = os.path.basename(data)
command = 'bedtools intersect -a %s -b %s -wa -wb   |sort |uniq > %s' % (
    RNA_mod_data, GWAS_data, GWAS_result_dir + 'GWAS.txt')
os.system(command)
# ClinVar
os.system('mkdir -p ' + ClinVar_result_dir)
filename = os.path.basename(data)
command = 'bedtools intersect -a %s -b %s -wa -wb   |sort |uniq > %s' % (
    RNA_mod_data, ClinVar_data, ClinVar_result_dir + 'ClinVar.txt')
os.system(command)
# COSMIC
os.system('mkdir -p ' + COSMIC_result_dir)
filename = os.path.basename(data)
command = 'bedtools intersect -a %s -b %s -wa -wb   |sort |uniq > %s' % (
    RNA_mod_data, COSMIC_data, COSMIC_result_dir + 'COSMIC.txt')
os.system(command)
# miRNA
os.system('mkdir -p ' + miRNA_result_dir)
command = 'bedtools intersect -a %s -b %s -wa -wb   |sort |uniq > %s' % (
    RNA_mod_data, miRNA_data, miRNA_result_dir + 'miRNA.txt')
os.system(command)
# RBP
os.system('mkdir -p ' + RBP_result_dir)
command = 'bedtools intersect -a %s -b %s -wa -wb |sort |uniq > %s' % (
    RNA_mod_data, RBP_data, RBP_result_dir + 'RBP.txt')
os.system(command)
