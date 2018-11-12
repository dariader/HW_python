class Rna: #define  class 
    def __init__(self, acid):
        
        assert isinstance(acid, str)
        
        self.acid = acid.upper()
        
        if 'A' and 'C' and 'G' and 'U' in self.acid:
              raise 'TypeError01: Not RNA sequence, please, check the data'
        else:
            pass
        
        
    def gc(self): 
        print(self.acid, 'is your input, GC content is')
        return (self.acid.count('G') + self.acid.count('C')) / len(self.acid)
    
    def reverse_complement(self):
        print(self.acid, '5-3 RNA is your input, reverse complement is')
        return self.acid.translate(str.maketrans('AUGC', 'UACG'))[::-1]

class Dna(Rna): #define  class 
    def __init__(self, acid):
        
        assert isinstance(acid, str)
        self.acid = acid.upper()
        
        
        if 'A' and 'C' and 'G' and 'T' in self.acid:
              raise 'TypeError01: Not DNA sequence, please, check the data'
        else:
            pass
        
    def reverse_complement(self):
        print(self.acid, '5-3 DNA is your input, reverse complement is')
            
        return self.acid.translate(str.maketrans('ATGC', 'TACG'))[::-1]
        
    
    def transcribe(self):
           
        transcript = Rna(self.acid.translate(str.maketrans('T', 'U'))) 
        print(self.acid, '5-3 DNA is your input, transcript is','\n', transcript.acid)
         
        return transcript     #returns 5' - 3' RNA
    
    ###############test data
first = Dna(('AGATACACA'))
print(first.reverse_complement())
print(first.gc())
second = first.transcribe()
print(second)
second.reverse_complement()
first = Rna('GATTACA')
print(first.reverse_complement())
print(first.gc())
