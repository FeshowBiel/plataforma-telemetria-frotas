### 🧠 Modern Data Stack & Data Quality (Novo!)

Nesta última atualização, a plataforma evoluiu de um pipeline básico para uma **Modern Data Stack** completa com a introdução do **dbt (Data Build Tool)**. 

Ao lidar com dados críticos de telemetria e status de cargas químicas, a precisão da informação é inegociável. Por isso, implementamos:
- **Camada Staging:** Transformação de dados brutos aninhados (JSON de pressão de pneus) em colunas relacionais limpas e estruturadas usando modelos SQL.
- **Data Quality Automático:** Implementação de testes automatizados via `schema.yml` para garantir unicidade de chaves (PKs), ausência de valores nulos em sensores críticos e validação de categorias exatas (ex: travando o pipeline caso o sensor envie um status de carga química fora do padrão esperado, como 'VAZAMENTO_DETECTADO' ou 'NORMAL').
- **Isolamento de Ambientes:** Os dados crus permanecem intactos, enquanto o dashboard do Streamlit agora consome dados exclusivamente do schema `analytics`, garantindo performance e governança.