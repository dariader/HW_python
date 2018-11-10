class Rna: #define  class 
    def __init__(self, acid):
        self.acid = list(acid)
        
        if  'C' and 'A' and 'G' and 'U' not in list(self.acid):
            raise 'That is nor RNA sequence, please, check the data'
        else:
            pass
        
    def gc(self):
        j = 0
        for i in self.acid:
            if i == 'G' or i == 'C':
                j = j + 1
            else:
                print('0','%')
        return (j/len(self.acid)*100,'%')
    
    def reverse_complement(self):
        j = []
        for i in self.acid: # not really good dictionary. 
            if i == 'G':
                j += 'C'
            else:
                if i == 'C':
                    j += 'G'
                else: 
                    if i == 'A':
                        j += 'U'
                    else:
                        if i == 'U':
                            j += 'A'
        return j[::-1]   

class Dna: #define  class 
    def __init__(self, acid):
        self.acid = list(acid)
        
        if  'C' and 'A' and 'G' and 'T' not in list(self.acid):
            raise 'That is nor RNA sequence, please, check the data'
        else:
            pass
        
    def gc(self):
        j = 0
        for i in self.acid:
            if i == 'G' or i == 'C':
                j = j + 1
            else:
                print('0','%')
        return (j/len(self.acid)*100,'%')
    
    def reverse_complement(self):
        j = []
        for i in self.acid:
            if i == 'G':
                j += 'C'
            else:
                if i == 'C':
                    j += 'G'
                else: 
                    if i == 'A':
                        j += 'T'
                    else:
                        if i == 'T':
                            j += 'A'
        return j[::-1]   
    
    
    def transcribe(self): 
        j = []
        for i in self.acid:
            if i == 'G':
                j += 'C'
            else:
                if i == 'C':
                    j += 'G'
                else: 
                    if i == 'A':
                        j += 'U'
                    else:
                        if i == 'T':
                            j += 'A'
        return Rna(j)


first = Dna('ATGC')
first.reverse_complement()
first.transcribe()
