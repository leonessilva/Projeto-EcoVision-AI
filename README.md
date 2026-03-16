# 🔬 EcoVision AI

> Sistema de Visão Computacional + Microsserviços para Análise Automatizada de Microrganismos (Microalgas)

O **EcoVision AI** automatiza a contagem e classificação de microrganismos em amostras laboratoriais (ex: cianobactérias como Microcystis, Desmodesmus e Oscillatoria), substituindo a contagem manual demorada por um pipeline inteligente. 

Tecnologias principais:
- **Python + OpenCV** → Processamento de imagem e detecção de contornos.
- **Java + Spring Boot 3.5** → API REST, persistência (JPA + MySQL) e gerenciamento de análises.
- Comunicação via **HTTP POST** (JSON com resultados da visão computacional).

## Resultados Alcançados
- Contagem automática de até **500+ indivíduos** por imagem.
- Separação **isoladas vs. em colônia/cenóbio** com precisão alta (solidez >0.9 em isoladas).
- Métricas morfométricas: área média ~8-25 µm², circularidade ~0.7-0.9.
- Geração de relatórios em Excel/CSV com detalhes taxonômicos e estatísticos.
- Aplicação real em monitoramento ambiental/biotech (detecção de blooms tóxicos).

## Arquitetura do Sistema
Inteligência de borda (Python) + Backend escalável (Java).

```mermaid
graph LR
    A[📷 Captura/Geração de Imagem] -->|Python| B(👁️ Processamento OpenCV)
    B -->|JSON/HTTP POST| C{☕ API Spring Boot}
    C -->|JPA/Hibernate| D[(🗄️ Banco de Dados MySQL)]
    C --> E[Dashboard Web / Relatórios]
