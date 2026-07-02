# scripts/feature_flag.py
# Atividade desenvolvida por: Otavio Alves de Almeida
import json, os

with open("flags.json") as f:
    flags = json.load(f)

if flags.get("novo_layout"):
    print("[Feature Flag] Exibindo NOVO layout para o usuário.")
else:
    print("[Feature Flag] Exibindo layout ANTIGO (flag desligada).")

# Simulação de uso de segredo (nunca commitar valores reais!)
chave_api = os.environ.get("API_KEY_SIMULADA", "chave-nao-configurada")
print(f"[Secrets] Usando chave de API a partir de variável de ambiente: {chave_api}")