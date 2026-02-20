# Runbook — B0.3 Telemetry Analysis (laboratorio guiado)

## 1) Entorno
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2) Plot
```bash
python3 B0/src/telemetry/tm_plot.py --in B0/data/tm_case_01.csv --out B0/outputs/tm_plot.png
```

## 3) Análisis (eventos)
```bash
python3 B0/src/telemetry/tm_analyze.py --in B0/data/tm_case_01.csv
```

## 4) Actividad guiada (modificar un parámetro)
Abre `B0/src/telemetry/tm_analyze.py` y modifica **solo** la sección:

**PARÁMETROS DEL ALUMNO (MODIFICA SOLO ESTO)**

Ejemplos:
- `EPS_LOW_VOLTAGE_V`: `3.5` → `3.6`
- `COMMS_DROP_RSSI_DBM`: `-85` → `-90`

Vuelve a ejecutar el script y observa cómo cambian los eventos detectados.

## 5) Informe (obligatorio)
Crea:
- `B0/docs/tm_reports/<tu_nombre>_b03.md`

Incluye:
- eventos detectados (lista)
- subsistema implicado
- acción como operador
- qué parámetro cambiaste y qué efecto tuvo

## 6) Entrega
- `B0/outputs/tm_plot.png`
- tu informe en `B0/docs/tm_reports/`
