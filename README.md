# Taller 2 - Solución de Algoritmos Bioinspirados

## Descripción del Proyecto

Este proyecto contiene la implementación de tres algoritmos bioinspirados solicitados en el Taller 2, cada uno resolviendo un problema específico mediante técnicas inspiradas en la naturaleza.

---

## Punto 1: Evolución de Pokémon con Algoritmo Genético

### Problema
Diseñar un sistema que evolucione Pokémon hacia criaturas con mejores estadísticas mediante selección natural artificial.

### Solución Implementada

#### Estructura del Cromosoma (Pokémon)
```python
pokemon = {
    'ataque': 0.7,      # gen 1 (valor 0-1)
    'defensa': 0.3,     # gen 2
    'velocidad': 0.8,   # gen 3
    'vida': 0.5,        # gen 4
    'tipo': 'fuego'     # gen 5
}
```

#### Función de Fitness
```python
def evaluar_pokemon(pokemon):
    poder = (pokemon['ataque'] * 0.3 +
            pokemon['defensa'] * 0.2 +
            pokemon['velocidad'] * 0.25 +
            pokemon['vida'] * 0.25)
    
    # Bonus por tipo (fuego: +10%, agua: +5%)
    if pokemon['tipo'] == 'fuego': poder *= 1.1
    elif pokemon['tipo'] == 'agua': poder *= 1.05
    
    return poder
```

#### Operadores Genéticos Implementados

1. **Población Inicial**
   - 20 Pokémon generados aleatoriamente
   - Tipos: fuego, agua, planta, eléctrico

2. **Selección por Torneo**
   - Mantiene el 50% mejor de cada generación

3. **Cruzamiento (Crossover)**
   - Combinación aleatoria de genes parentales

4. **Mutación**
   - Tasa de mutación: 10%
   - Alteración de ±0.2 en características
   - Posible cambio de tipo

#### Resultados Obtenidos
- Evolución a través de 10 generaciones
- Mejora progresiva del poder de combate
- Pokémon final con estadísticas optimizadas
- Adaptación automática de tipos beneficiosos

---

## Punto 2: Algoritmo de Recomendación Musical con Colonias de Hormigas

### Problema
Crear un sistema de recomendación que genere playlists personalizadas basadas en preferencias del usuario.

### Solución Implementada

#### Estructura del Grafo Musical
```python
canciones = {
    'song1': {'rock': 0.8, 'energia': 0.9},
    'song2': {'pop': 0.9, 'energia': 0.6},
    'song3': {'jazz': 0.7, 'energia': 0.4}
}

feromonas = {
    'song1': {'song2': 1.0, 'song3': 1.0},
    'song2': {'song1': 1.0, 'song3': 1.0},
    'song3': {'song1': 1.0, 'song2': 1.0}
}
```

#### Clase UsuarioHormiga
```python
class UsuarioHormiga:
    def __init__(self, preferencias):
        self.playlist = []
        self.preferencias = preferencias

    def evaluar_transicion(self, cancion_actual, siguiente_cancion):
        similitud = calcular_similitud(cancion_actual, siguiente_cancion)
        afinidad_usuario = calcular_afinidad(siguiente_cancion, self.preferencias)
        
        return feromonas[cancion_actual][siguiente_cancion] * similitud * afinidad_usuario
```

#### Métricas de Evaluación

1. **Similitud Musical**
   - Compara características entre canciones
   - Calcula compatibilidad estilística

2. **Afinidad del Usuario**
   - Evalúa preferencias personales
   - Match entre características de canción y usuario

3. **Sistema de Feromonas**
   - Refuerza transiciones exitosas
   - Permite aprendizaje colectivo

#### Características del Sistema
- Recomendaciones personalizadas
- Transiciones suaves entre canciones
- Adaptación a preferencias del usuario
- Playlist dinámica y evolutiva

---

## Punto 3: Controlador de Robot de Carreras con Múltiples Algoritmos

### Problema
Desarrollar un controlador inteligente para un robot de carreras que combine tres enfoques bioinspirados.

### Solución Integrada

#### 3.1 Algoritmo Genético - Evolución de Parámetros
```python
controlador = {
    'agresividad': 0.7,
    'conservador': 0.3, 
    'adelantamiento': 0.8
}
```
- **Función**: Evoluciona el estilo de conducción
- **Mecanismo**: Mutación y selección basada en performance
- **Resultado**: Controlador adaptado al circuito

#### 3.2 Algoritmo de Partículas (PSO) - Optimización de Trayectoria
```python
class ControladorPSO:
    def decidir_adelantamiento(self, oponentes, pista):
        # Usa enjambre para encontrar mejor momento
```
- **Función**: Decide estrategias de adelantamiento
- **Mecanismo**: Enjambre de partículas optimiza timing
- **Variables**: Riesgo, oportunidad, posición de oponentes

#### 3.3 Algoritmo de Hormigas - Aprendizaje de Línea Óptima
```python
class HormigaRacing:
    def reforzar_trayectoria(self, tramo, tiempo):
        feromonas[tramo] += 1.0 / tiempo
```
- **Función**: Aprende la mejor línea de carrera
- **Mecanismo**: Feromonas en puntos de la pista
- **Resultado**: Trayectoria optimizada por tramos

#### Controlador Principal
```python
class ControladorRobotCarreras:
    def tomar_decision(self, estado_pista, oponentes):
        # Integra los tres algoritmos para decisión final
```

#### Módulos de Integración

1. **Toma de Decisiones**
   - Hormigas sugiere mejor línea
   - PSO optimiza adelantamientos
   - Genético define estilo de conducción

2. **Aprendizaje Continuo**
   - Actualización de feromonas por tramo
   - Evolución de parámetros basada en resultados
   - Optimización en tiempo real

3. **Métricas de Performance**
   - Adelantamientos exitosos/fallidos
   - Tiempos por tramo
   - Evolución de parámetros

