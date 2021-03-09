from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

Condon = Tuple[Nucleotide, Nucleotide, Nucleotide]

Gene = List[Condon]

gene_str: str = 'ACGTGGTC'

def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i+2) >= len(s):
            return gene
        condon: Condon = (Nucleotide[s[i]], Nucleotide[s[i+1]], Nucleotide[s[i+2]])
        gene.append(condon)
    return condon

string_to_gene(gene_str)

