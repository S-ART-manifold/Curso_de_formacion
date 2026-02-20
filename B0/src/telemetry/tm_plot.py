#!/usr/bin/env python3
"""B0.3 — Telemetry Plot

Uso:
  python3 src/telemetry/tm_plot.py --in data/tm_case_01.csv --out outputs/tm_plot.png

Objetivo:
  - Cargar el CSV
  - Convertir timestamp_utc a eje temporal
  - Graficar batt_v, temp_c y rssi_dbm vs tiempo
  - Guardar la figura en PNG
"""

import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--in", dest="in_path", required=True, help="CSV de entrada")
    p.add_argument("--out", dest="out_path", required=True, help="PNG de salida")
    return p.parse_args()


def load_tm(csv_path: str) -> pd.DataFrame:
    """Carga telemetría y hace validaciones mínimas."""
    df = pd.read_csv(csv_path)

    required = ["timestamp_utc", "batt_v", "temp_c", "rssi_dbm"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas: {missing}")

    if df[required].isna().any().any():
        raise ValueError("Hay valores NaN en columnas obligatorias.")

    # Parse time (ISO 8601 con Z)
    df["timestamp_utc"] = pd.to_datetime(df["timestamp_utc"], utc=True)
    if not df["timestamp_utc"].is_monotonic_increasing:
        raise ValueError("timestamp_utc no está ordenado crecientemente.")

    # Time axis in seconds from start
    t0 = df["timestamp_utc"].iloc[0]
    df["t_s"] = (df["timestamp_utc"] - t0).dt.total_seconds()
    return df


def main() -> None:
    args = parse_args()
    df = load_tm(args.in_path)

    os.makedirs(os.path.dirname(args.out_path) or ".", exist_ok=True)

    plt.figure()
    plt.plot(df["t_s"], df["batt_v"], label="batt_v [V]")
    plt.plot(df["t_s"], df["temp_c"], label="temp_c [C]")
    plt.plot(df["t_s"], df["rssi_dbm"], label="rssi_dbm [dBm]")
    plt.xlabel("t [s]")
    plt.ylabel("value")
    plt.title("Telemetry vs time")
    plt.legend()
    plt.tight_layout()
    plt.savefig(args.out_path, dpi=150)
    plt.close()

    print(f"OK: plot guardado en {args.out_path}")


if __name__ == "__main__":
    main()
