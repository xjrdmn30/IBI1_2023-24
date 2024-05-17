import re 
seq="ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA"
a=re.findall(r'(GTGTGT+)',seq)
b=re.findall(r'(GTCTGT+)',seq)
number=len(a)+len(b)
print(number)

