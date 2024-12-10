# vista.py
from colorama import Fore,Style

class CalcuVista:

    @staticmethod
    def menu():
        print(Fore.CYAN + "---Calculadora---"+ Style.RESET_ALL)
        print(Fore.CYAN+"1."+ Style.RESET_ALL,"Ingresar a la calculadora.")
        print(Fore.CYAN+"2."+Style.RESET_ALL,"Ver historial.")
        print(Fore.CYAN+"3."+Style.RESET_ALL,"salir")

    @staticmethod
    def datos():
        while True:
            try:
                numero1 = float(input("ingrese numero1: "))
                operador = input("ingrese el operador (+ , - , / , * ):")

                if operador not in ['+', '-', '*', '/']:
                    print("Operador inválido. Intente de nuevo.")
                    
                    
                    continue
                numero2 = float (input("Ingrese numero2: "))
                return numero1,operador,numero2
            
            except ValueError:
                print("Valor no valido, intentelo de nuevo.")
            
    @staticmethod
    def Mostrar_Resultado(resultado):
        print(f"{resultado}")
        


    @staticmethod
    def Mostrar_Historial(Historial):
        if not Historial:
            print("No hay operaciones en el historial.")
        else:
            print("---Historial_operaciones---")
        for operacion in Historial:
            print(f"(ID: {operacion[0]})    {operacion[1]} {operacion[2]} {operacion[3]} = {operacion[4]}")



    