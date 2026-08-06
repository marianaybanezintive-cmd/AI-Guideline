# Workflow: Historias de usuario desde épicas

**Skill:** `po-expert-user-stories`

**Carpeta de trabajo:** `analisis/`

## Cuándo usar

- Descomponer épicas en historias de usuario detalladas
- Refinamiento PO con escenarios Gherkin en español
- Exportar backlog a CSV compatible con hojas de cálculo

## Pasos

1. Colocar documentos de entrada (épicas, story maps, diagramas) en `analisis/inputs/`.
2. Abrir un chat nuevo e indicar: *"Trabaja en `analisis/`, usa `po-expert-user-stories` para…"*
3. El agente genera:
   - `.md` con todas las historias (formato completo del skill)
   - `.csv` con 4 columnas: Issue Type; Issue Key; Summary; Description
4. Verificar que ambos archivos compartan el mismo nombre base en `analisis/outputs/`.

## Salida por defecto

```
analisis/outputs/po-expert-output/
  po-historias-usuario-{YYYY-MM-DD}-{slug}.md
  po-historias-usuario-{YYYY-MM-DD}-{slug}.csv
```

## Referencia

Ver skill completo en `~/.agents/skills/po-expert-user-stories/SKILL.md`.
