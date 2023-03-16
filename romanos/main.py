'''
1-Crear una funcion que pase de entero >0 y <4000 a romano
2-cualquier otra entrada debe dar error
Casos de prueba
a)1994 -> MCMXCIV
b)4000 -> RomanNumberError("El valor debe ser menor de 4000")
c)"unacadena"-> RomanNumberError("Debe ser un entero")
d) 0-> RomanNumberError("El valor debe ser mayor de cero")
e) -3 ->RomanNumberError("El valor debe ser mayor de cero")
f) 4.5 -> RomanNumberError("Debe ser un entero")
M → 1000
D → 500
C → 100
L → 50
X → 10
V → 5
I → 1
'''
diccionario={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}

dic_entero_a_romanos={
    1:'I',2:'II',3:'III',
    4:'IV',5:'V',6:'VI',
    7:'VII',8:'VIII',9:'IX',

    10:'X',20:'XX',30:'XXX',
    40:'XL',50:'L',60:'LX',
    70:'LXX',80:'LXXX',90:'XC',

    100:'C',200:'CC',300:'CCC',
    400:'CD',500:'D',600:'DC',
    700:'DCC',800:'DCCC',900:'CM',

    1000:'M',2000:'MM',3000:'MMM'
}
#for c,v in diccionario.items():
#    print(c+"-"+str(v))



class RomanNumberError(Exception):
    pass

    #333
    #['0','3'.'3','3']
    #33
    #['0','0'.'3','3']
    #3
    #['0','0'.'0','3']

def entero_a_romano(numero):
    #numero = str(numero)#transformar en cadena
    numero = "{:0>4d}".format(numero)
    list_numero = list(numero)#transformar cadena en lista 
    valor_romano=""

    cont=0
    valor_num=1000
    while cont < len(list_numero):
        list_numero[cont] = int( list_numero[cont])*valor_num
        if list_numero[cont]==0:
            valor_romano+=""
        else:    
            valor_romano +=dic_entero_a_romanos.get(list_numero[cont])
        cont+=1
        valor_num /= 10

    '''
    antiguo for
    for i in range(0,len(list_numero)):#recorriendo la lista
        if i==0:
            list_numero[i] = int( list_numero[i])*1000
            valor_romano += millares.get(list_numero[i])
        elif i==1:
            list_numero[i] = int(list_numero[i])*100 
            valor_romano += centenas.get(list_numero[i])
        elif i==2:
            list_numero[i] = int(list_numero[i])*10
            valor_romano += decenas.get(list_numero[i])
        elif i==3:
            list_numero[i] = int(list_numero[i])
            valor_romano += unidades.get(list_numero[i])
    ''' 
    return valor_romano

print( entero_a_romano(333) )

