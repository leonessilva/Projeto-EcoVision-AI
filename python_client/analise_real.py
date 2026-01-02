import cv2
import numpy as np
import requests

# --- CONFIGURAÇÕES FINAIS ---
ARQUIVO_IMAGEM = "python_client/test.jpg"
AREA_MINIMA = 60       # Tamanho mínimo para ser considerado bicho
TAMANHO_MEDIO_ALGA = 85 # Aumentei um pouco para ele não exagerar na conta da colônia

def analisar_com_mascara():
    print(f"🚀 Iniciando Análise Focada (Com Máscara) em: {ARQUIVO_IMAGEM}...")
    
    img = cv2.imread(ARQUIVO_IMAGEM)
    if img is None:
        print("❌ Erro: Imagem não encontrada.")
        return

    # Pega altura (h) e largura (w) da imagem
    h, w = img.shape[:2]

    # --- NOVIDADE: A MÁSCARA CIRCULAR (Cortador de Biscoito) ---
    # Cria uma imagem preta vazia
    mascara_foco = np.zeros((h, w), dtype="uint8")
    # Desenha um círculo branco no meio (onde queremos olhar)
    raio = int(h / 2) - 10 
    cv2.circle(mascara_foco, (w // 2, h // 2), raio, 255, -1)
    
    # "Apaga" tudo que estiver fora do círculo na imagem original
    img_focada = cv2.bitwise_and(img, img, mask=mascara_foco)

    # 1. Processamento
    cinza = cv2.cvtColor(img_focada, cv2.COLOR_BGR2GRAY)
    suave = cv2.GaussianBlur(cinza, (5, 5), 0)
    
    # 2. Threshold Adaptativo
    binaria = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                    cv2.THRESH_BINARY_INV, 11, 2)

    # 3. Importante: Aplicar a máscara na binária também para limpar as bordas pretas
    binaria = cv2.bitwise_and(binaria, binaria, mask=mascara_foco)

    # 4. Contornos
    contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    total_organismos = 0
    img_resultado = img_focada.copy()

    for contorno in contornos:
        area = cv2.contourArea(contorno)
        
        if area > AREA_MINIMA:
            # Lógica de Colônia
            quantidade = 1
            if area > (TAMANHO_MEDIO_ALGA * 1.5):
                quantidade = int(area / TAMANHO_MEDIO_ALGA)
            
            total_organismos += quantidade
            
            # Desenho
            x, y, w, h = cv2.boundingRect(contorno)
            cor = (0, 255, 0)
            if quantidade > 1:
                cor = (255, 0, 0) # Azul
                cv2.putText(img_resultado, str(quantidade), (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, cor, 2)

            cv2.rectangle(img_resultado, (x, y), (x + w, y + h), cor, 2)

    # Salvar e Enviar
    cv2.imwrite("python_client/resultado_analise.jpg", img_resultado)
    print(f"🔬 Resultado Final: {total_organismos} organismos.")

    try:
        dados = {
            "especie": "Nível 3 - Focado",
            "quantidade": total_organismos,
            "confiancaIA": 95,
            "localColeta": "Lab Kleyton"
        }
        requests.post("http://localhost:8081/analises", json=dados)
        print("✅ Dados enviados!")
    except:
        pass

if __name__ == "__main__":
    analisar_com_mascara()