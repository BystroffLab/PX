#!/bin/env python
import sys
output = {}

with open("apc.csv") as fin:
    for line in fin:
        line = line.split(',')
        apc_score = float(line[2])
        if apc_score > 100:
            apc_score = 100.
        phosphate = line[0].split(".pdb")[0]
        resn = int(phosphate[:len(phosphate)-1])
        chain = phosphate[len(phosphate)-1].upper()
        output[(resn,chain)] = apc_score
    fin.close()

with open("px_chains.pdb") as fin:
    pdblines = [line.strip() for line in fin]
    fin.close()

fout = open("px_apc.pdb","w+")
for line in pdblines:
    if line[:6] != "ATOM  ":
        fout.write(line)
        fout.write('\n')
    else:
        resn = int(line[22:26])
        chain = line[21].upper()
        fout.write(line[:60])
        string = "%6.2f"%(output[(resn,chain)])
        fout.write(string)
        fout.write(line[66:])
        fout.write('\n')
fout.close()
