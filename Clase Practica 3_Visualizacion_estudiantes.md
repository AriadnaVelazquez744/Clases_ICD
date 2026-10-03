# Clase Práctica 3: Visualización de Datos

# Exploración y resultados con OpenCode

**Asignatura:** Introducción a la Ciencia de Datos
**Duración:** 90 minutos

---

## 1. ¿Por qué visualizar?

Una tabla de 500 números no dice nada. Un gráfico de 5 barras lo dice todo.

**La visualización cumple dos funciones:**


| Función       | Cuándo              | Ejemplo                                                     |
| ------------- | ------------------- | ----------------------------------------------------------- |
| **Explorar**  | Antes de analizar   | Ver la distribución de una variable, detectar valores raros |
| **Comunicar** | Después de analizar | Mostrar un resultado a quien decide                         |


> En ambos casos necesitas el mismo conocimiento: **qué tipo de gráfico usar según qué quieres mostrar**.

---



## 2. Elegir el gráfico correcto

La pregunta que decide el tipo de gráfico es **qué relación quieres ver entre las variables**:


| Si quieres ver...                         | Usa            | Ejemplo con datos de motos         |
| ----------------------------------------- | -------------- | ---------------------------------- |
| Cómo **cambia** una variable en el tiempo | Línea          | Evolución del precio medio por año |
| **Comparar** magnitudes entre categorías  | Barra          | Motos vendidas por provincia       |
| **Reparto** de un total en partes         | Pie / Dona     | % de motos por marca               |
| **Distribución** de una variable          | Histograma     | Precios agrupados en rangos        |
| **Relación** entre dos variables          | Dispersión     | Precio vs. año del modelo          |
| Evolución de **muchas** categorías        | Línea o área   | Tasa migratoria por provincia      |
| Ver **subconjuntos** de un total          | Línea + grupos | Hombres/Mujeres por año            |


**Error frecuente:** usar torta con más de 5 categorías. El ojo humano no puede comparar ángulos.

---



## 3. Exploración vs. Comunicación



### Exploración (antes de decidir)

Preguntas que responde la **exploración visual**:

- ¿Cómo se distribuye el precio? (histograma)
- ¿Hay valores extremos que distorsionan? (boxplot)
- ¿Las motos de qué provincia son más caras? (barra)
- ¿El precio sube con los años? (dispersión)



### Comunicación (después de decidir)

- El precio medio subió un 12% entre 2018 y 2024
- La Habana concentra el 38% de las publicaciones
- Las motos por debajo de 5 años concentran el 64% de la oferta

**Misma operación estadística, dos|goals visuales distintos.**

---



## 4. Estática vs. Interactiva



### Estática

- Imagen fija (PNG, SVG, PDF)
- Se ve de un vistazo
- Ideal para documentos, informes, artículos
- **Librerías:** matplotlib, seaborn



### Interactiva

- El usuario **explora** la gráfica
- Herramientas que PostData usa:
  - **Tocar una leyenda** → oculta/muestra esa serie (compara de a una)
  - **Pasa el mouse** → ver el valor exacto de un punto
  - **Zoom y scroll** → acercarse a una zona
  - **Selector desplegable** → cambiar de provincia, de año
- **Librerías:** Plotly, Altair, Bokeh, Panel



### Por qué la interacción cambia todo

En PostData, la gráfica de tasas migratorias permite **tocar en la leyenda** para ver:

```
Todas las provincias  →  ruido visual
Solo La Habana        →  tendencia clara
Solo La Habana + Holguín  →  comparación directa
```

> **Tú controlas qué se ve.** Eso es lo que hace interactiva a una visualización.

---



## 5. PostData: ejemplo de referencia

El sitio `postdataclub.github.io` es un punto de partida para esta clase:


| Análisis                                 | Visualización                 | Librería     |
| ---------------------------------------- | ----------------------------- | ------------ |
| Migración por provincia                  | Línea temporal + mapa         | C3 + Leaflet |
| Artículos de la Constitución modificados | Barra agrupada                | C3           |
| Salarios por sector                      | Área apilada                  | C3           |
| Rendimiento ENEE                         | Línea + torta                 | C3           |
| Correlaciones entre variables            | Dispersión                    | C3           |
| Panamericanos                            | Predicción (matplotlib) + web | Jupyter + JS |


**Todas usan el mismo principio:** un gráfico, una idea clara.

---



## 6. El flujo de trabajo con OpenCode



### 6.1 Preparación (una vez)

```bash
pip install pandas matplotlib seaborn plotly
```



### 6.2 El ciclo de trabajo

```
1. Describir qué quiero ver
        ↓
2. Pedirle el código a OpenCode
        ↓
3. Ejecutar y ver el resultado
        ↓
4. Si no es lo que quería → describir el cambio (nunca "arreglalo")
        ↓
5. Guardar el gráfico
```



### 6.3 El prompt: las 5 piezas

Un buen prompt para un gráfico tiene **cinco piezas**. Si falta una, OpenCode tiene que adivinar.

```
1. DATOS       → de dónde salen, qué columnas, cuántas filas
2. GRÁFICO     → qué tipo de gráfico quiero y por qué
3. VARIABLES   → qué variable va en X, cuál en Y, cuál se agrupa
4. TÍTULOS     → título, nombres de ejes, fuente
5. FORMATO     → tamaño, colores, si es interactivo o estático
```

**Ejemplo completo:**

```
DATOS:    Tengo un DataFrame df con los datos de motos de Cuba.
          Columnas: precio, anio, marca, provincia.
          Precio es numérico, anio es numérico, marca y provincia son texto.

GRÁFICO:  Un histograma de la distribución de precios.

VARIABLES: precio en el eje X, frecuencia en el eje Y.

TÍTULOS:  Título "Distribución de precios de motocicletas".
          Eje X: "Precio (CUP)", Eje Y: "Cantidad de motos".

FORMATO:  Figure size 10x6. Color azul. Grid suave. Fondo blanco.
          Guardar como PNG de 150 dpi en graficas/distribucion_precios.png
          Comentarios en español.
```

**El mismo prompt con solo el tipo de gráfico:**

```
Hazme un histograma del precio
```

OpenCode tendrá que inventar los datos, los títulos y el formato. El resultado funciona, pero no es lo que querías.

---



## 7. Prompts plantilla por tipo de gráfico



### Preparación común (siempre empieza así)

```
DATOS:    DataFrame df con motos de Cuba. Columnas: precio (numérico),
          anio (numérico), marca (texto), provincia (texto),
          estado (texto). 500 registros, algunos con precio nulo.
```



### Histograma (distribución)

```
[PREPARACIÓN]
GRÁFICO:  Histograma de df['precio'] con 30 bins.
VARIABLES: precio en X, frecuencia en Y.
NOTA:     Ignora los nulos automáticamente.
TÍTULOS:  "Distribución de precios". X: "Precio (CUP)". Y: "Cantidad".
FORMATO:  10x6, azul, grid, guardar en graficas/hist_precio.png
```



### Barra (comparar categorías)

```
[PREPARACIÓN]
GRÁFICO:  Barras horizontales del conteo de motos por marca.
VARIABLES: marca en Y, cantidad en X. Ordenar de mayor a menor.
TÍTULOS:  "Motos publicadas por marca". Y: "Marca". X: "Publicaciones".
FORMATO:  10x6, paleta de colores, guardar en graficas/barras_marca.png
```



### Barra agrupada (comparar 2 variables)

```
[PREPARACIÓN]
GRÁFICO:  Barras agrupadas: motos por provincia, separadas por estado.
VARIABLES: provincia en X, conteo en Y, estado define el color.
TÍTULOS:  "Motos por provincia y estado". X: "Provincia". Y: "Cantidad".
FORMATO:  11x6, leyenda a la derecha, guardar en graficas/grupo_provincia.png
```



### Línea (evolución temporal)

```
[PREPARACIÓN]
GRÁFICO:  Línea con el precio medio por año.
VARIABLES: anio en X, promedio de precio en Y. Un punto por año,
          ordenado cronológicamente.
TÍTULOS:  "Evolución del precio medio". X: "Año". Y: "Precio medio (CUP)".
FORMATO:  10x6, línea de 2.5px, marcadores, guardar en graficas/linea_precio.png
```



### Línea multi-serie (comparar categorías en el tiempo)

```
[PREPARACIÓN]
GRÁFICO:  Una línea por provincia con su precio medio por año.
VARIABLES: anio en X, precio medio en Y, provincia define el color.
TÍTULOS:  "Precio medio por año y provincia". X: "Año". Y: "Precio medio (CUP)".
FORMATO:  11x6, leyenda fuera, grid, guardar en graficas/linea_provincias.png
```



### Dispersión (correlación)

```
[PREPARACIÓN]
GRÁFICO:  Dispersión de precio vs. anio.
VARIABLES: anio en X, precio en Y, provincia como color.
NOTA:     Añade línea de tendencia.
TÍTULOS:  "Precio según año del modelo". X: "Año". Y: "Precio (CUP)".
FORMATO:  10x6, puntos con transparencia, guardar en graficas/disp_precio_anio.png
```



### Torta / Dona (reparto)

```
[PREPARACIÓN]
GRÁFICO:  Dona con el porcentaje de motos por marca, top 6 marcas.
VARIABLES: marca define el sector, porcentaje define el ángulo.
NOTA:     Agrupa el resto como "Otras".
TÍTULOS:  "Participación por marca". Leyenda a la derecha con porcentajes.
FORMATO:  8x8, guardar en graficas/dona_marcas.png
```



### Boxplot (valores extremos)

```
[PREPARACIÓN]
GRÁFICO:  Boxplot del precio por estado del vehículo.
VARIABLES: estado en X, precio en Y.
TÍTULOS:  "Distribución de precios por estado". X: "Estado". Y: "Precio (CUP)".
FORMATO:  10x6, guardar en graficas/boxplot_estado.png
```



### 🔑 Interactivo: Plotly (con tocar la leyenda)

```
[PREPARACIÓN]

GRÁFICO:  Gráfico INTERACTIVO con Plotly Express.
VARIABLES: anio en X, precio medio en Y, provincia define el color y la línea.
INTERACCIÓN:
   - Al tocar una provincia en la leyenda, esa línea se oculta.
   - Al tocarla de nuevo, reaparece. Esto es el comportamiento por defecto
     de Plotly y NO lo desactives.
   - Al pasar el mouse por un punto, muestra el valor exacto.
   - Cursor en modo "zoom".
   - Botón para volver al inicio (reset).
TÍTULOS:  Título, etiquetas de ejes, título de la leyenda "Provincia".
FORMATO:  write_html("graficas/interactivo_provincias.html") para guardar
          un archivo HTML autónomo. No usar fig.show() en la clase.
          Colores distintos por provincia.
```

> **Clave:** Plotly ya trae el comportamiento de ocultar series tocando la leyenda. **No hay que programarlo.** Solo hay que **no desactivarlo**, es decir, no escribir nunca `legend_itemclick=False` ni `legend_itemdoubleclick=False`.



### 🔑 Interactivo: selector desplegable (como en PostData)

```
[PREPARACIÓN]

GRÁFICO:  Gráfico INTERACTIVO con una lista desplegable para cambiar
          de provincia, igual que PostData.
CÓMO HACERLO:
   - Figura de Plotly con todas las provincias como líneas.
   - Botón "Actualizar" (updatemenus) que cambia la visibilidad de las
     líneas según el valor seleccionado.
   - Solo una provincia visible a la vez.
    - Etiquetas de los ejes correctas.
TÍTULOS:  "Tasa por provincia". Eje X: "Año". Eje Y: "Tasa por mil habitantes".
FORMATO:  write_html("graficas/interactivo_selector.html")
```

---



## 8. Errores frecuentes


| Error                         | Por qué falla                       | Solución en el prompt                                |
| ----------------------------- | ----------------------------------- | ---------------------------------------------------- |
| "No se puede guardar"         | La carpeta no existe                | "Crea la carpeta `graficas` si no existe"            |
| El gráfico sale vacío         | Hay nulos o columnas de texto       | "Ignora los nulos" / "Convierte a numérico antes"    |
| Las etiquetas se cortan       | Son muchas categorías               | "Muestra solo las 10 marcas más frecuentes"          |
| "Too many values to unpack"   | Se pidió una serie y hay varias     | "Agrupa por provincia y haz una línea por provincia" |
| La leyenda se encima          | Línea muy larga                     | "Leyenda fuera, a la derecha, con `bbox_to_anchor`"  |
| Se guarda en blanco           | Se hizo `plt.show()` y no `savefig` | "Guarda con `savefig` **antes** de `show()`"         |
| Sale "No module named plotly" | Falta instalar                      | `pip install plotly`                                 |


---



## 9. Ejercicio de la clase

**Objetivo:** cuatro gráficos del dataset de motos, uno de cada tipo.

```
1. Histograma  → distribución de precios    → graficas/hist_precio.png
2. Barra       → motos por marca            → graficas/barras_marca.png
3. Línea       → precio medio por año        → graficas/linea_precio.png
4. Interactivo → línea por provincia        → graficas/interactivo_provincias.html
                 (tocable en la leyenda)
```

**Todos con OpenCode, usando la plantilla de las 5 piezas.**

**Estructura esperada:**

```
/graficos/
├── datos/
│   └── motos_cuba.csv
├── graficas/
│   ├── hist_precio.png
│   ├── barras_marca.png
│   ├── linea_precio.png
│   └── interactivo_provincias.html
└── scripts/
    └── visualizacion.py
```

---



## 10. Verificación

- [ ] ¿Toca una leyenda y desaparece la línea?
- [ ] ¿Toca de nuevo y reaparece?
- [ ] ¿El mouse muestra el valor exacto?
- [ ] ¿Las gráficas tienen título, ejes rotulados y fuente?
- [ ] ¿Se guardaron todos los archivos?

¿Usé las 5 piezas del prompt?



