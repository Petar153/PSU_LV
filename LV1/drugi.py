while 1:
    try:
         print("Unesi broj izmedu 0.0 i 1.0")
         br=float(input())
         if br>=0.0 and br<=1.0:
            break
         else:
             print("Nije u intervalu")
    except:
         print("Ovo nije broj")

if br>=0.9:
    print("A")
elif br>=0.8:
    print("B")
elif br>=0.7:
    print("C")
elif br>=0.6:
    print("D")
else:
    print("F")
