
#Autor:Vanessa Diaz Layton
def Numerico(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False

print ("Calculadora")       
print ("Ingrese el digito correspondiente a la operacion que quiere realizar")
Operacion=int(input(" 1.Suma\n 2.Resta\n 3.Multiplicacion\n 4.División\n 5.Salir\n"))

while(Operacion!=5):
    
    if (Operacion!=5):
        Numero1=input("Ingrese el primer numero\n")
        Numero2=input("Ingrese el segundo numero\n")

        while Numerico(Numero1)==False or Numerico(Numero2)==False:
            print("Uno de los valores ingresados no corresponde con un numero, Por favor ingreselos nuevamente")
            Numero1=input("Ingrese el primer numero\n")
            Numero2=input("Ingrese el segundo numero\n")

        Numero1=float(Numero1)
        Numero2=float(Numero2)

    if Operacion==1:
        Suma=Numero1+Numero2
        print("El resultado de la suma es:", Suma)
        del Suma
    elif Operacion==2:
        Resta=Numero1-Numero2
        print("El resultado de la resta es: ", Resta)
        del Resta
    elif Operacion==3:
        Multiplicacion=Numero1*Numero2
        print("El resultado de la multiplicacion es: ", Multiplicacion)
        del Multiplicacion
    elif Operacion==4:
        try:
            Division= Numero1/Numero2
            print("El resultado de la division es: ", Division)
            del Division   
        except ZeroDivisionError as e:
            print(e,"La division no es valida")       
    else:
        print("El numero ingresado no se encuentra dentro de las opciones\n")
    del Operacion
    del Numero1
    del Numero2
    print("=======================================\n")
    print ("Ingrese el digito correspondiente a la operacion que quiere realizar")
    Operacion=int(input(" 1.Suma\n 2.Resta\n 3.Multiplicacion\n 4.División\n 5.Salir\n"))

