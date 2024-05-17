# Import the regular expression module
import re
# Prompt the user to enter the repetitive sequence
repeat_sequence = input("Enter the repetitive sequence (GTGTGT or GTCTGT): ")
# Define the filename of the input FASTA file
filename = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
# Define the filename for the output file containing duplicate genes
output_file = repeat_sequence + "_duplicate_genes.fa"
# Open the input FASTA file for reading
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", 'r') as content:
    genes = []  # List to store gene IDs and sequences
    gene_id = None  # Variable to store the current gene ID
    gene_sequence = ""  # Variable to store the current gene sequence
    genes_str = ""  # String to store the formatted output
    output_1 = False  # Flag to indicate whether to output the current gene
    # Iterate through each line in the input file
    for line in content:
        # Check if the line starts with ">"
        if line.startswith(">"):
            # If we have processed a gene and have its ID, add it to the list of genes
            if output_1 == True and gene_id:
                genes.append((gene_id, gene_sequence))
            
            # Count the number of repetitions of the repeat sequence in the gene sequence
            repeat_count = gene_sequence.count(repeat_sequence)
            
            # Extract the gene ID from the line
            gene_id = line[1:].split()[0]
            
            # Reset the gene sequence
            gene_sequence = ""
            
            # Reset the output flag
            output_1 = False
            
            # Check if the line contains the word "duplication"
            if re.search(r'duplication', line):
                output_1 = True
        else:
            # If the output flag is True, append the line to the gene sequence
            if output_1 == True:
                gene_sequence += line

# Process each gene in the list
for gene_id, gene_sequence in genes:
    # Count the number of repetitions of the repeat sequence in the gene sequence
    repeat_count = gene_sequence.count(repeat_sequence)
    
    # Format the gene information and append it to the output string
    genes_str += f">{gene_id}:{repeat_count}\n{gene_sequence}\n"
# Write the formatted output to the output file
with open(output_file, 'w') as output:
    output.write(genes_str)
# Print the filename of the output file
print(output_file)
