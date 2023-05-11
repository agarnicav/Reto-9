
# Punto 1

De los retos anteriores seleciones 3 funciones y escribalas en forma de lambdas.

1. calcular el factorial de un número ingresado por el usuario.

       if __name__ == "__main__":
           a = int(input("Ingrese número a: "))
  
           factorial = lambda n: 1 if n == 0 else n * factorial(n-1)
           for b in range(1, a+1):
               resultado = 1 
               resultado *= b

       print(factorial(resultado))
       
       
2.  Calcular la potencia de dos elevado a un numero n ingresado 

        if __name__ == "__main__":
            n = int(input("Ingrese un número: "))
  
            cuadrado = lambda x: 1 if x == 0 else 2**cuadrado(x-1)
  
            for u in range(1,n+1): 
                resultado= 2**u

        print(resultado)
        
        
3. Calcular la potencia de un numero x ingresado elvado a n ingresada 

       if __name__ == "__main__":
           x = float(input("Ingrese un número: "))
           n = int(input("Ingrese otro número: "))
  
           Potencia = lambda a: 1 if x == 0 else 2**cuadrado(a-1)
  
           for u in range(1,n+1): 
               resultado= x**u

       print(resultado)


#  2 punto 
De los retos anteriores seleciones 3 funciones y escribalas con argumentos no definidos (*args).

1. Calcular el promedio de las variables ingresadas a,b,c,d,e 


       def calcular_promedio(*args) -> float:
           promedio: float = 0.0
           for num in args:
               promedio += num / len(args)
           return promedio

       if __name__ == "__main__":
           a = float(input("Ingrese el primer número: "))
           b = float(input("Ingrese el segundo número: "))
           c = float(input("Ingrese el tercer número: "))
           d = float(input("Ingrese el cuarto número: "))
           e = float(input("Ingrese el quinto número: "))
    
           resultado = calcular_promedio(a, b, c, d, e)
       print("El promedio de los números es:", resultado)
  2. 


         def calcular_contagios(*args) -> int:
             C, D = args
             total_contagios = C * (2 ** D)
             return total_contagios

         if __name__ == "__main__":
              C = int(input("Ingrese el número actual de contagiados: "))
              D = int(input("Ingrese la cantidad de días a proyectar: "))

              total_contagios = calcular_contagios(C,D)

              print("El número total de personas contagiadas después de", D, "días será:", total_contagios)
    
3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
                
       def imprimir_pares_inversos(*args) -> None:
           for n in args:
                if n >= 2:
                    i = n if n % 2 == 0 else n - 1
                    while i >= 2:
                    print(i)
                    i -= 2
                else:
                     print("El número ingresado es menor que 2.")

       if __name__ == "__main__":
           n = int(input("Ingrese un número natural mayor o igual a 2: "))
           imprimir_pares_inversos(n)

# 3 Punto 
Escriba una función recursiva para calcular la operación de la potencia.

# 4 Punto 

Utilice la siguiente plantilla de code para contar el tiempo:
import time
start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa. Importante: Revisar este hilo.

def fibonacci_Recursivo(n : int )-> int:
  if n <=1:
    # caso base
    return 1
  else:
    # condicion
    return fibonacci_Recursivo(n-1)+fibonacci_Recursivo(n-2)  

if __name__ == "__main__":
  num = int(input("Ingrese numero: "))
  serieFibo = fibonacci_Recursivo(num)
  print("La serie de Fibonacci hasta " + str(num) + " es " + str(serieFibo))
  
import time

start_time = time.time()
fibonacci_Recursivo(30)
end_time = time.time()

timer_recursivo = end_time - start_time


print("Tiempo de ejecución del algoritmo recursivo: ", timer_recursivo)


Crear cuenta en stackoverflow y adjuntar imagen en el repo

