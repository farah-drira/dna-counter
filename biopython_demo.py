from Bio import SeqIO

record = SeqIO.read("example.fasta", "fasta")

print("ID:", record.id)
print("Length:", len(record.seq))
print("Sequence:", record.seq)
print("Reverse complement:", record.seq.reverse_complement())
print("Protein:", record.seq[:12].translate())
