# Ejemplos de uso — PO & Arquitecto SR

## Invocar el agente

En Cursor Agent, escribe:

```
Activa el skill po-architect-agent
```

O directamente:

```
Usa jira-stories-to-architecture con las historias PROJ-101, PROJ-102 y PROJ-103
```

## Ejemplo 1 — Desde claves Jira

**Usuario:**
> Genera la arquitectura completa para PROJ-45, PROJ-46 y PROJ-47

**Agente (Alex):**
1. Llama `read_jira_issue` por cada clave (MCP `user-jira`)
2. Analiza actores, entidades y flujos
3. Escribe carpeta `AI-Outputs/po-architect-agent/2026-06-30-proj-45/`
4. Ejecuta `python AI-Agents/jira-stories-to-architecture/scripts/render_mermaid.py AI-Outputs/po-architect-agent/2026-06-30-proj-45`
5. Responde con rutas y decisiones clave

## Ejemplo 2 — Búsqueda JQL

**Usuario:**
> Arquitectura de todas las stories del sprint actual del proyecto MIAPP

**Agente:**
1. `search_jira_issues` con JQL: `project = MIAPP AND sprint in openSprints() AND type = Story`
2. Mismo flujo de generación

## Ejemplo 3 — Sin Jira (modo manual)

**Usuario:**
> AR — aquí van las historias: [pega markdown con COMO/QUIERO/PARA y criterios]

**Agente:** Omite MCP; usa el texto como input.

## Ejemplo 4 — Solo diagrama

**Usuario:**
> DG — necesito un diagrama de secuencia para el flujo de notificación por email

**Agente:** Genera `.mmd` + `.png` puntual en `AI-Outputs/po-architect-agent/`.

## Regenerar PNG tras editar un diagrama

Desde la raíz del repo AI-Guideline:

```bash
python AI-Agents/jira-stories-to-architecture/scripts/render_mermaid.py AI-Outputs/po-architect-agent/2026-06-30-mi-proyecto/
```

## Menú del agente Alex

| Code | Acción |
|------|--------|
| JA | Paquete completo desde Jira |
| AR | Paquete desde texto manual |
| DG | Diagrama puntual |
| JR | Solo lectura/síntesis Jira |
