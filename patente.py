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