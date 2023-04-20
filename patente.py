import os
import time
import pickle

os.system ("cls")


class guardarpatente():
    def init(self):
        self.patentes = ""

def clear():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def validarPatente(patente): 
    if len(patente) > 5 and len(patente) < 8:
        if not patente[0:2].isalpha():
            print("Ingrese una patente valida")
            return False
        elif not patente[2].isalnum(): 
            print("Ingrese una patente valida")
            return False
        elif not patente[3:5].isdigit():
            print("Ingrese una patente valida")
            return False
        elif not patente[5].isalnum():
            print("Ingrese una patente valida")
            return False 
        elif  len(patente) == 7:
            if not patente[6].isalpha():
                print("Ingrese una patente valida")
                return False
            else:
                return True
        else:
            return True
    else:
        print("Ingrese una patente valida")
        return False
    
def buscarpatente(patente):
    b = False
    tamarchpat=os.path.getsize(afpatentes)
    alpatentes.seek(0)
    while alpatentes.tell()<tamarchpat and b == False:
        punteropat = alpatentes.tell()
        regp=pickle.load(alpatentes)
        if regp.patentes == patente:
            b = True
            return punteropat
        else:
            print("error")
    buscarpatente = b
            
            

def Menu1():
 print("")
 print()
 print("Menu principal:")
 print("")
 print(" |1| patentes \n |2| patentes registradas \n |0|Fin del programa \n")

def incorrecto():
    print("Opcion incorrecta")



os.chdir("c:/")
if os.path.exists("patentes-registradas") == True:
    print("")
else:
    os.mkdir("patentes-registradas")

#guardar las patentes registradas
afpatentes = "c:\\patentes-registradas\\patentes.dat"

if not os.path.exists(afpatentes):
    alpatentes = open(afpatentes, "w+b")
else:
    alpatentes = open (afpatentes, "r+b")

regp=guardarpatente()


Menu1()
menu = str(input("Ingrese una opcion: \n"))
clear()
while menu != "0":
    if menu == "1":    
        patenteValida = False
        while not patenteValida:
            patente = ""
            patente = (str(input("Ingrese la Patente: \n"))).upper()
            patenteValida = validarPatente(patente)
            clear()
            if patenteValida == True:
                regp=guardarpatente()
                print(patente)
                print("la patente se guardo")
                alpatentes.seek(0)
                pickle.dump(regp,alpatentes)
                alpatentes.flush()
            elif patenteValida == False:
                print("patente es invalida ingrese una correcta")
                patente = ""
                patente = (str(input("Ingrese la Patente: \n"))).upper()
                patenteValida = validarPatente(patente)
                patente=patente.ljust(7, " ")
                clear()
            else:
                print("")
            Menu1()
            menuPrincipal = str(input("Ingrese una opcion: \n"))
            clear() 
    elif menu == "2":
        pat1 = (str(input("Ingrese la Patente 1: \n"))).upper()
        if buscarpatente == True:
            print() 
            print("hola")
        else:
            print("patente no existe ")
        pat1 = (str(input("Ingrese la Patente 2: \n"))).upper()
    elif menu == "0":
        print("Salir del programa")
    else:
        incorrecto()
    Menu1()
    menu = str(input("Ingrese una opcion: \n"))
    clear()   