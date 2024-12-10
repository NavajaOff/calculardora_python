# main.py
from cal import ControladorCal
from cal import CalculadoraModelo
from cal import CalcuVista

if __name__ == "__main__":
    modelo = CalculadoraModelo()
    vista = CalcuVista()
    controlador = ControladorCal(modelo, vista)
    controlador.ejecutar()
