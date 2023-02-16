def nuevoTema(tema):
    print("\n===============",tema, "========\n")    

nuevoTema("Operador aritmetico")

print ("operador division entera (10//3)= ",10//3)
print(" Operador Potencia (5**3)=",5 ** 3)

nuevoTema("====== Operadores Logicos =======")

print("Operador and (True and False)=",True and False)

#Actividad: Imprimir la tabla de verdad de los operadores logicos.

nuevoTema("======Operador AND====")

print("Operador and (True and True)=",True and True)
print("Operador and (True and False)=",True and False)
print("Operador and (False and True)=",False and True)
print("Operador and (False and False)=",False and False)

nuevoTema("======Operador NOT====")

print("Operador not ( not True)=", not False)
print("Operador not ( not False)=", not True)
nuevoTema("======Operador OR ====")

print("Operador or (True or True)=",True or True)
print("Operador or (True or False)=",True or False)
print("Operador or (False or True)=",False or True)
print("Operador or (False or False)=",False or False)

nuevoTema("======Operadores de Comparacion====")

print(" 2== 3", 2 == 3)
print("5 > 3", 5 > 3)
print("300 != 200",300 != 200)
print("100000 <= 200000",100000 <= 200000)
print("23 < ",23 < 55)
print("3 >= 3",3 >= 3)

nuevoTema("====== Variables =======")
Variable1 =10
Variable2 =6.2456
Variable3 = "Fermin"
dosPalabras = "Hola"
dos_Palabras = "hello"
s = "\n"

print(Variable1,s,Variable2,s,Variable3,s,dosPalabras,s,dos_Palabras)

a,b,c = 10, 5.16, "Fermin"
print(a,b,c)

#Actividad 
nuevoTema(" ENTEROS ")
w=105
x = 78668965235632
y = -256
z = 0b00110011
h = 0xffa

print(w, type(w))
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(h, type(h))


nuevoTema("FLOTANTES")

x = 1297.50
print(x, type(x))
y = 0.5637939
print(y, type(y))

nuevoTema("NUMEROSCOMPLEJOS")
x= -46j
y = 12+45j
z = 2j

print(x,type(x))
print(y,type(y))
print(z,type(z))

nuevoTema("BOOLEANOS")

lis = [8]
print(lis, 'es', bool(lis))
t = ()
print(t, 'es', bool(t))
new = "hola"
print(new, 'es', bool(new))
num = 99
print(num, 'es', bool(num))
comp = 1 + 0j
print(comp, 'es', bool(comp))
val=None #None equivale a null
print(val, 'es', bool(val))

nuevoTema("LISTAS") # No son Arreglos

a = [10,20.5 , "Python list"]
print (a)
print(a[1])
a[0]="hola"
print(a)


nuevoTema("TUPLAS")

t = (25,'tuple', 1 + 10j, 3.1416)
print(t)
print(t[2])
print("t [1] =",t[1])
print("t[0:2]=",t[0:2])
#t[1] = 34 Operacion no valida en tuplas.
nuevoTema("Conjuntos")
t = {50,20,30,40,10,50}
print(" conjunto t=",t,type(t))

nuevoTema("Diccionario")
d = {1:"valor1","valor2":2j}
print(d,type(d))
print ("d[valor2]:", d["valor2"])

nuevoTema("cadena")
cadena1 = "Cadena con comillas dobles"
cadena2 = 'cadena con comillas simples'

print (cadena1, type(cadena1))
print(cadena2, type(cadena2))

cadenaMultilinea ='''Esta es una cadena de varias
lineas con tabulares y saltos de linea '''

print(cadenaMultilinea)
print("Segmentacion de Cadena")
print(cadena1[5:11])
print(cadena1[:5])
print(cadena1[7:])
print(cadena1[-8:-1])
print(cadena1[0:18:1])
print(cadena1[0:18:2])
print(cadena1[0:18:3])

cadena1 = "Hola"
cadena4 = (cadena1 + " ") * 5
print(cadena4)
cadena5 = cadena4.capitalize()
print(cadena5)