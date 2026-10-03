# Tutorial de JSON desde cero

> Para personas que nunca han programado. No necesitas instalar nada: solo leer y entender.

---

## 1. ¿Qué es JSON?

JSON (se lee *yeison* en inglés, o *jay-son*) significa **JavaScript Object Notation**.

Pero no te asustes por el nombre. JSON **no es un lenguaje de programación**.
Es simplemente una **forma de escribir información** para que:

- Los humanos la podamos leer fácilmente.
- Las computadoras la puedan entender con precisión.

Imagina que JSON es como un **formulario gigante** o una **ficha en una base de datos**.
Cuando una app te pide tu nombre y te responde "usuario creado", detrás de escena
esa información casi siempre se guarda o se envía en formato JSON.

Un ejemplo muy común de JSON:

```json
{
  "nombre": "Ana",
  "edad": 30,
  "ciudad": "Madrid"
}
```

Eso se lee así:

- Existe un objeto (las llaves `{}`) que describe a una persona.
- Esa persona tiene `nombre`, que vale `"Ana"`.
- Tiene `edad`, que vale `30`.
- Tiene `ciudad`, que vale `"Madrid"`.

Cada línea es un **dato** formado por una **clave** (el nombre del dato)
y un **valor** (el contenido del dato).

---

## 2. Las reglas de oro del JSON

JSON tiene reglas muy estrictas. Si se rompe una sola, el archivo deja de ser válido.
Esta estrictez es buena: significa que no hay ambigüedad.

Reglas básicas:

1. **La clave siempre va con comillas dobles**: `"nombre"`, nunca `nombre`.
2. **Dos puntos** separan la clave del valor: `"nombre": "Ana"`.
3. **Coma entre un dato y el siguiente**: no puede haber coma al final del último dato de cada grupo.
4. **Valores de texto van entre comillas dobles**: `"Madrid"`.
5. **Números NO llevan comillas**: `30`, `1.75`, `-5`.
6. **Verdadero/falso se escriben en minúscula**: `true` y `false`.
7. **El vacío se escribe** `null`.

Ejemplo que usa las reglas anteriores:

```json
{
  "nombre": "Luis",
  "edad": 25,
  "altura": 1.78,
  "estudiante": true,
  "hobbies": null
}
```

---

## 3. Los 4 bloques de construcción de JSON

Todo documento JSON se construye combinando estos bloques:

### a) El valor de texto (string)

Cualquier palabra, frase u oración, siempre entre comillas dobles.

```json
"hola"
"Madrid, España"
"42"  -> esto es TEXTO, no el número 42
```

### b) El número (number)

Puede ser entero o con decimales. Sin comillas.

```json
3
-10
25.5
```

### c) El valor lógico (boolean)

Solo dos opciones:

```json
true
false
```

### d) El vacío (null)

Significa "sin valor", "desconocido" o "no aplica".

```json
null
```

Y además tenemos dos **estructuras** que agrupan los valores anteriores:

### e) El objeto (object)

Se encierra entre llaves `{}`. Agrupa datos bajo distintas claves.

```json
{
  "nombre": "Ana",
  "edad": 30,
  "activa": true
}
```

### f) El arreglo (array)

Se encierra entre corchetes `[]`. Es una **lista ordenada** de valores.

```json
["Madrid", "Barcelona", "Valencia"]
```

Esta lista de números:

```json
[1, 2, 3, 4, 5]
```

Y hasta listas de objetos (¡lo más común en el mundo real!):

```json
[
  { "nombre": "Ana", "edad": 30 },
  { "nombre": "Luis", "edad": 25 }
]
```

---

## 4. Anidar: objetos dentro de objetos

En JSON puedes meter estructuras una dentro de otra, cuantas veces quieras.
Esto se llama **anidar**. Ejemplo: los datos de un empleado.

```json
{
  "empleado": {
    "nombre": "Marta",
    "departamento": "Ventas",
    "salario": {
      "bruto": 2400,
      "moneda": "EUR"
    },
    "idiomas": ["Español", "Inglés"]
  }
}
```

Leído de forma natural:

- El empleado es Marta.
- Su departamento es Ventas.
- Su salario es un objeto con `bruto` 2400 y moneda EUR.
- Habla dos idiomas: Español e Inglés.

---

## 5. Un ejemplo del mundo real

Una pizzería podría tener un pedido así:

```json
{
  "pedido": 1024,
  "cliente": {
    "nombre": "Carlos",
    "telefono": "555-9999"
  },
  "productos": [
    { "nombre": "Pizza margarita", "cantidad": 2, "precio": 8.5 },
    { "nombre": "Refresco", "cantidad": 2, "precio": 2.0 }
  ],
  "entregado": false
}
```

Fíjate cómo se combinan **objetos** `{}`, **arreglos** `[]`, **números**,
**texto** y **booleanos** en un mismo documento.

---

## 6. Errores que evitan los principiantes (y cómo corregirlos)

### Coma de más

```json
{
  "nombre": "Ana",
  "edad": 30,   <- error: coma que no debería estar
}
```

Correcto:

```json
{
  "nombre": "Ana",
  "edad": 30
}
```

### Comillas simples

```json
{ "nombre": 'Ana' }   <- error: JSON exige comillas dobles
```

Correcto:

```json
{ "nombre": "Ana" }
```

### Número entre comillas

```json
{ "edad": "30" }   <- dice que 30 es texto, no número
```

Correcto:

```json
{ "edad": 30 }
```

### Clave sin comillas

```json
{ nombre: "Ana" }   <- error
```

Correcto:

```json
{ "nombre": "Ana" }
```

---

## 7. ¿Cómo saber si tu JSON está bien escrito?

Puedes pegar tu JSON en un validador online gratuito (como jsonlint.com o
jsonparseronline.com). Si hay un error de puntuación, te lo dirá y hasta te
señalará la línea exacta.

También existe el comando:

```bash
jq . tu_archivo.json
```

si algún día usas Linux/Mac con `jq` instalado. Pero para empezar,
un validador web es más que suficiente.

---

## 8. ¿Para qué se usa JSON en la vida real?

- **APIs** (los "meseros digitales" entre apps): cuando una página pide datos a un servidor, casi siempre responde en JSON.
- **Archivos de configuración**: muchos programas guardan sus opciones en `.json` (por ejemplo algunos editores de código).
- **Bases de datos**: algunas bases (como MongoDB) guardan la información directamente en formato JSON.
- **Aplicaciones del móvil y la web**: guardan preferencias, resultados de partidas, carritos de compra, etc.

---

## 9. Practica (no necesitas programa, solo papel o tu mente)

Intenta escribir a mano tu respuesta y luego revisa las reglas del punto 2:

1. Escribe un objeto con tus **datos personales**: nombre, edad, y si estudias o no.
2. Escribe un **arreglo** con 3 comidas que te gusten.
3. Escribe un objeto llamado `"libro"` con: título, autor, año y una lista de capítulos.
4. Rodea con un círculo dónde usaste objetos (`{}`) y dónde arreglos (`[]`).

Respuestas de ejemplo (¡no mires antes de intentarlo!):

```json
1.
{ "nombre": "Rosa", "edad": 28, "estudias": true }

2.
["Paella", "Pizza", "Ensalada"]

3.
{
  "libro": {
    "titulo": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "anio": 1967,
    "capitulos": ["Capítulo uno", "Capítulo dos", "Capítulo tres"]
  }
}
```

---

## 10. Resumen rápido

| Concepto | Símbolo | Ejemplo |
|----------|---------|---------|
| Llaves (objeto) | `{}` | `{ "a": 1 }` |
| Corchetes (arreglo) | `[]` | `[1, 2, 3]` |
| Texto | `" "` | `"hola"` |
| Número | sin comillas | `42` |
| Verdadero / falso | `true` / `false` | `true` |
| Vacío | `null` | `null` |

**De un vistazo:**
- `{}` agrupa datos con nombre → `{ "nombre": "Ana" }`
- `[]` ordena una lista → `["Ana", "Luis"]`
- Se escribe todo con comillas dobles y sin comas de más.

Cuando domines esto, JSON te parecerá natural. Y lo bueno es que
sirve en cualquier lenguaje: JavaScript, Python, etc. Es un idioma universal
de información.