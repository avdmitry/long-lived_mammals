if (True):
  name_quant = "out/quants/SRR2123747_quant/quant.sf"
  name_prot = "out/transdecoder/GEBF01.1.fsa_nt.transdecoder.pep"
  name_out = "out/nmr_ids_prots.txt"

if (False):
  name_quant = "out/quants/SRR1685415_quant/quant.sf"
  name_prot = "out/transdecoder/bw_Trinity.fasta.transdecoder.pep"
  name_out = "out/bw_ids_prots.txt"

if (False):
  name_quant = "out/quants/SRR1302402_quant/quant.sf"
  name_prot = "out/transdecoder/m_Trinity.fasta.transdecoder.pep"
  name_out = "out/m_ids_prots.txt"

if (False):
  name_quant = "out/quants/SRR617087_quant/quant.sf"
  name_prot = "out/transdecoder/bb_Trinity.fasta.transdecoder.pep"
  name_out = "out/bb_ids_prots.txt"

if (False):
  name_quant = "out/quants/SRR594477_quant/quant.sf"
  name_prot = "out/transdecoder/Bos_taurus.ARS-UCD1.2.cdna.all.fa.transdecoder.pep"
  name_out = "out/c_ids_prots.txt"

if (False):
  name_quant = "out/quants/SRR13853443_quant/quant.sf"
  name_prot = "out/transdecoder/gw_Trinity.fasta.transdecoder.pep"
  name_out = "out/gw_ids_prots.txt"

###

fquant = open(name_quant, "r")
fprot = open(name_prot, "r")
fout = open(name_out, "w")

fall = open("/media/dmitriy/ssd2/data/all_prots_goa_p.txt", "r")
prots_all = set()
for line in fall:
  prots_all.add(line[:-1])


prots = {}
scores = {}
tpms = {}

genes = []
i = 0
for line in fquant:
  if (i==0):
    i = 1
    continue

  line = line.split()
  gene = line[0]
  tpm = float(line[3])
  if (tpm >= 1.0):
  #if (tpm > 0.0):
    genes.append(gene)
    #print(gene, tpm)

    prots[gene] = set()
    scores[gene] = 0
    tpms[gene] = tpm


for line in fprot:
  if (line[0]==">"):
    line_ = line.split()
    gene = line_[0][1:-3]
    if (gene in genes):
      #print(gene)
      line = line.split(",")
      for j in range(2, len(line)):
        if (line[j][:9]=="UniRef90_"):
          elems = line[j].split("|")
          pid = elems[0][9:]
          score = float(elems[1])
          #print(pid, score)
          #score = float(line[1][6:])
          #print(line[1][6:])

          #prots[gene].add(pid)
          if (score > scores[gene]):
            scores[gene] = score
            prots[gene] = set()
            prots[gene].add(pid)

"""
fprot = open("./nmr_uniref90.m8", "r")
for line in fprot:
  line_ = line.split("\t")
  gene = line_[0][:-3]
  if (gene in genes):
      pid = line_[1][9:]
      score = float(line_[2])
      if (score > scores[gene]):
            scores[gene] = score
            prots[gene] = set()
            prots[gene].add(pid)
"""

for key in prots.keys():
  iswrite = False
  res = key + " " + str(tpms[key])
  for prot in prots[key]:
    if (prot in prots_all):
      iswrite = True
      res += " " + prot
  #res += " " + prots[key]
  if (iswrite):
    fout.write("{}\n".format(res))

