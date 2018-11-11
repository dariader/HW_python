class Rna: #define  class 
    def __init__(self, acid):
        
        assert isinstance(acid, str)
        
        self.acid = acid.upper()
        
        if 'C' and 'A' and 'G' and 'U' not in self.acid:
            raise 'TypeError01: Not RNA sequence, please, check the data'
        else:
            pass
        
    def gc(self): 
        return (self.acid.count('G') + self.acid.count('C')) / len(self.acid)
    
    def reverse_complement(self):
        return self.acid.translate(str.maketrans('AUGC', 'UACG'))[::-1]

class Dna(Rna): #define  class 
    def __init__(self, acid):
        
        assert isinstance(acid, str)
        self.acid = acid.upper()
        
        if 'C' and 'A' and 'G' and 'T' not in self.acid:
            raise 'TypeError01: Not DNA sequence, please, check the data'
        else:
            pass
    def reverse_complement(self):
        return self.acid.translate(str.maketrans('ATGC', 'TACG'))[::-1]
    
     
    def transcribe(self):
        transcript = Rna(self.acid.translate(str.maketrans('T', 'U')))
        print(transcript.acid) #to check the result
        return transcript #to return an object
    
    ###test data
first = Dna(('AGATACACA'))
print(first.reverse_complement())
print(first.gc())
second = first.transcribe()
print(second)
second.reverse_complement()
