maxCalled = 0
minCalled = 0

def max_val(a,b):
    """:param max_val: Funcion que mira cual es el maximo
       :var a,b: se evaluan entre ella para ver cual es mayor"""
    global maxCalled
    maxCalled = maxCalled + 1
  
    if(a > b):
        return a   
    elif(b > a):
        return b
    else:
        return a

def min_val(a,b):
    """:param min_val: funcion en donde se evaluan los minimos
       :var a,b: se estan evaluando entre si para ver cual es menor"""
    global minCalled 
    minCalled = minCalled + 1
  
    if(a < b):
        return a
    elif(b < a):
        return b
    else:
        return a 

def print_usage(init_msg, max_val=True, min_val=True):
    global maxCalled, minCalled
    print (init_msg)
    if max_val:
        print('La funcion max_val fue llamada', maxCalled, ' times')
    if min_val:
        print('La funcion min_val fue llamada', minCalled, ' times')

if __name__ == '__main__':
    print('Llamando a la funcion max_val')
    max_val(1,4)
    max_val(2,b=1)
    max_val(b=4,a=3)

    print('Llamando a la funcion min_val')
    min_val(1,4)
    min_val(2,4)
    min_val(4,b=9)
    """:param print_usage: funcion llamada para imprimir su contenido"""
    print_usage('El uso de las funciones min_val y max_val')
