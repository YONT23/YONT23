import os

class persona():
    def __init__(self):
        self.__persona = {}
        self.__listapersonas = {}
    def agregarpersona(self, cedula,nombre, apellido, direccion, telefono);
        self.__persona = {
            'cedula': cedula,
            'nombre': nombre,
            'apellido': apellido,
            'direccion': direccion,
            'telefono': telefono,
        }
        self.__listapersonas.append(self.__persona)

class Empleado(persona):
    def __init__(self):
        super().__init__()
        self.__devengado = {}
        self.__deducciones = {}
        self.__listaempleados =[]
    
    def agregarempleado(self):
        cedula = input("Digite su cedula:")
        nombre = input("Digite su nombre:")
        apellido = input("Digite su apellido:")
        direccion = input("Digite su direccion:")
        telefono = input("Digite su telefono:")
        salario = float(input("Digite su ceedula:"))

        per = {
            'cedula': cedula,
            'nombre': nombre,
            'apellido': apellido,
            'direccion': direccion,
            'telefono': telefono,
        }

        self.__devengado ={
            'salario': salario,
            'alimentacion': alimentacion,
            'transporte': transporte,
        }

        self.__devengado ={
            'salud': salud,
            'pension': pension,
        }

        super().agregarpersona(cedula, nombre, apellido,direccion, telefono)

        self.__listaempleados.append([{"persona": per},{"devengado": self.__devengado},{"deducciones": self.__deducciones}])
    
    def calculardevengado(self):
        if self.__devengado['salario'] < 2000000:
            self.__devengado['alimentacion'] = 80000
            self.__devengado['transporte'] = 60000

    def calculardeducciones(self):
        self.__deducciones['salud'] = self.__devengado['salario'] * 0.04
        self.__deducciones['pension'] = self.__devengado['salario'] * 0.0337

    def menu(self, opciones):
        while(True):
             os.system("clear")
             for item in range(len(opciones)):
                 print(opciones[item])
            opcion = input("Digite una opcion correcta: ")

            if opcion == '1':
                os.system("clear")
                self.agregarempleado()
                self.calculardevengado()
                self.calculardeducciones()

            elif opcion == "2":
                os.system("clear")
                print(self.__listaempleados)
                input("Digite una tecla para continuar...")

def menuPrincipal():
    opciones = (
        os.system("clear")
        "MENU PRINCIPAL"
        "1. AdicionarEmpleados"
        "2. Mostrar Empleados"
        "3. Eliminar Empleados"
        "S. Salir"
    )

    emp = Empleado()
    emp.menu(opciones)

def main():
    menuPrincipal()

if __name__=="__main__":
    main() 