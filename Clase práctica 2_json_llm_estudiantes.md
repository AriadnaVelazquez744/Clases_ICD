# Clase práctica 2: JSON y LLM

Material de referencia para el trabajo con modelos de lenguaje (LLM) y el formato JSON en la extracción de información estructurada.

# Utilización de modelos de lenguaje para automatizar extracción de información estructurada de texto plano

## 1. Roles en los mensajes

Los modelos modernos funcionan con una estructura conversacional basada en roles:

| Rol           | Función práctica                                                                 |
| ------------- | -------------------------------------------------------------------------------- |
| **system**    | Define reglas, personalidad y comportamiento del modelo. Es como un contrato     |
| **user**      | Es la solicitud, pregunta o tarea a ejecutar.                                    |
| **assistant** | Respuestas previas del modelo; se usa para dar contexto en conversaciones largas.|

**Idea fundamental:**
El modelo se comporta según lo que diga el `system`, pero responde directamente a lo que diga el `user`.

## 2. Guía básica de prompting aplicada a Data Science

| Objetivo               | Técnica recomendada                       |
| ---------------------- | ----------------------------------------- |
| Extraer datos          | Roles + formato explícito + temperatura 0 |
| Resumir                | Instrucciones claras + temperatura media  |
| Clasificar             | Ejemplos + formato con etiquetas          |
| Generar código         | Especificar lenguaje + librerías exactas  |
| Convertir texto → JSON | Establecer claves, ejemplo y reglas       |

---

## 3. Las reglas de oro del JSON

JSON tiene reglas muy estrictas. Si se rompe una sola, el archivo deja de ser válido. Esta estrictez es buena: significa que no hay ambigüedad.

Reglas básicas:

1. **La clave siempre va con comillas dobles**: `"nombre"`, nunca `nombre`.
2. **Dos puntos** separan la clave del valor: `"nombre": "Ana"`.
3. **Coma entre un dato y el siguiente**: no puede haber coma al final del último dato de cada grupo.
4. **Valores de texto van entre comillas dobles**: `"Madrid"`.
5. **Números NO llevan comillas**: `30`, `1.75`, `-5`.
6. **Verdadero/falso se escriben en minúscula**: `true` y `false`.
7. **El vacío se escribe** `null`.

## 4. ¿Cómo saber si tu JSON está bien escrito?

Puedes pegar tu JSON en un validador online gratuito (como jsonlint.com o jsonparseronline.com). Si hay un error de puntuación, te lo dirá y hasta te señalará la línea exacta.

También existe el comando `jq . tu_archivo.json` si algún día usas Linux/Mac con `jq` instalado. Pero para empezar, un validador web es más que suficiente.

## 5. Resumen rápido de JSON

| Concepto | Símbolo | Ejemplo |
|----------|---------|---------|
| Llaves (objeto o diccionario) | `{}` | `{ "a": 1 }` |
| Corchetes (arreglo, array o lista) | `[]` | `[1, 2, 3]` |
| Texto | `" "` | `"hola"` |
| Número | sin comillas | `42` |
| Verdadero / falso | `true` / `false` | `true` |
| Vacío | `null` | `null` |

**De un vistazo:**

- `{}` agrupa datos con nombre → `{ "nombre": "Ana" }`
- `[]` ordena una lista → `["Ana", "Luis"]`
- Se escribe todo con comillas dobles y sin comas de más.

