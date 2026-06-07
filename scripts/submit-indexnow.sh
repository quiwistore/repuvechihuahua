#!/bin/bash
# Submit all URLs to IndexNow (Bing + Yandex via Cloudflare)
# Uso: bash scripts/submit-indexnow.sh
# Pre-requisito: el sitio ya debe estar deployado en producción

DOMAIN="repuvechihuahua.com"
KEY="a4105c0fe2ec394582709e9c23c8a365"
KEY_LOCATION="https://${DOMAIN}/${KEY}.txt"

# Construir lista de URLs
URLS=$(python3 -c "
import json
with open('data/repuve.json') as f:
    d = json.load(f)
urls = [f'https://{DOMAIN}/']
for p in d['pages_centrales']:
    urls.append(f\"https://{DOMAIN}/{p['slug']}/\")
for o in d['oficinas']:
    urls.append(f\"https://{DOMAIN}/oficinas/{o['slug']}/\")
for s in ['aviso-de-privacidad','contacto','sobre-nosotros']:
    urls.append(f'https://{DOMAIN}/{s}/')
print(json.dumps(urls))
" DOMAIN=$DOMAIN)

# Submit a IndexNow vía API de Bing
echo "Submitting $(echo $URLS | python3 -c 'import json,sys; print(len(json.loads(sys.stdin.read())))') URLs a IndexNow..."

curl -X POST 'https://api.indexnow.org/IndexNow' \
  -H 'Content-Type: application/json; charset=utf-8' \
  -d "{
    \"host\": \"${DOMAIN}\",
    \"key\": \"${KEY}\",
    \"keyLocation\": \"${KEY_LOCATION}\",
    \"urlList\": ${URLS}
  }" \
  -w "\n\nHTTP Status: %{http_code}\n"

echo ""
echo "Esperado: 200 OK (aceptado) o 202 (en cola)"
echo "Si recibes 403 SiteVerificationNotCompleted, esperá 5-30 minutos y reintentá."
