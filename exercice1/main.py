L= [17,38,10,25,72,45,14]
print(L)
#3. Afficher l’indice de l’élément 17
indx=L.index(17)
print(indx)
# 5. Ajouter la valeur 30 entre 25 et 72.
L.insert(4,30)
print(L)

# 1. Ajouter la valeur 1 à chacun de ses éléments.

a=0
while a<len(L) :
    L[a]+=1
    a+=1    
print(L)
# 2. Ajouter les valeurs 12 et 13 à la fin de la liste et afficher la liste.
L.append(12)
L.append(13)
print(L)
#4. Construire la liste "paires" qui contient les nombres pairs de L et la liste "impaire" qui contient les nombres "impaires" de L.

paires=[]
impaire=[]
x=0
for x in L :
    

 
    if x%2==0 :
        paires.append(x)
        
    else: 
        impaire.append(x)
        


print("list paire")       
print(paires)
print("list impaire")  
print(impaire)
# 5. Ajouter la valeur 30 entre 25 et 72.
L.insert(3,30)
print(L)
# Supprimer la valeur 30.
L.remove(30)
print(L)
# 7. Inverser l'ordre des éléments de L.
L.reverse()
print(L)
# 8. Demander à l'utilisateur de fournir un nombre au hasard et dire si ce nombre est présent dans L.
# number=input("enter un nombre au hasard")
def verifier_number(num,l):
    x=0
    for x in l:
        if x==num:
            print("le nombre existe dans la liste !" )
        else:
             print("le nombre n\'existe pas dans la liste !" )
        break




verifier_number(10,L)
#9. Afficher la sous-liste du 2e au 3e élément.
print(L[1:3])
#10. Afficher la sous-liste du début au 2e élément.
print(L[:3])
#11. Afficher le dernier élément en utilisant un indice négatif.
print(L[-1:])