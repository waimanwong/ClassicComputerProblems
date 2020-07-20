class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene:str) -> None:
        self.bit_string = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2

            if nucleotide == "A": 
                # change last two bits to 00             
                self.bit_string |= 0b00
            elif nucleotide == "C": 
                # change last two bits to 01             
                self.bit_string |= 0b01
            elif nucleotide == "G":
                # change last two bits to 10             
                self.bit_string |= 0b10
            elif nucleotide == "T":
                # change last two bits to 11
                self.bit_string |= 0b11
            else:
                raise ValueError(f"Invalid Nucleotide:{nucleotide}")

    def decompress(self) -> str:
        gene: str = ""

        for i in range(0, self.bit_string.bit_length() - 1, 2): # - 1 to exclude sentinel
            bits: int = self.bit_string >> i & 0b11 # get just 2 relevant bits
            if bits == 0b00: # A
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif its == 0b11:
                gene += "T"
            else:
                raise ValueError(f"Invalid bits {bits}")
    
    def __str__(self) -> str:
        return self.decompress()

if __name__ == "__main__":
    from sys import getsizeof
    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print("original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original) # compress
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print(compressed)
