import re 
import sys

def somador(input):
    
    contador = 0
    estado = False
    
    lista_final = []
    
    with open(input,"r") as ficheiro:
        
        # Adicionar todos os On/Off/=/números numa lista
        for line in ficheiro:
            capture = re.findall(r'(on|off|=|\d+)', line, re.IGNORECASE)
            lista_final.extend(capture)
        print(lista_final)
        for elemento in lista_final:
            if elemento == "=":
                print("Total atual : " + str(contador)) 
            elif elemento.isnumeric() and estado == True:
                contador += int(elemento)
            elif elemento.upper() == "OFF":
                estado = False
            elif elemento.upper() == "ON":
                estado = True        
                
if __name__ == "__main__":
    
    somador("input.txt")
