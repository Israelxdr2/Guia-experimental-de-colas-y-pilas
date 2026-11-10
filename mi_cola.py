from pasajero import Pasajero


class MiCola:
    """Cola (FIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos  -> [FRENTE, ..., FINAL, None, None]
    FRENTE -> datos[0]             (el primero que llegó: el único que sale)
    FINAL  -> datos[cantidad - 1]  (los nuevos se ponen detrás de él)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
       sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def encolar(self, pasajero):                     # ✅ resuelto (= añadir de MiLista)
        if self.cantidad == self.capacidad:
            print("  ⚠ La cola está llena")
            return False
        self.datos[self.cantidad] = pasajero          # se pone a la fila por detrás
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ EJEMPLO: del FRENTE al FINAL
        if self.cantidad == 0:
            print("  (cola vacía)")
            return
        for i in range(self.cantidad):                # 0, 1, ..., cantidad-1  (hacia adelante)
            if i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FRENTE")
            elif i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← FINAL")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✍ IMPLEMENTA (tabla 3) · recorre SIEMPRE del frente al final -------
    def desencolar(self):
        if self.esta_vacia():
            print(" La cola está vacía")
            return None
        
        pasajero_eliminado = self.datos[0]

        for i in range(self.cantidad -1):
            self.datos[i]= self.datos[i +1]
        
        self.datos[self.cantidad -1] = None
        self.cantidad = self.cantidad - 1
        return pasajero_eliminado
    

    def ver_frente(self):
        if self.esta_vacia():
               return None
        return self.datos[0]
   
    def buscar(self, numero):
           for i in range(self.cantidad):
               if  self.datos[i] is not None and numero == self.datos[i].numero:
                   return i
           return -1

    
    def modificar(self, numero, nuevo_destino, nuevo_asiento):
            mod_pos= self.buscar(numero)
            if mod_pos != -1:
                self.datos[mod_pos].destino= nuevo_destino
                self.datos[mod_pos].asiento= nuevo_asiento
                return True
            else:
                return False

    def eliminar_por_numero(self, numero):
        encontrado = False
        inicial = self.cantidad  
        for i in range(inicial):

            p = self.desencolar()  

            if p.numero == numero:
                encontrado = True 
            else:
                self.encolar(p)    
        return encontrado

    def copiar(self):
        copia = MiCola(self.capacidad)
        for i in range( self.cantidad ):
            copia.encolar(self.datos[i])
        return copia
    

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0

    def ordenar(self):
        if self.cantidad <= 1:
            return  

        temp = []
        for i in range(self.cantidad):
            temp.append(self.datos[i])

        
        n = len(temp)
        for i in range(n):
            for j in range(n - 1):
               
                if temp[j].numero > temp[j + 1].numero:
                    aux = temp[j]
                    temp[j] = temp[j + 1]
                    temp[j + 1] = aux

        self.cantidad = 0
        for i in range(len(temp)):
            self.encolar(temp[i])
    
    def binario(self, numero):
        inicio = 0
        fin = self.cantidad - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2
            
            if self.datos[medio] is not None:
                if self.datos[medio].numero == numero:
                    return medio  
                elif self.datos[medio].numero < numero:
                    inicio = medio + 1 
                else:
                    fin = medio - 1     
            else:
                break
        return -1  