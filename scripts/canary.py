# scripts/canary.py
# Atividade desenvolvida por: Otavio Alves de Almeida
import random

PORCENTAGEM_CANARY = 10  # 10% dos usuários recebem a nova versão

def rotear_usuario():
    return "versao_nova" if random.randint(1, 100) <= PORCENTAGEM_CANARY else "versao_estavel"

if __name__ == "__main__":
    contagem = {"versao_nova": 0, "versao_estavel": 0}
    for _ in range(100):
        contagem[rotear_usuario()] += 1
    print(f"[Canary] {contagem['versao_nova']} usuários na versão nova, "
          f"{contagem['versao_estavel']} na versão estável (alvo: {PORCENTAGEM_CANARY}%).")