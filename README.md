# Conectate-Uis

Integrantes
- David Santiago Sandoval Mancilla — 2242009  
- Luiggy Ivan Rios Enrique — 2243166  
- Maria Alejandra Hernandez Perez — 2242001  
- Vicktor Josué David Ardila Carreño — 2230266

Introducción
En el contexto universitario, la gestión de rutas y conexiones entre distintos edificios y zonas del campus puede ser compleja, especialmente cuando buscamos eficiencia y claridad en la información. La problemática surge al intentar representar estas conexiones de manera estructurada y navegable, de modo que se puedan consultar rutas, accesibilidad y relaciones jerárquicas de manera sencilla y visual.

1. **Listas enlazadas:** la primera fase del proyecto consistió en manejar relaciones simples, uno a uno, entre los distintos puntos del campus. Esta implementación nos permitió comprender la base de la gestión de conexiones, pero mostró limitaciones a medida que el número de nodos y relaciones crecía.

2. **Árboles:** para superar las limitaciones de las listas, implementamos árboles jerárquicos usando la librería **BigTree**. Esta fase permite manejar relaciones de uno a muchos, ideal para representar un campus con múltiples edificios, zonas y niveles de conexión. Además, ofrece funciones visuales que facilitan la comprensión de la estructura y la navegación entre nodos.

3. **Grafos:** como siguiente evolución, el proyecto incluye grafos, que permiten modelar relaciones más complejas, incluyendo conexiones muchos a muchos. Esto es crucial para simular rutas reales, optimizar caminos y considerar accesibilidad en diferentes escenarios del campus.

## Descripción General del Proyecto
El proyecto tiene como objetivo crear un sistema de gestión de rutas y conexiones del campus universitario que sea:

- **Escalable:** capaz de crecer conforme se agregan más edificios y zonas.
- **Intuitivo y visual:** mediante representaciones jerárquicas (árboles) y gráficas (grafos) para facilitar la comprensión.
- **Interactivo:** el usuario puede agregar nodos, buscar por nombre o ID, listar zonas accesibles y calcular rutas entre ubicaciones.
- **Flexible:** la transición de listas a árboles y grafos permite manejar distintos niveles de complejidad según la necesidad.

Cada fase del proyecto incorpora funcionalidades clave:

- **Listas enlazadas:** manejo básico de nodos y conexiones uno a uno.
- **Árboles:** jerarquía, búsqueda por nombre o ID, visualización con indentación, y rutas jerárquicas.
- **Grafos:** modelado de rutas complejas, optimización de caminos y cálculo de distancias posibles.

Con esta implementación, buscamos no solo resolver un problema práctico de organización y navegación, sino también desarrollar habilidades en estructuras de datos, algoritmos y representación visual de información compleja.
