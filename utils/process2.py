if (True):
  name_prots = "out/nmr_ids_prots.txt"
  name_out = "out/nmr_ids_goa.txt"

if (False):
  name_prots = "out/bw_ids_prots.txt"
  name_out = "out/bw_ids_goa.txt"

if (False):
  name_prots = "out/m_ids_prots.txt"
  name_out = "out/m_ids_goa.txt"

if (False):
  name_prots = "out/bb_ids_prots.txt"
  name_out = "out/bb_ids_goa.txt"

if (False):
  name_prots = "out/c_ids_prots.txt"
  name_out = "out/c_ids_goa.txt"

if (False):
  name_prots = "out/gw_ids_prots.txt"
  name_out = "out/gw_ids_goa.txt"

###

fprots = open(name_prots, "r")
fout = open(name_out, "w")

fgoa = open("/media/dmitriy/ssd2/data/goa_uniprot_p.gaf", "r")

prots = {}
for line in fprots:
  fields = line[:-1].split()
  prots[fields[2]] = set()

i = 0
for line in fgoa:
  i += 1

  if (i % 1000000 == 0):
    print(i)

  if (i<=9):
    continue
  else:
    fields = line.split()
    prot = fields[1]
    if (prot in prots.keys()):
      prots[prot].add(fields[4])

for key in prots.keys():
  res = key
  for go in prots[key]:
    res += " " + go
  fout.write("{}\n".format(res))

