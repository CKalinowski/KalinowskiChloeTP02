print ('1.1 accès aux éléments d’une chaine')
ch = 'Esope reste ici et se repose' 
longueur = len(ch)
print(longueur)
mot = ch.split(" ")
print(mot[1:2])
print(mot[5:6])
print(mot[5:])
print(ch[13:14])
print(ch[13])

print('1.2 Utilisation combinée de chaines et de variables')
# afficher aujourd’hui, il fait 24° , la vitesse du vent est 12Km/h ,l’humidité est 45%' 
meteo = 'aujourd’hui, il fait %s , la vitesse du vent est %s ,l’humidité est %s' 
tempDeg = "24°"
vitesse = "12Km/h"
humidite = "45%"

print(meteo % (tempDeg, vitesse, humidite))

#aujourd’hui, il fait beau , la vitesse du vent est faible ,l’humidité est correcte
beau = 'beau'
faible = 'faible'
correcte = 'correcte'

print(meteo % (beau, faible, correcte))

# afficher cette chaine contient 34 caractères et  celle-ci contient 40 caractères par contre

chaineA = "cette chaine" 
chaineB = "contient %s caractères" 
chaineC = "par contre" 
chaineD = "celle-ci" 
chaine1 = chaineA + ' ' + chaineB
chaine2 = chaineD + ' ' + chaineB + ' ' + chaineC
print(chaine1 % len(chaine1))
print(chaine2 % len(chaine2))


chaineBnew = chaineB.replace('%s','{}') 
print(chaineBnew)
#chaineE est construite à partir des chaines chaineA et chaineBnew 
#chaineF est construite à partir des chaines chaineD chaineBnew et chaineC 
chaineE = chaineA + ' ' + chaineBnew
chaineF = chaineD + ' ' + chaineBnew + ' ' + chaineC
longueurE = len(chaineE)
longueurF = len(chaineF)
print(chaineE.format(longueurE))
print(chaineF.format(longueurF))