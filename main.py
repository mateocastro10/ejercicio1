import csv
archivo = open('Libro1.csv')
reader = csv.reader(archivo,delimiter=',')
for fila in reader:
 nv = int(fila[1])
 d = str(fila[2])
 n = str(fila[3])
 a = str(fila[4])
 ma = int(fila[5])
 Viajero[i] = ViajeroFrecuente(nv,d, n, a, ma)

 lineaCompleta = fila + [round(costo,2)]
 print(lineaCompleta)
print('Total de compra: {0:.2f}'.format(total))
archivo.close()
