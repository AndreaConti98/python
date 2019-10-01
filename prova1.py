'''def printList(L):
    if L:
        print(L[0])
    #[1:]
        printList(L[1:])
        
str=["afgh", "mrml","clct"]
printList(str)'''

'''def fattoriale(n):
    if n ==1:
        return 1
    else:
        return n * fattoriale(n-1)

print (fattoriale(7))'''

'''def countdown(T):
    if T==0:
        return 0
    else:
        print (T)
        return countdown(T-1)

F = int(input("Numero: "))
print (countdown(F))'''

'''def countdown(T):
        return countdown(T)

F = int(input("Numero: "))
print (countdown(F))'''

'''def palindromo(T):
    I, L = T[0], len(T)
    F = T[L-1]
    if I == F or F == 1:
        print ('è palindroma')
    elif I == F:
        return palindromo(T[I+1:F-1])
    else:
        print("non è palindroma")

s = str(input("parola: "))
palindromo(s.replace(" ",""))'''


'''def numeri(R,S,T):
    if T >= S and S >= R:
        print(T)
    elif S >= T and S >= R:
            print (S)
    elif R >= T and R >= S:
                print (R)
    elif R == T and R == S:
        print (R,S,T)
    

a = int(input("numero1: "))
b = int(input("numero2: "))
c = int(input("numero3: "))
numeri(a,b,c)'''



'''def numeri(R,S,T):
    if T >= S and S >= R:
        return T
    elif S >= T and S >= R:
        return S
    elif R >= T and R >= S:
        return R
    elif R == T and R == S:
        return R, S, T

lista = [[1,5,7], [8,9,9], [3,17,1], [21,4,7], [15,15,15], [6,6,3], [12,3,8], [11,4,11]]  

for x in range (0, len(lista), 1):
        print ("Il maggiore è: ", numeri (lista[x][0], lista[x][1], lista[x][2]))'''


'''vocali = ("a","e","i","o","u")

def carattere(L):
    if L in vocali:
        print ("è una vocale")
    else:
        print ("non è una vocale")

Lettera = input("La lettera è: ")
carattere(Lettera.lower())'''





'''def frase(F):
    D = len(F)
    U = D-1
    parola = ""
    
    for x in range(U,-1,-1):
        parola = parola + F[x]
    print (parola)

S = input("inserisci una frase: ")
frase(S)'''


'''def frase(F):
    
    return F[::-1]

S = input("inserisci una frase: ")
print (frase(S))'''


def criptare(F):
    frase = ""
    cifrario = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
            'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
            'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
            'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
            'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
            'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
            'W':'J', 'X':'K', 'Y':'L', 'Z':'M', " ":" "}
    
    for x in range(0,len(F)):
        if (F[x]) in cifrario:
            frase1 = (cifrario[F[x]])
        frase = frase + frase1 
    print (frase)
        

S = input("iserisci una frase: ")
criptare(S)

























