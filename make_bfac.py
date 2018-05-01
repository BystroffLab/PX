#!/bin/env python
"""
This script was used to help generate publication figures.  Changes bfactor to
atom_pair_constraint score value.  This will allow easy coloring of a structure
cartoon.
"""
import sys
output = {}

# read the scores
with open("apc.csv") as fin:
    for line in fin:
        line = line.split(',')
        apc_score = float(line[2])
        if apc_score > 100:
            apc_score = 100.
        # identify the phosphate chain and number
        phosphate = line[0].split(".pdb")[0]
        resn = int(phosphate[:len(phosphate)-1])
        chain = phosphate[len(phosphate)-1].upper()
        # save the score
        output[(resn,chain)] = apc_score
    fin.close()

# read px structure
with open("px_chains.pdb") as fin:
    pdblines = [line.strip() for line in fin]
    fin.close()
# output with new bfactors
fout = open("px_apc.pdb","w+")
for line in pdblines:
    # skip non-atom lines
    if line[:6] != "ATOM  ":
        fout.write(line)
        fout.write('\n')
    else:
        # get the residue number and chain
        resn = int(line[22:26])
        chain = line[21].upper()
        # write up to the bfactor line
        fout.write(line[:60])
        # write the corresponding bfactor for that phosphate
        string = "%6.2f"%(output[(resn,chain)])
        fout.write(string)
        # write the rest of the line
        fout.write(line[66:])
        fout.write('\n')
fout.close()
