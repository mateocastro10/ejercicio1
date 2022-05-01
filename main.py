from mail import Email
import csv

if __name__=='__main__':
    i = input("ingrese id cuenta")
    d = input("ingrese dominio")
    t = input("ingrese tipo de dominio")
    c = input("ingrese contraseña")
    nombre = input("ingrese su nombre")
    unMail = Email(i, d, t, c)
    print('Estimado, {}, le enviaremos los mensajes a su cuenta: {}'.format(nombre, unMail.retornamail()))
    unMail.getDominio()
    unMail.modifica()
    mail = input("ingrese correo")
    otroMail = Email('a', 'b', 'c', 'd')
    otroMail.crearcuenta(mail)
    archivo = open('Correos.csv')
    reader = csv.reader(archivo,delimiter=',')
    cont = 0
    id=input('Ingrese identificador a buscar: ')
    for fila in reader:
        i = str(fila[0])
        d = str(fila[1])
        t = str(fila[2])
        c = str(fila[3])
        if fila[0] == id:
            cont += 1
    print("La cantidad de personas con el identificador '{}' es: {}".format(id,cont))
    if cont > 1:
        print("El identificador se repite")
    else:
        print("El identificador no se repite")
    archivo.close()
