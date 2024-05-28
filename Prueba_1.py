#Ingreso de datos del usuario

print("***** Bienvenidos a Burguer King *****")
cliente= input("Por favor ingrese su nombre: ")
cedula= int(input("Por favor ingrese su numero de cedula: "))
correo= input("Por favor ingrese su correo electronico: ")
cantidadHamburguesas= int(input("Por favor ingrese la cantidad que desea adquirir: "))
print("Por favor seleccione el tipo de hamburguesa que va a adquirir: ")
print("1) Sencilla")
print("2) Doble")
print("3) Triple")
tipoHamburguesa= int(input("Por favor ingrese el numero correspondiente: "))
print("Por favor seleccione la forma de pago: ")
print("1) Tarjeta de credito")
print("2) Efectivo")
formaPago= int(input("Por favor ingrese el numero correspondiente: "))
costo=0.0
total=0.0

#Calculos

if (tipoHamburguesa==1):
    costo = float(cantidadHamburguesas*1.5)
elif (tipoHamburguesa==2):
    costo = float(cantidadHamburguesas*2.50)
elif (tipoHamburguesa==3):
    costo = float(cantidadHamburguesas*3.25)
else:
    print("Por favor introduzca un tipo de hamburguesa valido")    


if (formaPago==1):
    total = float(costo+(costo*0.05))
    print("El valor total de su compra es: ",total)
elif (formaPago==2):
    total = (costo)
    print("El valor total de su compra es: ",costo)
else:
    print("Por favor introduzca una forma de pago valida") 

numeroTruncado= round(total, 2)

#Impresion de resultado

print("*****Factura*****")
print("Nombre del cliente: ",cliente)
print("Cedula:" ,cedula)
print("Correo electronico: ",correo)
print("Cantidad de hamburguesas adquiridas: ",cantidadHamburguesas)
print("Tipo de Hamburguesa: ",tipoHamburguesa)
print("Forma de pago: " ,formaPago)
print("El valor total su compra es de: ",numeroTruncado)
print("Muchas gracias por su compra")
print("La factura se enviara a su correo electronico: ",correo)
