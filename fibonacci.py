import time

def gerar_fibonacci(n: int) -> list[int]:
    """
    Gera os primeiros 'n' números da sequência de Fibonacci.

    Args:
        n (int): O número de elementos da sequência de Fibonacci a serem gerados.

    Returns:
        list[int]: Uma lista contendo os primeiros 'n' números da sequência de Fibonacci.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    
    sequencia_fibonacci = [1, 1]
    while len(sequencia_fibonacci) < n:
        proximo_numero = sequencia_fibonacci[-1] + sequencia_fibonacci[-2]
        sequencia_fibonacci.append(proximo_numero)
    
    return sequencia_fibonacci

def imprimir_fibonacci(sequencia: list[int]) -> None:
    """
    Imprime a sequência de Fibonacci no terminal com um atraso entre cada número.

    Args:
        sequencia (list[int]): A lista de números da sequência de Fibonacci a serem impressos.
    """
    for numero in sequencia:
        print(numero)
        time.sleep(0.08)  # Espera 0,08 segundos antes de imprimir o próximo número

def main():
    """
    Função principal do programa. Pergunta ao usuário quantos elementos da sequência de Fibonacci ele deseja,
    gera a sequência e a imprime no terminal.
    """
    try:
        num_elementos = int(input("Quantos números da sequência de Fibonacci você deseja gerar? "))
        if num_elementos <= 0:
            print("Por favor, insira um número maior que 0.")
            return

        sequencia_fibonacci = gerar_fibonacci(num_elementos)
        imprimir_fibonacci(sequencia_fibonacci)
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()
