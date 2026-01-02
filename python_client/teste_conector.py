import requests
import json
import random

# O endereço onde o Java está "escutando"
url = 'http://localhost:8081/analises'

# Simulando dados que o OpenCV capturaria
especies = ["Chlorella", "Spirulina", "Volvox", "Microcystis"]
especie_detectada = random.choice(especies)
qtd_detectada = random.randint(50, 2000)

dados_da_ia = {
    "especie": especie_detectada,
    "localColeta": "Amostra Python Automatizada",
    "confiancaIA": 97.5,
    "quantidade": qtd_detectada
}

print(f"🤖 Tentando enviar: {dados_da_ia['especie']} com {dados_da_ia['quantidade']} unidades...")

try:
    # O momento do envio (POST)
    resposta = requests.post(url, json=dados_da_ia)

    if resposta.status_code == 200:
        print("✅ SUCESSO! O Java recebeu e salvou no banco.")
        print("📩 Resposta do servidor:", resposta.json())
    else:
        print(f"❌ Erro {resposta.status_code}: {resposta.text}")

except Exception as e:
    print("❌ Falha na conexão. O servidor Java está rodando?")
    print(e)