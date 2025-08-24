import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("=== Gerador de Senhas Aleatórias ===")
    
    try:
        tamanho = int(input("Digite o tamanho da senha (ex: 12): "))
    except ValueError:
        print("Entrada inválida! Usando valor padrão (12).")
        tamanho = 12
    
    senha = gerar_senha(tamanho)
    print(f"\nSua senha gerada é:\n👉 {senha}")

if __name__ == "__main__":
    main()
