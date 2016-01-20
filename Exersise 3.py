from bitarray import bitarray		#To Install "sudo pip install bitarray"
import mmh3		#To Install "sudo pip install mmh3"
import string

class BloomFilter:
    
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        
    def add(self, string):
        for seed in xrange(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            self.bit_array[result] = 1
            
    def lookup(self, string):
                punctuations = "!@#$%^&*()-_[]{}\|;:\"?/<>,."				
                clean_string = ""
                puncts = ""

                for char in string:
                    if char not in punctuations:
						clean_string += char
						puncts += " "
                    else:
						puncts += char
                            
                str_tmp = clean_string.lower()
				
                for seed in xrange(self.hash_count):
                    result = mmh3.hash(str_tmp, seed) % self.size
                    if self.bit_array[result] == 0:                  
						string = "--"+clean_string+"--"
						gaps = len(clean_string)*" "
						return puncts.replace(gaps, string)
                return string
 
bf = BloomFilter(500000, 7)

lines = open("american-english").read().splitlines()		#Cross-Platform (You will need the 'american-english' file from Linux)
#lines = open("/usr/share/dict/american-english").read().splitlines()		#Linux

for line in lines:
    bf.add(line)

str = raw_input(">Enter Phrase to Check: ")
str = str.split(" ")
for i in str:
	#print str		//[FOR DEBUGGING PURPOSES]
	if "-" in i[1:-1]:
		words = i.split("-")
		word = []
		for j in words:
			word.append(bf.lookup(j))
		print "-".join(word),		
	else:
		print bf.lookup(i),