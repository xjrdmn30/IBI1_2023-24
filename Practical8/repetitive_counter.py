# Import the regular expression module
import re 
# Define the DNA sequence
seq = "ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA"
# Find all occurrences of the pattern 'GTGTGT+' (three or more consecutive 'GT')
a = re.findall(r'(GTGTGT+)', seq)
# Find all occurrences of the pattern 'GTCTGT+' (two or more consecutive 'GT' followed by a 'C' and then more 'GT')
b = re.findall(r'(GTCTGT+)', seq)
# Calculate the total number of occurrences of the patterns
number = len(a) + len(b)
# Print the total number of occurrences
print(number)
