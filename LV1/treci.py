lst=[]
while 1:
    
    
    try:
         print("Unesi broj")
         br=input()
         if br=="Done":
            break
         br=float(br)

         lst.append(br)

    except:
         print("Ovo nije broj")

print("Duljina: ", len(lst))
print("Srednja vrijednost: ", sum(lst) / len(lst))
print("minimalna: ", min(lst))
print("Maximalna: ", max(lst))
print("Sortirana lista", sorted(lst))
