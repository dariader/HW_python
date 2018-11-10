class Rna: #define  class 
    def __init__(self, acid):
        
        assert isinstance(acid, str)
        self.acid = acid.upper()
        
        if  'C' and 'A' and 'G' and 'U' not in self.acid:
            raise 'That is nor RNA sequence, please, check the data'
        else:
            pass
        
    def gc(self): 
        return (self.acid.count('G') + self.acid.count('C')) / len(self.acid)
    
    def reverse_complement(self):
        return self.acid.translate(str.maketrans('AUGC', 'UACG'))

class Dna: #define  class 
    def __init__(self, acid):
        
        assert isinstance(acid, str)
        self.acid = acid.upper()
        
        if  'C' and 'A' and 'G' and 'T' not in self.acid:
            raise 'That is nor DNA sequence, please, check the data'
        else:
            pass
        
    def gc(self):  
        return (self.acid.count('G') + self.acid.count('C')) / len(self.acid)
    
    def reverse_complement(self):
        return self.acid.translate(str.maketrans('ATGC', 'TACG'))
    
    
    def transcribe(self):
        transcript = self.reverse_complement().translate(str.maketrans('T', 'U'))
        return Rna(transcript)


first = Dna('ATGC')
print(first.reverse_complement())
print(first.gc())
print(first.transcribe())
