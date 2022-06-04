# TABLA DE SIMBOLOS

def updateSimbolTable(simbolo,tipo,tabla_de_simbolos,Simbol_Index):
    tabla_de_simbolos[simbolo] = {} # Nos permite crear un diccionario de tipo NESTED
    tabla_de_simbolos[simbolo]["Index"] = Simbol_Index # Guardamos la posicion en la tabla de simbolos
    tabla_de_simbolos[simbolo]["Type"] = tipo # Guardamos en el diccionario el tipo de la variable
    Simbol_Index = Simbol_Index + 1 # Incrementamos la posicion de la tabla de simbolos
    return Simbol_Index

# CUADRUPLOS
temporales = []     # Variable para ingresar los temporales
temporalCounter = 1 # Variable para contar el numero de temporales (T1 inicial)
sTemporal = "T"     # String constante para los temporales

# Funcion que permite generar cuadruplos
def genTemporales():
    global temporalCounter
    temporal = sTemporal + str(temporalCounter) # Creamos un temporal tipo String
    temporales.append(temporal)                 # Añadimos al arreglo de temporales el string 
    temporalCounter = temporalCounter + 1       # Aumentamos en 1 nuestro contador de temporales

def genCuadruplos(simbolo,operation,pila_operandos):
    if (operation == "="):  # Validacion de Creacion / asignacion
        operand1 = pila_operandos.pop()
        result   = simbolo
        if not simbolo in pila_operandos:                 # Verificamos si el simbolo ya habia sido declarado, para no meterlo en la pila mas veces
            pila_operandos.append(result)        
            cuadruplo = [operation, operand1," ", result] # Armamos el cuadruplo
            print("Cuadruplo -> ",cuadruplo)              # Imprimimos el cuadruplo
            #print(pila_operandos)
            print(" ")
        else:
            cuadruplo = [operation, operand1," ", result] # Armamos el cuadruplo
            print("Cuadruplo -> ",cuadruplo)              # Imprimimos el cuadruplo
            #print(pila_operandos)
            print(" ")
    elif (operation == "++" or operation == "--"):  # Validacion de Creacion / asignacion
        operand1 = simbolo
        result   = simbolo
        if not simbolo in pila_operandos:                 # Verificamos si el simbolo ya habia sido declarado, para no meterlo en la pila mas veces
            pila_operandos.append(result)        
            cuadruplo = [operation, operand1," ", result] # Armamos el cuadruplo
            print("Cuadruplo -> ",cuadruplo)              # Imprimimos el cuadruplo
            #print(pila_operandos)
            print(" ")
        else:
            cuadruplo = [operation, operand1," ", result] # Armamos el cuadruplo
            print("Cuadruplo -> ",cuadruplo)              # Imprimimos el cuadruplo
            #print(pila_operandos)
            print(" ")
    elif(operation == "+" or operation == "-" or operation == "*" or operation == "/"): # Validacion Aritmetica
        operand2 = pila_operandos.pop()
        operand1 = pila_operandos.pop()
        genTemporales()                                     # Generamos un temporal
        result = temporales.pop()     
        pila_operandos.append(result)
        cuadruplo = [operation, operand1, operand2, result] # Armamos el cuadruplo
        print("Cuadruplo -> ",cuadruplo)                    # Imprimimos el cuadruplo
        #print(pila_operandos)
        print(" ")

    elif(operation == "&" or operation == "==" or operation == "!=" or 
        operation == ">" or operation == ">=" or operation == "<=" or 
        operation == "|" or operation == "!" or operation == "<"): # Validacion logica

        operand2 = pila_operandos.pop()
        operand1 = pila_operandos.pop()
        genTemporales()                                     # Generamos un temporal
        result = temporales.pop()    
        pila_operandos.append(result)
        cuadruplo = [operation, operand1, operand2, result] # Armamos el cuadruplo
        print("Cuadruplo -> ",cuadruplo)                    # Imprimimos el cuadruplo
        #print(pila_operandos)
        print(" ")        
    else:
        print(operation)
        print("error detected! bad logic!!")
