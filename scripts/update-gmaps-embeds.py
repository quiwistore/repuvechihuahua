#!/usr/bin/env python3
"""Actualiza data/repuve.json con los pb (Google Maps embed) reales para 5 oficinas."""
import json
from pathlib import Path

DATA = Path('/Users/quiwistore/Downloads/repuve-chihuahua/data/repuve.json')

# Mapping slug -> pb del iframe verificado del user
PB_EMBEDS = {
    'chihuahua-capital': '!1m18!1m12!1m3!1d3415.5806655545966!2d-106.02707132471815!3d28.62304088451202!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x86ea5b5674ad5563%3A0xbee22f19b394849d!2sRepuve%20Chihuahua!5e1!3m2!1ses-419!2sar!4v1780845042593!5m2!1ses-419!2sar',
    'ciudad-juarez': '!1m18!1m12!1m3!1d17898.8574928375!2d-106.45960588015951!3d31.75257423387174!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x86e7591d6d1ac2c1%3A0xb481342b2c9d5adc!2sRepuve%20CD%20Juarez!5e1!3m2!1ses-419!2sar!4v1780845167036!5m2!1ses-419!2sar',
    'cuauhtemoc': '!1m18!1m12!1m3!1d3509.18477925645!2d-106.86017142454419!3d28.413680793985336!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x86c1cbb10cd8d1b3%3A0xc8dcc881d038d2e2!2sRecaudacion%20De%20Rentas!5e0!3m2!1ses!2sar!4v1780846392543!5m2!1ses!2sar',
    'delicias': '!1m18!1m12!1m3!1d3513.981004822708!2d-105.4822994245488!3d28.26859280051458!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x86eb13ea741764b9%3A0x73fff0bea3f1193a!2sRecaudaci%C3%B3n%20de%20Rentas!5e0!3m2!1ses!2sar!4v1780846411163!5m2!1ses!2sar',
    'hidalgo-del-parral': '!1m18!1m12!1m3!1d3469.1041752300102!2d-105.6676324247737!3d26.931870259267363!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x86e9c4ce31f68ef1%3A0x10400f02d1421485!2sM%C3%B3dulo%20de%20Recaudaci%C3%B3n%20de%20Rentas!5e1!3m2!1ses-419!2sar!4v1780845334936!5m2!1ses-419!2sar',
    'nuevo-casas-grandes': '!1m18!1m12!1m3!1d6711.169402287284!2d-107.92012412465522!3d30.41607250086792!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x86dcad91e2e9a143%3A0xabe52121a87a6388!2sREPUVE%20Nuevo%20Casas%20Grandes!5e1!3m2!1ses-419!2sar!4v1780845008123!5m2!1ses-419!2sar',
    'camargo': '!1m18!1m12!1m3!1d3445.701925663314!2d-105.18079872474951!3d27.68300772656491!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8694aef899207b8f%3A0x39c8c8d20d11aa03!2sRegistro%20Civil%20de%20Ciudad%20Camargo!5e1!3m2!1ses-419!2sar!4v1780845381517!5m2!1ses-419!2sar',
}

# También actualizo coordenadas con las REALES verificadas
COORDS_REAL = {
    'chihuahua-capital': (28.62304088451202, -106.02707132471815),
    'ciudad-juarez': (31.75257423387174, -106.45960588015951),
    'cuauhtemoc': (28.413680793985336, -106.86017142454419),
    'delicias': (28.26859280051458, -105.4822994245488),
    'hidalgo-del-parral': (26.931870259267363, -105.6676324247737),
    'nuevo-casas-grandes': (30.41607250086792, -107.92012412465522),
    'camargo': (27.68300772656491, -105.18079872474951),
}

data = json.loads(DATA.read_text())
updated = 0

for o in data['oficinas']:
    slug = o['slug']
    if slug in PB_EMBEDS:
        o['gmaps_embed_pb'] = PB_EMBEDS[slug]
        if slug in COORDS_REAL:
            o['latitude'], o['longitude'] = COORDS_REAL[slug]
        updated += 1
        print(f"  ✓ {slug}: embed real agregado (coords {o['latitude']:.4f}, {o['longitude']:.4f})")
    else:
        # Cuauhtemoc y Delicias mantienen coords actuales + sin embed real
        print(f"  ⚠ {slug}: SIN embed verificado, queda con coords genéricas {o['latitude']:.4f}, {o['longitude']:.4f}")

DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2))
print(f"\n✓ {updated}/7 oficinas con embed real verificado.")
print(f"⚠ 2 oficinas pendientes: cuauhtemoc, delicias (esperar iframes correctos del user)")
