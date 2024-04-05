# Sokoban-by-Guillermo 🎮

[Sokoban](https://en.wikipedia.org/wiki/Sokoban) es una palabra japonesa que significa "guardián de almacén" y es un juego de video tradicional. El juego es un rompecabezas de transporte, donde el jugador debe empujar todas las cajas en la habitación hacia las ubicaciones de almacenamiento / objetivos. La posibilidad de cometer errores irreversibles hace que estos rompecabezas sean tan desafiantes, especialmente para los algoritmos de [aprendizaje por refuerzo](https://es.wikipedia.org/wiki/Aprendizaje_por_refuerzo), que en su mayoría carecen de la capacidad de pensar con anticipación. 🧩

El repositorio implementa el juego Sokoban basado en las reglas presentadas en el artículo de [DeepMind](https://deepmind.com/)'s "Imagination Augmented Agents for Deep Reinforcement Learning" (Agentes Aumentados de Imaginación para el Aprendizaje Profundo por Refuerzo). La generación de habitaciones es aleatoria y, por lo tanto, permitirá entrenar redes neuronales profundas sin sobreajuste en un conjunto de habitaciones predefinidas. 🤖

## Ejemplo de Juegos

| Juego de Ejemplo 1 | Juego de Ejemplo 2 | Juego de Ejemplo 3 |
| :---: | :---: | :---: |
| ![Juego 1](/img/img1.png) | ![Juego 2](/img/img2.png) | ![Juego 3](/img/img3.png) |

## 1 Instalación

### Desde el Repositorio
```bash
git https://github.com/guillsil/Sokoban-by-Guillermo.git
cd Sokoban-by-Guillermo
pip install -e .
```

## 2 Entorno de Juego

### 2.1 Elementos de la Habitación
Cada habitación consta de cinco elementos principales: paredes, suelo, cajas, objetivos de cajas y un jugador. Pueden tener estados diferentes si se superponen con un objetivo de caja o no. 🏠

| Tipo       | Estado      | Gráfico |
| ---        | -----      | :---: | 
| Pared      | Estático     | ![Pared](/img/wall.gif "Pared") |
| Suelo      | Vacío      | ![Suelo](/img/ground.gif "Suelo") | 
| Suelo con objetivo | Vacío      | ![ObjetivoCaja](/img/goal.gif "Objetivo de Caja") |
| Caja        | Fuera de objetivo | ![CajaFueraObjetivo](/img/box.gif "Caja") |
| Objetivo de caja     | En objetivo  | ![CajaEnObjetivo](/img/box.gif "Caja") |
| Jugador     | Fuera de objetivo | ![JugadorFueraObjetivo](/img/player.gif "Jugador") |
| Jugador con objetivo    | En objetivo  | ![JugadorEnObjetivo](/img/player.gif  "Jugador") |

### 2.2 Acciones
El juego proporciona 10 acciones para interactuar con el entorno. Acciones de Empujar y Mover en las direcciones Arriba, Abajo, Izquierda y Derecha. La acción de Pista que te muestra un movimiento. La acción de deshacer y rehacer que modifica los movimientos realizados. Y la acción de reinicio que devuelve el juego a su estado inicial. 🎮

| Acción       | ID    | 
| --------     | :---: |    
| Mover Arriba      |   w   |
| Mover Abajo    |   s   |
| Mover Izquierda    |   a   |
| Mover Derecha   |   d   |
| Reiniciar        |   f   |
| Deshacer         |   z   |
| Rehacer         |   y   |
| Pista         |   r   |
| Siguiente nivel   |   e   |
| Nivel anterior |  q   |
