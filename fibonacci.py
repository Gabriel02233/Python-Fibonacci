import time
import sys

def gerar_fibonacci(n: int) -> list[int]:
    """Gera os primeiros 'n' números da sequência de Fibonacci."""
    sequencia_fibonacci = [1, 1]
    while len(sequencia_fibonacci) < n:
        proximo_numero = sequencia_fibonacci[-1] + sequencia_fibonacci[-2]
        sequencia_fibonacci.append(proximo_numero)
    return sequencia_fibonacci

def imprimir_fibonacci(sequencia: list[int]) -> None:
    """Imprime a sequência de Fibonacci no terminal."""
    for numero in sequencia:
        print(numero)
        time.sleep(0.08)

def main():
    num_elementos = 10  # Número de elementos desejados na sequência
    sequencia_fibonacci = gerar_fibonacci(num_elementos)
    imprimir_fibonacci(sequencia_fibonacci)

if _name_ == "_main_":
    main()
    
