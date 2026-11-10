from pasajero import Pasajero


class MiPila:
    """Pila (LIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos -> [fondo, ..., TOPE, None, None]
    TOPE  -> datos[cantidad - 1]  (el último que entró: el único que se ve y el único que sale)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
       sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def apilar(self, pasajero):                      # ✅ resuelto (= añadir de MiLista)
        if self.cantidad == self.capacidad:
            print("  ⚠ La pila está llena")
            return False
        self.datos[self.cantidad] = pasajero          # el nuevo queda encima: es el TOPE
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ EJEMPLO: del TOPE al FONDO
        if self.cantidad == 0:
            print("  (pila vacía)")
            return
        for i in range(self.cantidad - 1, -1, -1):    # cantidad-1, ..., 1, 0  (hacia atrás)
            if i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← TOPE")
            elif i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FONDO")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✍ IMPLEMENTA (tabla 3) · recorre SIEMPRE del tope al fondo -------
    def desapilar(self):

        if self.esta_vacia():
            print(" La pila está vacía")
            return None
        
        tope_pos = self.cantidad - 1
        pasajero_eliminado = self.datos[tope_pos]
        
        self.datos[tope_pos] = None
        self.cantidad = self.cantidad - 1
        return pasajero_eliminado
    

    def ver_tope(self):
        if self.esta_vacia():
            return None
        return self.datos[self.cantidad-1]

    def buscar(self, numero):
        for i in range(self.cantidad -1, -1, -1):
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
        aux = MiPila(self.capacidad)
        bandera = False
        while not self.esta_vacia():
            p = self.desapilar()
            if p.numero == numero:
                bandera= True
            else:
                aux.apilar(p)
        while not aux.esta_vacia():
            self.apilar(aux.desapilar())

        return bandera
    

    def copiar(self):
        copia = MiPila(self.capacidad)
        for i in range( self.cantidad ):
          copia.apilar(self.datos[i])
        return copia

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad==0