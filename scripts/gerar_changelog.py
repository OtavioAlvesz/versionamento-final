# scripts/gerar_changelog.py
# Atividade desenvolvida por: Otavio Alves de Almeida
import subprocess

saida = subprocess.run(
    ["git", "log", "--pretty=format:%s"],
    capture_output=True, text=True
).stdout.splitlines()

categorias = {"feat": [], "fix": [], "docs": [], "refactor": [], "outros": []}
for linha in saida:
    tipo = linha.split(":")[0].strip()
    if tipo in categorias:
        categorias[tipo].append(linha)
    else:
        categorias["outros"].append(linha)

with open("CHANGELOG.md", "w", encoding="utf-8") as f:
    f.write("# CHANGELOG\n\n")
    titulos = {"feat": "### ✨ Funcionalidades", "fix": "### 🐛 Correções",
               "docs": "### 📝 Documentação", "refactor": "### ♻️ Refatorações", "outros": "### 📦 Outros"}
    for chave, itens in categorias.items():
        if itens:
            f.write(f"{titulos[chave]}\n")
            for item in itens:
                f.write(f"- {item}\n")
            f.write("\n")

print("CHANGELOG.md gerado com sucesso!")