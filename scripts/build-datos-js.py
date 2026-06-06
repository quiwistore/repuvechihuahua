#!/usr/bin/env python3
"""
Convierte data/repuve.json en src/data/datos.js que Astro importa
para generar las paginas estaticas del sitio REPUVE Chihuahua.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(ROOT, 'data', 'repuve.json'), encoding='utf-8') as f:
    data = json.load(f)

OUT = os.path.join(ROOT, 'src', 'data', 'datos.js')

js = "// Generado automaticamente. No editar a mano.\n"
js += "// Fuente: data/repuve.json\n\n"
js += "export const site = " + json.dumps(data['site'], ensure_ascii=False, indent=2) + ";\n\n"
js += "export const oficinas = " + json.dumps(data['oficinas'], ensure_ascii=False, indent=2) + ";\n\n"
js += "export const pagesCentrales = " + json.dumps(data['pages_centrales'], ensure_ascii=False, indent=2) + ";\n\n"
js += "export const meta = " + json.dumps(data.get('meta', {}), ensure_ascii=False, indent=2) + ";\n\n"

js += """// =====================================
// Helpers para los templates Astro
// =====================================

export function getOficinaBySlug(slug) {
  return oficinas.find(o => o.slug === slug);
}

export function getPageBySlug(slug) {
  return pagesCentrales.find(p => p.slug === slug);
}

export function getPagesByCategory(category) {
  return pagesCentrales.filter(p => p.category === category);
}

export function getCategories() {
  const cats = new Set();
  for (const p of pagesCentrales) {
    if (p.category) cats.add(p.category);
  }
  return Array.from(cats);
}

export function getOficinaCapital() {
  return oficinas.find(o => o.es_capital === true);
}

export function getOficinasFrontera() {
  return oficinas.filter(o => o.es_frontera === true);
}

// Para sidebar: 5-6 paginas relacionadas excluyendo la actual
export function getRelatedPages(currentSlug, n = 6) {
  return pagesCentrales
    .filter(p => p.slug !== currentSlug)
    .slice(0, n);
}

// Para sidebar de oficinas: otras oficinas
export function getOtrasOficinas(currentSlug, n = 6) {
  return oficinas.filter(o => o.slug !== currentSlug).slice(0, n);
}

// Para iconos por categoria (Font Awesome)
export function iconForCategory(category) {
  const map = {
    'Consulta': 'fa-magnifying-glass',
    'Tramite': 'fa-file-pen',
    'Informacion': 'fa-circle-info',
    'Contacto': 'fa-phone',
    'Cita': 'fa-calendar-check',
    'Ubicacion': 'fa-location-dot',
  };
  return map[category] || 'fa-file-lines';
}

// Format horario (lunes-domingo) para tabla
export function getDayKeys() {
  return ['lunes','martes','miercoles','jueves','viernes','sabado','domingo'];
}

export function getDayNames() {
  return {
    lunes: 'Lunes',
    martes: 'Martes',
    miercoles: 'Miercoles',
    jueves: 'Jueves',
    viernes: 'Viernes',
    sabado: 'Sabado',
    domingo: 'Domingo',
  };
}

// Today in TZ Mexico (used for highlighting current day in hours table)
export function todayKey() {
  // En SSR estatico, no hay "today" real — devolver vacio para no resaltar nada
  // El highlighting de "hoy" lo hacemos via JS en cliente si quisieramos
  return null;
}
"""

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    f.write(js)

print(f"Generado src/data/datos.js ({len(js):,} bytes)")
print(f"  site.domain: {data['site']['domain']}")
print(f"  oficinas: {len(data['oficinas'])}")
print(f"  pages_centrales: {len(data['pages_centrales'])}")
