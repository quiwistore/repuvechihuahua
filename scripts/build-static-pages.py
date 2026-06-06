#!/usr/bin/env python3
"""Genera las 3 paginas estaticas: aviso-de-privacidad, contacto, sobre-nosotros."""
from pathlib import Path

PAGES_DIR = Path('/Users/quiwistore/Downloads/repuve-chihuahua/src/pages')

aviso = '''---
import Base from '../layouts/Base.astro';
import Breadcrumbs from '../components/Breadcrumbs.astro';
import { site } from '../data/datos.js';

const breadcrumbs = [
  { label: 'Inicio', href: '/' },
  { label: 'Aviso de privacidad' }
];
---

<Base
  title="Aviso de Privacidad"
  description="Aviso de privacidad del sitio informativo REPUVE Chihuahua. Politica de tratamiento de datos personales y cookies."
>
  <div class="container container-narrow">
    <Breadcrumbs items={breadcrumbs} />

    <header class="page-header">
      <div class="eyebrow"><i class="fa-solid fa-shield-halved"></i> Legal</div>
      <h1>Aviso de Privacidad</h1>
      <p class="lede">Informacion sobre el tratamiento de datos personales en este sitio informativo.</p>
    </header>

    <article class="article-main">
      <h2>Responsable del sitio</h2>
      <p>
        Este sitio web (<strong>{site.domain}</strong>) es un proyecto informativo independiente,
        sin fines de lucro de informacion oficial, dedicado a recopilar y difundir informacion publica
        sobre el Registro Publico Vehicular (REPUVE) en el estado de Chihuahua, Mexico.
      </p>
      <p>
        <strong>No tenemos vinculo, afiliacion, asociacion, patrocinio ni representacion</strong> con el Gobierno de Mexico,
        la Secretaria Ejecutiva del Sistema Nacional de Seguridad Publica (SESNSP), el REPUVE oficial,
        el Gobierno del Estado de Chihuahua ni ningun organismo gubernamental.
      </p>

      <h2>Datos personales que recolectamos</h2>
      <p>
        Este sitio web es <strong>puramente informativo</strong> y no requiere registro ni recolecta datos personales
        de los visitantes en formularios propios. No procesamos consultas vehiculares: para eso debes acudir
        al portal oficial <a href={site.official_site} rel="noopener nofollow">repuve.gob.mx</a>.
      </p>
      <p>Los unicos datos que se generan automaticamente al visitar el sitio son los siguientes:</p>
      <ul>
        <li><strong>Logs de servidor:</strong> direccion IP, fecha y hora de visita, paginas visitadas, navegador y sistema operativo (datos tecnicos estandar de cualquier sitio web).</li>
        <li><strong>Cookies de analisis:</strong> usamos herramientas analiticas (como Cloudflare Analytics) que pueden almacenar cookies para medir trafico anonimo y mejorar el contenido.</li>
      </ul>

      <h2>Finalidad del tratamiento</h2>
      <p>Los datos tecnicos anteriores se utilizan exclusivamente para:</p>
      <ul>
        <li>Garantizar la seguridad y funcionamiento del sitio.</li>
        <li>Estadisticas anonimas de visitas para mejorar el contenido.</li>
        <li>Detectar y prevenir abusos o ataques al servidor.</li>
      </ul>

      <h2>Cookies</h2>
      <p>
        Este sitio puede usar cookies tecnicas y analiticas. Las cookies son archivos pequenos que tu navegador
        almacena para mejorar tu experiencia. Puedes desactivarlas en la configuracion de tu navegador.
        No utilizamos cookies de publicidad personalizada.
      </p>

      <h2>Comparticion de datos con terceros</h2>
      <p>
        <strong>No vendemos, compartimos ni transferimos datos personales a terceros</strong>. Los datos tecnicos
        de logs se mantienen privados y se utilizan solo para los fines descritos arriba.
      </p>

      <h2>Derechos ARCO</h2>
      <p>
        Aunque no recolectamos datos personales sensibles, si crees que alguno de tus datos aparece en este sitio
        y deseas ejercer derechos de Acceso, Rectificacion, Cancelacion u Oposicion (ARCO), puedes contactarnos
        a traves del formulario de <a href="/contacto/">contacto</a>.
      </p>

      <h2>Cambios al aviso de privacidad</h2>
      <p>
        Este aviso de privacidad puede actualizarse periodicamente. La fecha de ultima actualizacion aparece
        al final de este documento. Te recomendamos revisarlo periodicamente.
      </p>

      <h2>Tramites oficiales</h2>
      <p>
        Para realizar tramites oficiales del REPUVE (consultas, inscripciones, citas), siempre dirigete al
        sitio oficial: <a href={site.official_site} rel="noopener nofollow">{site.official_site}</a> o llama al
        <a href={`tel:${site.phone_repuve.replace(/\\s/g,'')}`}>{site.phone_repuve}</a>.
      </p>

      <div class="tip-box">
        <p>
          <i class="fa-solid fa-circle-info"></i>
          <span><strong>Ultima actualizacion:</strong> Junio de 2026.</span>
        </p>
      </div>
    </article>
  </div>
</Base>
'''

contacto = '''---
import Base from '../layouts/Base.astro';
import Breadcrumbs from '../components/Breadcrumbs.astro';
import { site } from '../data/datos.js';

const breadcrumbs = [
  { label: 'Inicio', href: '/' },
  { label: 'Contacto' }
];
---

<Base
  title="Contacto"
  description="Informacion de contacto para REPUVE Chihuahua. Telefonos oficiales, correos y portales gubernamentales para tramites vehiculares en Chihuahua."
>
  <div class="container container-narrow">
    <Breadcrumbs items={breadcrumbs} />

    <header class="page-header">
      <div class="eyebrow"><i class="fa-solid fa-phone"></i> Contacto</div>
      <h1>Contacto REPUVE Chihuahua</h1>
      <p class="lede">Telefonos y portales oficiales para tus tramites del Registro Publico Vehicular en Chihuahua.</p>
    </header>

    <article class="article-main">
      <div class="warning-box">
        <p>
          <i class="fa-solid fa-triangle-exclamation"></i>
          <span>
            <strong>Este sitio es informativo y no procesa tramites.</strong> Si necesitas atencion oficial,
            usa los canales gubernamentales listados a continuacion. No respondemos consultas individuales
            sobre vehiculos especificos.
          </span>
        </p>
      </div>

      <h2>Canales oficiales REPUVE</h2>

      <div class="info-cards-grid" style="margin-top:1.5rem">
        <div class="info-card">
          <div class="icon-wrap"><i class="fa-solid fa-phone"></i></div>
          <h3>Linea Nacional REPUVE</h3>
          <p>Atencion gratuita 24 horas para consultas y tramites del Registro Publico Vehicular.</p>
          <a href={`tel:${site.phone_repuve.replace(/\\s/g,'')}`} class="btn btn-primary">{site.phone_repuve}</a>
        </div>
        <div class="info-card">
          <div class="icon-wrap"><i class="fa-solid fa-globe"></i></div>
          <h3>Portal Oficial REPUVE</h3>
          <p>Consulta ciudadana online, tramites y citas. Disponible 24/7.</p>
          <a href={site.official_site} rel="noopener nofollow" class="btn btn-primary">repuve.gob.mx</a>
        </div>
        <div class="info-card">
          <div class="icon-wrap"><i class="fa-solid fa-building"></i></div>
          <h3>Gobierno de Chihuahua</h3>
          <p>Para temas estatales: Control Vehicular, placas, tenencia, refrendo.</p>
          <a href={`tel:${site.state_govt_phone.replace(/\\s/g,'')}`} class="btn btn-primary">{site.state_govt_phone}</a>
        </div>
      </div>

      <h2>Para tramites especificos</h2>
      <ul>
        <li><strong>Consulta ciudadana online:</strong> <a href={site.official_consulta} rel="noopener nofollow">{site.official_consulta}</a></li>
        <li><strong>Regularizacion de autos chocolate:</strong> <a href="https://regularizaauto.sspc.gob.mx" rel="noopener nofollow">regularizaauto.sspc.gob.mx</a></li>
        <li><strong>Reporte de robo vehicular:</strong> Llama al 911 o a la Fiscalia Especializada en Robo de Vehiculos del Estado de Chihuahua.</li>
        <li><strong>Atencion ciudadana del Gobierno:</strong> <a href={`mailto:${site.state_attorney_email}`}>{site.state_attorney_email}</a></li>
      </ul>

      <h2>Oficinas REPUVE en Chihuahua</h2>
      <p>Visita la pagina de cada oficina para ver direccion, mapa, telefono local y horarios:</p>
      <ul>
        <li><a href="/oficinas/chihuahua-capital/">Chihuahua capital</a> - Av. Deportiva Sur 8403, Avalos</li>
        <li><a href="/oficinas/ciudad-juarez/">Ciudad Juarez</a> - Blvd. Oscar Flores 3920</li>
        <li><a href="/oficinas/cuauhtemoc/">Cuauhtemoc</a></li>
        <li><a href="/oficinas/delicias/">Delicias</a></li>
        <li><a href="/oficinas/hidalgo-del-parral/">Hidalgo del Parral</a></li>
        <li><a href="/oficinas/nuevo-casas-grandes/">Nuevo Casas Grandes</a></li>
        <li><a href="/oficinas/camargo/">Camargo</a></li>
      </ul>

      <h2>Sobre este sitio</h2>
      <p>
        Este es un sitio informativo independiente. Para conocer mas sobre nuestra mision y editores,
        visita la pagina <a href="/sobre-nosotros/">sobre nosotros</a>.
      </p>
    </article>
  </div>
</Base>
'''

sobre = '''---
import Base from '../layouts/Base.astro';
import Breadcrumbs from '../components/Breadcrumbs.astro';
import { site } from '../data/datos.js';

const breadcrumbs = [
  { label: 'Inicio', href: '/' },
  { label: 'Sobre nosotros' }
];
---

<Base
  title="Sobre Nosotros"
  description="Informacion sobre REPUVE Chihuahua: sitio informativo independiente con guias, oficinas, tramites y consultas del Registro Publico Vehicular en Chihuahua."
>
  <div class="container container-narrow">
    <Breadcrumbs items={breadcrumbs} />

    <header class="page-header">
      <div class="eyebrow"><i class="fa-solid fa-circle-info"></i> Informacion</div>
      <h1>Sobre REPUVE Chihuahua</h1>
      <p class="lede">Quienes somos, que hacemos y por que creamos este sitio informativo.</p>
    </header>

    <article class="article-main">
      <h2>Que es este sitio</h2>
      <p>
        <strong>REPUVE Chihuahua</strong> es un sitio informativo independiente dedicado a recopilar,
        ordenar y difundir informacion publica sobre el Registro Publico Vehicular (REPUVE) en el
        estado de Chihuahua, Mexico.
      </p>
      <p>
        Nuestro objetivo es <strong>simplificar el acceso a la informacion oficial</strong> para que
        los ciudadanos puedan realizar sus tramites vehiculares de forma rapida, sin perder tiempo
        navegando entre portales gubernamentales fragmentados o desactualizados.
      </p>

      <h2>Que encontraras aqui</h2>
      <ul>
        <li><strong>Directorio de oficinas REPUVE</strong> en las principales ciudades de Chihuahua: capital, Ciudad Juarez, Cuauhtemoc, Delicias, Parral, Nuevo Casas Grandes y Camargo.</li>
        <li><strong>Guias paso a paso</strong> para realizar consultas ciudadanas, agendar citas, inscribir vehiculos, regularizar autos chocolate y todos los tramites comunes.</li>
        <li><strong>Informacion sobre requisitos, costos y horarios</strong> actualizada con base en fuentes oficiales y reportes ciudadanos.</li>
        <li><strong>Respuestas a preguntas frecuentes</strong> sobre el REPUVE, NIV, chip vehicular, tarjeta de circulacion, cambio de propietario y mas.</li>
      </ul>

      <h2>Lo que NO somos</h2>
      <div class="warning-box">
        <p>
          <i class="fa-solid fa-triangle-exclamation"></i>
          <span>
            <strong>Este sitio NO es oficial.</strong> No tenemos vinculo, afiliacion, asociacion,
            patrocinio ni representacion con el Gobierno de Mexico, la Secretaria Ejecutiva del Sistema
            Nacional de Seguridad Publica (SESNSP), el REPUVE oficial, el Gobierno del Estado de Chihuahua
            ni ningun organismo gubernamental. Tampoco procesamos tramites ni consultas vehiculares en
            nombre de los usuarios.
          </span>
        </p>
      </div>

      <h2>Como trabajamos</h2>
      <p>Nuestro contenido se elabora siguiendo estos principios:</p>
      <ul>
        <li><strong>Fuentes oficiales:</strong> toda la informacion se basa en datos publicos del REPUVE, gobierno de Chihuahua y reportes verificables.</li>
        <li><strong>Actualizacion periodica:</strong> revisamos costos, horarios y direcciones de oficinas para mantenerlas vigentes.</li>
        <li><strong>Claridad y accesibilidad:</strong> evitamos lenguaje tecnico innecesario. Explicamos los tramites como si fueramos un amigo que ya paso por ese proceso.</li>
        <li><strong>Transparencia:</strong> siempre indicamos cuando la informacion es de referencia y recomendamos verificar en fuentes oficiales antes de cualquier tramite.</li>
      </ul>

      <h2>Para tramites oficiales, siempre acude a</h2>
      <div class="info-cards-grid" style="margin-top:1.5rem">
        <div class="info-card">
          <div class="icon-wrap"><i class="fa-solid fa-globe"></i></div>
          <h3>Portal Oficial REPUVE</h3>
          <p>{site.official_site}</p>
          <a href={site.official_site} rel="noopener nofollow" class="btn btn-primary">Visitar</a>
        </div>
        <div class="info-card">
          <div class="icon-wrap"><i class="fa-solid fa-phone"></i></div>
          <h3>Linea Nacional</h3>
          <p>{site.phone_repuve}</p>
          <a href={`tel:${site.phone_repuve.replace(/\\s/g,'')}`} class="btn btn-primary">Llamar</a>
        </div>
      </div>

      <h2>Contacto</h2>
      <p>
        Si tienes sugerencias, correcciones o aportes para mejorar este sitio, visita la
        seccion de <a href="/contacto/">contacto</a>. Recibimos comentarios sobre contenido,
        pero <strong>no procesamos tramites individuales</strong> ni respondemos consultas
        de vehiculos especificos.
      </p>

      <div class="tip-box">
        <p>
          <i class="fa-solid fa-circle-info"></i>
          <span>
            <strong>Aviso legal:</strong> Los datos publicados (direcciones, telefonos, horarios) son
            de referencia y pueden cambiar. Antes de cualquier tramite presencial, verifica llamando
            al {site.phone_repuve} o consulta directamente al sitio oficial repuve.gob.mx.
          </span>
        </p>
      </div>
    </article>
  </div>
</Base>
'''

for filename, content in [
    ('aviso-de-privacidad.astro', aviso),
    ('contacto.astro', contacto),
    ('sobre-nosotros.astro', sobre),
]:
    path = PAGES_DIR / filename
    path.write_text(content, encoding='utf-8')
    print(f"OK: {filename} ({len(content):,} chars)")

print(f"\nTotal: 3 paginas estaticas generadas")
