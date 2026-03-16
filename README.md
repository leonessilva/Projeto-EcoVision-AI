# 🔬 EcoVision AI

Sistema híbrido para contagem automática de microalgas em laboratório.

**Python + OpenCV** → detecção e métricas  
**Java + Spring Boot** → API REST + MySQL

### Principais resultados
- Até 500+ indivíduos por imagem  
- Separa isoladas vs. colônias (Microcystis, Desmodesmus, Oscillatoria)  
- Área média: ~8-25 µm² | Solidez >0.9 em isoladas  
- Relatórios em Excel/CSV

### Arquitetura
```mermaid
graph LR
    Imagem --> Python --> API[Spring Boot] --> MySQL
