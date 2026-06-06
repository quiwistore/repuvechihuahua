#!/usr/bin/env python3
"""
Procesa el GeoJSON oficial del DMV de California y genera src/data/offices.js
Fuente: https://gis.data.ca.gov/datasets/DMVfac::department-of-motor-vehicles-office-locations.geojson
Uso: python3 scripts/build-data.py
"""
import json, re, os, sys
from collections import defaultdict, Counter

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
GEOJSON_PATH = os.path.join(PROJECT_ROOT, 'data', 'dmv-ca-raw.geojson')
OUT_PATH = os.path.join(PROJECT_ROOT, 'src', 'data', 'offices.js')

if not os.path.exists(GEOJSON_PATH):
    print(f"ERROR: no encuentro {GEOJSON_PATH}", file=sys.stderr)
    sys.exit(1)

def slugify(s):
    s = s.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s)
    return re.sub(r'-+', '-', s).strip('-')

# Horarios estándar DMV California (todas las oficinas comparten este patrón base)
# Lun: 8-5, Mar: 9-5, Mie: 8-5, Jue: 8-5, Vie: 8-5. Algunas abren distinto pero esto es el estándar oficial.
def standard_hours():
    h = {}
    schedule = {'mon':('08:00','17:00'),'tue':('09:00','17:00'),'wed':('08:00','17:00'),
                'thu':('08:00','17:00'),'fri':('08:00','17:00')}
    def fmt(t):
        hh, mm = t.split(':'); hh = int(hh)
        ap = 'AM' if hh < 12 else 'PM'; h12 = hh if 1<=hh<=12 else (hh-12 if hh>12 else 12)
        return f"{h12}:{mm} {ap}"
    for k,(o,c) in schedule.items():
        h[k] = f"{fmt(o)} - {fmt(c)}"
        h[f"{k}_iso"] = {"opens": o, "closes": c}
    h['sat']="Closed"; h['sun']="Closed"; h['sat_iso']=None; h['sun_iso']=None
    return h

with open(GEOJSON_PATH) as f:
    data = json.load(f)

offices = []
slug_counter = Counter()
DMV_PHONE = "1-800-777-0133"
SERVICES = ["Driver's License & ID","Vehicle Registration","REAL ID","Driving Test (Behind-the-Wheel)","Written Knowledge Test","Title Transfer"]

for ft in data['features']:
    props = ft['properties']
    geom = ft.get('geometry', {})
    coords = geom.get('coordinates', [None, None])
    lng, lat = (coords[0], coords[1]) if len(coords) >= 2 else (None, None)

    name = props.get('Name', '').strip()
    zip_code = str(props.get('ZIP', '')).strip().zfill(5)
    addr_raw = props.get('Address', '').strip()

    # Address viene como "903 West C Street\nAlturas, CA 96101"
    parts = addr_raw.split('\n')
    street = parts[0].strip() if parts else ''
    city = name  # el Name del DMV es la ciudad/oficina
    # extraer ciudad real de la segunda línea si existe
    if len(parts) > 1:
        m = re.match(r'([^,]+),', parts[1])
        if m: city = m.group(1).strip()

    if not street or not city:
        continue

    city_slug = slugify(city)
    base_id = city_slug
    slug_counter[base_id] += 1
    office_id = base_id if slug_counter[base_id] == 1 else f"{base_id}-{slug_counter[base_id]}"

    office_name = f"{name} DMV Office" if name else f"{city} DMV Office"
    full_address = f"{street}, {city}, CA {zip_code}"

    offices.append({
        "id": office_id,
        "facId": props.get('FAC_ID',''),
        "name": office_name,
        "officeLabel": name,
        "address": street,
        "fullAddress": full_address,
        "city": city,
        "citySlug": city_slug,
        "state": "CA",
        "zip": zip_code,
        "lat": lat,
        "lng": lng,
        "phone": DMV_PHONE,
        "hours": standard_hours(),
        "services": SERVICES,
    })

offices.sort(key=lambda x: (x['city'], x['address']))
print(f"Procesadas {len(offices)} oficinas DMV de California")
print(f"Ciudades únicas: {len(set(o['citySlug'] for o in offices))}")

js = '''// Generado automáticamente desde el GeoJSON oficial del DMV de California
// Fuente: https://gis.data.ca.gov/datasets/DMVfac::department-of-motor-vehicles-office-locations.geojson

export const offices = '''
js += json.dumps(offices, indent=2, ensure_ascii=False)
js += ';\n\n'
js += '''export function getOfficeById(id) {
  return offices.find(o => o.id === id);
}
export function getOfficesByCity(citySlug) {
  return offices.filter(o => o.citySlug === citySlug.toLowerCase());
}
export function getCities() {
  const cityMap = {};
  for (const office of offices) {
    if (!cityMap[office.citySlug]) {
      cityMap[office.citySlug] = { name: office.city, slug: office.citySlug, count: 0 };
    }
    cityMap[office.citySlug].count++;
  }
  return Object.values(cityMap).sort((a, b) => a.name.localeCompare(b.name));
}
export function getMapEmbedUrl(office) {
  return `https://www.google.com/maps?q=${encodeURIComponent(office.fullAddress)}&output=embed`;
}
export function getMapDirectionsUrl(office) {
  return `https://www.google.com/maps/dir/?api=1&destination=${encodeURIComponent(office.fullAddress)}`;
}
export function getNearbyOffices(office, limit = 6) {
  if (office.lat == null || office.lng == null) return [];
  const withDist = offices
    .filter(o => o.id !== office.id && o.lat != null && o.lng != null)
    .map(o => {
      const dLat = o.lat - office.lat, dLng = o.lng - office.lng;
      return { office: o, dist: Math.sqrt(dLat*dLat + dLng*dLng) };
    })
    .sort((a, b) => a.dist - b.dist)
    .slice(0, limit);
  return withDist.map(x => x.office);
}
'''

os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
with open(OUT_PATH, 'w', encoding='utf-8') as f:
    f.write(js)
print(f"Generado: {OUT_PATH} ({len(js):,} bytes)")

print("\nTop 10 ciudades:")
cc = Counter(o['city'] for o in offices)
for city, n in cc.most_common(10):
    print(f"  {city}: {n}")
