sequence = ""

with open("example.fasta") as file:
    for line in file:
        line = line.strip()
        if not line.startswith(">"):
            sequence += line

for base in "ATGC":
    print(base, ":", sequence.count(base))

gc = (sequence.count("G") + sequence.count("C")) / len(sequence) * 100
print("GC content:", round(gc, 1), "%")
