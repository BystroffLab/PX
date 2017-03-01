import Bio
import Bio.PDB

def getDnaAtoms(structure):
    '''Takes a BioPython PDB structure and extracts and returns a list of the atoms for the PX-DNA (Chains W,X,Y,Z)'''
    output = []
    for char in ['W','X','Y','Z']:
        tempRes = [res for res in structure[0][char]]
        for res in tempRes:
            tempAtom = [atom for atom in res]
            for atom in tempAtom:
                output.append(atom)

    #get rid of the HO atoms that are only present in some structures
    i = 0
    size = len(output)
    while i < size:
        if "HO" in output[i].get_id() or output[i].get_id()[0] == 'H':
            output.pop(i)
            size -= 1
        else:
            i += 1
    return output



def getSuperimposition(base,pdb):
    '''returns and writes out to pdb_sup.pdb the superimposition of the px-dna from pdb onto base.
    INPUT: base - Bio.PDB structure for the base pdb
    INPUT: pdb - Bio.PDB structure for the pdb to be superimposed
    OUTPUT: pdb_sup - Bio.PDB structure for the superimposed PDB, also written to a pdb file'''

    #get all atomsets necessary
    baseDna = getDnaAtoms(base)
    pdbDna = getDnaAtoms(pdb)
    #initialize Superimposer object
    sup = Bio.PDB.Superimposer()
    #Do the superimposition
    try:
        sup.set_atoms(baseDna,pdbDna)
    except Exception as e:
        print baseDna
        print
        print pdbDna
        raise e
    sup.apply(pdb[0].get_atoms())
    #create PDBIO object and save output
    io = Bio.PDB.PDBIO()
    io.set_structure(pdb)
    output = pdb.get_id().split(".pdb")[0]+"_sup.pdb"
    io.save(output)

    #return the superimposed atoms
    return pdb


def main():
    #filename that will be the basis for all of the superimpositions
    base = 'px_base.pdb'
    #list of pdbs to be superimposed
    pdbs = [line.strip() for line in open("pdbs.txt")]
    #Create PDBParser
    p = Bio.PDB.PDBParser()
    baseStructure = p.get_structure(base,base)
    pdbStructures = [p.get_structure(pdb,pdb) for pdb in pdbs]
    SuperimposedStructures = []
    for pdb in pdbStructures:
        print "Superimposing %s"%(pdb.get_id())
        SuperimposedStructures.append(getSuperimposition(baseStructure,pdb))

if __name__ == "__main__":
    main()
