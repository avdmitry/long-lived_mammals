#./tools/salmon-1.9.0/bin/salmon quant \
#    -i nmr_index -l A \
#    -1 ../../data/rnaseq/naked_mole_rat/SRR2123747_pass_1_trimmed.fastq.gz \
#    -2 ../../data/rnaseq/naked_mole_rat/SRR2123747_pass_2_trimmed.fastq.gz \
#    --threads 7 --validateMappings -o quants/SRR2123747_quant

#./tools/salmon-1.9.0/bin/salmon quant \
#    -i bw_index -l A \
#    -1 ../../data/rnaseq/bowhead_whale/SRR1685415_pass_1_trimmed.fastq.gz \
#    -2 ../../data/rnaseq/bowhead_whale/SRR1685415_pass_2_trimmed.fastq.gz \
#    --threads 7 --validateMappings -o quants/SRR1685415_quant

#./tools/salmon-1.9.0/bin/salmon quant \
#    -i m_index -l A \
#    -1 ../../data/rnaseq/mouse/SRR1302402_pass_1_trimmed.fastq.gz \
#    -2 ../../data/rnaseq/mouse/SRR1302402_pass_2_trimmed.fastq.gz \
#    --threads 7 --validateMappings -o quants/SRR1302402_quant

#./tools/salmon-1.9.0/bin/salmon quant \
#    -i bb_index -l A \
#    -1 ../../data/rnaseq/brandts_bat/SRR617087_pass_1_trimmed.fastq.gz \
#    -2 ../../data/rnaseq/brandts_bat/SRR617087_pass_2_trimmed.fastq.gz \
#    --threads 7 --validateMappings -o quants/SRR617087_quant

#./tools/salmon-1.9.0/bin/salmon quant \
#    -i c_index -l A \
#    -1 ../../data/rnaseq/cow/SRR594477_pass_1_trimmed.fastq.gz \
#    -2 ../../data/rnaseq/cow/SRR594477_pass_2_trimmed.fastq.gz \
#    --threads 7 --validateMappings -o quants/SRR594477_quant

./tools/salmon-1.9.0/bin/salmon quant \
    -i gw_index -l A \
    -1 ../../data/rnaseq/gray_whale/SRR13853443_pass_1_trimmed.fastq.gz \
    -2 ../../data/rnaseq/gray_whale/SRR13853443_pass_2_trimmed.fastq.gz \
    --threads 7 --validateMappings -o quants/SRR13853443_quant

