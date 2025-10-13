pokemon = {
    'ataque': 0.7,
    'defensa': 0.3,
    'velocidad': 0.8,
    'vida': 0.5,
    'tipo': 'fuego'
}

def evaluar_pokemon(pokemon):
    poder = (pokemon['ataque'] * 0.3 +
    pokemon['defensa'] * 0.2 +
    pokemon['velocidad'] * 0.25 +
    pokemon['vida'] * 0.25)
    
    if pokemon['tipo'] == 'fuego': poder *= 1.1
    elif pokemon['tipo'] == 'agua': poder *= 1.05
    
    return poder

import random

tipos = ['fuego', 'agua', 'planta', 'electrico']

def crear_pokemon_aleatorio():
    return {
        'ataque': random.random(),
        'defensa': random.random(),
        'velocidad': random.random(),
        'vida': random.random(),
        'tipo': random.choice(tipos)
    }

def mutar_pokemon(pokemon, tasa_mutacion=0.1):
    nuevo_pokemon = pokemon.copy()
    
    if random.random() < tasa_mutacion:
        nuevo_pokemon['ataque'] = max(0, min(1, nuevo_pokemon['ataque'] + random.uniform(-0.2, 0.2)))
    
    if random.random() < tasa_mutacion:
        nuevo_pokemon['defensa'] = max(0, min(1, nuevo_pokemon['defensa'] + random.uniform(-0.2, 0.2)))
    
    if random.random() < tasa_mutacion:
        nuevo_pokemon['velocidad'] = max(0, min(1, nuevo_pokemon['velocidad'] + random.uniform(-0.2, 0.2)))
    
    if random.random() < tasa_mutacion:
        nuevo_pokemon['vida'] = max(0, min(1, nuevo_pokemon['vida'] + random.uniform(-0.2, 0.2)))
    
    if random.random() < tasa_mutacion:
        nuevo_pokemon['tipo'] = random.choice(tipos)
    
    return nuevo_pokemon

def cruzar_pokemon(padre, madre):
    hijo = {}
    
    hijo['ataque'] = random.choice([padre['ataque'], madre['ataque']])
    hijo['defensa'] = random.choice([padre['defensa'], madre['defensa']])
    hijo['velocidad'] = random.choice([padre['velocidad'], madre['velocidad']])
    hijo['vida'] = random.choice([padre['vida'], madre['vida']])
    hijo['tipo'] = random.choice([padre['tipo'], madre['tipo']])
    
    return hijo

def evolucionar_poblacion(poblacion, num_generaciones=10):
    for generacion in range(num_generaciones):
        evaluaciones = [(p, evaluar_pokemon(p)) for p in poblacion]
        evaluaciones.sort(key=lambda x: x[1], reverse=True)
        
        mejores = evaluaciones[:len(poblacion)//2]
        
        nueva_poblacion = [p[0] for p in mejores]
        
        while len(nueva_poblacion) < len(poblacion):
            padre = random.choice(mejores)[0]
            madre = random.choice(mejores)[0]
            hijo = cruzar_pokemon(padre, madre)
            hijo = mutar_pokemon(hijo)
            nueva_poblacion.append(hijo)
        
        poblacion = nueva_poblacion
        
        mejor_actual = evaluaciones[0]
        print(f"Generación {generacion + 1}:")
        print(f"  Poder = {mejor_actual[1]:.3f}")
        print(f"  Ataque = {mejor_actual[0]['ataque']:.3f}")
        print(f"  Defensa = {mejor_actual[0]['defensa']:.3f}")
        print(f"  Velocidad = {mejor_actual[0]['velocidad']:.3f}")
        print(f"  Vida = {mejor_actual[0]['vida']:.3f}")
        print(f"  Tipo = {mejor_actual[0]['tipo']}")
        print()
    
    return poblacion

poblacion_inicial = [crear_pokemon_aleatorio() for _ in range(20)]

poblacion_final = evolucionar_poblacion(poblacion_inicial)

mejor_pokemon = max(poblacion_final, key=evaluar_pokemon)
print(f"Mejor Pokémon evolucionado:")
print(f"Ataque: {mejor_pokemon['ataque']:.3f}")
print(f"Defensa: {mejor_pokemon['defensa']:.3f}")
print(f"Velocidad: {mejor_pokemon['velocidad']:.3f}")
print(f"Vida: {mejor_pokemon['vida']:.3f}")
print(f"Tipo: {mejor_pokemon['tipo']}")
print(f"Poder total: {evaluar_pokemon(mejor_pokemon):.3f}")
