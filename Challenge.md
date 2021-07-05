# Definición del problema
Para focalizar mejor los esfuerzos de testeo, las autoridades sanitarias buscan localizar las zonas del país con mayor concentración de casos de COVID. 

Se cuenta con un set de datos de geolocalización tomado de eventos de GPS registrados por aplicaciones de celular durante un periodo de tiempo. 

El objetivo es desarrollar un proceso de simulación que, dado un conjunto de usuarios que se conoce que ya están infectado, pueda mostrar en qué regiones hay más concentración de contagiados, luego de 15 días.

El equipo de investigación definió los siguientes parámetros para la simulación.
## Definiciones
Se considera que dos personas estuvieron en contacto si pasaron al menos 30 minutos a una distancia menor de 10 metros.
Una persona contagiada tiene una probabilidad de morir de 0.05. En caso de que esto ocurra, la muerte ocurre entre los 7 y los 25 días del contagio (con una confianza del 95%).
En caso de que no muera, se recupera entre los 10 y 35 días de ser contagiada (con una confianza del 95%).
Los individuos que mueren o se curan dejan de contagiar. 
## Simulación
Se comienza la simulación con 100 individuos contagiados distribuidos uniformemente entre la población (que se observa en los eventos disponibles).
Cada día, en cada cada contacto de una persona sana con una contagiada, hay una probabilidad de 0.00005 de que la sana sea contagiada.
Se calculan los nuevos contagiados de forma diaria.
El ciclo se repite 15 veces (para poder predecir los contagios en un mes).

## Resultado
Un histograma en dos dimensiones (latitud y longitud), donde cada rectángulo tiene la cantidad de eventos de geolocalización emitidos por personas contagiadas.
Una línea de tiempo donde en cada día pueda leerse la cantidad de individuos contagiados.

## Consiga
Desarrollar un proceso -preferentemente usando Apache Spark- que, dada una tabla de eventos de localización, y una lista inicial de contagiados, corra la simulación para un día.

Definir casos de prueba.

La tabla de entrada tiene las siguientes columnas
id
latitude
longitude
Timestamp

Hacer una presentación de 20 minutos para mostrar:
Resultados
Diseño del proceso
Decisiones tomadas
Futuras mejoras
Productivización futura (infraestructura, sizing, costos, etc).
A tener en cuenta
¿Qué estructura de datos es la más adecuada para representar el problema?
¿Cómo sería la forma más conveniente de dividir el proceso en partes más chicas? ¿Qué parte es más pesada en términos de procesamiento?
Haciendo algunos cambios en el algoritmo, y evaluando su impacto, ¿se puede simplificar el proceso -tal vez para hacerlo más rápido o más simple de desarrollar? ¿Cuáles serían las concesiones razonables?
¿Cuáles son los casos bordes?
¿Qué posibles problemas de perfomance podría haber? 
