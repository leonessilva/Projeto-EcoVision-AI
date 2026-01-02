# 🔬 EcoVision AI

> Sistema de Visão Computacional e Arquitetura de Microsserviços para análise biológica automatizada.

O **EcoVision AI** é uma solução tecnológica desenvolvida para automatizar a contagem e identificação de microrganismos (microalgas) em laboratório. O projeto substitui a contagem manual por um fluxo automatizado utilizando **Python (OpenCV)** para processamento de imagem e **Java (Spring Boot)** para gestão e persistência dos dados.

---

## 🚀 Arquitetura do Sistema

O projeto segue uma arquitetura distribuída onde a inteligência de borda (Visão Computacional) se comunica com uma API robusta de backend.

```mermaid
graph LR
    A[📷 Captura/Geração de Imagem] -->|Python| B(👁️ Processamento OpenCV)
    B -->|JSON/HTTP POST| C{☕ API Spring Boot}
    C -->|JPA/Hibernate| D[(🗄️ Banco de Dados MySQL)]