# controlador.py



class ControladorCal:
    def __init__(self,modelo,vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        """Ejecuta la lógica de la calculadora."""
        while True:
            self.vista.menu()
            try:
                opcion = input("Selecciona una opcion:")

                match opcion:

                    case "1":
                        numero1,operador,numero2 = self.vista.datos()
                        self.modelo.operaciones(numero1,operador,numero2)

                        id_operacion = self.modelo.ultimo_id()
                        while True:

                                if operador == "/":
                                    resultado = numero1 / numero2
                                    print(f"El resultado es:{resultado}")
                                    self.modelo.Resultado(resultado)
                                    
                                    id_resultado = self.modelo.ultimo_id()
                                    self.modelo.Historial(id_operacion,id_resultado)
                                    break

                                elif operador == "*":
                                    resultado = numero1 * numero2
                                    print(f"El resultado es:{resultado}")
                                    self.modelo.resultado(resultado)

                                    id_resultado = self.modelo.ultimo_id()
                                    self.modelo.Historial(id_operacion,id_resultado)
                                    break

                                elif operador == "+":
                                    resultado = numero1 + numero2
                                    print(f"El resultado es:{resultado}")
                                    self.modelo.resultado(resultado)

                                    id_resultado = self.modelo.ultimo_id()
                                    self.modelo.Historial(id_operacion,id_resultado)
                                    break

                                elif operador == "-":
                                    resultado = numero1 - numero2
                                    print(f"El resultado es:{resultado}")
                                    self.modelo.resultado(resultado)

                                    id_resultado = self.modelo.ultimo_id()
                                    self.modelo.Historial(id_operacion,id_resultado)
                                    break
                                
                                else:
                                    print(f"Operación no valida.")
                        
                    

                    case "2":
                        Historial = self.modelo.Ver_Historial()
                        self.vista.Mostrar_Historial(Historial)

                    case "3":
                        print("¡Hasta luego!")
                        self.modelo.cerrar_conexion()
                        break


                    case _:
                        print("Opción no válida. Intente de nuevo.")
            except ValueError:
                print("Valor ingresado no válido. Intente de nuevo.")