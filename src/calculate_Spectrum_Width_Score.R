# The script wes used to calculate the Spectrum Width Score.
# @author Lee

setwd("")
data <- read.table("", sep = "\t", header = T, quote = NULL)

colnames(data) <- c("RNA_mod_peak", "Conservation", "Scale", "peak_info", "RBP", 
    "miRNA", "ClinVar", "GWAS", "COSMIC", "eQTL", "meQTL", "pQTL", "sQTL", "circQTL")
rbp_scale <- data$RBP/sum(data$RBP)
mirna_scale <- data$miRNA/sum(data$miRNA)
clinvar_scale <- data$ClinVar/sum(data$ClinVar)
gwas_scale <- data$GWAS/sum(data$GWAS)
eqtl_scale <- data$eQTL/sum(data$eQTL)
meqtl_scale <- data$meQTL/sum(data$meQTL)
sqtl_scale <- data$sQTL/sum(data$sQTL)
pqtl_scale <- data$pQTL/sum(data$pQTL)
circqtl_scale <- data$circQTL/sum(data$circQTL)
cosmic_scale <- data$COSMIC/sum(data$COSMIC)
data_scale <- cbind(rbp_scale, mirna_scale, clinvar_scale, gwas_scale, cosmic_scale, 
    eqtl_scale, meqtl_scale, sqtl_scale, pqtl_scale, circqtl_scale)
score <- rowSums(data_scale)
data <- cbind(data, score)
Spectrum_Width_Score <- (data$score - min(data$score))/(max(data$score) - min(data$score))
data <- cbind(data, Spectrum_Width_Score)
write.table(data, "", col.names = T, row.names = F, sep = "\t", quote = F)
