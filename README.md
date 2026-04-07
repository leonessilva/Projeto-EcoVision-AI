# 🔬 EcoVision AI

**Sistema híbrido para contagem automática de microalgas em laboratório.**

Combina visão computacional (Python + OpenCV) com uma API REST robusta (Java + Spring Boot) para automatizar a análise de amostras de microalgas — substituindo a contagem manual por microscopia.

---

## 🎯 Problema

A contagem manual de microalgas é lenta, subjetiva e propensa a erros. Um analista pode levar horas para processar uma única amostra em câmara de Neubauer. O EcoVision AI automatiza esse processo com análise de imagem, entregando resultados em segundos.

## 🧪 Principais Resultados

| Métrica | Valor |
|---|---|
| Indivíduos detectados | Até **500+** por imagem |
| Classificação | Isoladas vs. Colônias |
| Gêneros suportados | *Microcystis*, *Desmodesmus*, *Oscillatoria* |
| Área média celular | ~8–25 µm² |
| Solidez (isoladas) | > 0.9 |
| Exportação | Excel (.xlsx) e CSV |

## 🏗️ Arquitetura

```
┌─────────────────────┐       HTTP/JSON       ┌──────────────────────┐
│   Python Client      │ ◄──────────────────► │  Spring Boot API     │
│   OpenCV + NumPy     │                       │  REST Controllers    │
│   Análise de imagem  │                       │  Service Layer       │
│   Máscara circular   │                       │  MySQL / JPA         │
└─────────────────────┘                        └──────────────────────┘
```

- **Python Client** — Processamento de imagem: segmentação, detecção de contornos com máscara circular, cálculo de métricas morfológicas (área, perímetro, solidez, circularidade).
- **Spring Boot API** — Persistência dos resultados, endpoints REST para consulta e gerenciamento de análises, dashboard web.
- **MySQL** — Armazenamento de dados biológicos e histórico de análises.

## 🛠️ Tech Stack

**Back-end (Java)**
- Java 17+
- Spring Boot 3
- Spring Data JPA
- MySQL 8
- Maven

**Visão Computacional (Python)**
- Python 3.10+
- OpenCV
- NumPy
- Pandas
- OpenPyXL

## 📁 Estrutura do Projeto

```
EcoVision-AI/
├── src/                        # Código Java (Spring Boot)
│   ├── main/
│   │   ├── java/               # Controllers, Services, Models, Repositories
│   │   └── resources/          # application.properties, templates
│   └── test/
├── python_client/              # Algoritmo de visão computacional
│   └── ...                     # Scripts de análise com OpenCV
├── dados_biologicos.csv        # Dataset de exemplo
├── amostra_microalgas.png      # Imagem de amostra para testes
├── pom.xml                     # Dependências Maven
└── README.md
```

## 🚀 Como Executar

### Pré-requisitos

- Java 17+
- Maven 3.8+
- Python 3.10+
- MySQL 8 rodando localmente

### 1. Banco de Dados

```sql
CREATE DATABASE ecovision_db;
```

Configure as credenciais em `src/main/resources/application.properties`.

### 2. Back-end (Spring Boot)

```bash
./mvnw spring-boot:run
```

A API estará disponível em `http://localhost:8080`.

### 3. Cliente Python

```bash
cd python_client
pip install -r requirements.txt
python main.py
```

## 📊 Funcionalidades

- **Upload de imagem** de amostra de microalgas
- **Segmentação automática** com máscara circular (simula campo do microscópio)
- **Detecção e contagem** de organismos individuais e colônias
- **Métricas morfológicas**: área, perímetro, solidez, circularidade
- **Classificação** por gênero (Microcystis, Desmodesmus, Oscillatoria)
- **Dashboard web** para visualização dos resultados
- **Exportação** em Excel e CSV

## 📡 Endpoints da API

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/api/analises` | Lista todas as análises |
| `POST` | `/api/analises` | Cria nova análise |
| `GET` | `/api/analises/{id}` | Detalhe de uma análise |
| `DELETE` | `/api/analises/{id}` | Remove uma análise |

## 🧬 Como Funciona a Detecção

1. **Pré-processamento** — Conversão para escala de cinza, aplicação de blur gaussiano
2. **Máscara circular** — Isola a região de interesse (campo do microscópio)
3. **Limiarização** — Segmentação por threshold adaptativo
4. **Detecção de contornos** — Identificação de organismos via `findContours`
5. **Filtragem** — Remoção de artefatos por área mínima/máxima
6. **Classificação** — Distinção entre células isoladas e colônias por solidez e circularidade
7. **Métricas** — Cálculo de área média, contagem total, distribuição por classe

## 📄 Licença

Este projeto é de uso acadêmico e educacional.

## 👤 Autor

**Leones** — Estudante de Ciência da Computação @ FBV/Wyden, Recife-PE

[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin)](https://linkedin.com/in/seu-perfil)
[![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/seu-usuario)
