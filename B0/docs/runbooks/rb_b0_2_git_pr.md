# Runbook — B0.2 Git + Pull Request (PR)

## 0) Idea del ejercicio
Vas a hacer tu primera contribución al repositorio del curso usando el flujo profesional:
**rama → commits → push → PR → review → merge**.

## 1) Clonar el repositorio
```bash
git clone <URL_DEL_REPO>
cd <NOMBRE_DEL_REPO>
git status
```

## 2) Crear una rama (nunca trabajes en main)
```bash
git checkout -b feature/<tu_nombre>-cubesat-notes
git branch
```

## 3) Añadir tu entrega B0.1
Crea/edita:
- `B0/docs/cubesat_notes/submissions/<tu_nombre>.md`
- (Opcional) `B0/docs/cubesat_notes/submissions/<tu_nombre>_diagram.png`

## 4) Commit + push
```bash
git add B0/docs/cubesat_notes/submissions/
git commit -m "docs: add cubesat notes (B0.1)"
git push -u origin feature/<tu_nombre>-cubesat-notes
```

## 5) Abrir Pull Request (PR)
En GitHub/GitLab:
- Título claro (ej. `B0.1: cubesat notes - <tu_nombre>`)
- Describe qué has añadido
- Marca checklist
- Asigna al menos 1 reviewer

## 6) Responder al review
Si te piden cambios:
1. Edita los archivos en la **misma rama**
2. Haz commit + push
3. Responde al comentario indicando qué cambiaste

## 7) Merge (solo si cumple)
- 1 aprobación
- sin conversaciones abiertas
- checklist completo
