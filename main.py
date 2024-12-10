# main.py
from Controllers.CalController import ControladorCal
from Models.cal import CalculadoraModelo
from views.CalView import CalcuVista

if __name__ == "__main__":
    modelo = CalculadoraModelo()
    vista = CalcuVista()
    controlador = ControladorCal(modelo, vista)
    controlador.ejecutar()
