#  Plataforma de Telemetria e SST para Frotas (Modern Data Stack)

![Badge Status](https://img.shields.io/badge/Status-Concluído-success)
![Docker](https://img.shields.io/badge/Docker-Integrado-blue)
![Apache Airflow](https://img.shields.io/badge/Apache_Airflow-2.7-017CEE)
![dbt](https://img.shields.io/badge/dbt-Data_Quality-FF694B)

##  Visão Geral do Projeto
Este projeto é uma solução arquitetural **End-to-End de Engenharia de Dados**, desenvolvida para resolver um desafio crítico no setor de logística e transporte de produtos químicos: garantir que os dados de telemetria dos caminhões (pressão dos pneus, temperatura, status das válvulas) sejam ingeridos, processados, testados e visualizados com confiabilidade e automação total.

##  Arquitetura e Tecnologias (Tech Stack)
O ecossistema foi 100% conteinerizado usando **Docker** e segue as melhores práticas da *Modern Data Stack*:

1. **Ingestão (API & Mensageria):** `FastAPI` recebe os JSONs dos sensores simulados e os envia para o `RabbitMQ` (garantindo que nenhum dado seja perdido em picos de tráfego).
2. **Processamento (Worker):** Um script Python consome a fila do RabbitMQ e insere os dados brutos no banco.
3. **Armazenamento (Data Warehouse):** `PostgreSQL` armazenando tanto a camada bruta quanto a camada analítica.
4. **Transformação & Data Quality:** `dbt (Data Build Tool)` rodando nativamente. Limpa estruturas aninhadas e executa testes rigorosos (ex: bloqueia dados se o sensor enviar valores absurdos).
5. **Orquestração:** `Apache Airflow` coordena todo o fluxo. As DAGs ativam o dbt diariamente de forma isolada e segura.
6. **Visualização:** `Streamlit` consome os dados modelados e exibe indicadores críticos em tempo real para a tomada de decisão da diretoria.

##  Como Executar o Projeto Localmente

**Pré-requisitos:** Ter o [Docker](https://www.docker.com/) e o `Git` instalados na sua máquina.

1. Clone este repositório:
```bash
git clone [https://github.com/FeshowBiel/plataforma-telemetria-frotas.git](https://github.com/FeshowBiel/plataforma-telemetria-frotas.git)