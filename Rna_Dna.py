class Rna: #define  class 
    def __init__(self, acid):
        
        assert isinstance(acid, str)
        self.reverse_complement = ""
        self.acid = acid.upper()
        
        if not filter(lambda m: m not in 'AUGC', self.acid):
            raise 'TypeError01: Not RNA sequence, please, check the data'
        else:
            print(acid, '5-3 RNA is your input')
            pass
        
        
    def gc(self): 
        return (self.acid.count('G') + self.acid.count('C')) / len(self.acid)
    
    def reverse_complement(self):
        
        return self.acid.translate(str.maketrans('AUGC', 'UACG'))[::-1]

class Dna(Rna): #define  class 
    def __init__(self, acid):
        
        assert isinstance(acid, str)
        self.acid = acid.upper()
            
        if not filter(lambda m: m not in 'ATGC', self.acid):
            raise 'TypeError01: Not DNA sequence, please, check the data'
        else:
            print(acid, '5-3 DNA is your input')
            pass
        
    def reverse_complement(self):
        return self.acid.translate(str.maketrans('ATGC', 'TACG'))[::-1]
        
    
    def transcribe(self):
        transcript = Rna(self.acid.translate(str.maketrans('T', 'U'))) 
        
        
        return (transcript.acid)         #returns 5' - 3' RNA
    
    
 ############# Usage examples
    
input_dna = Dna(('GGGG'))
print(input_dna.reverse_complement())
print(input_dna.gc())
output_rna = input_dna.transcribe()
print(output_rna)
