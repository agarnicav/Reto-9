def fibonacci_Recursivo(n : int )-> int:
  if n <=1:
    return 1
  else:
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
