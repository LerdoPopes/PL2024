import re 
import sys

def somador(input):
    
    contador = 0
    #numero_string = ""
    #numero_inteiro = 0
    estado = False
    
    lista_final = []
    
    #Versão que soma o contador número a número 
    with open(input,"r") as ficheiro:
        
        # Adicionar todos os On/Off/=/números numa lista
        for line in ficheiro:
            capture = re.findall(r'(on|off|=|\d)', line, re.IGNORECASE)
            lista_final.extend(capture)
        for elemento in lista_final:
            if elemento == "=":
                print("Total atual : " + str(contador)) 
            elif elemento.isnumeric() and estado == True:
                contador += int(elemento)
            elif elemento.upper() == "OFF":
                estado = False
            elif elemento.upper() == "ON":
                estado = True        

    #with open(input,"r") as ficheiro:
    #    for line in ficheiro:
    #        capture = re.findall(r'(on|off|=|\d)', line, re.IGNORECASE)
    #        lista_final.extend(capture)
    #    print(lista_final)
    #    for elemento in lista_final:
    #        if elemento == "=":
    #            print(contador) 
    #        elif elemento.isnumeric() and estado == True:
    #           numero_string += elemento
    #        elif elemento.upper() == "OFF" and estado == True:
    #            numero_inteiro = int(numero_string)
    #            numero_string = ""
    #            contador += numero_inteiro
    #            estado = False
    #        elif elemento.upper() == "ON" and estado == True:
    #            numero_inteiro = int(numero_string)
    #            numero_string = ""
    #            contador += numero_inteiro
    #            estado = True
    #        elif elemento.upper() == "ON" and estado == False:
    #            estado == True
    #        elif elemento.upper() == "OFF" and estado == False:
    #            estado == False

                
if __name__ == "__main__":
    
    somador("input.txt")
