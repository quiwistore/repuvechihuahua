#!/usr/bin/env python3
"""
Genera las variantes de paginas por intencion de busqueda para cada estudio.
Cada variante responde una intencion DISTINTA (no es la misma pagina con KW cambiada).
Salida: data/paginas.json con todas las paginas a generar.
"""
import json, os, re, unicodedata

def slugify(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')
    s = re.sub(r'[^\w\s-]', '', s.lower()).strip()
    return re.sub(r'[\s_]+', '-', s)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(ROOT, 'data', 'estudios.json'), encoding='utf-8') as f:
    DATA = json.load(f)

CIUDAD = DATA['ciudad']
estudios = DATA['estudios']

def fmt_precio(e):
    return f"${e['precioMin']} a ${e['precioMax']} MXN"

def variantes_de_estudio(e):
    nombre = e['nombre']
    nombreL = nombre.lower()
    precio = fmt_precio(e)
    paginas = []

    paginas.append({
        "slug": f"precios/{e['slug']}/precio-{e['slug']}",
        "intent": "precio_directo", "estudio": e['slug'],
        "title": f"Precio de {nombre} en Salud Digna Culiacan 2026",
        "h1": f"Precio de {nombre} en Salud Digna Culiacan",
        "meta": f"Cual es el precio de {nombreL} en Salud Digna Culiacan? Costo {precio}, con 10% de descuento pagando en linea. Sucursales, horarios y como agendar.",
        "lead": f"El precio de {nombreL} en Salud Digna Culiacan es de aproximadamente <strong>{precio}</strong>. Pagando en linea puedes obtener hasta un 10% de descuento en estudios seleccionados."
    })
    paginas.append({
        "slug": f"precios/{e['slug']}/cuanto-cuesta-{e['slug']}",
        "intent": "cuanto_cuesta", "estudio": e['slug'],
        "title": f"Cuanto cuesta una {nombre} en Salud Digna Culiacan?",
        "h1": f"Cuanto cuesta una {nombre} en Salud Digna Culiacan?",
        "meta": f"Cuanto cuesta una {nombreL} en Salud Digna Culiacan? Te explicamos el costo ({precio}), que incluye, descuentos y como agendar tu cita.",
        "lead": f"Una {nombreL} en Salud Digna Culiacan cuesta entre <strong>{precio}</strong>. A continuacion te explicamos que incluye ese precio, como ahorrar con el descuento en linea y donde realizarte el estudio en la ciudad."
    })
    paginas.append({
        "slug": f"precios/{e['slug']}/costo-{e['slug']}",
        "intent": "costo", "estudio": e['slug'],
        "title": f"Costo de {nombre} en Salud Digna Culiacan",
        "h1": f"Costo de {nombre} en Salud Digna Culiacan",
        "meta": f"Costo de {nombreL} en Salud Digna Culiacan: {precio}. Conoce que incluye, preparacion necesaria y las sucursales donde puedes realizarte el estudio.",
        "lead": f"El costo de {nombreL} en Salud Digna Culiacan ronda los <strong>{precio}</strong>, uno de los mas accesibles de la ciudad."
    })
    paginas.append({
        "slug": f"precios/{e['slug']}/que-es-{e['slug']}",
        "intent": "que_es", "estudio": e['slug'],
        "title": f"Que es la {nombre} y para que sirve? - Salud Digna Culiacan",
        "h1": f"Que es la {nombre} y para que sirve?",
        "meta": f"Que es la {nombreL}, para que sirve y cuanto cuesta en Salud Digna Culiacan ({precio}). Guia completa del estudio.",
        "lead": e['queEs']
    })
    paginas.append({
        "slug": f"precios/{e['slug']}/preparacion-{e['slug']}",
        "intent": "preparacion", "estudio": e['slug'],
        "title": f"Preparacion para {nombre} en Salud Digna Culiacan",
        "h1": f"Como prepararse para una {nombre}?",
        "meta": f"Requisitos y preparacion para tu {nombreL} en Salud Digna Culiacan. {'Requiere ayuno' if e['ayuno'] else 'No requiere ayuno'}. Precio {precio} y como agendar.",
        "lead": e['preparacion']
    })
    for sin in e.get('sinonimos', []):
        sin_slug = slugify(sin)
        if len(sin_slug) < 3 or sin_slug == e['slug']:
            continue
        paginas.append({
            "slug": f"precios/{e['slug']}/{sin_slug}",
            "intent": "sinonimo", "estudio": e['slug'],
            "title": f"{sin.capitalize()} en Salud Digna Culiacan - Precio y Citas",
            "h1": f"{sin.capitalize()} en Salud Digna Culiacan",
            "meta": f"{sin.capitalize()} (tambien conocida como {nombreL}) en Salud Digna Culiacan. Precio {precio}, sucursales y como agendar tu cita.",
            "lead": f"<strong>{sin.capitalize()}</strong> es otra forma de referirse a la {nombreL}. En Salud Digna Culiacan este estudio cuesta {precio}.",
            "sinonimo": sin
        })
    paginas.append({
        "slug": f"precios/{e['slug']}",
        "intent": "hub_estudio", "estudio": e['slug'],
        "title": f"{nombre} en Salud Digna Culiacan: Precio, Citas y Sucursales 2026",
        "h1": f"{nombre} en Salud Digna Culiacan",
        "meta": f"Todo sobre la {nombreL} en Salud Digna Culiacan: precio ({precio}), que es, preparacion, sucursales y como agendar tu cita en linea.",
        "lead": f"Aqui encuentras todo lo que necesitas saber sobre la {nombreL} en Salud Digna Culiacan: precio actualizado, que incluye, como prepararte y en que sucursales realizarte el estudio.",
        "es_hub": True
    })
    return paginas

todas = []
for e in estudios:
    todas.extend(variantes_de_estudio(e))

from collections import Counter
intents = Counter(p['intent'] for p in todas)
print(f"=== Generadas {len(todas)} paginas para {len(estudios)} estudios ===\n")
print("Por tipo de intencion:")
for intent, n in intents.most_common():
    print(f"  {intent}: {n}")
print(f"\nPromedio de variantes por estudio: {len(todas)/len(estudios):.1f}")

out = {"meta": dict(estudios=len(estudios), paginas=len(todas)), "paginas": todas}
with open(os.path.join(ROOT, 'data', 'paginas.json'), 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(f"\nGuardado en data/paginas.json")

print("\n=== Ejemplo: variantes de 'biometria-hematica' ===")
for p in todas:
    if p['estudio'] == 'biometria-hematica':
        print(f"  [{p['intent']}] /{p['slug']}/")
