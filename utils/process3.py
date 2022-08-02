if (True):
 name_goa = "out/nmr_ids_goa.txt"
 name_prots = "out/nmr_ids_prots.txt"
 name_res = "out/nmr_res.txt"

if (False):
 name_goa = "out/bw_ids_goa.txt"
 name_prots = "out/bw_ids_prots.txt"
 name_res = "out/bw_res.txt"

if (False):
 name_goa = "out/m_ids_goa.txt"
 name_prots = "out/m_ids_prots.txt"
 name_res = "out/m_res.txt"

if (False):
 name_goa = "out/bb_ids_goa.txt"
 name_prots = "out/bb_ids_prots.txt"
 name_res = "out/bb_res.txt"

if (False):
 name_goa = "out/c_ids_goa.txt"
 name_prots = "out/c_ids_prots.txt"
 name_res = "out/c_res.txt"

if (False):
 name_goa = "out/gw_ids_goa.txt"
 name_prots = "out/gw_ids_prots.txt"
 name_res = "out/gw_res.txt"

###

fgoa = open(name_goa, "r")
fprots = open(name_prots, "r")
fres = open(name_res, "w")

prots = {}
tpms = {}
for line in fprots:
  fields = line[:-1].split()
  gene = fields[0]
  tpm = float(fields[1])
  prot = fields[2]
  prots[gene] = set()
  prots[gene].add(prot)
  tpms[gene] = tpm

gos = {}
for line in fgoa:
  fields = line[:-1].split()
  prot = fields[0]
  gos[prot] = []
  for i in range(1, len(fields)):
    gos[prot].append(fields[i])

res = {}
for key in prots.keys():
  #res = key + " " + str(tpms[key])
  curr = set()
  #prot = prots[key]
  for prot in prots[key]:
    if (prot in gos):
      for go in gos[prot]:
        curr.add(go)

  for go in curr:
    if (go not in res):
      res[go] = 0.0
    res[go] += tpms[key]


scale = 1#6200/len(res)
last_tpm = 0
idx = 0
idx_cat = 0
for go in sorted(res, key=res.get, reverse=True):
  #tpm = round(res[go])
  tpm = res[go]
  idx += 1
  if (tpm!=last_tpm):
    last_tpm = tpm
    idx_cat = idx
  fres.write("{} {}\n".format(go, round(idx_cat*scale)))

