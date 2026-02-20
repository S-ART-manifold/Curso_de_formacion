# Curso de Formación — S-ART

Repositorio del curso de onboarding y formación práctica para nuevos miembros de S-ART.

## Estructura
- `B0/` Fundamentos + herramientas (Git/GitHub, Python primer, telemetría)
- `B1/` 𝙇𝙤𝙖𝙙𝙞𝙣𝙜…
- `B2/` 𝙇𝙤𝙖𝙙𝙞𝙣𝙜…
- `B3/` 𝙇𝙤𝙖𝙙𝙞𝙣𝙜…
- `shared/` Recursos comunes (plantillas, runbooks globales)

## Cómo empezar (nuevo miembro)
1. Entra en `B0/docs/00_onboarding/course_overview.md`
2. Sigue las instrucciones del Bloque 0
3. Entrega todo por Pull Request (no se permiten commits a `main`)

## B0 — Telemetría (rápido)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python3 B0/src/telemetry/tm_plot.py --in B0/data/tm_case_01.csv --out B0/outputs/tm_plot.png
python3 B0/src/telemetry/tm_analyze.py --in B0/data/tm_case_01.csv
```

## Reglas del curso
- Si no está en el repo, no existe.
- Entregas siempre por PR + review.
- No subir archivos grandes (datasets, binarios, vídeos).

## Bloque 0 (guía y entregas)
- Guía: `B0/docs/block0_guide.pdf`
- Rúbrica: `B0/docs/rubric_block0.md`
- B0.1 (notes): `B0/docs/cubesat_notes/README.md`
- Runbook B0.2 (Git/PR): `B0/docs/runbooks/rb_b0_2_git_pr.md`
- Runbook B0.3 (telemetría): `B0/docs/runbooks/rb_b0_3_tm.md`
