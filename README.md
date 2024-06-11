# Arbol-Animales

  Programa básico que muestra un ciclo que simula el aprendizaje máquina por consola.   
  (Enfoque en Matemáticas Discretas)

El árbol de animales:
    El programa interactúa con el usuario para crear un árbol de preguntas y nombres de animales. Aquí
    tenemos un ejemplo de ejecución:
    
    Estás pensando en un animal? si
    Es un pájaro? no
    Qué tipo de animal es? perro
    Qué pregunta distinguiría a un perro de un pájaro? Puede volar?
    Si el animal fuera un perro, cuál sería la respuesta? no
    Estás pensando en un animal? si
    Puede volar? no
    Es un perro? no
    Cómo se llama el animal? gato
    Qué pregunta distinguiría a un gato de un perro? Ladra?
    Si el animal fuera un gato, cuál sería la respuesta? no
    Estás pensando en un animal? si
    Puede volar? no
    Ladra? si
    Es un perro? si
    Soy el más grande?
    Estás pensando en un animal? no
    
Al principio de cada ronda, el programa empieza en lo alto del árbol y hace la primera pregunta.
Dependiendo de la respuesta, se mueve al hijo de la izquierda o de la derecha y sigue hasta que llega a
un nodo hoja. En ese momento, intenta adivinar. Si falla, pide al usuario el nombre del nuevo animal
y una pregunta que distinga al intento fallido del nuevo animal. Entonces añade un nodo al árbol con
la nueva pregunta y el nuevo animal.
