#!/usr/bin/env python3
"""
FASE 2: Expande el contenido de las 7 páginas críticas para SEO.

Cada página pasa de ~800-1200 palabras a ~1800-2500 palabras con:
- Intro expandido (2-3 párrafos)
- 5-7 secciones (en lugar de 3-4)
- Sub-secciones h3 cuando aplica
- 6-8 FAQs (en lugar de 3-5)
- Contenido específico de Chihuahua

Páginas críticas (mayor volumen + mayor intención comercial):
1. consulta-ciudadana    (Consulta intent)
2. consulta-por-placa    (Consulta intent)
3. consulta-por-niv      (Consulta intent)
4. agendar-cita          (Tramite intent)
5. requisitos            (Tramite intent)
6. costos                (Tramite intent)
7. regularizacion-autos-chocolate (Tramite intent, TOP keyword)

Mantengo la intención de búsqueda de cada slug.
Este script es REUTILIZABLE: cambiar las constantes ESTADO_*, CIUDADES_*, etc.
para clonar a Coahuila, Querétaro, etc.
"""
import json
from pathlib import Path

DATA = Path('/Users/quiwistore/Downloads/repuve-chihuahua/data/repuve.json')

# ============ CONFIG DEL ESTADO (cambiar para clonar) ============
ESTADO = "Chihuahua"
ESTADO_GENTILICIO = "chihuahuense"
CAPITAL = "Chihuahua"
CIUDADES_PRINCIPALES = ["Chihuahua capital", "Ciudad Juárez", "Cuauhtémoc", "Delicias", "Hidalgo del Parral", "Nuevo Casas Grandes", "Camargo"]
FRONTERA_PRINCIPAL = "Ciudad Juárez"
TELEFONO_REPUVE = "800 737 8831"
TELEFONO_GOBIERNO = "614 429 3300"
COSTO_REGULARIZACION = "$2,500 MXN"
DOMINIO_OFICIAL = "repuve.gob.mx"

# ============ CONTENIDO EXPANDIDO ============

EXPANDED_PAGES = {
    # ========================================================================
    # 1. CONSULTA CIUDADANA — entrada principal
    # ========================================================================
    "consulta-ciudadana": {
        "h1": f"Consulta Ciudadana REPUVE {ESTADO}: Cómo Verificar un Vehículo Gratis",
        "title": f"Consulta Ciudadana REPUVE {ESTADO} 2026 - Verifica Placas, NIV, Reporte Robo",
        "meta": f"Consulta ciudadana REPUVE {ESTADO} 100% gratis. Verifica placas, NIV o folio. Detecta vehículos con reporte de robo en {ESTADO} antes de comprar. Tutorial paso a paso 2026.",
        "category": "Consulta",
        "status_chip": "Gratis · En línea · 2 minutos",
        "intro": (
            f"La <strong>consulta ciudadana del REPUVE en {ESTADO}</strong> es el servicio gratuito más importante para "
            f"verificar el estatus legal de cualquier vehículo registrado en México. Ya sea que estés a punto de comprar "
            f"un auto usado en Chihuahua capital, Ciudad Juárez o cualquier otro municipio del estado, esta consulta "
            f"te dice <strong>en menos de 2 minutos</strong> si el vehículo tiene reporte de robo, restricciones legales o "
            f"si está limpio para ser transferido a tu nombre. "
            f"<br><br>"
            f"El servicio lo opera la Secretaría Ejecutiva del Sistema Nacional de Seguridad Pública (SESNSP), "
            f"organismo federal del Gobierno de México que mantiene la base de datos nacional vehicular. "
            f"<strong>La consulta es 100% gratuita, sin registro y disponible 24/7.</strong> "
            f"Si alguien te cobra por hacerla, es un fraude — denúncialo."
        ),
        "sections": [
            {
                "heading": "Qué es la consulta ciudadana del REPUVE",
                "body": [
                    f"La <strong>consulta ciudadana REPUVE</strong> es una herramienta pública del Gobierno de México que permite a cualquier "
                    f"ciudadano verificar el estatus legal de un vehículo automotor registrado en territorio nacional. "
                    f"Está diseñada principalmente como mecanismo de defensa antes de comprar un auto usado: "
                    f"con una sola consulta, sabes si el vehículo está vinculado a un reporte de robo o si tiene alguna alerta judicial activa.",

                    f"El REPUVE cruza información de <strong>tres fuentes oficiales</strong>: la base de datos federal del Registro Público Vehicular, "
                    f"los registros de las fiscalías estatales (en este caso la Fiscalía General del Estado de {ESTADO}) "
                    f"y la base de la OCRA (Oficina Coordinadora de Riesgos Asegurados, que aglutina datos de las aseguradoras).",

                    f"Cada consulta devuelve uno de cuatro estatus posibles: <strong>'sin reporte'</strong> (el vehículo está limpio), "
                    f"<strong>'con reporte de robo'</strong> (NO comprar), <strong>'recuperado'</strong> (fue robado pero ya recuperado, requiere validar situación legal), "
                    f"o <strong>'sin información'</strong> (el NIV o placa no figura en el registro nacional, lo que puede indicar un vehículo no inscrito o un dato mal ingresado)."
                ]
            },
            {
                "heading": f"Cómo hacer la consulta REPUVE paso a paso en {ESTADO}",
                "body": [
                    f"<strong>1. Acudí al portal oficial:</strong> ingresá a <a href='https://www2.repuve.gob.mx:8443/ciudadania/'>www2.repuve.gob.mx:8443/ciudadania/</a>. "
                    f"Es el único sitio oficial autorizado. Cualquier otra URL que te cobre por la consulta es fraudulenta.",

                    f"<strong>2. Elegí el tipo de búsqueda.</strong> Podés consultar por uno de cuatro datos: número de placa (5-7 caracteres alfanuméricos), "
                    f"NIV (Número de Identificación Vehicular, 17 caracteres), folio de constancia de inscripción o NCI (Número de Constancia de Inscripción).",

                    f"<strong>3. Ingresá el dato sin guiones ni espacios.</strong> El sistema es estricto con el formato: "
                    f"placas se escriben todas juntas (ejemplo: <code>ABC1234</code>, no <code>ABC-1234</code>), "
                    f"y el NIV se escribe completo en mayúsculas sin separadores.",

                    f"<strong>4. Resolvé el captcha</strong> que aparece en pantalla (suelen ser caracteres deformados o una imagen). Esto previene consultas automatizadas masivas.",

                    f"<strong>5. Pulsá 'Buscar' y esperá la respuesta.</strong> El sistema puede tardar entre 5 segundos y 1 minuto. En horarios pico (mediodía, fines de semana) puede ser más lento.",

                    f"<strong>6. Revisá el resultado.</strong> El portal te muestra datos básicos del vehículo (marca, modelo, año, color, motor) "
                    f"y el estatus legal. Si todo está limpio, guardá una captura de pantalla con fecha visible."
                ]
            },
            {
                "heading": "Qué información necesito para hacer la consulta",
                "body": [
                    "Para una <strong>consulta exitosa</strong> necesitás al menos uno de los siguientes datos del vehículo:",

                    "<strong>Número de placa:</strong> la matrícula vigente del vehículo, asignada por el estado donde fue emplacado. En Chihuahua suelen ser 7 caracteres alfanuméricos (ejemplo: <code>ABC1234</code>). No incluyas guiones ni espacios.",

                    "<strong>NIV (Número de Identificación Vehicular):</strong> también conocido como VIN. Son 17 caracteres alfanuméricos únicos por vehículo. Lo encontrás en el parabrisas (lado del conductor, visible desde afuera), en la puerta del piloto, en la tarjeta de circulación o en la factura. <strong>El NIV no contiene las letras I, O ni Q</strong> (para evitar confusión con 1 y 0).",

                    "<strong>Folio o NCI:</strong> número de la constancia de inscripción al REPUVE. Aparece en el documento emitido al momento de inscribir el vehículo.",

                    "<strong>Recomendación práctica:</strong> si vas a comprar un auto, <strong>pedí el NIV antes que la placa</strong>. Las placas se cambian al hacer cambio de propietario; el NIV es único e invariable durante toda la vida del vehículo. Si las placas y el NIV no coinciden con la factura, es señal de auto clonado o robado."
                ]
            },
            {
                "heading": "Cuáles son los posibles resultados de la consulta",
                "body": [
                    "<strong>Sin reporte:</strong> el vehículo no tiene reporte de robo ni alertas judiciales. Es el resultado esperado para autos legales. Sigue todos los demás pasos de verificación antes de comprar (revisión mecánica, comparar NIV con la factura, etc.), pero al menos no hay alerta legal activa.",

                    "<strong>Con reporte de robo:</strong> el vehículo fue reportado como robado y está en la base de datos. <strong>NO compres bajo ningún concepto.</strong> Si ya lo tenés en tus manos (porque era una compra en proceso), suspendé la operación y denuncia a las autoridades.",

                    "<strong>Recuperado:</strong> el vehículo fue robado pero las autoridades lo recuperaron. Esto NO significa que sea libremente comerciable: puede estar en un depósito a la espera de entrega al dueño original, o tener algún proceso legal pendiente. Antes de comprar, exigí al vendedor que demuestre la cadena de custodia legal del vehículo desde su recuperación.",

                    "<strong>Sin información:</strong> el NIV o placa que ingresaste no aparece en la base nacional. Puede deberse a varios motivos: el vehículo no está inscrito en el REPUVE (común en autos chocolate sin regularizar), un dato mal ingresado, o que la base no esté actualizada con un registro reciente. Si el vendedor te dice que es porque el auto es nuevo, exigí ver la factura original con sello del fabricante.",

                    f"<strong>Datos complementarios:</strong> además del estatus, la consulta te devuelve marca, modelo, año, color, número de motor, planta de ensamble, país de origen y fecha de inscripción al REPUVE. Compará todos esos datos con la factura del vehículo — si alguno no coincide, hay irregularidad."
                ]
            },
            {
                "heading": "Qué hacer si la consulta REPUVE no carga o da error",
                "body": [
                    f"El portal oficial del REPUVE <strong>está en proceso de modernización</strong> y por momentos presenta intermitencias. Si no carga, no significa que el sistema esté caído permanentemente — suele resolverse en minutos u horas.",

                    f"<strong>Alternativas si el portal está caído:</strong>",

                    f"<strong>1. Esperá 15-30 minutos y reintentá.</strong> La mayoría de las caídas son temporales.",

                    f"<strong>2. Probá desde otro navegador o dispositivo.</strong> A veces el problema es de caché o cookies. Probá en modo incógnito.",

                    f"<strong>3. Llamá a la línea nacional REPUVE: <a href='tel:{TELEFONO_REPUVE.replace(' ','')}'>{TELEFONO_REPUVE}</a></strong> (800 REPUVE 1). Atención gratuita 24 horas. El operador puede hacer la consulta por vos y darte el resultado verbalmente.",

                    f"<strong>4. Acudí personalmente a la oficina REPUVE más cercana.</strong> En Chihuahua tenés 7 oficinas: capital, Ciudad Juárez, Cuauhtémoc, Delicias, Hidalgo del Parral, Nuevo Casas Grandes y Camargo. Ver <a href='/oficinas/'>directorio completo</a>.",

                    f"<strong>5. Consulta en gob.mx</strong>: la página informativa <a href='https://www.gob.mx/sesnsp/acciones-y-programas/consulta-ciudadana-del-registro-publico-vehicular-repuve'>gob.mx/sesnsp</a> está alojada en infraestructura distinta y suele estar siempre disponible. Desde ahí podés acceder al portal de consulta."
                ]
            },
            {
                "heading": "Errores frecuentes al consultar el REPUVE",
                "body": [
                    "<strong>Error: 'No se encontraron resultados'</strong> aunque el auto sí está inscrito. Generalmente es por formato: estás ingresando guiones, espacios o letras minúsculas. Reintentá escribiendo todo en mayúsculas, sin separadores.",

                    "<strong>Error: el captcha no se valida.</strong> El captcha es sensible a mayúsculas y minúsculas. Si las letras se ven borrosas, recargá la imagen del captcha con el botón de recarga.",

                    "<strong>Error: 'Servicio no disponible'.</strong> El sistema oficial tuvo caída temporal. Esperá 15-30 min y reintentá, o llamá al 800 REPUVE.",

                    "<strong>El vehículo aparece 'sin información' pero el vendedor jura que es legal.</strong> Pedile ver la factura original — si tiene factura legítima y el auto es de 2023+, puede ser que aún no esté en la base por demora administrativa del estado de emplacado. Pero verificá igualmente: <strong>compará el NIV de la factura con el grabado en el chasis y en el parabrisas</strong>.",

                    "<strong>El NIV en la factura no coincide con el del vehículo.</strong> Es un caso grave: posible auto clonado o NIV alterado. No completes la compra y denunciá al Ministerio Público."
                ]
            }
        ],
        "faqs": [
            {"q": "¿La consulta ciudadana del REPUVE realmente es gratis?", "a": f"Sí, 100% gratis. El servicio es operado por el Gobierno de México como herramienta de seguridad pública. <strong>No hay ningún cobro oficial</strong>. Si un sitio web o tercero te cobra por hacer la consulta, es fraude — la consulta real solo se hace en el portal oficial <a href='https://www2.repuve.gob.mx:8443/ciudadania/'>www2.repuve.gob.mx:8443/ciudadania/</a> o llamando al {TELEFONO_REPUVE}."},
            {"q": "¿Puedo consultar el REPUVE desde mi celular?", "a": "Sí, el portal oficial funciona en móviles. Si no carga, probá rotar el celular a horizontal (el captcha a veces se ve mejor) o usar un navegador distinto (Chrome o Firefox)."},
            {"q": "¿Cuánto tiempo tarda en aparecer un robo recién reportado?", "a": "Una vez que se levanta la denuncia ministerial, suele tardar entre <strong>24 y 72 horas</strong> en reflejarse en el REPUVE. Si denunciaste recién y querés que aparezca rápido, podés acelerar el proceso solicitando explícitamente al Ministerio Público la actualización al REPUVE — algunos estados lo hacen automáticamente, otros tardan."},
            {"q": "¿La consulta REPUVE me dice si tiene adeudos de tenencia o multas?", "a": f"No. El REPUVE solo refleja <strong>reportes de robo y estatus legal federal</strong>. Para adeudos de tenencia, refrendo o multas, debés consultar el sistema fiscal del estado donde está emplacado el vehículo. En Chihuahua, eso se hace en el portal de la Secretaría de Hacienda del estado o llamando al {TELEFONO_GOBIERNO}. Ver <a href='/adeudos-vehiculares/'>adeudos vehiculares</a>."},
            {"q": "¿Sirve la consulta REPUVE para motocicletas?", "a": "Sí, el REPUVE registra motos exactamente igual que autos. Podés consultar por placa o NIV de la moto. Ver <a href='/repuve-motos/'>REPUVE motos</a> para detalles específicos del trámite y oficinas."},
            {"q": "¿Qué hago si el resultado dice 'recuperado' pero quiero comprar el auto?", "a": "Procedé con extrema cautela. 'Recuperado' significa que fue robado y posteriormente recuperado por las autoridades, pero NO siempre significa que sea libremente comerciable. Exigí al vendedor: <strong>(1)</strong> denuncia ministerial original que activó el reporte, <strong>(2)</strong> acta o resolución de devolución por parte de la autoridad, <strong>(3)</strong> factura original con cadena de endosos clara desde la recuperación. Si falta alguno de esos documentos, NO compres."},
            {"q": f"¿Puedo hacer la consulta REPUVE desde Ciudad Juárez si el auto es de otro estado?", "a": f"Sí. El REPUVE es <strong>una base de datos federal</strong> que cubre los 32 estados de México. Podés consultar desde Cd. Juárez (o cualquier ciudad de {ESTADO}) un auto emplacado en CDMX, Veracruz, Yucatán, etc. La consulta no tiene restricción geográfica."},
            {"q": "¿Es lo mismo que hacer una verificación por la aseguradora?", "a": "No, son complementarios. El REPUVE es público y gratuito, refleja reportes oficiales de robo. La aseguradora hace una verificación interna (a través de OCRA) que puede incluir datos adicionales como historial de siniestros, pero solo para sus clientes. <strong>Antes de comprar siempre hacé la consulta REPUVE</strong>; la aseguradora es una capa adicional para autos asegurados."}
        ]
    },

    # ========================================================================
    # 2. CONSULTA POR PLACA
    # ========================================================================
    "consulta-por-placa": {
        "h1": f"Consulta REPUVE por Placa en {ESTADO}: Verifica Cualquier Vehículo Gratis",
        "title": f"Consulta REPUVE por Placa {ESTADO} - Gratis y Sin Registro (2026)",
        "meta": f"Cómo consultar el REPUVE por placa en {ESTADO} paso a paso. Verificá reporte de robo, estatus legal y datos del vehículo gratis en menos de 2 minutos. Tutorial 2026.",
        "category": "Consulta",
        "status_chip": "Gratis · 5-7 caracteres · Sin registro",
        "intro": (
            f"La <strong>consulta REPUVE por placa</strong> es la forma más rápida de verificar un vehículo en {ESTADO}. "
            f"Si vas a comprar un auto usado y solo tenés a la vista las placas (porque el vendedor todavía no te muestra la factura), "
            f"con este dato podés saber en <strong>menos de 2 minutos</strong> si el vehículo tiene reporte de robo, alertas legales "
            f"o si el estatus es 'limpio'."
            f"<br><br>"
            f"En {ESTADO}, las placas particulares son alfanuméricas con formato típico de 7 caracteres "
            f"(ejemplo: <code>ABC1234</code>). El sistema del REPUVE acepta consultas con placas de cualquier estado de la República "
            f"— no hay restricción geográfica, es una base federal."
        ),
        "sections": [
            {
                "heading": "Cómo consultar el REPUVE por placa paso a paso",
                "body": [
                    f"<strong>1. Andá al portal oficial</strong> en <a href='https://www2.repuve.gob.mx:8443/ciudadania/'>www2.repuve.gob.mx:8443/ciudadania/</a>. Es el único lugar autorizado. Cualquier sitio que te cobre por la consulta es fraude.",

                    f"<strong>2. Elegí la opción 'Consulta por placa'</strong> en el formulario del portal. Es la primera opción y la más usada.",

                    f"<strong>3. Escribí la placa SIN guiones ni espacios.</strong> El sistema es estricto: <code>ABC1234</code> es correcto, <code>ABC-1234</code> no funcionará. Usá mayúsculas siempre.",

                    f"<strong>4. Resolvé el captcha</strong> que aparece debajo (caracteres deformados o imagen). Si no se entiende, podés recargar el captcha con el botón de refresh.",

                    f"<strong>5. Pulsá 'Buscar'</strong> y esperá entre 5 y 30 segundos. En horarios pico el sistema puede tardar más.",

                    f"<strong>6. Interpretá el resultado.</strong> Te mostrará datos básicos del vehículo (marca, modelo, año, color) y el estatus legal: 'sin reporte', 'con reporte de robo', 'recuperado' o 'sin información'."
                ]
            },
            {
                "heading": "Formato correcto de las placas mexicanas",
                "body": [
                    "Las placas vehiculares en México siguen formatos diferentes según el estado de emplacado y el tipo de vehículo:",

                    f"<strong>Particulares estándar:</strong> 3 letras + 3 o 4 números (ejemplo: <code>ABC1234</code>, <code>XYZ123</code>). Es el formato más común en {ESTADO} y otros estados.",

                    "<strong>Particulares antiguas:</strong> en algunos estados las placas viejas tienen formato 3 números + 3 letras (ejemplo: <code>123ABC</code>). El REPUVE acepta ambos formatos.",

                    "<strong>Servicio público (taxis, transporte):</strong> color verde, formato distinto. También consultables vía REPUVE.",

                    "<strong>Motocicletas:</strong> placas más pequeñas, formato similar a particulares.",

                    "<strong>Fronterizas (en Cd. Juárez, Tijuana, etc.):</strong> tienen códigos especiales que reflejan la franja fronteriza. También se pueden consultar en REPUVE normalmente.",

                    f"<strong>Importante:</strong> al escribir la placa en el portal, no uses guiones, puntos ni espacios. Solo letras y números."
                ]
            },
            {
                "heading": "Qué datos te devuelve la consulta por placa",
                "body": [
                    "Al hacer la consulta exitosa, el sistema te muestra los siguientes datos del vehículo asociado a la placa:",

                    "<strong>Datos identificatorios:</strong> NIV completo (17 caracteres), número de motor, número de serie, placa actual, color, marca, modelo, año del modelo, tipo de vehículo (sedán, SUV, pickup, moto), número de puertas, cilindrada, número de cilindros.",

                    "<strong>Datos de origen:</strong> país de origen del vehículo (México, EE.UU., Japón, Alemania, etc.), planta de ensamble.",

                    "<strong>Datos de registro:</strong> fecha y hora de registro en el REPUVE, entidad federativa donde está emplacado, fecha de expedición de las placas actuales, último movimiento administrativo registrado.",

                    "<strong>Estatus legal:</strong> el dato más importante. Indica si tiene reporte de robo, si está recuperado, o si está sin alerta.",

                    "<strong>Información que NO aparece en esta consulta:</strong> propietario actual (por privacidad), historial de propietarios anteriores, adeudos de tenencia o multas estatales, accidentes registrados (para eso necesitás servicios pagos como Carfax o consultar directamente al estado de emplacado)."
                ]
            },
            {
                "heading": "Diferencias entre consultar por placa vs por NIV",
                "body": [
                    "Ambas consultas devuelven el mismo tipo de información, pero hay diferencias prácticas importantes:",

                    "<strong>Consulta por placa</strong> es más cómoda porque las placas están a la vista del vehículo. Si vas a ver un auto al lote o a casa del vendedor, es lo más fácil de copiar. <strong>Pero tiene un riesgo:</strong> las placas se cambian al hacer cambio de propietario o al cambiar de estado. Una placa puede haber estado asociada a un vehículo robado hace años y ahora estar en un auto totalmente distinto.",

                    "<strong>Consulta por NIV</strong> es más confiable porque <strong>el NIV es único e invariable</strong> durante toda la vida del vehículo. Si el NIV figura como robado, no hay manera de 'limpiarlo' cambiando datos. Para una verificación de máxima seguridad, siempre <strong>consultá por NIV</strong>.",

                    f"<strong>Recomendación práctica:</strong> hacé ambas consultas. Primero por placa (rápido al ver el auto). Después por NIV (más profundo, antes de pagar). Si los resultados de ambas no coinciden — por ejemplo, la placa dice un modelo y el NIV otro — es señal de fraude. <a href='/consulta-por-niv/'>Consultá por NIV acá</a>."
                ]
            },
            {
                "heading": "Casos en que la consulta por placa puede fallar",
                "body": [
                    "<strong>Vehículos importados sin regularizar:</strong> los autos 'chocolate' que aún no completaron la <a href='/regularizacion-autos-chocolate/'>regularización federal</a> no tienen placas mexicanas oficiales, por lo que no aparecen en el REPUVE. Para esos casos consultá por NIV.",

                    "<strong>Vehículos nuevos recién comprados:</strong> entre el momento de venta y el alta de placas pueden pasar 2-4 semanas. Durante ese periodo la consulta por placa puede no devolver datos. Usa el NIV o esperá unas semanas.",

                    "<strong>Placas dadas de baja:</strong> si las placas fueron canceladas por baja vehicular previa, la consulta puede devolver 'sin información'. Verificá con el NIV.",

                    "<strong>Placas de otra época:</strong> placas muy antiguas (de antes de la creación del REPUVE en 2005) pueden no estar digitalizadas.",

                    "<strong>Placas alteradas o falsas:</strong> si la consulta arroja un modelo o color distinto al vehículo que estás viendo, hay fraude. Por ejemplo, la placa de un Volkswagen Jetta 2018 aparece, pero el auto frente a vos es un Toyota Corolla 2015. <strong>No compres y reportá.</strong>"
                ]
            }
        ],
        "faqs": [
            {"q": "¿Puedo consultar placas de cualquier estado de México?", "a": f"Sí, el REPUVE es una base de datos federal nacional. Desde {ESTADO} podés consultar placas de CDMX, Nuevo León, Yucatán, Veracruz o cualquier otro estado. No hay restricción geográfica."},
            {"q": "¿La consulta por placa es válida para motocicletas?", "a": "Sí, motos y autos comparten la misma base. Ingresá la placa de la moto sin guiones. Ver <a href='/repuve-motos/'>REPUVE motos</a>."},
            {"q": "¿Qué hago si las placas del auto no coinciden con la factura?", "a": "Es señal de posible fraude o irregularidad. <strong>No completes la compra</strong> y consultá tanto por placa como por NIV. Si los datos siguen sin coincidir, denuncia al Ministerio Público. Las placas se pueden cambiar legalmente solo por trámites oficiales en Control Vehicular del estado."},
            {"q": f"¿Necesito acudir a una oficina REPUVE en {ESTADO} para consultar por placa?", "a": "No. La consulta por placa es 100% en línea. Solo necesitás acudir a oficina para trámites presenciales (inscripción, regularización, alta/baja de placas). Ver <a href='/oficinas/'>oficinas REPUVE en {ESTADO}</a>."},
            {"q": "¿Cuánto tiempo demora en aparecer un robo recién denunciado?", "a": "Entre 24 y 72 horas tras la denuncia ministerial, dependiendo del estado y la fiscalía. Para casos urgentes (robo reciente), podés pedir al Ministerio Público que escale la actualización al REPUVE de inmediato."},
            {"q": "¿Puedo descargar un PDF con el resultado de la consulta?", "a": "El portal oficial del REPUVE no genera un PDF automático, pero podés hacer captura de pantalla con fecha visible. Para fines legales (por ejemplo, anexar a un contrato de compraventa), la captura sirve como evidencia del estatus al momento de la consulta."},
            {"q": "¿La consulta queda registrada con mi nombre o IP?", "a": "El portal oficial registra IPs y user-agents por seguridad, pero <strong>no requiere registro personal</strong> ni te identifica. La consulta es anónima desde el punto de vista del usuario."}
        ]
    },

    # ========================================================================
    # 3. CONSULTA POR NIV
    # ========================================================================
    "consulta-por-niv": {
        "h1": f"Consulta REPUVE por NIV en {ESTADO}: Verifica por Número de Identificación Vehicular",
        "title": f"Consulta REPUVE por NIV/VIN {ESTADO} 2026 - 17 Caracteres Únicos",
        "meta": f"Consulta REPUVE por NIV en {ESTADO}: la verificación más confiable de cualquier vehículo. Tutorial paso a paso, dónde encontrar el NIV, errores comunes. Gratis 2026.",
        "category": "Consulta",
        "status_chip": "17 caracteres exactos · Único por vehículo",
        "intro": (
            f"La <strong>consulta REPUVE por NIV</strong> (Número de Identificación Vehicular, también llamado VIN) es la "
            f"verificación más confiable que existe para un vehículo. A diferencia de las placas — que pueden cambiarse "
            f"con cualquier trámite de Control Vehicular — el NIV es <strong>único, irrepetible y permanente</strong> durante "
            f"toda la vida del vehículo. Cualquier intento de alterarlo es un delito federal grave."
            f"<br><br>"
            f"En {ESTADO} y en todo México, antes de comprar un auto usado o realizar un trámite vehicular importante, "
            f"<strong>siempre conviene consultar por NIV</strong>. Es el dato que el REPUVE usa para cruzar información "
            f"con todas las bases nacionales y de seguridad."
        ),
        "sections": [
            {
                "heading": "Qué es el NIV y por qué es tan importante",
                "body": [
                    "El <strong>NIV (Número de Identificación Vehicular)</strong> es un código único de <strong>17 caracteres alfanuméricos</strong> asignado al vehículo durante su fabricación. Es el equivalente del 'DNI' o 'huella digital' del auto. Cada NIV es único en todo el mundo — no existen dos vehículos con el mismo NIV.",

                    "El NIV sigue un estándar internacional (ISO 3779) y codifica información sobre el fabricante, el modelo, el año, la planta de ensamble y un número de serie único. Por ejemplo, los primeros 3 caracteres identifican el país y fabricante, los siguientes 6 describen el vehículo, y los últimos 8 son el número de serie.",

                    "<strong>El NIV no contiene las letras I, O ni Q</strong>: esto es deliberado, para evitar confusión con los números 1 y 0. Si crees ver una de esas letras, en realidad es 1, 0 o 0.",

                    "<strong>Por qué el NIV es la verificación más confiable:</strong> mientras las placas pueden cambiarse, las facturas pueden falsificarse y los nombres de propietarios cambian con cada venta, el NIV es <strong>físicamente grabado en el chasis y otras partes del vehículo</strong>. Alterarlo requiere intervención mecánica y es un delito federal."
                ]
            },
            {
                "heading": "Cómo hacer la consulta REPUVE por NIV paso a paso",
                "body": [
                    f"<strong>1. Conseguí el NIV del vehículo.</strong> Lo encontrás en varios lugares (ver siguiente sección). Asegurate de tener los 17 caracteres exactos en orden.",

                    f"<strong>2. Ingresá al portal oficial</strong>: <a href='https://www2.repuve.gob.mx:8443/ciudadania/'>www2.repuve.gob.mx:8443/ciudadania/</a>. Es la única URL oficial. No uses sitios de terceros que cobren.",

                    f"<strong>3. Elegí la opción 'Consulta por NIV'</strong> en el formulario.",

                    f"<strong>4. Escribí el NIV exactamente como aparece en el vehículo.</strong> Todo en mayúsculas, sin guiones ni espacios. Ejemplo: <code>3VWFE21C04M000001</code>.",

                    f"<strong>5. Resolvé el captcha</strong> de validación.",

                    f"<strong>6. Pulsá 'Buscar'</strong>. El sistema responde en 5-60 segundos.",

                    f"<strong>7. Verificá los datos devueltos.</strong> El resultado debe coincidir 100% con el vehículo que tenés frente a vos (marca, modelo, año, color, número de motor). Si algo no coincide, hay fraude o irregularidad."
                ]
            },
            {
                "heading": "Dónde encontrar el NIV en el vehículo",
                "body": [
                    "El NIV está grabado en varios lugares del vehículo. Los principales son:",

                    "<strong>1. Parabrisas (lado del conductor):</strong> visible desde afuera, en la esquina inferior izquierda del parabrisas. Hay una pequeña placa metálica con el NIV grabado. Es la ubicación más fácil de revisar al ver un auto.",

                    "<strong>2. Puerta del piloto:</strong> en el marco interior de la puerta (visible al abrirla), hay una etiqueta del fabricante con el NIV, fecha de fabricación, modelo, etc.",

                    "<strong>3. Tarjeta de circulación:</strong> el NIV aparece impreso en la tarjeta como dato del vehículo.",

                    "<strong>4. Factura original:</strong> debe coincidir 100% con el NIV del vehículo. Si no coincide, es señal de fraude.",

                    "<strong>5. Motor (algunas marcas):</strong> algunos fabricantes graban el NIV también en el bloque del motor.",

                    "<strong>6. Chasis (grabado físico):</strong> el NIV original viene grabado físicamente en el bastidor (chasis) del vehículo. En autos importados regularizados se verifica este número durante el trámite.",

                    "<strong>Tip de verificación:</strong> compará el NIV del parabrisas, de la puerta y de la factura. Los 3 deben ser idénticos. Si alguno difiere, hay alteración o el vehículo es producto de 'cortar y pegar' partes de varios autos. Ver <a href='/donde-esta-niv/'>guía completa de ubicación del NIV</a>."
                ]
            },
            {
                "heading": "Errores comunes al consultar por NIV",
                "body": [
                    "<strong>Confundir letras con números:</strong> el NIV no usa I, O ni Q. Si en el parabrisas ves lo que parece una I, es un 1; lo que parece una O es 0. Si seguís dudando, mirá la factura.",

                    "<strong>Faltar o sobrar caracteres:</strong> el NIV tiene exactamente 17 caracteres. Si escribís 16 o 18, el sistema te lo rechaza. Contá dos veces antes de buscar.",

                    "<strong>Espacios o guiones:</strong> el NIV se escribe todo junto. Sin espacios, guiones ni puntos.",

                    "<strong>Minúsculas:</strong> el portal acepta solo mayúsculas. Si pegás un NIV de un Excel o WhatsApp, fijate que esté todo en mayúsculas.",

                    "<strong>NIV truncado o ilegible en el parabrisas:</strong> en autos viejos o accidentados, la placa del parabrisas puede estar deteriorada. Verificá en la tarjeta de circulación o en la factura.",

                    "<strong>El sistema dice 'sin información' aunque el NIV es legítimo:</strong> puede ser que el vehículo sea muy nuevo (recién importado o recién comprado) y aún no esté indexado, o que sea un auto chocolate sin regularizar. En este último caso, hacelo regularizar antes de comprar. Ver <a href='/regularizacion-autos-chocolate/'>regularización</a>."
                ]
            },
            {
                "heading": "Qué información devuelve la consulta por NIV",
                "body": [
                    "Una consulta exitosa por NIV te devuelve datos completos del vehículo:",

                    "<strong>Identificación:</strong> NIV (los 17 caracteres), número de motor, número de serie, placa actual (si está vinculada).",

                    "<strong>Datos técnicos:</strong> marca, modelo, año, color, tipo de carrocería (sedán, SUV, pickup, motocicleta, camión), número de puertas, capacidad de pasajeros, cilindrada, número de cilindros.",

                    "<strong>Origen y fabricación:</strong> país de origen, planta de ensamble, fecha de fabricación.",

                    "<strong>Registro nacional:</strong> fecha de inscripción al REPUVE, entidad federativa de emplacado, fecha de expedición de placas actuales, último movimiento administrativo (cambio de propietario, baja, etc.).",

                    "<strong>Estatus legal (el dato más crítico):</strong> 'sin reporte', 'con reporte de robo' o 'recuperado'.",

                    "<strong>NCI:</strong> número de constancia de inscripción al REPUVE.",

                    "<strong>Datos que NO aparecen por privacidad:</strong> nombre del propietario actual, dirección registrada, historial de propietarios anteriores."
                ]
            }
        ],
        "faqs": [
            {"q": "¿Cuál es la diferencia entre NIV y VIN?", "a": "Ninguna técnica. <strong>NIV</strong> es el término en español ('Número de Identificación Vehicular') y <strong>VIN</strong> es la abreviatura en inglés ('Vehicle Identification Number'). Son exactamente lo mismo: el código único de 17 caracteres del vehículo."},
            {"q": "¿El NIV cambia si cambio el motor del auto?", "a": "No. El NIV identifica el chasis del vehículo, no el motor. Si cambias el motor, el NIV sigue siendo el mismo, pero deberías actualizar el número de motor en Control Vehicular para mantener la concordancia documental."},
            {"q": "¿Dónde encuentro el NIV en una motocicleta?", "a": "En motocicletas el NIV se ubica en el cuello del manillar (cerca del eje de dirección) o en el chasis cerca del motor. También en la tarjeta de circulación y factura. Ver <a href='/donde-esta-niv/'>guía completa</a>."},
            {"q": "¿Qué pasa si el NIV del auto está alterado o ilegible?", "a": "Es una <strong>señal de alarma grave</strong>. La alteración de NIV es delito federal. Si comprás un auto con NIV alterado, podrías quedar como cómplice. <strong>No compres y denuncia.</strong> Si el NIV está ilegible por deterioro natural (no alteración), debés acudir a perito de Control Vehicular para que dictamine."},
            {"q": "¿Sirve para consultar autos importados de Estados Unidos?", "a": "Sí, si están <strong>regularizados</strong> en México. Los autos chocolate sin regularizar no aparecen en REPUVE porque no están inscritos. Una vez regularizados ($2,500 MXN, ver <a href='/regularizacion-autos-chocolate/'>regularización</a>), figuran normalmente."},
            {"q": "¿Puedo conseguir el NIV de un auto sin verlo físicamente?", "a": "Solo si el vendedor te lo proporciona (por foto, WhatsApp, etc.) o aparece en la factura/tarjeta de circulación. Idealmente, antes de comprar, <strong>verificá el NIV físicamente</strong> en el parabrisas y la puerta del piloto al ver el vehículo."},
            {"q": "¿El consulado o aseguradora pueden hacer la consulta REPUVE por mí?", "a": "Sí, pero no es necesario porque la consulta ciudadana es 100% gratuita. Cualquier intermediario que te cobre por hacerla está cobrando por algo que vos podés hacer gratis en 2 minutos."},
            {"q": "¿Qué hago si la consulta por NIV no devuelve nada pero el auto es legal?", "a": "Posibles causas: (1) auto recién registrado, aún no indexado; (2) auto importado sin regularizar; (3) error en el NIV ingresado; (4) caída temporal del sistema. Reintentá en 30 minutos. Si persiste, llamá al 800 REPUVE 1 (800 737 8831) o acudí a una oficina REPUVE."}
        ]
    },
}

# Función helper para actualizar pages
def update_pages(data):
    updated = 0
    for page in data['pages_centrales']:
        slug = page['slug']
        if slug in EXPANDED_PAGES:
            new_data = EXPANDED_PAGES[slug]
            for key in ['h1', 'title', 'meta', 'category', 'status_chip', 'intro', 'sections', 'faqs']:
                if key in new_data:
                    page[key] = new_data[key]
            updated += 1
            words = sum(len(s.get('heading', '').split()) + sum(len(b.split()) for b in s.get('body', [])) for s in page.get('sections', []))
            print(f"  ✓ {slug}: {len(page.get('sections', []))} secciones, {len(page.get('faqs', []))} FAQs, ~{words} palabras de contenido")
    return updated

if __name__ == '__main__':
    data = json.loads(DATA.read_text())
    updated = update_pages(data)
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    print(f"\n✓ {updated}/{len(EXPANDED_PAGES)} páginas críticas expandidas. Pendientes: agendar-cita, requisitos, costos, regularizacion-autos-chocolate.")
    print(f"\nEjecutá ahora: python3 scripts/build-datos-js.py")
