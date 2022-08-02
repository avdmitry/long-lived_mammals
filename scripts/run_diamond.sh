#./tools/diamond-2.0.14.152 blastp \
#    -d "/media/dmitriy/Seagate Expansion Drive/data/uniref90.dmnd" \
#    -q ./GEBF01.1.fsa_nt.transdecoder_dir/longest_orfs.pep \
#    --more-sensitive -o nmr_uniref90.m8 \
#    -f 6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore

#./tools/diamond-2.0.14.152 blastp \
#    -d "/media/dmitriy/Seagate Expansion Drive/data/uniref90.dmnd" \
#    -q ./bw_Trinity.fasta.transdecoder_dir/longest_orfs.pep \
#    --more-sensitive -o bw_uniref90.m8 \
#    -f 6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore

#./tools/diamond-2.0.14.152 blastp \
#    -d "/media/dmitriy/Seagate Expansion Drive/data/uniref90.dmnd" \
#    -q ./m_Trinity.fasta.transdecoder_dir/longest_orfs.pep \
#    --more-sensitive -o m_uniref90.m8 \
#    -f 6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore

#./tools/diamond-2.0.14.152 blastp \
#    -d "/media/dmitriy/Seagate Expansion Drive/data/uniref90.dmnd" \
#    -q ./bb_Trinity.fasta.transdecoder_dir/longest_orfs.pep \
#    --more-sensitive -o bb_uniref90.m8 \
#    -f 6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore

#./tools/diamond-2.0.14.152 blastp \
#    -d "/media/dmitriy/Seagate Expansion Drive/data/uniref90.dmnd" \
#    -q ./Bos_taurus.ARS-UCD1.2.cdna.all.fa.transdecoder_dir/longest_orfs.pep \
#    --more-sensitive -o c_uniref90.m8 \
#    -f 6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore

./tools/diamond-2.0.14.152 blastp \
    -d "/media/dmitriy/Seagate Expansion Drive/data/uniref90.dmnd" \
    -q ./gw_Trinity.fasta.transdecoder_dir/longest_orfs.pep \
    --more-sensitive -o gw_uniref90.m8 \
    -f 6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore

