sequence = "ATGCGTACGTTAGC"

for base in "ATGC":
    print(base, ":", sequence.count(base))

gc = (sequence.count("G") + sequence.count("C")) / len(sequence) * 100
print("GC content:", round(gc, 1), "%")
