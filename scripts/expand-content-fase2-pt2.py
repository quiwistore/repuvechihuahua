#!/usr/bin/env python3
"""FASE 2 - PARTE 2: Expande agendar-cita, requisitos, costos, regularizacion-autos-chocolate."""
import json
from pathlib import Path

DATA = Path('/Users/quiwistore/Downloads/repuve-chihuahua/data/repuve.json')

ESTADO = "Chihuahua"
CAPITAL = "Chihuahua"
TELEFONO_REPUVE = "800 737 8831"
TELEFONO_GOBIERNO = "614 429 3300"

EXPANDED_PAGES = {
    # ========================================================================
    # 4. AGENDAR CITA
    # ========================================================================
    "agendar-cita": {
        "h1": f"Agendar Cita REPUVE en {ESTADO}: Cómo Reservar Online en 2026",
        "title": f"Cita REPUVE {ESTADO} 2026 - Cómo Agendar Online en 5 Minutos",
        "meta": f"Cómo agendar tu cita REPUVE en {ESTADO} paso a paso. Plataforma oficial, requisitos, qué hacer si no hay cupo. Citas para regularización, inscripción y chip vehicular. Guía 2026.",
        "category": "Tramite",
        "status_chip": "Cita previa obligatoria · Online · Gratis",
        "intro": (
            f"Agendar una <strong>cita REPUVE en {ESTADO}</strong> es el paso obligatorio antes de acudir a cualquier oficina para hacer trámites "
            f"presenciales. Sin cita previa, no te atenderán. La plataforma oficial es <strong>regularizaauto.sspc.gob.mx</strong> "
            f"(para regularización de autos chocolate) y está disponible 24/7."
            f"<br><br>"
            f"En {ESTADO}, las citas se reservan principalmente para 3 tipos de trámites: <strong>regularización de autos chocolate</strong> "
            f"(el más demandado, especialmente en Ciudad Juárez por ser frontera), <strong>inscripción al REPUVE</strong> de vehículos nuevos "
            f"o usados, y <strong>instalación/reposición del chip REPUVE</strong>. Las consultas ciudadanas son online y no requieren cita."
            f"<br><br>"
            f"Las citas se llenan rápido — especialmente en módulos itinerantes — por lo que conviene agendar apenas se abra cada periodo."
        ),
        "sections": [
            {
                "heading": f"Plataforma oficial para agendar citas REPUVE en {ESTADO}",
                "body": [
                    f"Para <strong>regularización de autos chocolate</strong>, la plataforma oficial es <a href='https://regularizaauto.sspc.gob.mx' rel='noopener nofollow'>regularizaauto.sspc.gob.mx</a>, operada por la Secretaría de Seguridad y Protección Ciudadana (SSPC) del Gobierno Federal. Es donde generás tu línea de captura ($2,500 MXN) y agendás cita en el módulo de tu preferencia.",

                    f"Para <strong>inscripción al REPUVE de vehículos nuevos o usados</strong>, el proceso varía: si comprás auto nuevo en agencia, la propia agencia hace el alta. Si es usado y querés inscribirlo, podés acudir a la oficina REPUVE más cercana — en {ESTADO} tenemos 7 oficinas — o llamar al <a href='tel:{TELEFONO_REPUVE.replace(' ','')}'>{TELEFONO_REPUVE}</a> para coordinar.",

                    f"Para <strong>chip REPUVE</strong>, la instalación se hace en módulo. No siempre requiere cita previa formal (algunos módulos atienden por orden de llegada en horarios específicos), pero conviene llamar antes para confirmar.",

                    f"<strong>Tip importante:</strong> el portal del REPUVE oficial principal (<a href='https://www2.repuve.gob.mx:8443/ciudadania/'>www2.repuve.gob.mx:8443/ciudadania/</a>) es solo para CONSULTAS gratuitas, no para agendar citas presenciales. Para citas, usá regularizaauto.sspc.gob.mx o llamá a la línea nacional."
                ]
            },
            {
                "heading": "Cómo agendar tu cita paso a paso",
                "body": [
                    "<strong>1. Entrá a regularizaauto.sspc.gob.mx</strong> (para regularización) o llamá al 800 REPUVE 1 (para otros trámites). Si es regularización, creá tu cuenta con CURP, correo electrónico y teléfono.",

                    "<strong>2. Llenás el formulario con datos del vehículo:</strong> NIV (17 caracteres), marca, modelo, año, color, placas si tiene. Datos personales: nombre completo, CURP, ID oficial, comprobante de domicilio.",

                    "<strong>3. Generá la línea de captura</strong> ($2,500 MXN si es regularización; otros trámites pueden ser gratuitos). Te aparece una referencia bancaria.",

                    f"<strong>4. Pagá en banco autorizado:</strong> HSBC, Banamex, Banorte, BBVA, Santander, Scotiabank. Podés pagar en sucursal, app o transferencia. <strong>Conservá el comprobante de pago</strong> — lo necesitás el día de la cita.",

                    f"<strong>5. Elegí el módulo donde vas a acudir</strong>: en {ESTADO} podés elegir entre Chihuahua capital, Ciudad Juárez (varios módulos), Cuauhtémoc, Delicias, Parral, Nuevo Casas Grandes o Camargo. Cuidado: no todos los módulos están operativos todo el año (los itinerantes abren por temporadas).",

                    "<strong>6. Seleccioná fecha y hora.</strong> El sistema muestra solo los slots disponibles. <strong>Las citas se llenan rápido</strong>, especialmente en Ciudad Juárez.",

                    "<strong>7. Confirmá la cita.</strong> Recibís un correo con los detalles. <strong>Imprimí el comprobante</strong> o guardalo en tu celular — lo presentarás el día del trámite."
                ]
            },
            {
                "heading": "Documentos que llevar el día de la cita",
                "body": [
                    "<strong>Identificación oficial vigente</strong> del propietario: INE o pasaporte mexicano. Si sos extranjero residente, FM2/FM3 o tarjeta de residente.",

                    "<strong>CURP</strong> del propietario (impreso o digital del portal renapo.gob.mx).",

                    "<strong>Comprobante de domicilio</strong> reciente: recibo de luz, agua, gas, predial o teléfono fijo. No mayor a 3 meses.",

                    "<strong>Factura original del vehículo</strong>: para autos nacionales, factura del fabricante o de la agencia. Para autos importados regularizados, título original del país de origen (Title en autos de EE.UU.).",

                    "<strong>Tarjeta de circulación</strong> vigente (si el auto ya tenía placas).",

                    "<strong>Para regularización de autos chocolate</strong>: manifiesto firmado en tinta azul + 2 fotografías del vehículo (parabrisas con NIV visible y puerta del piloto).",

                    "<strong>Comprobante de pago bancario</strong> ($2,500 MXN para regularización) — el original sellado por el banco o la confirmación de transferencia.",

                    "<strong>Cita previa impresa o en celular</strong> — con el folio claramente visible.",

                    "<strong>El vehículo físicamente</strong> debes presentarlo. Si llegas sin auto el módulo te rechaza el trámite."
                ]
            },
            {
                "heading": "Qué hacer si no hay cupo disponible en tu ciudad",
                "body": [
                    f"Las citas en Chihuahua, especialmente en Ciudad Juárez, se llenan rápido por el alto volumen de regularización de autos chocolate. Si no encontrás cupo, hay varias opciones:",

                    f"<strong>1. Revisá otros módulos del estado.</strong> Si vivís en Ciudad Juárez pero podés desplazarte 200 km, en Cuauhtémoc o Chihuahua capital suele haber más disponibilidad. Ver <a href='/oficinas/'>oficinas REPUVE en {ESTADO}</a>.",

                    "<strong>2. Esperá a que liberen cupos por cancelaciones.</strong> El sistema libera cupos cuando alguien cancela. Refrescá la página varias veces al día — especialmente lunes por la mañana y viernes a la tarde.",

                    "<strong>3. Esperá apertura de nuevo periodo.</strong> Los módulos itinerantes abren periodos de 2-4 semanas y luego cierran. Cuando se abre uno nuevo, los cupos se liberan masivamente — estate atento al sitio oficial.",

                    "<strong>4. Considerá un módulo itinerante en municipio cercano.</strong> En temporadas de alta demanda, el gobierno federal abre módulos temporales en otros municipios para descongestionar. Verificá el calendario oficial.",

                    f"<strong>5. Llamá al <a href='tel:{TELEFONO_REPUVE.replace(' ','')}'>{TELEFONO_REPUVE}</a></strong> para preguntar por opciones extraordinarias."
                ]
            },
            {
                "heading": "Cancelar o reagendar una cita REPUVE",
                "body": [
                    "Si no podés acudir a tu cita confirmada, <strong>cancelala con anticipación</strong>. No solo evitás 'quemar' tu lugar (que podría ser ocupado por otra persona que lo necesita), sino que también evitás que el sistema te marque como 'no show' (lo cual puede dificultar futuras citas).",

                    "<strong>Cancelar cita de regularización:</strong> ingresá a regularizaauto.sspc.gob.mx con tu cuenta, andá a 'Mis citas' y elegí 'Cancelar'. El sistema te confirma la cancelación. Tu línea de captura sigue vigente (no perdés el pago), podés reagendar con la misma referencia.",

                    "<strong>Reagendar cita:</strong> después de cancelar, podés reagendar inmediatamente eligiendo nueva fecha. Si no hay cupo en el módulo original, probá en otros municipios. Ver <a href='/cancelar-cita/'>cómo cancelar paso a paso</a>.",

                    "<strong>Si no se cancela y faltás:</strong> el sistema te marca como 'no show'. Algunos módulos restringen tu capacidad de agendar nuevas citas por un periodo (típicamente 30-60 días).",

                    "<strong>Si el módulo cierra antes de tu cita:</strong> algunas veces el gobierno cierra módulos itinerantes antes de la fecha programada. En ese caso, te notifican por correo y te ofrecen reagendar en otro módulo automáticamente."
                ]
            }
        ],
        "faqs": [
            {"q": f"¿Necesito cita para hacer la consulta ciudadana REPUVE en {ESTADO}?", "a": "No. Las consultas (verificar placa o NIV) son 100% en línea y gratuitas, sin cita previa. Solo las trámites presenciales (regularización, chip, inscripción) requieren cita."},
            {"q": "¿Puedo agendar cita para otra persona (familiar, amigo)?", "a": "Sí, pero el día de la cita debe asistir la persona titular con su identificación oficial. La cita está vinculada al CURP del propietario del vehículo, no al de quien la agendó."},
            {"q": "¿Cuánto tiempo dura el trámite presencial el día de la cita?", "a": "Entre 1 y 2 horas si el módulo está poco saturado. En Cd. Juárez en horarios pico puede ser 3-4 horas. <strong>Llegá con 30 minutos de anticipación.</strong>"},
            {"q": "¿Qué pasa si llego tarde a mi cita?", "a": "Tolerancia típica: 15-30 minutos. Si llegás después, el módulo puede rechazarte y deberías reagendar. Llamá al módulo antes si vas tarde."},
            {"q": f"¿Es gratis agendar la cita en {ESTADO}?", "a": f"<strong>Agendar la cita es gratis</strong>. El costo va por el trámite específico: regularización $2,500 MXN, inscripción/chip generalmente sin costo. Pago es a través de línea de captura bancaria."},
            {"q": "¿Puedo cambiar de módulo después de agendar?", "a": "Sí. Andá a 'Mis citas' en la plataforma, cancelá la cita original y agendá nueva en el módulo de tu preferencia. Tu pago se mantiene vigente con la misma línea de captura."},
            {"q": "¿Atienden citas los fines de semana?", "a": "Algunos módulos sí, otros no. En Chihuahua capital, sábados de 8:00 a 13:00 (variable). Ciudad Juárez tiene módulos abiertos sábado. Confirmá horario al agendar — el sistema solo muestra slots disponibles."},
            {"q": "¿Puedo agendar para alguien que vive en otro estado pero el auto se va a regularizar en Chihuahua?", "a": "Sí. El propietario puede ser de cualquier estado, lo importante es que asista a la cita en el módulo elegido en Chihuahua. La residencia del propietario no limita en qué módulo regularizar."}
        ]
    },

    # ========================================================================
    # 5. REQUISITOS
    # ========================================================================
    "requisitos": {
        "h1": f"Requisitos REPUVE {ESTADO} 2026: Documentos para Cada Trámite",
        "title": f"Requisitos REPUVE {ESTADO} 2026 - Documentos Necesarios por Trámite",
        "meta": f"Documentos requeridos para trámites REPUVE en {ESTADO} 2026: regularización, inscripción, cambio propietario, baja vehicular. Listas completas + tips para no perder el viaje. Guía oficial.",
        "category": "Tramite",
        "status_chip": "Lista verificada 2026 · Por trámite",
        "intro": (
            f"Saber exactamente <strong>qué documentos llevar al módulo REPUVE en {ESTADO}</strong> es la diferencia entre completar tu trámite en 1 hora "
            f"o perder un día entero. Cada trámite tiene requisitos específicos, y la mayoría exige documentación original "
            f"(no fotocopias). Si te falta uno solo, el módulo te rechaza y tenés que reagendar — perdiendo tu lugar."
            f"<br><br>"
            f"En esta guía actualizada a 2026 te detallamos los requisitos para los <strong>6 trámites más comunes</strong> en {ESTADO}: "
            f"regularización de autos chocolate, inscripción al REPUVE, cambio de propietario, alta de placas, baja vehicular y reposición de chip. "
            f"Compará tu carpeta con esta lista antes de salir de tu casa."
        ),
        "sections": [
            {
                "heading": "Requisitos para regularización de autos chocolate",
                "body": [
                    "El trámite más solicitado en Chihuahua por ser estado fronterizo. Aplica solo para vehículos importados al país <strong>antes del 19 de octubre de 2021</strong>.",

                    "<strong>Documentos del propietario:</strong>",
                    "&bull; Identificación oficial vigente (INE, pasaporte o cédula profesional).",
                    "&bull; CURP impreso (del portal renapo.gob.mx).",
                    "&bull; Comprobante de domicilio reciente (luz, agua, gas, predial), no mayor a 3 meses.",
                    "&bull; Correo electrónico activo y teléfono.",

                    "<strong>Documentos del vehículo:</strong>",
                    "&bull; Título original del país de origen (Title de EE.UU.).",
                    "&bull; Manifiesto firmado en tinta azul (formato disponible en el portal regularizaauto.sspc.gob.mx).",
                    "&bull; 2 fotografías del vehículo: una del parabrisas con NIV visible, otra de la puerta del piloto.",
                    "&bull; Pedimento de internación temporal (si lo tenés).",

                    "<strong>Pago:</strong>",
                    "&bull; Línea de captura por <strong>$2,500 MXN</strong>, pagada en banco autorizado.",
                    "&bull; Comprobante bancario original con sello del banco o confirmación de transferencia.",

                    "<strong>Cita previa:</strong> obligatoria en regularizaauto.sspc.gob.mx con el folio impreso o en celular.",

                    "Ver <a href='/regularizacion-autos-chocolate/'>guía completa de regularización</a>."
                ]
            },
            {
                "heading": "Requisitos para inscripción al REPUVE (vehículos nuevos o usados)",
                "body": [
                    "Si comprás un auto nuevo en agencia, la agencia hace la inscripción automáticamente. Si es usado o querés re-inscribirlo, llevá:",

                    "<strong>Del propietario:</strong> INE vigente, CURP, comprobante de domicilio reciente.",

                    "<strong>Del vehículo:</strong> factura original (con endoso si fue traspasada), tarjeta de circulación vigente (si tiene), pedimento de importación (si es vehículo importado regularizado).",

                    "<strong>Pago:</strong> generalmente gratuito. Si hay costo administrativo es menor a $200 MXN.",

                    "<strong>El vehículo físicamente</strong> — el módulo verifica el NIV grabado en el chasis.",

                    "<strong>Tip:</strong> verificá que el NIV de la factura coincida con el grabado en el parabrisas y la puerta antes de acudir. Si no coincide, el módulo rechaza el trámite y deberías investigar la procedencia del vehículo."
                ]
            },
            {
                "heading": "Requisitos para cambio de propietario",
                "body": [
                    "Trámite obligatorio dentro de los 30 días posteriores a una compraventa de auto usado en Chihuahua.",

                    "<strong>Documentos del comprador (nuevo propietario):</strong>",
                    "&bull; INE vigente.",
                    "&bull; CURP.",
                    "&bull; Comprobante de domicilio reciente en Chihuahua.",

                    "<strong>Documentos del vendedor:</strong>",
                    "&bull; INE vigente (puede ir con el comprador o entregar copia certificada).",
                    "&bull; Firma en el endoso de la factura.",

                    "<strong>Documentos del vehículo:</strong>",
                    "&bull; <strong>Factura original con endoso completo</strong> (nombre del comprador, fecha, firma del vendedor en el reverso).",
                    "&bull; Tarjeta de circulación vigente.",
                    "&bull; Constancia REPUVE (gratis online).",
                    "&bull; Refrendo vehicular al corriente (sin adeudos).",
                    "&bull; Pago de derechos de cambio de propietario ($1,500-$2,200 MXN según modelo).",

                    "Ver <a href='/cambio-propietario/'>guía completa de cambio de propietario</a>."
                ]
            },
            {
                "heading": "Requisitos para alta de placas (vehículo nuevo)",
                "body": [
                    "Cuando comprás auto nuevo en agencia, los requisitos para emplacar en Chihuahua son:",

                    "<strong>Factura original</strong> del vehículo (de la agencia o fabricante).",

                    "<strong>Identificación oficial</strong> vigente del propietario.",

                    "<strong>CURP</strong> y <strong>comprobante de domicilio</strong> en Chihuahua.",

                    "<strong>Constancia de inscripción al REPUVE</strong> (gratuita, online).",

                    "<strong>Pago de derechos</strong>: aproximadamente $1,800 a $2,500 MXN dependiendo del modelo, año y tipo de vehículo.",

                    "<strong>Verificación vehicular vigente</strong> (si aplica para vehículos comerciales).",

                    "<strong>El vehículo físicamente</strong> en la oficina de Control Vehicular del estado."
                ]
            },
            {
                "heading": "Requisitos para baja vehicular",
                "body": [
                    "Cuando vas a dar de baja un auto por robo, siniestro total, exportación o desuso:",

                    "<strong>Documento causal:</strong> según el motivo: denuncia ministerial (robo), constancia de siniestro total de la aseguradora, pedimento de exportación, etc.",

                    "<strong>Tarjeta de circulación original</strong> (excepto en caso de robo, donde la denuncia sustituye).",

                    "<strong>Placas físicas</strong> (excepto en robo).",

                    "<strong>Factura original</strong>.",

                    "<strong>INE</strong> y <strong>CURP</strong> del propietario.",

                    "<strong>Comprobante de domicilio</strong>.",

                    "<strong>Refrendo y multas al corriente</strong>: si hay adeudos, deben pagarse antes de la baja.",

                    "<strong>Pago de derechos de baja</strong>: $250-$400 MXN aproximadamente.",

                    "Ver <a href='/baja-vehicular/'>guía completa</a>."
                ]
            },
            {
                "heading": "Requisitos para chip REPUVE",
                "body": [
                    "El chip REPUVE es gratuito y se instala en módulo. Requisitos:",

                    "<strong>Constancia de inscripción al REPUVE</strong> (si el auto no está inscrito, primero hacé la <a href='/inscribir-vehiculo/'>inscripción</a>).",

                    "<strong>Tarjeta de circulación vigente</strong>.",

                    "<strong>Identificación oficial</strong> del propietario.",

                    "<strong>El vehículo físicamente</strong>.",

                    "<strong>Para reposición</strong> (chip dañado o cambio de parabrisas): mismos requisitos + evidencia del daño (fotografía o el chip dañado).",

                    "Ver <a href='/chip-repuve/'>guía completa del chip REPUVE</a>."
                ]
            }
        ],
        "faqs": [
            {"q": "¿Aceptan fotocopias en lugar de originales?", "a": "<strong>No.</strong> El módulo siempre exige documentos originales. Las copias se sacan en el módulo si las necesitan archivar. Lleva originales + 2 juegos de copias por las dudas."},
            {"q": "¿El comprobante de domicilio puede estar a nombre de un familiar?", "a": "Sí, pero deberías llevar también <strong>una declaración de domicilio firmada por el titular</strong> del recibo (carta simple manuscrita) y copia de su INE. Si estás casado, el comprobante a nombre del cónyuge es aceptado sin más."},
            {"q": "¿Qué hago si perdí la factura del vehículo?", "a": "Necesitás hacer <strong>reposición de factura</strong> antes de hacer cualquier trámite REPUVE. Se hace ante la agencia/fabricante donde se compró originalmente, o si fue importado, ante el agente aduanal. Es un trámite separado y puede tomar 4-8 semanas."},
            {"q": "¿Qué pasa si llego al módulo sin uno de los documentos requeridos?", "a": "El módulo te rechaza el trámite. <strong>No hay flexibilidad</strong>: debés reagendar cita y volver con todo completo. Por eso es vital revisar la lista antes de salir de casa."},
            {"q": "¿Necesito CURP del cónyuge o solo del propietario titular?", "a": "Solo del propietario que figurará en los documentos. Si la factura quedará a tu nombre, llevás solo tu CURP."},
            {"q": "¿Los extranjeros residentes pueden hacer trámites REPUVE?", "a": "Sí, con su <strong>tarjeta de residencia vigente</strong> (FM2/FM3 o tarjeta verde) en lugar del INE. Los demás requisitos son los mismos."},
            {"q": "¿El comprobante de domicilio puede ser digital o necesita ser impreso?", "a": "Impreso. Si tu recibo de luz/agua te llega solo por correo, descargalo del portal de la empresa, imprimilo y llevalo. El módulo necesita papel."},
            {"q": "¿Cuánto tiempo de vigencia tienen los documentos?", "a": "<strong>Identificación oficial:</strong> vigente al momento del trámite. <strong>Comprobante de domicilio:</strong> no mayor a 3 meses. <strong>Constancia REPUVE:</strong> sin caducidad pero verificá que esté actualizada. <strong>Verificación vehicular (si aplica):</strong> vigente al momento del trámite."}
        ]
    },

    # ========================================================================
    # 6. COSTOS
    # ========================================================================
    "costos": {
        "h1": f"Costos REPUVE {ESTADO} 2026: Precios Actualizados por Trámite",
        "title": f"Costos REPUVE {ESTADO} 2026 - Precios Trámites Vehiculares Actualizados",
        "meta": f"Costos actualizados de trámites REPUVE en {ESTADO} 2026: regularización $2,500 MXN, cambio propietario, alta placas, baja, chip. Tabla completa de precios + dónde pagar.",
        "category": "Tramite",
        "status_chip": "Tabla 2026 · Pagos bancarios",
        "intro": (
            f"Saber <strong>cuánto cuesta cada trámite vehicular en {ESTADO}</strong> te permite presupuestar correctamente antes de iniciar. "
            f"Algunos trámites del REPUVE son <strong>completamente gratuitos</strong> (consulta ciudadana, chip RFID, instalación), "
            f"mientras que otros tienen costos que van desde $250 MXN (baja vehicular) hasta $2,500 MXN (regularización de autos chocolate)."
            f"<br><br>"
            f"<strong>Cuidado con cobros no oficiales:</strong> si alguien te cobra por hacer la consulta ciudadana, agendar cita o instalar el chip "
            f"REPUVE, está cometiendo fraude. Solo los trámites de Control Vehicular del Estado de {ESTADO} y la regularización federal "
            f"tienen costos legítimos."
        ),
        "sections": [
            {
                "heading": "Tabla resumen de costos REPUVE 2026",
                "body": [
                    "<strong>Trámites gratuitos:</strong>",
                    "&bull; Consulta ciudadana REPUVE (por placa, NIV o folio): <strong>$0 MXN</strong>",
                    "&bull; Agendar cita en plataforma oficial: <strong>$0 MXN</strong>",
                    "&bull; Instalación del chip REPUVE: <strong>$0 MXN</strong>",
                    "&bull; Constancia de inscripción REPUVE (digital): <strong>$0 MXN</strong>",

                    "<strong>Trámites con costo (federal):</strong>",
                    "&bull; Regularización de auto chocolate: <strong>$2,500 MXN</strong>",
                    "&bull; Regularización de motocicleta chocolate: <strong>$2,500 MXN</strong>",

                    "<strong>Trámites con costo (estatal Chihuahua):</strong>",
                    "&bull; Alta de placas nuevas: <strong>$1,800-$2,500 MXN</strong>",
                    "&bull; Reposición de placa (una): <strong>$450 MXN</strong>",
                    "&bull; Reposición de juego de placas: <strong>$850 MXN</strong>",
                    "&bull; Cambio de propietario: <strong>$1,500-$2,200 MXN</strong>",
                    "&bull; Reposición de tarjeta de circulación: <strong>$250-$400 MXN</strong>",
                    "&bull; Baja vehicular: <strong>$250-$400 MXN</strong>",
                    "&bull; Refrendo anual: variable según valor del vehículo (~$500-$1,500 MXN)",

                    "<strong>Otros costos relacionados:</strong>",
                    "&bull; Verificación vehicular (solo comerciales): <strong>$200-$600 MXN</strong>",
                    "&bull; Tenencia vehicular: variable según modelo y año (Chihuahua actualmente la subsidia para autos particulares modelo ≤8 años).",

                    "<strong>Importante:</strong> los precios pueden tener pequeñas variaciones por municipio (Cd. Juárez vs Chihuahua capital). Confirmá el monto exacto al generar tu línea de captura."
                ]
            },
            {
                "heading": "Detalle: regularización de autos chocolate",
                "body": [
                    "El trámite federal más caro pero también el más demandado en Chihuahua frontera. <strong>Costo único: $2,500 MXN</strong>.",

                    "<strong>Qué incluye:</strong> inscripción al REPUVE, asignación de NCI (Número de Constancia de Inscripción), instalación de chip RFID, regularización legal del vehículo en el padrón nacional.",

                    "<strong>Qué NO incluye:</strong> el alta de placas en Control Vehicular del estado (eso es un trámite estatal posterior, ~$1,800-$2,500 MXN adicionales), ni la tenencia/refrendo del estado.",

                    "<strong>Cómo pagar:</strong>",
                    "&bull; <strong>1.</strong> Generá la línea de captura en regularizaauto.sspc.gob.mx con tu CURP y datos del vehículo.",
                    "&bull; <strong>2.</strong> El sistema te devuelve una referencia bancaria.",
                    "&bull; <strong>3.</strong> Pagás en banco autorizado: HSBC, Banamex, Banorte, BBVA, Santander, Scotiabank.",
                    "&bull; <strong>4.</strong> Podés pagar en sucursal, app móvil, transferencia SPEI o ventanilla.",

                    "<strong>Tip:</strong> conservá el comprobante con sello del banco. Algunos módulos no aceptan comprobantes de app sin sello físico — confirmá antes."
                ]
            },
            {
                "heading": "Detalle: costos de alta y reposición de placas en Chihuahua",
                "body": [
                    "<strong>Alta de placas nuevas (vehículo nuevo o usado primer empadrón en Chihuahua):</strong>",
                    "&bull; Auto particular nuevo: <strong>$1,800-$2,200 MXN</strong>",
                    "&bull; Auto particular usado: <strong>$2,000-$2,500 MXN</strong>",
                    "&bull; Motocicleta: <strong>$800-$1,200 MXN</strong>",
                    "&bull; Servicio público (taxi, transporte): variable, más caro.",

                    "<strong>Reposición por daño/pérdida:</strong>",
                    "&bull; Una placa: <strong>$450 MXN</strong>",
                    "&bull; Juego de placas: <strong>$850 MXN</strong>",
                    "&bull; Tarjeta de circulación: <strong>$250-$400 MXN</strong>",

                    "<strong>Refrendo anual:</strong> variable según valor catastral del vehículo. Para un auto modelo 2020 valor $200,000 MXN, refrendo típico es $700-$900 MXN/año.",

                    "<strong>Multas por refrendo atrasado:</strong> 5% mensual sobre el monto pendiente. Si pasaste 3 meses sin pagar, ya tenés 15% extra.",

                    f"<strong>Dónde pagar:</strong> Recaudación de Rentas del Estado de Chihuahua, oficinas físicas o portal en línea <a href='https://www.chihuahua.gob.mx' rel='noopener nofollow'>chihuahua.gob.mx</a>. Métodos: SPEI, tarjeta de débito/crédito, OXXO, transferencia."
                ]
            },
            {
                "heading": "Cómo pagar tus trámites: métodos aceptados",
                "body": [
                    "<strong>Pago en banco (más común):</strong> el portal oficial te genera una línea de captura con código de barras. Llevás esa línea (impresa o en celular) a una sucursal bancaria autorizada. HSBC, Banamex, Banorte, BBVA, Santander, Scotiabank son los principales.",

                    "<strong>Pago en línea (SPEI/transferencia):</strong> desde tu app bancaria, ingresá la línea de captura como referencia y hacés transferencia interbancaria. Inmediato.",

                    "<strong>Pago en convenio (OXXO, 7-Eleven):</strong> algunos trámites estatales se pueden pagar en tiendas de conveniencia. Verificá si tu línea de captura es compatible.",

                    "<strong>Tarjeta de crédito/débito en oficina:</strong> en Recaudación de Rentas Chihuahua aceptan tarjetas. En módulos federales (REPUVE) generalmente solo pago previo bancario.",

                    f"<strong>NUNCA pagues en efectivo a un 'gestor' que diga ser del REPUVE.</strong> El REPUVE oficial NO cobra en efectivo, nunca. Si alguien te pide dinero directo para 'agilizar' un trámite, es fraude. Llamá al <a href='tel:{TELEFONO_REPUVE.replace(' ','')}'>{TELEFONO_REPUVE}</a> para denunciar."
                ]
            },
            {
                "heading": "Costos ocultos a tener en cuenta",
                "body": [
                    "<strong>Comisiones bancarias:</strong> algunos bancos cobran $20-$50 MXN por gestionar el pago de línea de captura. Banamex y BBVA suelen no cobrar.",

                    "<strong>Adeudos previos al cambio de propietario:</strong> si el vendedor te traspasa un auto con multas o refrendos atrasados, vos los heredás al hacer el cambio. <strong>Antes de comprar, exigí al vendedor que pague todo lo pendiente.</strong>",

                    "<strong>Diferencia entre municipios:</strong> Cd. Juárez puede tener pequeñas variaciones de precios respecto a Chihuahua capital. Generalmente diferencias de $50-$200 MXN.",

                    "<strong>Refrendo prorrateado al cambiar de propietario:</strong> si el vendedor ya pagó el refrendo del año en curso, generalmente el comprador no paga nuevamente — pero confirmá esto al hacer el trámite.",

                    "<strong>Servicios de gestor (opcionales):</strong> si contratás un gestor para hacer el trámite por vos, costará entre $500 y $2,000 MXN adicionales según complejidad. <strong>No es obligatorio</strong> contratar gestor — el trámite lo podés hacer vos."
                ]
            }
        ],
        "faqs": [
            {"q": "¿Por qué algunos sitios cobran por la consulta REPUVE si es gratis?", "a": "Es fraude. La consulta ciudadana del REPUVE es 100% gratuita en el portal oficial. Los sitios que cobran están aprovechándose de gente que no sabe dónde acceder al servicio oficial. Denuncia esos sitios al 800 REPUVE 1."},
            {"q": "¿El costo de $2,500 de regularización es por vehículo o por persona?", "a": "Por vehículo. Si querés regularizar 2 autos, pagás $5,000 MXN en total. Cada vehículo genera su propia línea de captura."},
            {"q": "¿Puedo pagar el refrendo y multas con tarjeta de crédito?", "a": "Sí, en Recaudación de Rentas Chihuahua aceptan tarjeta. También por el portal en línea chihuahua.gob.mx con métodos de pago electrónico."},
            {"q": "¿Hay descuentos por pago anticipado del refrendo?", "a": "Sí, en Chihuahua hay descuentos por pago anticipado del refrendo durante los primeros meses del año (enero-marzo típicamente). Verificá en el portal oficial del estado el calendario y porcentaje de descuento vigente."},
            {"q": "¿El costo de cambio de propietario incluye placas nuevas?", "a": "Depende. En algunos casos se mantienen las placas (más barato), en otros se cambian (más caro, ~$2,200 MXN). El sistema determina automáticamente cuál aplica según la antigüedad de las placas."},
            {"q": "¿Cuánto cuesta hacer todo el trámite completo si compré un auto chocolate y quiero emplacarlo?", "a": "Aproximadamente: <strong>$2,500 (regularización federal) + $2,000 (alta de placas Chihuahua) + $700 (refrendo año actual) = ~$5,200 MXN</strong>. Más cualquier multa pendiente del estado de origen del vehículo."},
            {"q": "¿Las motos tienen el mismo costo de regularización que los autos?", "a": "Sí, el costo de regularización federal es $2,500 MXN para ambos. El costo estatal de placas para motos es más bajo (~$800-$1,200 MXN)."},
            {"q": "¿Puedo deducir los gastos REPUVE en mi declaración fiscal?", "a": "Solo si es un vehículo registrado a tu nombre con fines comerciales (empresa, taxi, repartos). Para autos particulares de uso personal no son deducibles. Consultá con tu contador."}
        ]
    },

    # ========================================================================
    # 7. REGULARIZACION AUTOS CHOCOLATE (TOP keyword Chihuahua)
    # ========================================================================
    "regularizacion-autos-chocolate": {
        "h1": f"Regularización de Autos Chocolate en {ESTADO} 2026: Guía Completa Paso a Paso",
        "title": f"Regularización Autos Chocolate {ESTADO} 2026 - $2,500 MXN Paso a Paso",
        "meta": f"Cómo regularizar tu auto chocolate en {ESTADO} 2026: requisitos, costo $2,500 MXN, módulos en Ciudad Juárez, Chihuahua, Cuauhtémoc. Guía completa del Decreto Federal.",
        "category": "Tramite",
        "status_chip": "$2,500 MXN · Trámite federal · Cita previa",
        "intro": (
            f"La <strong>regularización de autos chocolate en {ESTADO}</strong> es el trámite más demandado del estado, especialmente en Ciudad Juárez por su condición fronteriza con El Paso, Texas. "
            f"Si tenés un vehículo de procedencia extranjera ingresado al país <strong>antes del 19 de octubre de 2021</strong>, podés legalizarlo de forma federal pagando "
            f"<strong>$2,500 MXN</strong> en los módulos REPUVE habilitados en {ESTADO}."
            f"<br><br>"
            f"El Decreto de Regularización fue publicado por el Gobierno Federal y es operado por la Secretaría de Seguridad y Protección Ciudadana (SSPC). "
            f"Te da <strong>seguridad jurídica</strong>, permite emplacar legalmente en {ESTADO}, evita decomisos en retenes y te permite circular en todo el país sin riesgo legal."
            f"<br><br>"
            f"En esta guía completa te explicamos desde cero: qué es un auto chocolate, si tu vehículo califica, qué documentos necesitás, cómo pagar, dónde acudir y cómo emplacar después."
        ),
        "sections": [
            {
                "heading": f"Qué es un auto chocolate y por qué regularizarlo en {ESTADO}",
                "body": [
                    "Un <strong>auto chocolate</strong> es un vehículo de procedencia extranjera (la mayoría de Estados Unidos) que circula en México sin haber sido legalmente importado. No está registrado en el padrón vehicular nacional, no tiene placas mexicanas oficiales, y técnicamente está en una situación irregular.",

                    "En Chihuahua, por la cercanía con la frontera (El Paso, Las Cruces, Albuquerque), <strong>se estima que hay más de 200,000 autos chocolate</strong>. La mayoría están en Ciudad Juárez (1.5M habitantes) y zonas aledañas, donde el cruce fronterizo es habitual.",

                    "<strong>Por qué regularizar:</strong>",

                    "&bull; <strong>Seguridad jurídica:</strong> tenés certeza legal sobre la propiedad del vehículo. Antes de regularizar, si tu auto es robado o accidentado, no podés reclamar legalmente porque 'no existe' en el padrón.",

                    "&bull; <strong>Posibilidad de emplacar:</strong> sin regularización no podés conseguir placas mexicanas legales. Con regularización, podés emplacar en Chihuahua y circular legalmente.",

                    "&bull; <strong>Evitar decomisos:</strong> los retenes federales (Guardia Nacional, INE) y estatales pueden decomisarte el auto si circula irregular. Una vez regularizado, ya no te pueden detener por ese motivo.",

                    "&bull; <strong>Tránsito libre por todo el país:</strong> hoy muchos autos chocolate solo pueden circular cerca de la frontera (zona libre). Regularizados, podés ir a cualquier punto de México.",

                    "&bull; <strong>Acceso a seguros:</strong> las aseguradoras solo aseguran vehículos legales. Sin regularización no tenés cobertura amplia."
                ]
            },
            {
                "heading": "¿Tu auto califica? Requisitos de elegibilidad",
                "body": [
                    "El Decreto de Regularización tiene <strong>condiciones específicas de elegibilidad</strong>. No todos los autos importados pueden regularizarse bajo este programa.",

                    "<strong>1. Fecha de ingreso al país:</strong> el vehículo debe haber ingresado a México <strong>antes del 19 de octubre de 2021</strong>. Vehículos posteriores a esa fecha NO califican y deberían pasar por importación definitiva regular con agente aduanal (proceso mucho más caro, $50,000-$150,000 MXN).",

                    "<strong>2. Tipo de vehículo:</strong> califican autos particulares, motocicletas y pickups de uso particular. Vehículos pesados, autobuses y maquinaria especial tienen otros procesos.",

                    "<strong>3. Año modelo:</strong> sin restricción de año modelo bajo el Decreto vigente. Aplica para autos de cualquier antigüedad.",

                    "<strong>4. Estado físico:</strong> el vehículo debe estar operativo y presentarse físicamente al módulo. Autos en pérdida total o desarmados no califican.",

                    "<strong>5. NIV legible:</strong> el NIV de 17 caracteres debe estar legible en el parabrisas, puerta del piloto y chasis. Si está alterado o ilegible, deberías acudir a perito primero.",

                    "<strong>6. Sin reporte de robo:</strong> si el vehículo tiene reporte de robo en EE.UU. o México, no se puede regularizar. Antes de iniciar, verificá en el sitio de Carfax o equivalente que esté limpio.",

                    "<strong>7. Propietario residente en México:</strong> el propietario debe acreditar residencia legal en México (INE para mexicanos, tarjeta de residencia para extranjeros)."
                ]
            },
            {
                "heading": "Requisitos completos: qué documentos necesitás",
                "body": [
                    "<strong>Documentos del propietario:</strong>",
                    "&bull; CURP impreso del portal renapo.gob.mx.",
                    "&bull; Identificación oficial vigente: INE para mexicanos, FM2/FM3/tarjeta de residencia para extranjeros.",
                    "&bull; Comprobante de domicilio reciente (no mayor a 3 meses): luz, agua, gas, predial, teléfono.",
                    "&bull; Correo electrónico activo y teléfono celular.",

                    "<strong>Documentos del vehículo:</strong>",
                    "&bull; <strong>Título original del país de origen</strong> (Title de EE.UU.). Debe estar a nombre del propietario o tener endoso firmado.",
                    "&bull; <strong>Manifiesto firmado en tinta azul</strong>: formato oficial disponible en regularizaauto.sspc.gob.mx. Imprimilo, llenalo a mano con tinta azul (no negra) y firmalo.",
                    "&bull; <strong>2 fotografías</strong> a color, una del vidrio frontal con NIV visible (incluir matrícula provisoria si tiene) y otra de la puerta del piloto.",

                    "<strong>Pago:</strong>",
                    "&bull; Línea de captura por <strong>$2,500 MXN</strong>.",
                    "&bull; Pagada en banco autorizado (HSBC, Banamex, Banorte, BBVA, Santander, Scotiabank).",
                    "&bull; Comprobante bancario con sello físico o confirmación de transferencia.",

                    "<strong>Cita previa:</strong>",
                    "&bull; Obligatoria, generada en regularizaauto.sspc.gob.mx.",
                    "&bull; Imprimí el comprobante o tenelo en el celular.",

                    "<strong>Vehículo físicamente:</strong> presentarlo el día de la cita en el módulo seleccionado. Sin auto, no hay trámite."
                ]
            },
            {
                "heading": "Módulos REPUVE para regularización en Chihuahua",
                "body": [
                    f"En {ESTADO} hay módulos de regularización en las principales ciudades. Disponibilidad varía según el calendario federal:",

                    "<strong>Chihuahua capital:</strong> Av. Deportiva Sur 8403, Ávalos, CP 31074. Lunes a viernes de 8:00 a 15:00. Es el módulo permanente principal. <a href='/oficinas/chihuahua-capital/'>Ver detalles</a>.",

                    "<strong>Ciudad Juárez:</strong> el módulo de mayor demanda. Varios sub-módulos itinerantes (El Punto, presidencia municipal, Modulo Mitla, Zaragoza, Pronaf). Horarios variables. <a href='/oficinas/ciudad-juarez/'>Ver detalles</a>.",

                    "<strong>Cuauhtémoc, Delicias, Hidalgo del Parral, Nuevo Casas Grandes, Camargo:</strong> módulos itinerantes que abren por periodos de 2-4 semanas. Verificá calendario en regularizaauto.sspc.gob.mx.",

                    "<strong>Tip:</strong> en Ciudad Juárez los cupos se agotan en días. En módulos itinerantes de municipios chicos hay más disponibilidad. Si podés desplazarte 100-200 km, te ahorra semanas de espera."
                ]
            },
            {
                "heading": "Proceso paso a paso: del registro al emplacado",
                "body": [
                    "<strong>1. Verificá elegibilidad (10 min):</strong> confirmá que tu auto ingresó al país antes del 19 oct 2021 y tiene Title original.",

                    "<strong>2. Creá cuenta en la plataforma (15 min):</strong> entrá a regularizaauto.sspc.gob.mx y registrate con CURP, correo, teléfono.",

                    "<strong>3. Llená el formulario (30 min):</strong> datos personales completos + datos del vehículo (NIV de 17 chars, marca, modelo, año, color, datos del motor).",

                    "<strong>4. Generá línea de captura (5 min):</strong> el sistema te devuelve una referencia bancaria de $2,500 MXN.",

                    "<strong>5. Pagá en banco (mismo día):</strong> presencial o por app. Guardá el comprobante.",

                    "<strong>6. Agendá cita (10 min):</strong> elegí el módulo (Cd. Juárez, Chihuahua capital, etc.) y fecha disponible. Imprimí el comprobante.",

                    "<strong>7. Preparate para la cita:</strong> imprimí manifiesto, sacá las 2 fotos del vehículo, reuní todos los documentos en una carpeta.",

                    "<strong>8. Día de la cita (1-3 horas):</strong> llegá 30 min antes con el vehículo. Personal del REPUVE: verifica documentos → inspecciona el vehículo (NIV físico) → cobra (si no pagaste antes) → instala chip → entrega constancia de inscripción.",

                    "<strong>9. Después de la regularización: emplacar en Chihuahua (1-2 semanas):</strong> con la constancia REPUVE, acudí a Control Vehicular del estado a tramitar placas chihuahuenses. Costo adicional: $1,800-$2,500 MXN.",

                    "<strong>10. Pagá refrendo del año:</strong> aproximadamente $700 MXN."
                ]
            },
            {
                "heading": "Errores comunes y cómo evitarlos",
                "body": [
                    "<strong>Error 1: No tener el Title original.</strong> Si compraste un auto chocolate sin Title o solo con 'carta poder', NO podés regularizar. Necesitás el Title legítimo de EE.UU. con endoso a tu nombre o cadena de endosos clara desde el dueño en EE.UU.",

                    "<strong>Error 2: NIV alterado o ilegible.</strong> El módulo rechaza inmediatamente. Si tu NIV está deteriorado, acudí primero a un perito de la Fiscalía para que dictamine y emita un documento que respalde la identidad del vehículo.",

                    "<strong>Error 3: Pagar en efectivo a 'gestores'.</strong> Hay personas que ofrecen 'arreglar todo' por $4,000-$8,000 MXN incluyendo el trámite. Si pagás en efectivo a un tercero, no tenés garantía. El trámite real son $2,500 MXN al gobierno, pagados en banco con línea de captura. Hacelo vos.",

                    "<strong>Error 4: No pagar antes de la cita.</strong> El módulo no procesa sin el comprobante bancario previo. Pagá con 24-48h de anticipación para asegurar acreditación.",

                    "<strong>Error 5: Llegar tarde a la cita.</strong> Tolerancia típica 15-30 min. Después de ese tiempo perdés el lugar y debés reagendar — y si el módulo es itinerante, puede haber cerrado para cuando consigas nueva cita.",

                    "<strong>Error 6: Olvidar el manifiesto firmado.</strong> Es el documento más olvidado. Imprímilo, firmalo en tinta azul y revisalo antes de salir de casa."
                ]
            }
        ],
        "faqs": [
            {"q": "¿Sigue vigente el Decreto de Regularización en 2026?", "a": "Sí, el Decreto sigue vigente para vehículos ingresados al país antes del 19 de octubre de 2021. El programa ha tenido prórrogas sucesivas. Confirmá fecha de cierre actualizada en regularizaauto.sspc.gob.mx."},
            {"q": "¿Qué pasa si mi auto ingresó después del 19 de octubre de 2021?", "a": "<strong>No califica</strong> para este programa de regularización. Tu opción es la <strong>importación definitiva con agente aduanal</strong>, que es mucho más cara ($50,000-$150,000 MXN) e implica pago de impuestos de importación, ISAN, IVA, etc. Es viable solo para autos de alto valor."},
            {"q": "¿Cuánto tiempo total desde el inicio hasta tener placas chihuahuenses?", "a": "<strong>4-8 semanas en promedio</strong>: 1-2 semanas para conseguir cita y completar regularización federal, 1-2 semanas para emplacar en Control Vehicular del estado. En zonas con alta demanda (Cd. Juárez) puede tardar más."},
            {"q": "¿El chip REPUVE viene incluido en los $2,500 MXN?", "a": "Sí. El día de la cita, después de verificar tus documentos y el vehículo, el módulo instala el chip RFID en tu parabrisas sin costo adicional. Forma parte del proceso de regularización."},
            {"q": "¿Puedo regularizar una motocicleta chocolate con el mismo trámite?", "a": "Sí. Las motocicletas tienen el mismo proceso, mismo costo ($2,500 MXN) y mismos requisitos. El módulo realiza la inspección y la instalación del chip de la misma manera."},
            {"q": "¿Qué pasa si compré el auto chocolate sin Title?", "a": "Tu opción es <strong>recuperar el Title original</strong>. Contactá al DMV del estado donde fue emplacado el auto originalmente en EE.UU. y solicitá una reposición. Demora 4-8 semanas. Sin Title no podés regularizar."},
            {"q": "¿Después de regularizar puedo circular en cualquier estado?", "a": "Sí. Una vez regularizado y emplacado en Chihuahua, podés circular libremente en cualquier estado de México sin restricciones. El REPUVE es base federal."},
            {"q": f"¿Si vivo en Ciudad Juárez puedo hacer el trámite en otro módulo de {ESTADO}?", "a": "Sí. No hay restricción geográfica dentro del estado. Si Cd. Juárez está saturado, podés agendar en Chihuahua capital, Cuauhtémoc o cualquier otro módulo abierto. Solo necesitás trasladarte el día de la cita."},
            {"q": "¿Hay riesgo de que el auto sea decomisado durante el trámite?", "a": "Mientras tengas el comprobante de cita confirmada y la línea de captura pagada, podés mostrar esos documentos en caso de retén. Las autoridades suelen respetar trámites en proceso. Una vez que tenés la constancia REPUVE, ya estás regularizado."},
            {"q": "¿Puedo vender el auto inmediatamente después de regularizarlo?", "a": "Sí, pero los compradores generalmente pagan más por autos ya con placas mexicanas. Conviene completar también el emplacado en Control Vehicular antes de vender."}
        ]
    },
}

# Actualizar el JSON
data = json.loads(DATA.read_text())
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

DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2))
print(f"\n✓ {updated}/4 páginas expandidas en Parte 2.")
print(f"\nTotal expandido (Parte 1 + 2): 7 páginas críticas.")
print(f"\nEjecutá ahora: python3 scripts/build-datos-js.py")
