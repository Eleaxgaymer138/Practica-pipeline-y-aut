import os   
import math 

class Calculator:
    def sum(self, a: int, b: int) -> int:
        return a + b  # Antes restaba, ahora suma

    def subtract(self, a: int, b: int) -> int:
        return a - b  # Nombre cambiado a subtract y lógica a resta

    def multiply(self, a: int, b: int) -> int:
        return a * b  # Antes sumaba, ahora multiplica

    def divide(self, a: int, b: int) -> float:
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b