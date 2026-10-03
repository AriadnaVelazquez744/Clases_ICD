# Utilización de modelos de lenguaje para automatizar extracción de información estructurada de texto plano

## 1. ¿Qué significa usar un modelo de lenguaje (LM) desde código?

Un LM (Language Model), es un modelo entrenado para entender texto, generar texto y extraer información.
Como científicos de datos, no siempre usarán una interfaz gráfica como ChatGPT; muchas veces necesitarán:

- Automatizar tareas
- Procesar grandes volúmenes de texto
- Integrar LLMs dentro de un pipeline de datos
- Convertir texto desordenado en datos estructurados (JSON)

Esto se hace escribiendo código (normalmente Python) que envía un texto al modelo y recibe una respuesta.

## 2. Maneras de ejecutar un LM desde código

Existen dos grandes enfoques para usar modelos sin interfaz visual:

### A. Ejecutar modelos LOCALMENTE (sin conexión, sin servicio externo)

Herramientas como LM Studio, Ollama, GPT4All, o llama.cpp permiten:

- Descargar un modelo (por ejemplo Llama 3 o Mistral).
- Ejecutarlo en tu propia computadora.
- Enviarle prompts desde Python a un servidor local.

**Ventajas**:

- No hay costo por uso.
- No se envían datos a terceros (privacidad).
- Funciona sin Internet.

**Desventajas**:

- Necesitas suficiente memoria RAM y CPU/GPU.
- Los modelos locales suelen ser menos potentes que los de la nube.

**Ejemplo conceptual**  

LM Studio puede levantar un servidor local en <http://localhost:1234>
Tu código en Python envía peticiones allí como si fuera una API.

### B. Usar APIs EXTERNAS (modelos alojados en la nube)

**Ejemplos**:

- Gemini API (Google)
- OpenAI API
- Hugging Face Inference API

Aquí no descargas nada.
Solo envías un request a Internet y obtienes la respuesta.

**Ventajas**:

- Modelos más potentes.
- No requieren hardware local.
- Muy rápido de implementar.

**Desventajas**:

- Tienen costo tras un límite gratuito.
- Se necesita Internet.
- Debes cuidar credenciales y seguridad.

### Hugging Face: una alternativa híbrida

Hugging Face puede usarse de tres formas:

- Descargar modelos y ejecutarlos localmente (como LM Studio).
- Usar la Inference API (como Gemini o OpenAI).
- Usar espacios (Spaces) que ejecutan demos pre-configuradas.

Es una plataforma útil para buscar modelos y documentación.

## 3. ¿Qué lleva la llamada a un modelo?

Cuando trabajamos con un LLM desde código, necesitamos enviar:

- El endpoint donde se encuentra el modelo.
- Una clave de autenticación (si es un modelo externo).
- El nombre del modelo.
- Los mensajes que queremos que procese (prompt).
- Parámetros de configuración (temperatura, tokens, etc.).

La biblioteca de OpenAI simplifica todo esto, ocultando detalles como los headers y la firma de la petición, y permitiendo centrarnos únicamente en la parte funcional.

## 4. Inicializar el cliente de OpenAI

    from openai import OpenAI

    API_BASE = "DIRECTION_DEL_MODELO"
    API_KEY = "TU_API_KEY"
    MODELO_ACTUAL = "NOMBRE_DEL_MODELO"

    try:
        client = OpenAI(base_url=API_BASE, api_key=API_KEY)
        print(f"✅ Conexión configurada a: {API_BASE}")
    except Exception as e:
        print(f"❌ ERROR al configurar la conexión. Detalle: {e}")

Este cliente ya incorpora:

- Autenticación
- Encabezados
- Manejo de errores
- Construcción del cuerpo de la solicitud

Por ello no necesitamos requests, fetch ni definir headers manuales.

## 5. Roles en los mensajes

    messages=[
            {"role": "system", "content": "Habla como un profesor experto."},
            {"role": "user", "content": "Explícame qué es un vector."}
        ]

Los modelos modernos funcionan con una estructura conversacional basada en roles:

| Rol           | Función práctica                                                                  |
| ------------- | --------------------------------------------------------------------------------- |
| **system**    | Define reglas, personalidad y comportamiento del modelo. Es como un contrato                         |
| **user**      | Es la solicitud, pregunta o tarea a ejecutar.                                     |
| **assistant** | Respuestas previas del modelo; se usa para dar contexto en conversaciones largas. |

**Idea fundamental**:
El modelo se comporta según lo que diga el system, pero responde directamente a lo que diga el user.

## 6. Parámetros más importantes al llamar a un modelo

Estos parámetros influyen en el comportamiento de la generación:

### `temperature`

Controla la variabilidad:

- **0.0** → Respuestas precisas, determinísticas (ideal para extracción de datos, JSON).
- **0.4–0.7** → Balance ideal para explicaciones.
- **>1.0** → Creatividad.

### `max_tokens`

Cantidad máxima de tokens generados.

- max_tokens=300

### `response_format`

Para forzar salida JSON válida:

- response_format={"type": "json_object"}

### `top_p`, `frequency_penalty`, `presence_penalty`, `stop`

Son parámetros secundarios pero útiles:

| Parámetro             | Para qué sirve                                   |
| --------------------- | ------------------------------------------------ |
| **top_p**             | Controla probabilidad acumulada, se deja en 1.0. |
| **frequency_penalty** | Evita repeticiones.                              |
| **presence_penalty**  | Incentiva ideas nuevas.                          |
| **stop**              | Fuerza un final específico de generación.         |

## 7. Uso de modelos LOCALES con sintaxis OpenAI

Muchos servidores locales (LM Studio, Ollama, etc.) ofrecen **"OpenAI API Compatibility Mode"**.

Esto permite usar exactamente la misma sintaxis, solo cambia:

- La **URL** (`base_url`)
- No se usa API key real

```python
client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="not-required-but-must-be-set"
)
```

## 8. Comandos principales de la biblioteca de OpenAI

### ✔ Crear cliente

- client = OpenAI(api_key="...")

### ✔ Llamada de chat (más usada)

- client.chat.completions.create(...)

### ✔ Listar modelos

- client.models.list()

### ✔ Obtener detalles de un modelo

- client.models.retrieve("gpt-4.1-mini")

## 9. Buenas prácticas generales al usar modelos desde código

Aunque OpenAI maneja los headers internamente, **sí debemos seguir buenas prácticas** en el flujo de interacción:

- **Usa modelos diseñados para el propósito de tu tarea**

  - Extracción → modelos pequeños, temperatura baja.
  - Análisis o razonamiento → modelos medianos.
  - Explicación o creatividad → modelos grandes.

- **Siempre define un rol system claro**: Evita ambigüedades y mejora la calidad.

- **Cuando necesites datos estructurados, fuerza JSON**: Reduce errores, facilita procesamiento.

- **Valida siempre el JSON que retorna el modelo**: Especialmente con modelos locales.

- **Evita enviar información excesiva o irrelevante**: Reduce costo y ruido

## 10. ¿Qué es el *prompting*?

El *prompting* es el proceso de **dar instrucciones a un modelo de lenguaje** para que produzca una respuesta útil, siguiendo nuestras reglas, formato o estilo.

Es equivalente a:

- Escribir un “enunciado” bien diseñado.
- Dar instrucciones claras.
- Especificar formato y restricciones.

Un mal prompt produce resultados inconsistentes.
Un buen prompt produce datos estables, con menos errores.

## 11. Cómo escribir un buen mensaje **system** (Contexto y reglas)

El rol **system** debe:

1. Definir la tarea general claramente.
2. Especificar el formato deseado.
3. Incluir restricciones.
4. Indicar qué hacer en casos especiales (datos faltantes, ambigüedad, ruido).

Aquí un ejemplo **bien diseñado**:

```python
{
    "role": "system",
    "content": (
        "Eres un asistente especializado en extracción y limpieza de datos. "
        "Tu tarea es analizar textos y devolver únicamente un JSON válido. "
        "Si un dato no aparece explícitamente, usa null. "
        "No inventes información. "
        "No incluyas explicaciones ni texto adicional fuera del JSON."
    )
}
```

**Principios clave**:

- Tono directo
- Reglas explícitas
- Prohibiciones (“no inventes”, “no incluyas texto extra”)
- Comportamiento definido (“solo JSON válido”)

## 12. Cómo escribir un buen mensaje **user** (Qué queremos extraer)

El mensaje **user** debe:

1. Incluir el texto a analizar.
2. Especificar exactamente qué campos se deben extraer.
3. Incluir ejemplos cuando sea necesario.

Ejemplo:

```python
{
    "role": "user",
    "content": (
        "Extrae del siguiente texto los campos: nombre, edad, ciudad, email.\n\n"
        "Texto: Maria Lopez tiene 24 años y vive en Madrid. Su email es maria@example.com."
    )
}
```

### 💡 Recomendación práctica

Los modelos funcionan mejor si le dices **qué campos y en qué orden**.

## 13. ¿Y si `response_format={"type": "json_object"}` NO está disponible?

Esto ocurre:

- en modelos antiguos,
- modelos locales,
- algunas APIs no compatibles,
- plataformas sin soporte para JSON mode.

En esos casos, se fuerza manualmente mediante **instrucciones en el rol system**, por ejemplo:

```python
{
    "role": "system",
    "content": (
        "Devuelve *únicamente* un JSON válido con las claves: nombre, edad, ciudad, email. "
        "No incluyas comentarios, explicaciones ni texto fuera del JSON. "
        "Si un campo falta, escribe null."
    )
}
```

Y si deseamos máxima confiabilidad, añadimos un ejemplo explícito:

```python
{
    "role": "system",
    "content": (
        "Devuelve únicamente un JSON válido. Formato esperado:\n"
        "{\n"
        "  \"nombre\": \"string\",\n"
        "  \"edad\": number,\n"
        "  \"ciudad\": \"string\",\n"
        "  \"email\": \"string\"\n"
        "}"
    )
}
```

➡ Los ejemplos son una técnica fundamental de *prompt engineering*:
**cuando muestras el formato deseado, el modelo tiende a imitarlo con precisión.**

## 14. Estrategias de Prompt Engineering para mejorar extracciones

A continuación, las técnicas más prácticas para estudiantes.

### **Instrucciones claras y explícitas**

Evitar promts vagos como:

> “Analiza este texto y dame la información."

Mejor:

> “Extrae las entidades: nombre, edad, ciudad, email.
> Devuelve únicamente un JSON válido con esas claves.”

### **Few-shot prompting (varios ejemplos)**

Ideal cuando:

- El texto es complejo.
- Queremos que el modelo aprenda un patrón preciso.
- Se mezcla español e inglés, estructuras caóticas, etc.

### **Descripciones de fallos esperados**

Las reglas negativas son muy poderosas:

- “No inventes datos.”
- “No deduzcas información implícita.”
- “No incluyas texto antes o después del JSON.”
- “No uses comentarios.”

Esto reduce al mínimo:

- alucinaciones,
- explicaciones innecesarias,
- formato incorrecto.

### **Control de formato mediante listas de claves**

Siempre lista las claves que quieres.

Ejemplo:

    Devuelve un JSON con las claves: nombre, edad, dirección, telefono.

El modelo rara vez agregará más campos.

### **Divide en pasos (Chain-of-thought oculto)**

Si la tarea es muy difícil:

```python
{
  "role": "system",
  "content": (
      "Primero analiza internamente el texto paso a paso, "
      "pero no muestres tu razonamiento. "
      "Después, devuelve únicamente un JSON válido."
  )
}
```

Permite que el modelo piense antes de responder, sin mostrarlo.

---

## 15. Guía básica de prompting aplicada a Data Science

Los estudiantes deben aprender a pensar así:

| Objetivo               | Técnica recomendada                       |
| ---------------------- | ----------------------------------------- |
| Extraer datos          | Roles + formato explícito + temperatura 0 |
| Resumir                | Instrucciones claras + temperatura media  |
| Clasificar             | Ejemplos + formato con etiquetas          |
| Generar código         | especificar lenguaje + librerías exactas  |
| Convertir texto → JSON | Establecer claves, ejemplo y reglas       |

## 16. Recomendaciones finales

1. **Siempre empieza por el rol system.** Ahí está el “contrato”.
2. **Define claves y formato explícito.**
3. **Usa ejemplos siempre que puedas.**
4. **Usa temperatura 0 para extracción de datos.**
5. **Si un modelo no soporta JSON mode, fuerza JSON mediante instrucciones.**
6. **Evita prompts vagos.**
7. **Revisa cuidadosamente la salida por si hay errores menores de formato.**
