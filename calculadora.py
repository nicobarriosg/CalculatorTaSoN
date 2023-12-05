def menu():
    while True:
        try:
            print("Calculadora TaSoN")
            print("1)Ingresar un triangulo a calcular")
            print("2)Salir")
            opcion=int(input("\nIngrese la opcion deseada: "))
            if opcion>=1 and opcion<=2:
                return opcion
            else:
                print("\nIngrese solo opciones validas")
        except:
            print("\nIngrese solo numeros")
          
def leerLados():
    while True:
        try:
            lado_a=float(input("\nIngrese la longitud del lado a: "))
            lado_b=float(input("Ingrese la longitud del lado b: "))
            lado_c=float(input("Ingrese la longitud del lado c: "))
            if lado_a+lado_b>lado_c and lado_b+lado_c>lado_a and lado_a+lado_c>lado_b:
                return lado_a, lado_b, lado_c
            else:
                print("Los lados no forman un triangulo valido")
        except:
            print("Ingrese solo numeros validos")
    
def calculadora_trigonometrica_lados(a, b, c):
        seno = b / c
        coseno = a / c
        tangente = seno / coseno
        cosecante = 1 / seno
        secante = 1 / coseno
        cotangente = coseno / seno
        
        return  "\nSeno: "+str(seno)+"\n"+\
                "Coseno: "+str(coseno)+"\n"+\
                "Tangente: "+str(tangente)+"\n"+\
                "Secante: "+str(secante)+"\n"+\
                "Cosecante: "+str(cosecante)+"\n"+\
                "Cotangente: "+str(cotangente)+"\n"

#MAIN
while True:
    opcion=menu()
    if opcion==1:
        a,b,c=leerLados()
        print(calculadora_trigonometrica_lados(a,b,c))
    else:
        break