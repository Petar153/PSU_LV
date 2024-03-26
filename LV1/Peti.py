file=open("song.txt")

rjecnik={}
for line in file:
    line=line.rstrip()
    words = line.split()
    for i in words:
        if i in
    rjecnik[words]+=1
    

for rj in rjecnik:
    if rjecnik[rj]==1:
        print(rj)




file.close()