import px_autodock as px
import glob

# for ch in ['W','X','Y','Z']:
#   for i in range(1,28):
#     px.minimize("../test%i_%s.pdb"%(i,ch),"%i%smin.pdb"%(i,ch),"%i%s.cst"%(i,ch))
# px.minimize("../test28_W.pdb","28Wmin.pdb","28W.cst")
# px.minimize("../test28_Z.pdb","28Zmin.pdb","28Z.cst")

to_min = glob.glob("*min.pdb")
for pdb in to_min:
    for i in range(20):
        if i == 0:
            px.minimize(pdb,"%s1.pdb"%(pdb),"%s.cst"%(pdb.split('min')[0]))
        else:
            px.minimize("%s%i.pdb"%(pdb,i),"%s%i.pdb"%(pdb,i+1),"%s.cst"%(pdb.split('min')[0]))
