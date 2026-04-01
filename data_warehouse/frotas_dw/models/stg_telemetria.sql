-- arquivo: data_warehouse/frotas_dw/models/stg_telemetria.sql

WITH raw_data AS (
    -- Referenciamos a fonte que mapeamos no sources.yml
    SELECT * FROM {{ source('sistema_operacional', 'telemetria_frota') }}
)

SELECT
    id AS id_leitura,
    veiculo_id,
    timestamp AS data_hora_leitura,
    velocidade_kmh,
    temperatura_motor_celsius,
    alerta_fadiga,
    carga_perigosa_status,
    
    -- Extraindo os dados de dentro do JSON (pressao_pneus_psi) e convertendo para FLOAT
    CAST(pressao_pneus_psi->>'eixo_1_esq' AS FLOAT) AS pressao_eixo_1_esq,
    CAST(pressao_pneus_psi->>'eixo_1_dir' AS FLOAT) AS pressao_eixo_1_dir,
    CAST(pressao_pneus_psi->>'eixo_2_esq' AS FLOAT) AS pressao_eixo_2_esq,
    CAST(pressao_pneus_psi->>'eixo_2_dir' AS FLOAT) AS pressao_eixo_2_dir

FROM raw_data