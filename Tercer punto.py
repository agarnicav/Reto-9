def potencia(base, exponente)-> int:  # Definimos la funcion para hallar la potencia
    if exponente == 0:  # Se declaran los casos bases 
        return 1
    elif exponente == 1:
        return base
    
    
    else:
        _potencia = base**exponente
        return _potencia
        
if __name__ == "__main__":
  n = int(input("Ingrese numero base: "))
  x = int(input("Ingrese numero exponente : "))
  Potencia_num = potencia(n,x)
  
print("La potencia de " + str(n) + " elevado a " + str(x) + " es " + str(Potencia_num))