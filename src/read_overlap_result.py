#!/usr/bin/python
# -*-coding:utf-8-*-
# @author Lee

RNA_mod_data = ''
eQTL_data = ''
meQTL_data = ''
pQTL_data = ''
sQTL_data = ''
circQTL_data = ''
ClinVar_data = ''
GWAS_data = ''
COSMIC_data = ''
RBP_data = ''
miRNA_data = ''

# get Webtable
# RNA_mod
RNA_mod = {}
with open(RNA_mod_data, 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        line = line.split('\t')
        key = line[0] + ':' + line[1] + '-' + line[2]
        RNA_mod[key] = line[-1]
# eQTL
RNA_mod_meQTL = {}

with open(eQTL_data, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')
        line = line.split('\t')
        RNA_mod_id = '%s:%s-%s' % (line[0], line[1], line[2])
        key = RNA_mod_id
        eqtl_pos = '%s:%s-%s' % (line[3], line[4], line[5])
        fwline = '%s|%s' % (eqtl_pos, line[-1])
        if key not in RNA_mod_meQTL.keys():
            RNA_mod_meQTL[key] = fwline
        elif key in RNA_mod_meQTL.keys():
            if fwline not in RNA_mod_meQTL[key]:
                RNA_mod_meQTL[key] += '@' + fwline

# meQTL
RNA_mod_meQTL = {}
with open(meqtl_data, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')
        line = line.split('\t')
        RNA_mod_id = '%s:%s-%s' % (line[0], line[1], line[2])
        key = RNA_mod_id
        meqtl_pos = '%s:%s-%s' % (line[3], line[4], line[5])
        fwline = '%s|%s' % (meqtl_pos, line[-1])
        if key not in RNA_mod_meQTL.keys():
            RNA_mod_meQTL[key] = fwline
        elif key in RNA_mod_meQTL.keys():
            if fwline not in RNA_mod_meQTL[key]:
                RNA_mod_meQTL[key] += '@' + fwline
# pQTL
RNA_mod_pQTL = {}
with open(pQTL_data, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')
        line = line.split('\t')
        RNA_mod_id = '%s:%s-%s' % (line[0], line[1], line[2])
        key = RNA_mod_id
        pqtl_pos = '%s:%s-%s' % (line[3], line[4], line[5])
        fwline = '%s|%s' % (pqtl_pos, line[-1])
        if key not in RNA_mod_pQTL.keys():
            RNA_mod_pQTL[key] = fwline
        elif key in RNA_mod_pQTL.keys():
            if fwline not in RNA_mod_pQTL[key]:
                RNA_mod_pQTL[key] += '@' + fwline
# sQTL
RNA_mod_sQTL = {}
with open(sqtl_data, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')
        line = line.split('\t')
        RNA_mod_id = '%s:%s-%s' % (line[0], line[1], line[2])
        key = RNA_mod_id
        sqtl_pos = '%s:%s-%s' % (line[3], line[4], line[5])
        fwline = '%s|%s' % (sqtl_pos, line[-1])
        if key not in RNA_mod_sQTL.keys():
            RNA_mod_sQTL[key] = fwline
        elif key in RNA_mod_sQTL.keys():
            if fwline not in RNA_mod_sQTL[key]:
                RNA_mod_sQTL[key] += '@' + fwline
# circQTL
RNA_mod_circQTL = {}
with open(circqtl_data, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')
        line = line.split('\t')
        RNA_mod_id = '%s:%s-%s' % (line[0], line[1], line[2])
        key = RNA_mod_id
        circqtl_pos = '%s:%s-%s' % (line[3], line[4], line[5])
        fwline = '%s|%s' % (circqtl_pos, line[-1])
        if key not in RNA_mod_circQTL.keys():
            RNA_mod_circQTL[key] = fwline
        elif key in RNA_mod_circQTL.keys():
            if fwline not in RNA_mod_circQTL[key]:
                RNA_mod_circQTL[key] += '@' + fwline

# ClinVar
RNA_mod_ClinVar = {}
with open(ClinVar_data, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')
        line = line.split('\t')
        RNA_mod_id = '%s:%s-%s' % (line[0], line[1], line[2])
        key = RNA_mod_id
        clinvar_pos = '%s:%s-%s' % (line[3], line[4], line[5])
        v = '%s|%s' % (clinvar_pos, line[-1])
        if key not in RNA_mod_ClinVar.keys():
            RNA_mod_ClinVar[key] = v
        elif key in RNA_mod_ClinVar.keys():
            if v not in RNA_mod_ClinVar[key]:
                RNA_mod_ClinVar[key] += '@' + v
# GWAS
RNA_mod_GWAS = {}
with open(GWAS_data, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')
        line = line.replace('PCDHA@,', 'PCDHA,')
        line = line.replace('PCDHG@,', 'PCDHG,')
        line = line.replace('SNORD116@', 'SNORD116')
        line = line.split('\t')
        RNA_mod_id = '%s:%s-%s' % (line[0], line[1], line[2])
        gwas_pos = '%s:%s-%s' % (line[3], line[4], line[5])
        key = RNA_mod_id
        v = '%s|%s' % (gwas_pos, line[-1])
        if key not in RNA_mod_GWAS.keys():
            RNA_mod_GWAS[key] = v
        elif key in RNA_mod_GWAS.keys():
            if v not in RNA_mod_GWAS[key]:
                RNA_mod_GWAS[key] += '@' + v
#COSMIC
RNA_mod_COSMIC = {}
with open(COSMIC_data, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')
        line = line.split('\t')
        RNA_mod_id = '%s:%s-%s' % (line[0], line[1], line[2])
        key = RNA_mod_id
        cosmic_pos = '%s:%s-%s' % (line[3], line[4], line[5])
        v = '%s|%s' % (cosmic_pos, line[-1])
        if key not in RNA_mod_COSMIC.keys():
            RNA_mod_COSMIC[key] = v
        elif key in RNA_mod_COSMIC.keys():
            if v not in RNA_mod_COSMIC[key]:
                RNA_mod_COSMIC[key] += '@' + v
# RBP
RNA_mod_RBP = {}
with open(RBP_data, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line.replace('starbase2', 'starBase2')
        line = line.strip('\n')
        line = line.split('\t')
        RNA_mod_id = '%s:%s-%s' % (line[0], line[1], line[2])
        key = RNA_mod_id
        rbp_pos = '%s:%s-%s' % (line[3], line[4], line[5])
        v = '%s|%s' % (rbp_pos, line[-1])
        if key not in RNA_mod_RBP.keys():
            RNA_mod_RBP[key] = v
        elif key in RNA_mod_RBP.keys():
            if v not in RNA_mod_RBP[key]:
                RNA_mod_RBP[key] += '@' + v
# miRNA
RNA_mod_miRNA = {}
with open(miRNA_data, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line.replace('Starbase2', 'starBase2')
        line = line.strip('\n')
        line = line.split('\t')
        RNA_mod_id = '%s:%s-%s' % (line[0], line[1], line[2])
        key = RNA_mod_id
        mirna_pos = '%s:%s-%s' % (line[3], line[4], line[5])
        v = '%s|%s' % (mirna_pos, line[-1])
        if key not in RNA_mod_miRNA.keys():
            RNA_mod_miRNA[key] = v
        elif key in RNA_mod_miRNA.keys():
            if v not in RNA_mod_miRNA[key]:
                RNA_mod_miRNA[key] += '@' + v
