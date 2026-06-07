#!/usr/bin/env python3
"""Genera sitemap.xml, sitemap-0.xml, sitemap-index.xml y robots.txt para repuve-chihuahua."""
import json
from datetime import date
from pathlib import Path

ROOT = Path('/Users/quiwistore/Downloads/repuve-chihuahua')
DATA = ROOT / 'data' / 'repuve.json'
DIST = ROOT / 'dist'
PUBLIC = ROOT / 'public'

data = json.loads(DATA.read_text())
domain = f"https://{data['site']['domain']}"
today = date.today().isoformat()

# Build URL list
urls = []

# Home
urls.append({'loc': f'{domain}/', 'priority': '1.0', 'changefreq': 'weekly'})

# Pages centrales (32)
priority_categories = {'Consulta': '0.9', 'Tramite': '0.8', 'Informacion': '0.7'}
for p in data['pages_centrales']:
    prio = priority_categories.get(p.get('category', ''), '0.7')
    urls.append({
        'loc': f"{domain}/{p['slug']}/",
        'priority': prio,
        'changefreq': 'monthly'
    })

# Oficinas (7) + índice /oficinas/
urls.append({
    'loc': f'{domain}/oficinas/',
    'priority': '0.9',
    'changefreq': 'monthly'
})
for o in data['oficinas']:
    urls.append({
        'loc': f"{domain}/oficinas/{o['slug']}/",
        'priority': '0.8',
        'changefreq': 'monthly'
    })

# Static pages (3)
for slug in ['aviso-de-privacidad', 'contacto', 'sobre-nosotros']:
    urls.append({
        'loc': f"{domain}/{slug}/",
        'priority': '0.3',
        'changefreq': 'yearly'
    })

print(f"Total URLs: {len(urls)}")

# Build sitemap-0.xml
sitemap_0 = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_0 += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in urls:
    sitemap_0 += f'  <url>\n'
    sitemap_0 += f'    <loc>{u["loc"]}</loc>\n'
    sitemap_0 += f'    <lastmod>{today}</lastmod>\n'
    sitemap_0 += f'    <changefreq>{u["changefreq"]}</changefreq>\n'
    sitemap_0 += f'    <priority>{u["priority"]}</priority>\n'
    sitemap_0 += f'  </url>\n'
sitemap_0 += '</urlset>\n'

# Build sitemap-index.xml
sitemap_index = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_index += '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sitemap_index += f'  <sitemap>\n'
sitemap_index += f'    <loc>{domain}/sitemap-0.xml</loc>\n'
sitemap_index += f'    <lastmod>{today}</lastmod>\n'
sitemap_index += f'  </sitemap>\n'
sitemap_index += '</sitemapindex>\n'

# Also write a regular sitemap.xml as alias
sitemap = sitemap_0

# robots.txt
robots = f"""User-agent: *
Allow: /

Sitemap: {domain}/sitemap-index.xml
Sitemap: {domain}/sitemap.xml
"""

# Write to public/ (for next dev) AND dist/ (for current build)
for target_dir in [PUBLIC, DIST]:
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / 'sitemap.xml').write_text(sitemap, encoding='utf-8')
    (target_dir / 'sitemap-0.xml').write_text(sitemap_0, encoding='utf-8')
    (target_dir / 'sitemap-index.xml').write_text(sitemap_index, encoding='utf-8')
    (target_dir / 'robots.txt').write_text(robots, encoding='utf-8')
    print(f"Wrote to {target_dir.name}/: sitemap.xml, sitemap-0.xml, sitemap-index.xml, robots.txt")

print(f"\nDone. URLs in sitemap: {len(urls)}")
print(f"Robots.txt:\n{robots}")
