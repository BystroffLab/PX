#!/bin/env python
import Bio
import Bio.PDB
import Bio.PDB.Structure
import Bio.PDB.Model
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def get_distances(px_file="px_chains.pdb"):
    parser = Bio.PDB.PDBParser()
    px = parser.get_structure('PX',px_file)
    chainW = px[0]['W']
    chainX = px[0]['X']
    chainY = px[0]['Y']
    chainZ = px[0]['Z']
    dists = {}
    for chain1 in [chainW,chainX]:
        for res1 in chain1:
            for chain2 in [chainY,chainZ]:
                if chain1.get_id() == 'W' and chain2.get_id() != 'Z':
                    continue
                if chain1.get_id() == 'X' and chain2.get_id() != 'Y':
                    continue
                for res2 in chain2:
                    if res1 == res2:
                        continue
                    try:
                        dists[chain1.get_id(),res1.get_id()[1],chain2.get_id(),res2.get_id()[1]] = res1['P']-res2['P']
                    except:
                        pass
    return dists

def write_dist_csv(dists,csv_file):
    fout = open(csv_file,'w+')
    fout.write("chain1,res1,chain2,res2,dist\n")
    for chain1 in ['W','X','Y','Z']:
        for res1 in range(29):
            for chain2 in ['W','X','Y','Z']:
                for res2 in range(29):
                    try:
                        if 35 <= dists[(chain1,res1,chain2,res2)] and dists[(chain1,res1,chain2,res2)] <= 39:
                            fout.write("%s, %i, %s, %i, %f\n"%(chain1,res1,chain2,res2,dists[(chain1,res1,chain2,res2)]))
                    except:
                        pass
    fout.close()

def main():
    dists = get_distances()
    write_dist_csv(dists,"phos_dists.csv")

if __name__ == "__main__":
    main()
