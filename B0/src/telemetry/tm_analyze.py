#!/usr/bin/env python3
"""B0.3 — Telemetry Analysis (laboratorio guiado)

Uso:
  python3 B0/src/telemetry/tm_analyze.py --in B0/data/tm_case_01.csv

Qué hace este script:
  1) Carga el CSV
  2) Convierte el tiempo a segundos desde el inicio (t_s)
  3) Detecta eventos (intervalos) donde una condición se cumple durante un tiempo mínimo
  4) Imprime los eventos detectados

IMPORTANTE (actividad del laboratorio):
  - NO tienes que reescribir el algoritmo.
  - SOLO debes modificar los umbrales/tiempos mínimos en la sección:
      "PARÁMETROS DEL ALUMNO"
  - Después, vuelve a ejecutar el script y observa cómo cambian los eventos.

Eventos (por defecto):
  - EPS_LOW:       batt_v < 3.5 V durante >= 10 s
  - THERMAL_HIGH:  temp_c > 45 C durante >= 20 s
  - COMMS_DROP:    rssi_dbm < -85 dBm durante >= 5 s
"""

import argparse
import pandas as pd


# ============================================================
# PARÁMETROS DEL ALUMNO (MODIFICA SOLO ESTO)
# ============================================================
EPS_LOW_VOLTAGE_V = 3.5          # ejemplo: prueba 3.6
EPS_LOW_MIN_DURATION_S = 10      # ejemplo: prueba 5 o 20

THERMAL_HIGH_TEMP_C = 45.0       # ejemplo: prueba 44.0 o 46.0
THERMAL_HIGH_MIN_DURATION_S = 20

COMMS_DROP_RSSI_DBM = -85.0      # ejemplo: prueba -90.0
COMMS_DROP_MIN_DURATION_S = 5
# ============================================================


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--in", dest="in_path", required=True, help="CSV de entrada")
    return p.parse_args()


def load_tm(csv_path: str) -> pd.DataFrame:
    """Carga telemetría y crea columna t_s (segundos desde inicio)."""
    df = pd.read_csv(csv_path)

    required = ["timestamp_utc", "batt_v", "temp_c", "rssi_dbm"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas obligatorias: {missing}")

    if df[required].isna().any().any():
        raise ValueError("Hay valores NaN en columnas obligatorias.")

    df["timestamp_utc"] = pd.to_datetime(df["timestamp_utc"], utc=True)
    if not df["timestamp_utc"].is_monotonic_increasing:
        raise ValueError("timestamp_utc no está ordenado crecientemente.")

    t0 = df["timestamp_utc"].iloc[0]
    df["t_s"] = (df["timestamp_utc"] - t0).dt.total_seconds()
    return df


def _find_intervals(mask: pd.Series, t_s: pd.Series, min_duration_s: float):
    """Devuelve intervalos True con duración mínima.

    Salida: lista de tuplas (t_start, t_end, idx_start, idx_end)
    """
    intervals = []
    in_run = False
    i0 = None

    mask_list = mask.to_list()
    for i, is_true in enumerate(mask_list):
        if is_true and not in_run:
            in_run = True
            i0 = i

        if (not is_true) and in_run:
            in_run = False
            i1 = i - 1
            t_start = float(t_s.iloc[i0])
            t_end = float(t_s.iloc[i1])
            if (t_end - t_start) >= min_duration_s:
                intervals.append((t_start, t_end, i0, i1))

    if in_run and i0 is not None:
        i1 = len(mask_list) - 1
        t_start = float(t_s.iloc[i0])
        t_end = float(t_s.iloc[i1])
        if (t_end - t_start) >= min_duration_s:
            intervals.append((t_start, t_end, i0, i1))

    return intervals


def detect_anomalies(df: pd.DataFrame):
    """Detecta eventos de anomalía usando los parámetros globales."""
    events = []

    # --- EPS LOW ---
    eps_mask = df["batt_v"] < EPS_LOW_VOLTAGE_V
    for t_start, t_end, i0, i1 in _find_intervals(eps_mask, df["t_s"], EPS_LOW_MIN_DURATION_S):
        seg = df.iloc[i0:i1+1]
        events.append({
            "kind": "EPS_LOW",
            "t_start_s": t_start,
            "t_end_s": t_end,
            "details": {
                "threshold_v": EPS_LOW_VOLTAGE_V,
                "batt_min_v": float(seg["batt_v"].min()),
                "batt_mean_v": float(seg["batt_v"].mean()),
            }
        })

    # --- THERMAL HIGH ---
    th_mask = df["temp_c"] > THERMAL_HIGH_TEMP_C
    for t_start, t_end, i0, i1 in _find_intervals(th_mask, df["t_s"], THERMAL_HIGH_MIN_DURATION_S):
        seg = df.iloc[i0:i1+1]
        events.append({
            "kind": "THERMAL_HIGH",
            "t_start_s": t_start,
            "t_end_s": t_end,
            "details": {
                "threshold_c": THERMAL_HIGH_TEMP_C,
                "temp_max_c": float(seg["temp_c"].max()),
                "temp_mean_c": float(seg["temp_c"].mean()),
            }
        })

    # --- COMMS DROP ---
    comms_mask = df["rssi_dbm"] < COMMS_DROP_RSSI_DBM
    for t_start, t_end, i0, i1 in _find_intervals(comms_mask, df["t_s"], COMMS_DROP_MIN_DURATION_S):
        seg = df.iloc[i0:i1+1]
        events.append({
            "kind": "COMMS_DROP",
            "t_start_s": t_start,
            "t_end_s": t_end,
            "details": {
                "threshold_dbm": COMMS_DROP_RSSI_DBM,
                "rssi_min_dbm": float(seg["rssi_dbm"].min()),
                "rssi_mean_dbm": float(seg["rssi_dbm"].mean()),
            }
        })

    events.sort(key=lambda e: e["t_start_s"])
    return events


def main() -> None:
    args = parse_args()
    df = load_tm(args.in_path)
    events = detect_anomalies(df)

    print("Parámetros actuales:")
    print(f"- EPS_LOW: batt_v < {EPS_LOW_VOLTAGE_V} V durante >= {EPS_LOW_MIN_DURATION_S} s")
    print(f"- THERMAL_HIGH: temp_c > {THERMAL_HIGH_TEMP_C} C durante >= {THERMAL_HIGH_MIN_DURATION_S} s")
    print(f"- COMMS_DROP: rssi_dbm < {COMMS_DROP_RSSI_DBM} dBm durante >= {COMMS_DROP_MIN_DURATION_S} s")
    print()

    if not events:
        print("No se detectaron anomalías con los parámetros actuales.")
        return

    print("Anomalías detectadas:")
    for e in events:
        print(f"- {e['kind']}: {e['t_start_s']:.0f}s → {e['t_end_s']:.0f}s | {e['details']}")


if __name__ == "__main__":
    main()
