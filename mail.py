class Email:
    __idCuenta= str
    __dominio= str
    __tipodominio= str
    __contraseña= str
    def __init__(self, i=None, d=None, t=None, c=None):
        if(type(t)==str and type(d)==str and type(i)==str and type(c)==str):
            self.__idcuenta = i
            self.__dominio= d
            self.__tipodominio = t
            self.__contraseña = c
        else:
            print('DATOS INCORRECTOS')

    def retornamail(self):
        cadena=(self.__idcuenta + '@')+(self.__dominio + '.')+(self.__tipodominio)
        return cadena

    def __str__(self):
        return "%s %s %s %s" % (self.__idcuenta,self.__dominio,self.__tipodominio,self.__contraseña)
    def getDominio(self):
            return(self.__dominio)

    def crearcuenta(self,mail):
        if(type(mail)==Email):
            if (mail.find('@')!= -1):
                xc= mail.split('@')
                idnuevo= xc[0]
                if (xc[1].find('.')!= -1):
                    dc= xc[1].split('.')
                    xd= dc[0]
                    xtd= dc[1]
                    c=input('ingrese contraseña')
                    self.__init__(idnuevo,xd,xtd,c)
                    print('Correo creado con exito')
                else: print('Error: El dominio no contiene punto')
            else: print ('Error: El correo ingresado no contiene @')

    def modifica(self):
        x = input("ingrese contraseña actual")
        while(x != self.__contraseña):
            print("contraseña incorrecta")
            x = input("ingrese contraseña actual")
        else:
             self.__contraseña = input("ingrese nueva contraseña")
