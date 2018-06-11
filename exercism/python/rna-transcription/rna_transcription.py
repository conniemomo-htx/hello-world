def to_rna(dna_strand):

    validdna = ['A','C','G','T']
    validrna = ['U','G','C','A']

    invalid = [ x for x in dna_strand if x not in validdna ]

    rna_strand = "RNA strand is not determined."

    try:
        if ( len(invalid) == 0 ):
            rna_strand = ''.join( validrna[ validdna.index(y) ] for y in dna_strand  )
        else:
            raise ValueError('DNA sequence contains invalid characters')
            
    finally:
        return rna_strand

if __name__ == '__main__':
    print( to_rna(input("Enter DNA Strand: ")))
