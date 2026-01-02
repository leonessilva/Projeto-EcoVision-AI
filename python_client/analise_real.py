import cv2
import numpy as np
import requests
import random

# URL da sua API Java
url = 'http://localhost:8081/analises'

def criar_imagem_simulada():
    """Gera uma imagem preta com pontos brancos simulando microalgas"""
    # Cria uma imagem preta de 500x500 pixels
    img = np.zeros((500, 500), dtype=np.uint8)
    
    # Desenha bolinhas brancas aleatórias (entre 20 e 100 bolinhas)
    qtd_real = random.randint(20, 100)
    print(f"🎨 Gerando imagem simulada com {qtd_real} microalgas...")
    
    for _ in range(qtd_real):
        cx = random.randint(20, 480)
        cy = random.randint(20, 480)
        cv2.circle(img, (cx, cy), 3, (255, 255, 255), -1) # Pontos brancos
        
    # Salva para você ver depois
    cv2.imwrite("amostra_microalgas.png", img)
    return img

def contar_microalgas(imagem):
    """Usa OpenCV para contar os pontos brancos"""
    # 1. Aplica um limiar (garante que só o que for bem branco seja contado)
    _, thresh = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)
    
    # 2. Encontra os contornos (as bordas das bolinhas)
    contornos, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    return len(contornos)

# --- EXECUÇÃO DO FLUXO ---

# 1. Obter a imagem (na vida real, viria da câmera do microscópio)
imagem = criar_imagem_simulada()

# 2. Processar com Visão Computacional
qtd_contada = contar_microalgas(imagem)
print(f"👁️ Visão Computacional detectou: {qtd_contada} organismos.")

# 3. Preparar dados para o Java
dados = {
    "especie": "Simulacao OpenCV",
    "localColeta": "Gerador Sintetico v1",
    "confiancaIA": 99.9,
    "quantidade": qtd_contada
}

# 4. Enviar para o Backend
try:
    print("📡 Enviando dados para o Java...")
    resposta = requests.post(url, json=dados)
    
    if resposta.status_code == 200:
        print("✅ SUCESSO! Dados salvos no banco.")
        print(f"💾 ID salvo: {resposta.json()['id']}")
    else:
        print(f"❌ Erro: {resposta.text}")
except Exception as e:
    print("❌ Falha na conexão com o Java.")
    print(e)