import cv2
import numpy as np
import requests
import random

# --- CONFIGURAÇÃO ---
# Se a imagem for escura com bichos claros, use cv2.THRESH_BINARY
# Se a imagem for clara com bichos escuros, use cv2.THRESH_BINARY_INV
TIPO_LIMIAR = cv2.THRESH_BINARY
ARQUIVO_IMAGEM = "python_client/teste.jpg" # O nome da sua foto real

def analisar_imagem_real():
    print(f"📸 Lendo imagem real: {ARQUIVO_IMAGEM}...")
    
    # 1. Carregar a imagem real
    imagem = cv2.imread(ARQUIVO_IMAGEM)
    
    if imagem is None:
        print("❌ ERRO: Não achei a imagem! Verifique se o nome está 'teste.jpg' na pasta python_client")
        return

    # 2. Converter para Tons de Cinza (O computador vê melhor assim)
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # 3. Aplicar Limiar (Threshold) para separar o que é bicho do que é fundo
    # Ajuste o 127 se precisar (0 a 255)
    _, mascara = cv2.threshold(cinza, 127, 255, TIPO_LIMIAR)

    # 4. Contar os elementos (Análise de Conectividade)
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mascara)
    
    # (num_labels conta o fundo também, então subtraímos 1)
    quantidade_detectada = num_labels - 1
    
    print(f"🔬 Análise Concluída: {quantidade_detectada} organismos encontrados.")

    # 5. Preparar dados para o Java
    dados_para_api = {
        "especie": "Amostra Real (Microscópio)",
        "quantidade": quantidade_detectada,
        "confiancaIA": random.randint(85, 99), # Simulado por enquanto
        "localColeta": "Laboratório Kleyton"
    }

    # 6. Enviar para o Java
    try:
        url = "http://localhost:8081/analises"
        resposta = requests.post(url, json=dados_para_api)
        
        if resposta.status_code == 200:
            print("✅ SUCESSO! Dados enviados para o Dashboard Java.")
            print("👉 Atualize sua tela: http://localhost:8081")
        else:
            print(f"⚠️ Erro ao enviar: {resposta.status_code}")
            
    except Exception as e:
        print(f"❌ Erro de conexão: {e}")

# Executar
if __name__ == "__main__":
    analisar_imagem_real()