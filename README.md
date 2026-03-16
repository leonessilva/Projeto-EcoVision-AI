# 🔬 EcoVision AI

Sistema híbrido de **visão computacional** + **microsserviços** para contagem e análise automatizada de microrganismos (microalgas) em laboratório.

Substitui a contagem manual por pipeline inteligente:  
**Python + OpenCV** → detecção, contornos e métricas morfométricas  
**Java + Spring Boot** → API REST + persistência em MySQL

### Resultados principais
- Contagem automática: até 500+ indivíduos por imagem  
- Separação isoladas vs. colônias (Microcystis, Desmodesmus, Oscillatoria)  
- Métricas: área média ~8-25 µm², solidez >0.9 em isoladas  
- Relatórios em Excel/CSV com dados taxonômicos e estatísticos

### Arquitetura
```mermaid
graph LR
    A[Imagem] --> B[Python + OpenCV]
    B --> C[JSON / HTTP POST]
    C --> D[API Spring Boot]
    D --> E[MySQL]
