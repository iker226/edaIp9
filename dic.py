#           llave   valor
diasdeMes= {"Enero":31, "Febrero":28, "Marzo":31, "Abril":30, "Mayo":31,
"Junio":30, "Julio":31, "Agosto":31, "Septiembre":30, "Octubre":31,
"Noviembre":30, "Diciembre":31}

print(diasdeMes)
print(diasdeMes.keys())

for llave in diasdeMes.keys():
    print(llave)

print(diasdeMes.items()) #Imprime keys y el contenido 

print("Enero tiene {} dias".format(diasdeMes["Enero"]))
print("Julio tiene {} dias".format(diasdeMes["Julio"]))
print("Agosto tiene {} dias".format(diasdeMes["Agosto"]))
print("Diciembre tiene {} dias".format(diasdeMes["Diciembre"]))
