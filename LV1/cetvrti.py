print("Ime datoteke: ")
ime = input()
average=0.0
br=0
file=open(ime)
for line in file:
    line=line.rstrip()
    words = line.split()
    if len(words)<=1:
        continue
    if words[0] == "X-DSPAM-Confidence:":
        average=average+float(words[1])
        br=br+1
print("Average X-DSPAM-Confidence: ", average/br)
file.close()