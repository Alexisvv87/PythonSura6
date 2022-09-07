# los diccionarios son variables especiales
# que me permite almacenar multiples datos de 
# diferente tipo en una sola variable

empleado={
'Nombre':"Juan",
'Cedula':1020408506,
'cargo':"Analista de datos",
'Salario':4000000,
'horastrabajadas':40,
'AplicaSubdetraspote':False,
'deudas':[15000000,800000]

} 

print(empleado)
print(empleado['deudas'][1])

#RECORRIDO UN DICCIONARIO

for observadorAtributo,ObservadorValor in empleado.items():

    print (observadorAtributo)
    print (ObservadorValor)
