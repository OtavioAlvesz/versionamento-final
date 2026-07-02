# scripts/deploy_blue_green.py
# Atividade desenvolvida por: Otavio Alves de Almeida
import json, os

ARQUIVO_STATUS = "ambiente_ativo.json"

def ambiente_atual():
    if os.path.exists(ARQUIVO_STATUS):
        with open(ARQUIVO_STATUS) as f:
            return json.load(f)["ativo"]
    return "azul"

def alternar_ambiente():
    atual = ambiente_atual()
    novo = "verde" if atual == "azul" else "azul"
    with open(ARQUIVO_STATUS, "w") as f:
        json.dump({"ativo": novo}, f)
    print(f"[Blue-Green] Tráfego migrado do ambiente '{atual}' para o ambiente '{novo}'.")
    print(f"[Blue-Green] Ambiente '{atual}' permanece de reserva para rollback imediato.")

if __name__ == "__main__":
    alternar_ambiente()