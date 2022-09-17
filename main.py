from colorama import Fore, Back, Style, init
import pyfiglet

T = "BiteDegreesCalc"
ASCII_art_1 = pyfiglet.figlet_format(T)
print(ASCII_art_1)
init()

       
            
def CtoF (degres) :
    degres = (degres *(9/5))+32
    print(degres,scales_fin+"°")
def CtoK (degres) :
    degres = degres + 273.15
    print(degres,scales_fin+"°")
def KtoC (degres) :
    degres = degres - 273.15
    print(degres,scales_fin+"°")
def KtoF (degres) :     
    degres =  (degres - 273.15)*(9/5)+32
    print(degres,scales_fin+"°")
def FtoC (degres) :
    degres = (degres - 32 ) *(5/9)
    print(degres,scales_fin+"°")
def FtoK (degres) : 
    degres = (degres - 32) * (5/9)+273.15
    print(degres,scales_fin+"°")
            
            
            
            
            
print(Fore.GREEN+"temperature scales changer \n")


degres = float(input("First enter number:"))

boucle_enclanchement = False
while boucle_enclanchement == False :
    print("what scales it is ? C/F/K")
    scales_debut = str(input())
    if scales_debut == "C" or scales_debut == "F" or scales_debut == "K" :
        boucle_enclanchement = True
    else :
        pass
boucle_enclanchement2 = False 
while boucle_enclanchement2 == False :
    print("to ? C/F/K")
    scales_fin = str(input())
    if scales_fin == "C" or scales_fin == "F" or scales_fin == "K" :
        boucle_enclanchement2 = True
        
    else :
        pass

if scales_debut == scales_fin :
    print(degres,scales_fin+"°")
elif scales_debut == "C" and scales_fin == "F" :
    CtoF(degres)
elif scales_debut == "C" and scales_fin == "K" :
    CtoK(degres)
elif scales_debut == "F" and scales_fin == "C" :
    FtoC(degres)
elif scales_debut == "F" and scales_fin == "K" :
    FtoK(degres)
elif scales_debut == "K" and scales_fin == "F" :
    KtoF(degres)
elif scales_debut == "K" and scales_fin == "C" :
    KtoC(degres)
else :
    print("error")

input()
input()
