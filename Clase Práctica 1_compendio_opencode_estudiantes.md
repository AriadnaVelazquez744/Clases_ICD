# Compendio de OpenCode: definiciones, características y buenas prácticas

Material de apoyo para la **Clase Práctica 1** — Introducción a OpenCode.

Pueden consultar documentación de opencode en https://opencode.ai/docs/es

---

## 1. Definiciones

### 1.1 Agente de código
Programa que combina un **modelo de lenguaje grande (LLM)** con herramientas del sistema (lectura/escritura de archivos, terminal, búsqueda, Web) para ejecutar tareas de desarrollo de forma **autónoma, dirigida y conversacional**. A diferencia de un asistente de chat, un agente **actúa sobre el proyecto**: crea, modifica y ejecuta.

### 1.2 OpenCode
**Agente de código abierto** para IA, que trabaja desde la terminal mediante una **interfaz de usuario interactiva (TUI)**. Se conecta a más de 75 proveedores de modelos (Anthropic, OpenAI, Google, etc.) y a modelos locales. Sus características valoradas:

- **Código abierto** y respaldado por una comunidad activa (Discord, X).
- **Multi-provider**: un solo cliente para muchos proveedores y modelos.
- **Multi-agente**: agentes especializados (Build, Plan, subagentes).
- **Contextualizado**: usa el repositorio del proyecto para dar respuestas pertinentes.
- **Extensible**: comandos personalizados, skills, plugins, MCP.
- **Colaborativo**: compartir sesiones y "handoff" del trabajo.
- **Múltiples modalidades**: terminal (recomendada), versión web (`opencode web`) y aplicación de escritorio (`opencode.ai/download`).
- **Medición de uso y costes**: monitoriza tokens y coste estimado.

### 1.3 TUI (Terminal User Interface)
Interfaz de usuario que se ejecuta en la terminal. En OpenCode permite escribir prompts, ejecutar comandos (con `/`), referenciar archivos (con `@`) y ejecutar comandos del sistema (con `!`), todo sin salir de la terminal.

A diferencia de una **GUI (Graphical User Interface)** —interfaz gráfica con iconos y menús que se operan con ratón, touchpad o pantalla táctil (p. ej. GIMP, Firefox, VLC)—, la TUI se limita al terminal.

| Criterio | TUI | GUI |
|----------|-----|-----|
| Entorno | Terminal (texto) | Escritorio/ventanas (gráficos) |
| Entrada | Teclado (y ratón ocasional) | Ratón, touchpad o pantalla táctil |
| Curva de aprendizaje | Media | Baja (más intuitiva) |
| Eficiencia | Alta: menos recursos y atajos de teclado | Menor: consume más recursos, clicks |
| Acceso a funciones | Granular (`!` comandos, `@` archivos, `/` acciones) | Visual (menús e iconos) |
| Idoneidad | Usuarios técnicos (desarrolladores, científico de datos) | Usuario promedio |

La TUI es "parte GUI y parte CLI": más interacción visual que una línea de comandos pura, pero sigue siendo texto en terminal. **Relevancia para el científico de datos:** permite trabajar en servidores remotos vía SSH y automatizar flujos (pipelines, Git).

### 1.4 Sesión
Conversación contextualizada entre el usuario y el agente. Las sesiones pueden **guardarse, retomarse, exportarse y compartirse** (`/sessions`, `/export`, `/share`).

Sin persistencia de sesiones, **cada sesión empieza desde cero**.

### 1.5 Contexto
Conjunto de información que el agente tiene en cuenta al responder: archivos del proyecto, AGENTS.md, mensajes anteriores, referencias `@archivo` y hasta reglas globales del usuario.

**El contexto está limitado por los tokens.** Un **token** es la unidad mínima de texto que un LLM procesa (no coincide con la palabra: puede equivaler a una sílaba, una palabra corta o parte de una palabra; un carácter ocupa 1-2 tokens y en español una palabra promedio son ~1-2 tokens). El modelo tiene una **ventana de contexto** (máximo de tokens que puede "ver" en cada respuesta); todo lo que entra en esa ventana (conversación + archivos + reglas) **consume tokens**.

En la TUI de OpenCode se muestra **el porcentaje de la ventana de contexto que ya se ha usado** en la sesión actual: cuando se acerca al 100 %, hay que compactar (`/compact`), iniciar una sesión nueva (**journal/handoff**) o cerrar archivos referenciados; de lo contrario el modelo "olvida" lo inicial o falla. El porcentaje crece con cada mensaje, con cada archivo referenciado (`@`) y con cada skill cargada.

Regla práctica: menos contexto = más barato y más rápido.

### 1.6 Prompting
**Prompting** es la habilidad de redactar instrucciones efectivas para un modelo de lenguaje grande (LLM). Un buen prompt incluye cinco componentes: **rol** (a quién se le pide), **tarea** concreta y medible, **contexto** (archivos/datos), **restricciones** (qué no hacer) y **formato de salida** esperado.

---

## 2. Componentes clave

### 2.1 Agentes
OpenCode dispone de **agentes primarios** (se alternan con la tecla `Tab`; son el hilo principal de conversación) y **subagentes** (especializados, se invocan con `@nombre` o automáticamente).

| Agente | Tipo | Uso típico |
|--------|------|------------|
| **Build** | primario (por defecto) | Construir e implementar: lee, escribe y ejecuta. |
| **Plan** | primario (restringido) | Analizar y planificar **sin modificar** el repositorio. |
| **General** | subagente | Investigación y tareas de varios pasos; puede editar. |
| **Explore** | subagente (solo lectura) | Buscar archivos y responder preguntas del código. |

### 2.2 Modelos y proveedores
- OpenCode usa el **AI SDK** y **Models.dev**: soporta **75+ proveedores** y modelos locales.
  - **AI SDK**: kit de desarrollo de Vercel (ai-sdk.dev) que unifica el acceso a muchos proveedores de LLM con una API común; es la capa que OpenCode utiliza para conectarse con los modelos.
  - **Models.dev**: catálogo comunitario de identificadores y metadatos de modelos; OpenCode lo usa para reconocer cada modelo y tratarlo de forma consistente entre proveedores.
- Uso: `/models` para listar y seleccionar; `/connect` para añadir proveedores con sus claves.
- Identificador con formato `provider/model`, p. ej. `anthropic/claude-sonnet-4-20250514`.
- **Variantes** de razonamiento por modelo (p. ej. Anthropic `high`/`max`; OpenAI `low`/`high`/`xhigh`). Se ciclan con `ctrl+t`.
- **Planes de acceso**: BYOK (traes tus claves), OpenCode Go (cuota plana ~10$/mes), OpenCode Zen (monedero, pagas lo que usas) y OpenCode Free (modelos gratuitos con límite). Los **modelos locales** (p. ej. llama.cpp) cuestan cero y son privados (trabajan sin internet).
- **Modelos gratuitos (plan Free de OpenCode)**: MiMo-V2.5 Free, Ling 3.0 Flash Fin Free, Nemotron 3 Ultra Free, Nemotron 3.5 Lightning Free, Big Pickle y Muse Spark 1.3 Contributor Free. Están disponibles por tiempo limitado y sirven para aprender sin coste.
- **Modelos más utilizados actualmente** (docs oficiales, sep. 2026): GPT 5.2, GPT 5.1 Codex, Claude Opus 4.5, Claude Sonnet 4.5, Gemini 3 Pro y MiniMax M2.1. La lista cambia con el tiempo; en el plan Go abundan además los modelos abiertos (GLM, Qwen, DeepSeek, Kimi, Grok…).
- **Medición**: `opencode stats` (tokens por sesión, coste por modelo, herramientas) y herramientas como `tokscale`.

Regla práctica: tareas sencillas con variante baja, análisis exigente con variante alta.

### 2.3 Comandos de la TUI (slashes)
Comandos integrados frecuentes:

| Comando | Acción |
|---------|--------|
| `/init` | Crea o actualiza `AGENTS.md` (reglas del proyecto). |
| `/connect` | Añade un proveedor/API key. |
| `/models` | Lista los modelos disponibles. |
| `/new` | Nueva sesión. |
| `/sessions` | Lista y cambia de sesión. |
| `/undo` / `/redo` | Deshacer/rehacer mensajes (usa Git). |
| `/compact` | Resume y compacta el contexto. |
| `/export` | Exporta la conversación a Markdown. |
| `/copy` | Copia una transcripción de la sesión al portapapeles. |
| `/diff` | Muestra las diferencias de implementación. |
| `/skills` | Muestra las skills instaladas. |
| `/mcps` | Muestra los MCP configurados. |
| `/share` / `/unshare` | Comparte / deja de compartir la sesión. |
| `/thinking` | Muestra u oculta los razonamientos del modelo. |
| `/help` | Diálogo de ayuda. |

### 2.4 Atajos útiles del TUI
- `@` — referenciar archivos del proyecto (búsqueda difusa).
- `!` al inicio del mensaje — ejecutar un comando del sistema y volcar su salida a la conversación.
- `Tab` — alternar agentes primarios.
- `ctrl+x` líder: `u` undo, `r` redo, `n` nueva sesión, `l` sesiones, `e` editor, `m` modelos, `t` temas, `x` exportar, `q` salir, `c` compactar.
- `ctrl+p` — paleta de comandos.

### 2.5 Skills (destrezas)
Los **skills** son definiciones reutilizables de comportamiento que el agente carga **bajo demanda** con la herramienta `skill`. A diferencia de otras instrucciones, **no se cargan por defecto**: el agente solo tiene un **índice con el título y una descripción breve** de cada skill y decide cuándo cargarla si la tarea se relaciona con su descripción. Así consigue un comportamiento flexible y adaptativo sin sobrecargarse con información irrelevante.

- **Ubicaciones**: `.opencode/skills/<nombre>/SKILL.md` en el proyecto; también se buscan globalmente en `~/.config/opencode/skills/` y `~/.agents/skills/`, no solo en la carpeta `.opencode` del proyecto.
- **Frontmatter obligatorio** (`name` y `description`): `name` en minúsculas con guiones (1-64 caracteres), debe coincidir con el nombre de la carpeta; `description` de 1-1024 caracteres que defina qué hace el skill y cuándo usarlo. Opcionales: `license`, `compatibility`, `metadata`.
- **Permisos**: `permission.skill` (allow/ask/deny), con globs (`internal-*`).
- **Seguridad**: ten mucho cuidado con las skills: hay muchas por Internet, pero algunas pueden ser **no seguras o contener instrucciones maliciosas**. Usar solo skills de confianza y revisadas.

### 2.6 Ficheros Markdown de instrucciones
Cuatro **capas de personalización**, de menor a mayor especificidad:

1. **System prompt** — se construye automáticamente (instrucciones del modelo + herramientas + reglas del proyecto + skills cargadas). No se edita directamente.
2. **AGENTS.md** — reglas del proyecto; el punto de entrada principal. Se crea con `/init` o manualmente. Se recomienda **commitearlo** en Git. Debe mantenerse conciso (**hasta ~200 líneas**).
3. **Instrucciones adicionales** — ficheros en `docs/` referenciadas desde AGENTS.md con `@docs/filename.md` (carga bajo demanda). También el campo `instructions` de `opencode.json` admite múltiples rutas, globs e incluso URLs remotas (timeout 5 s).
4. **Skills** — comportamientos reutilizables cargados bajo demanda (sección 2.5).

- **Precedencia de AGENTS.md:** archivo de proyecto → `~/.config/opencode/AGENTS.md` (global) → `~/.claude/CLAUDE.md` (compatibilidad).
- **Comandos personalizados:** archivos `.md` en `.opencode/commands/` que se invocan con `/nombre`. Placeholders: `$ARGUMENTS`/`$1`, `$2`… (docs oficiales) o `$@` (convención manz); inyección de salida de comandos con `` !`comando` `` y referencias con `@archivo`.

### 2.7 Permisos
Control de acciones de los agentes: `"ask"` (preguntar), `"allow"` (permitir), `"deny"` (negar).

- Claves: `read`, `edit`, `bash`, `glob`, `grep`, `list`, `task`, `webfetch`, `websearch`, `lsp`, `skill`, `question`, `external_directory`, `todowrite`, etc.
- Soporta patrones (globs), p. ej. `"git push": "ask"` para pedir aprobación solo en publicaciones.
- **Buenas prácticas (manz):** revisar qué archivos va a modificar antes de confirmar; no dar permisos automáticos si no se confía en la tarea; usar `plan` para explorar; usar Git o backups antes de cambios grandes; elegir con cuidado los MCP y CLIs; en entornos sensibles, aislar con Docker.

### 2.8 Journal y Handoff (bitácora y paso de testigo)
Dos prácticas para **no perder contexto entre sesiones** (aplicables sin skills, con flujos manuales):

- **Journal (bitácora):** archivo persistente que **crece con el tiempo** (`./journal/YYYY-MM-DD.md`). Se genera al finalizar cada sesión con: qué se hizo, decisiones técnicas, archivos clave y pendientes. Se **lee al iniciar** una nueva sesión. Memoria acumulativa.
- **Handoff:** **snapshot puntual** de una sesión. Se genera antes de cerrar: un prompt conciso con estado actual, archivos relevantes (`@file/...`) y objetivo siguiente. Se **pega al iniciar** la nueva sesión. Transferencia inmediata.

| Característica | Journal | Handoff |
|----------------|---------|---------|
| Persistencia | Archivo que crece | Snapshot puntual |
| Frecuencia | Al finalizar cada sesión | Antes de cerrar la sesión |
| Alcance | Múltiples sesiones | 1 sesión → 1 handoff |
| Uso | Leer antes de empezar | Pegar al iniciar nueva sesión |
| Propósito | Memoria acumulativa | Transferencia de contexto inmediato |

**Fórmula del handoff efectivo (5 componentes):**
1. **Snapshot de estado** — valores actuales tipados.
2. **Contexto narrativo** — 3-5 oraciones que expliquen el porqué.
3. **Log de decisiones** — qué se decidió y qué se pospuso.
4. **Cola de prioridades** — qué hacer primero, segundo, tercero.
5. **Advertencias** — limitaciones y "cuidado con esto" (gotchas).

**Consejos:** sé consistente con la estructura; incluye fechas en los nombres; referencia archivos con `@`; **no guardes todo** (solo decisiones y estado); usa tags en los journals para buscar.

---

## 3. Características que la definen (para el científico de datos)

- **Automatización supervisada del análisis** — el agente inspecciona datos, escribe transformaciones y explica resultados.
- **Reproducibilidad** — el trabajo queda en el repositorio (scripts, AGENTS.md, exportaciones), sustentando la ciencia reproducible.
- **Transparencia** — las sesiones pueden exportarse, guardarse y compartirse (journaling).
- **Gobernabilidad** — permisos y agente `plan` permiten explorar y proponer sin alterar el repositorio.
- **Multi-proveedor** — no hay dependencia de un único modelo; permite comparar y usar recursos con criterio.

---

## 4. Buenas prácticas

### 4.1 De instalación y entorno
1. Instalar con el gestor disponible (`npm i -g opencode-ai@latest`, `brew install`, `curl -fsSL https://opencode.ai/install | bash`, etc.).
2. Configurar `EDITOR` (p. ej. `export EDITOR="code --wait"`) para que `/editor` y `/export` funcionen.
3. Trabajar siempre dentro de un **repositorio Git** para poder usar `/undo` y `/redo`.
4. No exponer claves de API: usar `/connect` y variables de entorno; nunca pegar llaves en prompts ni archivos versionados.
5. En Windows, usar **WSL** como entorno recomendado.

### 4.2 De construcción de contexto
6. Crear y mantener un `AGENTS.md` por proyecto (con `/init`); commitearlo.
7. Usar reglas globales (`~/.config/opencode/AGENTS.md`) solo para preferencias personales.
8. Referir archivos con `@` en lugar de copiar su contenido.
9. Mantener AGENTS.md **conciso** (≤ ~200 líneas) y modularizar el resto en `docs/` referenciadas con `@`; explicitar la lectura perezosa («lee @archivo solo si hace falta»).
10. Entender las **4 capas** de personalización (2.6) para elegir el lugar correcto de cada regla.

### 4.3 De prompting (efectividad)
11. Incluir: **rol**, **tarea** concreta y medible, **contexto** (archivos/datos), **restricciones** y **formato de salida**.
12. Ser específico: «calcula la media, el mínimo y el máximo de la columna `temperatura` de @datos.csv» supera a «analiza los datos».
13. Indicar las herramientas permitidas (`!` comando; `@` archivo) y aclarar qué no debe hacerse.
14. Iterar: pedir mejoras; usar `/undo` ante malos cambios.
15. Para labores de solo lectura o planificación, usar el agente **Plan**.

### 4.4 De agentes, modelos y costos
16. Alternar agentes con `Tab` según la tarea; invocar subagentes con `@general`, `@explore`.
17. Acotar las iteraciones con `steps` para controlar costo/tiempo.
18. Elegir la variante de razonamiento (`ctrl+t`) según la complejidad.
19. Probar el mismo prompt en varios modelos (`/models`) antes de adoptar uno.
20. Revisar `opencode stats` periódicamente para optimizar el uso (modelo pequeño para tareas simples).

### 4.5 De skills y comandos
21. Crear skills para tareas repetidas del dominio (p. ej. «resumen estadístico», «limpieza de tabla»).
22. Verificar nombre y descripción de cada skill (formato válido y único).
23. Cuidado con skills de terceros: **usar solo fuentes confiables y revisadas** (evitar instrucciones maliciosas).
24. Usar permisos de skill para proteger skills internas (`deny`/`ask`).

### 4.6 De journaling y handoff
25. Terminar cada sesión con un **journal** (`./journal/YYYY-MM-DD.md`) o `/export`.
26. Antes de cerrar, redactar un **handoff** con los **5 componentes** (2.8): estado, contexto narrativo, decisiones, prioridades, advertencias.
27. Incluir fechas, tags y referencias `@archivo`; **no guardar todo**, solo decisiones y estado.
28. Compartir sesiones (`/share`) solo si los datos lo permiten (privacidad).

### 4.7 Ética y responsabilidad
29. Revisar cambios que afecten datos personales; principio de **menor exposición**.
30. **Verificar los resultados** (el LLM puede errar en cálculos o interpretaciones).
31. Documentar el uso de IA: qué prompts se usaron y con qué modelo (transparencia metodológica).
32. Añadir a la **cola de advertencias** del handoff las limitaciones conocidas del modelo/datos.

---

## 5. Mini glosario

| Término | Significado |
|---------|-------------|
| **Prompt/Prompting** | Instrucción que se le da a un LLM; el arte de redactarla bien. |
| **System prompt** | Instrucción base automática que el agente envía al LLM en cada sesión. |
| **TUI** | Interfaz de usuario en terminal. |
| **LLM** | Large Language Model: modelo de lenguaje grande. |
| **Token** | Unidad mínima de texto que procesa un LLM (sílaba/palabra corta); todo el contexto se mide en tokens. |
| **Ventana de contexto** | Máximo de tokens que el modelo puede "ver" en una sesión; la TUI muestra su % de uso. |
| **Compactación** | Comprimir el contexto de la sesión en un resumen (`/compact`) para liberar ventana. |
| **Skill** | Destreza/instrucción reutilizable (`SKILL.md`), carga bajo demanda. |
| **Journal** | Bitácora persistente de sesiones (archivo que crece). |
| **Handoff** | Snapshot puntual para transferir contexto a otra sesión. |
| **Gotcha** | Trampa o "cuidado con esto" ya descubierto. |
| **Provider** | Proveedor de modelos de IA (Anthropic, OpenAI, Google…). |
| **AI SDK** | Kit de desarrollo (ai-sdk.dev) que unifica el acceso a los proveedores de LLM con una API común. |
| **Models.dev** | Catálogo comunitario de identificadores y metadatos de modelos que OpenCode usa de forma consistente. |
| **ByOK / Go / Zen / Free** | Planes de acceso a modelos cloud en OpenCode. |
| **MCP** | Model Context Protocol: conecta herramientas/servicios externos. |
| **Frontmatter** | Metadatos (YAML) al inicio de un archivo Markdown. |

---

*Fuentes consultadas: docs oficiales de OpenCode (sep. 2026), Guía de OpenCode y Skills e instrucciones de ai.manz.dev, y la Guía de Journal y Handoff (sin skills).*