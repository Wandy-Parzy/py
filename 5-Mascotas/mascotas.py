class Animal: 
    """clase par representar un animal"""
    def __init__(self, especie, edad) -> None:
        self.especie = especie
        self.edad = edad

    def __str__(self) -> str:
        return f"Animal [Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}]" 

class Mascota(Animal):
  def __init__(self, especie, edad, nombre) -> None:
      super().__init__(especie, edad)
      self.nombre = nombre

      def __init__(self) -> str:
          return f"Mascota [Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}]"

class registromascotas:
    def __init__(self) -> None:
        self.mascotas = [] 

    def agregar_mascotas(self, mascota):
        self.mascotas.append(mascota)

    def listar(self):
        if self.mascotas:
            print("Lista de mascotas \n ", "="*30)
            for i, mascota in enumerate(self.mascotas, start=1 ):
                print(f"{i}. {mascota}")
        else:
            print("No hay mascotas disponibles")

    def editar(self, indice, nueva_mascota):
        if indice < 0 or indice >= len(self.mascotas):
            print("No hay registro con este indice")
        else: 
            self.mascotas[indice] = nueva_mascota

    def eliminar(self, indice):
        if indice < 0 or indice >= len(self.mascotas):
            print("No hay registro con este indice")
        else:
            del self.mascotas[indice]
            print("Se elimino la mascota")
 
