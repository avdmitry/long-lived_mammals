ftax = open("mammalia_taxons.txt", "r")

taxons = []
for line in ftax:
  taxons.append(line[:-1])

fgoa = open("/media/dmitriy/Seagate Expansion Drive/data/goa_uniprot_all.gaf", "r")
fout = open("/media/dmitriy/ssd2/data/goa_uniprot_.gaf", "w")
fprot_out = open("/media/dmitriy/ssd2/data/all_prots_goa_.txt", "w")

num_read = 0
last_prot = "xxx"
i = 0
j = 0
k = 0
for line in fgoa:
  i += 1
  num_read += len(line)

  if (i % 1000000 == 0):
    print(i, j, k, num_read/(1024*1024*1024))

  if (i <= 9):
    fout.write(line)
  else:
    fields = line.split("\t")
    if (fields[0]=="UniProtKB" and fields[8]=="P"): # P C F
      taxon = fields[12][6:]
      if (taxon in taxons):
        fout.write(line)

        prot = fields[1]
        if (last_prot != prot):
          last_prot = prot
          fprot_out.write("{}\n".format(prot))
          k += 1
        j += 1
print(i, j, k)

