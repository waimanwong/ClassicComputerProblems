from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide] # alias for codons
Gene = List[Codon] # alias for gene

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"

def string_to_gene(s: str) -> Gene:
    gene: Gene =[]
    for i in range (0, len(s), 3):
        if(i+2) >= len(s):
            return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i+1]], Nucleotide[s[i+2]])
        gene.append(codon)

    return gene

def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    
    return False

if __name__ == "__main__":
    my_gene = string_to_gene(gene_str)
    
    acg = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
    gat = (Nucleotide.G, Nucleotide.A, Nucleotide.T)

    #Equivalent
    print(acg in my_gene)
    print (linear_contains(my_gene, acg))

    #Equivalent
    print(gat in my_gene) 
    print (linear_contains(my_gene, gat))
    
