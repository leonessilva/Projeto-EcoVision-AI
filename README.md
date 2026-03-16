# 🔬 EcoVision AI

Sistema híbrido de **visão computacional** + **microsserviços** para contagem e análise automatizada de microrganismos (microalgas) em laboratório.

Substitui contagem manual por pipeline inteligente:  
**Python + OpenCV** → detecção/contornos/métricas  
**Java + Spring Boot** → API REST + persistência MySQL

### Resultados principais
- Contagem automática: até 500+ indivíduos por imagem  
- Separação isoladas vs. colônias (Microcystis, Desmodesmus, Oscillatoria)  
- Métricas: área média ~8-25 µm², solidez >0.9 em isoladas  
- Relatórios em Excel/CSV com dados taxonômicos e estatísticos

### Arquitetura
```mermaid
graph LR
    Imagem --> Python/OpenCV --> JSON/POST --> API Spring Boot --> MySQL
Tecnologias

Backend: Java 17, Spring Boot 3.5 (Web, JPA, Lombok)
Visão: Python, OpenCV, Pandas
Banco: MySQL
Comunicação: REST API (HTTP POST)

Como rodar (local)
Backend
mvn spring-boot:run
