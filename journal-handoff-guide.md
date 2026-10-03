# Journal y Handoff en OpenCode: Guía sin Skills

## Journal (Bitácora)

### Qué es
Guardar contexto de sesiones para reusarlo después. Es un archivo persistente que crece con el tiempo.

### Flujo manual

#### Al finalizar cada sesión
Pide a OpenCode:
```
Guarda un resumen de esta sesión en un archivo markdown con:
- Qué se hizo
- Decisiones técnicas
- Archivos clave
- Pendientes
Guárdalo en ./journal/YYYY-MM-DD.md
```

#### Al iniciar nueva sesión
```
Lee ./journal/ y resume las sesiones recientes relevantes para continuar el trabajo
```

### Estructura de archivo
```markdown
# 2026-09-07
## Tarea: Implementar auth
## Completado:
- JWT configurado
- Middleware creado
## Pendiente:
- Tests
## Archivos: src/auth.ts, src/middleware.ts
```

---

## Handoff (Paso de testigo)

### Qué es
Transferir contexto a otra sesión/agente de forma estructurada. Es un snapshot puntual de una sesión específica.

### Flujo manual

#### Genera el handoff
```
Analiza esta conversación y genera un prompt conciso para la próxima sesión.
Incluye: estado actual, archivos relevantes (@file/...), y objetivo siguiente.
Formato markdown listo para copiar.
```

#### Pega en nueva sesión el prompt generado

### Ejemplo de handoff
```markdown
## Contexto
Implementando sistema de autenticación. JWT listo, falta middleware.

## Estado
- [x] Login endpoint
- [x] JWT tokens
- [ ] Middleware de protección
- [ ] Tests

## Archivos clave
@src/auth.ts
@src/middleware.ts

## Siguiente sesión
Crear middleware que verifique JWT en rutas protegidas
```

---

## Diferencias clave

| Característica | Journal | Handoff |
|----------------|---------|---------|
| Persistencia | Archivo que crece | Snapshot puntual |
| Frecuencia | Al finalizar cada sesión | Antes de cerrar sesión |
| Alcance | Múltiples sesiones | 1 sesión → 1 handoff |
| Uso | Leer antes de empezar | Pegar al iniciar nueva sesión |
| Propósito | Memoria acumulativa | Transferencia de contexto inmediato |

---

## Consejos prácticos

1. **Sé consistente** con la estructura de archivos
2. **Incluye fechas** en los nombres de archivo
3. **Referencia archivos** con `@file/path` para que OpenCode los cargue
4. **No guardes todo** - enfócate en decisiones y estado, no en cada línea de código
5. **Usa tags** en los journals para facilitar búsquedas futuras

---

## Bibliografía y Referencias

### Gestión de Contexto en Agentes IA

1. **Anthropic.** "Effective Context Engineering for AI Agents." *Anthropic Engineering Blog*, 2025.
   https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

2. **Packer, C. et al.** "MemGPT: Towards LLMs as Operating Systems." *arXiv preprint*, 2023.
   https://arxiv.org/abs/2310.08560
   - Paper seminal sobre gestión de memoria en LLMs usando virtualización de memoria (similar a OS)

3. **Zylos Research.** "Context Window Management and Session Lifecycle for Long-Running AI Agents." 2026.
   https://zylos.ai/research/2026-03-31-context-window-management-session-lifecycle-long-running-agents
   - Análisis completo de patrones de persistencia y handoffs

4. **Aureus.** "Building Reliable State Handoffs Between AI Agent Sessions." *DEV Community*, 2025.
   https://dev.to/aureus_c_b3ba7f87cc34d74d49/building-reliable-state-handoffs-between-ai-agent-sessions-1bk3
   - Investigación sobre los 5 niveles de un handoff efectivo

### Memoria en Agentes

5. **Zylos Research.** "AI Agent Memory Architectures: From Context Windows to Persistent Knowledge." 2026.
   https://zylos.ai/research/2026-04-05-ai-agent-memory-architectures-persistent-knowledge
   - Taxonomía de memoria episódica, semántica y procedimental

6. **Mem0 Research.** "Mem0: A Memory Layer for AI Agents." *arXiv*, 2025.
   https://arxiv.org/abs/2504.19413
   - Arquitectura de capas de memoria para agentes IA

7. **Zylos Research.** "Context Window Economics — Managing Token Budgets in Persistent AI Agents." 2026.
   https://zylos.ai/research/2026-05-27-context-window-economics-persistent-agents
   - Economía de tokens y gestión de presupuesto en agentes persistentes

### Frameworks y Herramientas

8. **Letta (MemGPT).** "Memory Blocks Architecture." 2026.
   https://www.letta.com/blog/memory-blocks
   - Implementación de memoria core/archival/recall

9. **LangChain.** "LangGraph Platform is now Generally Available." 2025.
   https://blog.langchain.com/langgraph-platform-ga/
   - Checkpointing y persistencia de estado

10. **Anthropic.** "Automatic Context Compaction — Claude Cookbook."
    https://platform.claude.com/cookbook/tool-use-automatic-context-compaction
    - Estrategias de compactación de contexto

### Patrones de Memoria Declarativa

11. **Zylos Research.** "Declarative Memory Injection: CLAUDE.md, AGENTS.md." 2026.
    - Patrón de archivos markdown inyectados en contexto como memoria persistente

12. **AutoDream System.** 2026.
    - Consolidación de memoria entre sesiones (similar a sueño REM)

---

## Conceptos teóricos de soporte

### Arquitectura de Memoria Jerárquica

Los agentes IA modernos usan 3 niveles de memoria:

1. **Memoria de trabajo (In-context):** Conversación activa. Volátil.
2. **Memoria de sesión (Session-scoped):** Archivos como `state.md`. Persiste entre reinicios.
3. **Memoria a largo plazo (Persistent):** Vector stores, databases. Se consulta bajo demanda.

### ¿Por qué importa?

Sin persistencia, cada sesión empieza desde cero. Con ella:
- El agente aprende patrones del usuario
- Se evita repetir decisiones
- Se mantiene coherencia entre sesiones
- Se reduce costo de tokens (no reenviar todo el historial)

### Fórmula del Handoff Efectivo

Un buen handoff tiene 5 componentes:
1. **Snapshot de estado** - valores actuales tipados
2. **Contexto narrativo** - 3-5 oraciones explicando el por qué
3. **Log de decisiones** - qué se decidió y qué se pospuso
4. **Cola de prioridades** - qué hacer primero, segundo, tercero
5. **Advertencias** - conocimiento institucional sobre limitaciones
