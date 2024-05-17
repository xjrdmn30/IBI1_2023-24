import re
repeat_sequence=input("Enter the repetitive sequence (GTGTGT or GTCTGT): ")

filename="Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"

output_file = repeat_sequence+"_duplicate_genes.fa"


with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r') as content :
    genes=[]
    gene_id=None
    gene_sequence=""
    genes_str = ""
    output_1= False

    
    for line in content:
        if line.startswith(">"):
            if output_1==True and gene_id :
                genes.append((gene_id, gene_sequence))
            repeat_count = gene_sequence.count(repeat_sequence)
            gene_id=line[1:].split()[0]
            gene_sequence=""
            output_1=False
            if re.search(r'duplication', line):
                output_1=True
                
        else: 
            if output_1==True :
                gene_sequence+=line
                    

for gene_id, gene_sequence in genes:
        repeat_count = gene_sequence.count(repeat_sequence)
        genes_str+= f">{gene_id}:{repeat_count}\n{gene_sequence}\n"


with open(output_file, 'w') as output:
    output.write(genes_str)
            
print(output_file)


