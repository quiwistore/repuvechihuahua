#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construye el dataset COMPLETO de estudios de Salud Digna Culiacan.
Cada estudio con contenido real y unico. Se ejecuta y sobreescribe data/estudios.json
manteniendo sucursales/telefono/horarios que ya estaban.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ====== ESTUDIOS (contenido real por estudio) ======
# campos: slug, nombre, categoria, precioMin, precioMax, ayuno, ordenMedica,
#         tiempoResultado, sinonimos[], queEs, paraQueSirve, preparacion, comoSeRealiza, incluye[]

ESTUDIOS = [
  # ---------- LABORATORIO ----------
  {
    "slug":"biometria-hematica","nombre":"Biometría Hemática","categoria":"Laboratorio",
    "precioMin":80,"precioMax":120,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"El mismo día (24 horas)",
    "sinonimos":["BH","BHC","hemograma completo","citometría hemática","biometría hemática completa"],
    "queEs":"La biometría hemática es un análisis de sangre que mide y evalúa las células que circulan en tu sangre: glóbulos rojos, glóbulos blancos y plaquetas. Es uno de los estudios más solicitados porque ayuda a detectar anemia, infecciones, problemas de coagulación y muchas otras condiciones.",
    "paraQueSirve":"Sirve para detectar anemia, infecciones, problemas en la coagulación, alteraciones del sistema inmune y para el control general de la salud. Los médicos suelen pedirla como primer estudio ante casi cualquier síntoma.",
    "preparacion":"No requiere ayuno en la mayoría de los casos. Si tu médico la pidió junto con química sanguínea u otros estudios, sí puede requerirse ayuno de 8 horas. Mantente hidratado bebiendo agua normal.",
    "comoSeRealiza":"Se toma una pequeña muestra de sangre de una vena del brazo. El procedimiento dura pocos minutos y la molestia es mínima. La muestra se analiza con equipos automatizados que cuentan y clasifican las células sanguíneas.",
    "incluye":["Conteo de glóbulos rojos (eritrocitos)","Conteo de glóbulos blancos (leucocitos)","Conteo de plaquetas","Hemoglobina y hematocrito","Fórmula leucocitaria (diferencial)"]
  },
  {
    "slug":"quimica-sanguinea","nombre":"Química Sanguínea","categoria":"Laboratorio",
    "precioMin":90,"precioMax":300,"ayuno":True,"ordenMedica":False,
    "tiempoResultado":"El mismo día (24 horas)",
    "sinonimos":["QS","química sanguínea 6 elementos","química sanguínea 27 elementos","perfil bioquímico","QS 35"],
    "queEs":"La química sanguínea es un conjunto de análisis que miden distintas sustancias en la sangre como glucosa, colesterol, triglicéridos, ácido úrico, urea y creatinina. Se ofrece en distintos paquetes según el número de elementos (6, 12, 24, 27, 35 o 45).",
    "paraQueSirve":"Permite evaluar el funcionamiento de órganos como riñones e hígado, detectar diabetes, problemas de colesterol, gota y enfermedades metabólicas. Es clave en chequeos preventivos y control de enfermedades crónicas.",
    "preparacion":"Requiere ayuno de 8 a 12 horas (solo agua). Evita alcohol 24 horas antes y no hagas ejercicio intenso la noche previa. Si tomas medicamentos, consulta si debes suspenderlos.",
    "comoSeRealiza":"Se extrae una muestra de sangre de una vena del brazo en ayunas. Los distintos elementos se analizan en equipos automatizados de laboratorio.",
    "incluye":["Glucosa","Colesterol total","Triglicéridos","Ácido úrico","Urea y creatinina","Otros elementos según el paquete elegido"]
  },
  {
    "slug":"examen-de-orina","nombre":"Examen General de Orina","categoria":"Laboratorio",
    "precioMin":60,"precioMax":90,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"El mismo día (24 horas)",
    "sinonimos":["EGO","análisis de orina","examen de orina","uroanálisis","prueba de orina"],
    "queEs":"El examen general de orina (EGO) es un análisis que evalúa las características físicas, químicas y microscópicas de la orina. Es un estudio básico y muy económico que aporta mucha información sobre tu salud.",
    "paraQueSirve":"Ayuda a detectar infecciones urinarias, problemas renales, diabetes, deshidratación y otras condiciones. Es parte de casi cualquier chequeo general y se pide con frecuencia en embarazos y controles de rutina.",
    "preparacion":"Recolecta la primera orina de la mañana (es la más concentrada). Usa el recipiente estéril que te proporcionen. Realiza aseo de la zona genital antes de la muestra y recoge el chorro medio. No requiere ayuno.",
    "comoSeRealiza":"Tú mismo recolectas la muestra de orina en un recipiente estéril siguiendo las indicaciones de higiene. La muestra se analiza mediante tiras reactivas y observación al microscopio.",
    "incluye":["Análisis físico (color, aspecto, densidad)","Análisis químico (glucosa, proteínas, pH)","Análisis microscópico (células, bacterias, cristales)","Reporte médico"]
  },
  {
    "slug":"urocultivo","nombre":"Urocultivo","categoria":"Laboratorio",
    "precioMin":150,"precioMax":220,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"De 3 a 5 días",
    "sinonimos":["cultivo de orina","urocultivo con antibiograma","cultivo urinario"],
    "queEs":"El urocultivo es un análisis que cultiva la orina en laboratorio para identificar qué bacteria está causando una infección urinaria y, con el antibiograma, a qué antibióticos es sensible.",
    "paraQueSirve":"Sirve para confirmar infecciones de vías urinarias y, sobre todo, para saber con precisión qué antibiótico será efectivo. Es muy útil en infecciones recurrentes o que no mejoran con tratamiento.",
    "preparacion":"Recolecta la primera orina de la mañana, con aseo genital previo y tomando el chorro medio en un recipiente estéril. No debes estar tomando antibióticos al momento de la muestra (pueden alterar el resultado).",
    "comoSeRealiza":"Se recolecta una muestra de orina estéril que se cultiva en el laboratorio durante varios días para identificar y contar las bacterias presentes, y probar su sensibilidad a antibióticos.",
    "incluye":["Identificación de bacterias","Recuento de colonias","Antibiograma (sensibilidad a antibióticos)","Reporte médico"]
  },
  {
    "slug":"prueba-de-embarazo","nombre":"Prueba de Embarazo en Sangre","categoria":"Laboratorio",
    "precioMin":120,"precioMax":200,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"El mismo día (24 horas)",
    "sinonimos":["beta hCG","prueba de embarazo de sangre","hCG cuantitativa","fracción beta de hCG","prueba cuantitativa de embarazo"],
    "queEs":"La prueba de embarazo en sangre mide la hormona gonadotropina coriónica humana (hCG), que produce el cuerpo durante el embarazo. La versión cuantitativa (beta hCG) mide la cantidad exacta de la hormona.",
    "paraQueSirve":"Confirma el embarazo con alta precisión, incluso en etapas muy tempranas (antes que las pruebas de orina). La versión cuantitativa ayuda a estimar las semanas de gestación y a hacer seguimiento.",
    "preparacion":"No requiere ayuno ni preparación especial. Puedes acudir en cualquier momento del día.",
    "comoSeRealiza":"Se toma una pequeña muestra de sangre de una vena del brazo y se mide la concentración de la hormona hCG.",
    "incluye":["Medición de hormona hCG","Resultado cuantitativo (cantidad exacta)","Reporte médico"]
  },
  {
    "slug":"prueba-de-vih","nombre":"Prueba de VIH","categoria":"Laboratorio",
    "precioMin":150,"precioMax":350,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"De 1 a 3 días",
    "sinonimos":["examen de VIH","prueba ELISA para VIH","prueba de SIDA","detección de VIH"],
    "queEs":"La prueba de VIH detecta anticuerpos o antígenos del virus de la inmunodeficiencia humana en la sangre. Salud Digna ofrece la prueba ELISA, de alta confiabilidad. El resultado es confidencial.",
    "paraQueSirve":"Sirve para detectar la infección por VIH de forma temprana, lo que permite iniciar tratamiento oportuno. Se recomienda como parte de chequeos de salud sexual y estudios prenupciales.",
    "preparacion":"No requiere ayuno. Para mayor confiabilidad, considera el periodo de ventana (el tiempo desde una posible exposición hasta que la prueba puede detectar el virus).",
    "comoSeRealiza":"Se toma una muestra de sangre de una vena del brazo y se analiza en laboratorio mediante la técnica ELISA. El resultado se entrega de forma confidencial.",
    "incluye":["Prueba ELISA de cuarta generación","Resultado confidencial","Reporte médico"]
  },
  {
    "slug":"perfil-tiroideo","nombre":"Perfil Tiroideo","categoria":"Laboratorio",
    "precioMin":200,"precioMax":500,"ayuno":True,"ordenMedica":False,
    "tiempoResultado":"De 1 a 3 días",
    "sinonimos":["perfil tiroideo completo","panel T3 T4 TSH","examen de tiroides","pruebas de tiroides"],
    "queEs":"El perfil tiroideo es un conjunto de análisis de sangre que miden las hormonas relacionadas con la glándula tiroides: TSH, T3 y T4. Evalúa el funcionamiento de la tiroides.",
    "paraQueSirve":"Detecta hipotiroidismo, hipertiroidismo y otros trastornos de la tiroides. Es útil ante síntomas como cansancio, cambios de peso, caída de cabello o alteraciones del ánimo.",
    "preparacion":"Se recomienda ayuno de 8 horas. Si tomas medicamento para la tiroides, consulta a tu médico si debes tomarlo antes o después de la muestra.",
    "comoSeRealiza":"Se extrae una muestra de sangre de una vena del brazo y se miden las concentraciones de las hormonas tiroideas.",
    "incluye":["TSH (hormona estimulante de tiroides)","T3 (triyodotironina)","T4 (tiroxina)","Reporte médico"]
  },
  {
    "slug":"perfil-de-lipidos","nombre":"Perfil de Lípidos","categoria":"Laboratorio",
    "precioMin":120,"precioMax":250,"ayuno":True,"ordenMedica":False,
    "tiempoResultado":"El mismo día (24 horas)",
    "sinonimos":["perfil lipídico","perfil de colesterol","colesterol y triglicéridos"],
    "queEs":"El perfil de lípidos mide las grasas en la sangre: colesterol total, colesterol HDL (bueno), colesterol LDL (malo) y triglicéridos. Es clave para evaluar el riesgo cardiovascular.",
    "paraQueSirve":"Ayuda a evaluar el riesgo de enfermedades del corazón y de las arterias. Es fundamental en el control de personas con sobrepeso, diabetes, hipertensión o antecedentes familiares.",
    "preparacion":"Requiere ayuno de 9 a 12 horas (solo agua). Evita comidas grasosas y alcohol el día anterior.",
    "comoSeRealiza":"Se toma una muestra de sangre en ayunas de una vena del brazo y se miden los distintos tipos de grasa en la sangre.",
    "incluye":["Colesterol total","Colesterol HDL","Colesterol LDL","Triglicéridos","Índice aterogénico"]
  },
  {
    "slug":"hemoglobina-glicosilada","nombre":"Hemoglobina Glicosilada","categoria":"Laboratorio",
    "precioMin":150,"precioMax":280,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"El mismo día (24 horas)",
    "sinonimos":["HbA1c","hemoglobina glucosilada","Hb glicosilada","examen de HbA1c"],
    "queEs":"La hemoglobina glicosilada (HbA1c) mide el promedio de azúcar en sangre de los últimos 2 a 3 meses. A diferencia de la glucosa en ayunas, refleja el control de la diabetes a largo plazo.",
    "paraQueSirve":"Es la prueba estándar para diagnosticar y controlar la diabetes. Permite saber si el tratamiento está funcionando a lo largo del tiempo, no solo en un momento puntual.",
    "preparacion":"No requiere ayuno. Puedes acudir en cualquier momento del día.",
    "comoSeRealiza":"Se toma una pequeña muestra de sangre de una vena del brazo y se mide el porcentaje de hemoglobina unida a glucosa.",
    "incluye":["Porcentaje de HbA1c","Estimación del promedio de glucosa","Reporte médico"]
  },
  {
    "slug":"antigeno-prostatico","nombre":"Antígeno Prostático","categoria":"Laboratorio",
    "precioMin":150,"precioMax":350,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"De 1 a 3 días",
    "sinonimos":["PSA","antígeno prostático específico","PSA total","PSA libre"],
    "queEs":"El antígeno prostático específico (PSA) es una proteína producida por la próstata que se mide en sangre. Niveles elevados pueden indicar problemas prostáticos.",
    "paraQueSirve":"Sirve para la detección temprana de cáncer de próstata, así como para evaluar inflamación o crecimiento de la próstata. Se recomienda en hombres a partir de los 45-50 años.",
    "preparacion":"Evita relaciones sexuales y ejercicio intenso (como bicicleta) 48 horas antes. No requiere ayuno.",
    "comoSeRealiza":"Se toma una muestra de sangre de una vena del brazo y se mide la concentración de PSA.",
    "incluye":["PSA total","PSA libre (según paquete)","Relación PSA libre/total","Reporte médico"]
  },
  {
    "slug":"reacciones-febriles","nombre":"Reacciones Febriles","categoria":"Laboratorio",
    "precioMin":90,"precioMax":180,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"De 1 a 2 días",
    "sinonimos":["reacciones febriles tifoideas","prueba de tifoidea","Widal"],
    "queEs":"Las reacciones febriles son un grupo de pruebas que detectan anticuerpos contra bacterias que causan fiebre, principalmente la salmonella (fiebre tifoidea) y brucella.",
    "paraQueSirve":"Ayudan a diagnosticar enfermedades febriles como la fiebre tifoidea y la brucelosis. Se piden ante fiebre prolongada de origen desconocido.",
    "preparacion":"No requiere ayuno ni preparación especial.",
    "comoSeRealiza":"Se toma una muestra de sangre de una vena del brazo y se buscan anticuerpos contra distintas bacterias.",
    "incluye":["Antígenos tifoídicos O y H","Antígenos paratíficos","Brucella","Proteus (OX-19)"]
  },
  {
    "slug":"coproparasitoscopico","nombre":"Coproparasitoscópico","categoria":"Laboratorio",
    "precioMin":80,"precioMax":150,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"De 1 a 3 días",
    "sinonimos":["copro","examen de heces","coproparasitoscópico en serie","CPS"],
    "queEs":"El coproparasitoscópico es un análisis de las heces que busca parásitos intestinales, sus huevos y larvas. Suele realizarse en serie de tres muestras para mayor precisión.",
    "paraQueSirve":"Detecta parasitosis intestinales como amebas, lombrices y giardia. Se pide ante diarrea persistente, dolor abdominal o como estudio preventivo.",
    "preparacion":"Recolecta la muestra de heces en el recipiente estéril que te proporcionen. Para la serie, se recolectan muestras de tres días distintos. No uses laxantes ni antiácidos antes.",
    "comoSeRealiza":"Tú recolectas la muestra de heces en casa siguiendo las indicaciones. En el laboratorio se examina al microscopio en busca de parásitos.",
    "incluye":["Búsqueda de parásitos, huevos y larvas","Análisis en serie (3 muestras)","Reporte médico"]
  },
  # ---------- IMAGEN ----------
  {
    "slug":"ultrasonido-abdominal","nombre":"Ultrasonido Abdominal","categoria":"Imagen",
    "precioMin":215,"precioMax":360,"ayuno":True,"ordenMedica":False,
    "tiempoResultado":"El mismo día",
    "sinonimos":["ecografía abdominal","ultrasonido de abdomen","USG abdominal","ultrasonido abdominal completo"],
    "queEs":"El ultrasonido abdominal es un estudio de imagen que usa ondas de sonido (sin radiación) para visualizar los órganos del abdomen: hígado, vesícula biliar, páncreas, riñones y bazo. Es indoloro y seguro.",
    "paraQueSirve":"Permite evaluar dolor abdominal, detectar cálculos en la vesícula o riñones, quistes, tumores e inflamación de órganos. Es uno de los estudios de imagen más solicitados por su versatilidad.",
    "preparacion":"Requiere ayuno de 6 a 8 horas antes del estudio. Para vías urinarias puede pedirse acudir con la vejiga llena. Sigue las indicaciones específicas que te den al agendar.",
    "comoSeRealiza":"Te recuestas en una camilla y el técnico aplica un gel sobre tu abdomen. Luego desliza un transductor que genera imágenes en tiempo real. Es indoloro y dura entre 15 y 30 minutos.",
    "incluye":["Evaluación de hígado, vesícula, páncreas, riñones y bazo","Imágenes en tiempo real","Interpretación por radiólogo","Reporte médico"]
  },
  {
    "slug":"ultrasonido-pelvico","nombre":"Ultrasonido Pélvico","categoria":"Imagen",
    "precioMin":200,"precioMax":370,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"El mismo día",
    "sinonimos":["ecografía pélvica","ultrasonido de pelvis","USG pélvico"],
    "queEs":"El ultrasonido pélvico es un estudio de imagen que examina los órganos reproductivos femeninos (útero, ovarios) y la vejiga mediante ondas de sonido, sin radiación.",
    "paraQueSirve":"Evalúa dolor pélvico, sangrados anormales, quistes ováricos, miomas y otras condiciones ginecológicas. También se usa para revisar la vejiga.",
    "preparacion":"Acude con la vejiga llena: bebe 1 litro de agua una hora antes del estudio y no orines. Esto permite ver mejor los órganos.",
    "comoSeRealiza":"Te recuestas y el técnico aplica gel en el bajo vientre, deslizando el transductor para obtener imágenes. Dura entre 15 y 30 minutos.",
    "incluye":["Evaluación de útero y ovarios","Revisión de vejiga","Interpretación por radiólogo","Reporte médico"]
  },
  {
    "slug":"ultrasonido-obstetrico","nombre":"Ultrasonido Obstétrico","categoria":"Imagen",
    "precioMin":195,"precioMax":560,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"El mismo día",
    "sinonimos":["ultrasonido de embarazo","ecografía obstétrica","ultrasonido prenatal","USG obstétrico"],
    "queEs":"El ultrasonido obstétrico es un estudio de imagen que permite ver y monitorear al bebé durante el embarazo, evaluando su desarrollo, posición y bienestar.",
    "paraQueSirve":"Confirma el embarazo, mide el crecimiento del bebé, revisa la placenta y el líquido amniótico, y detecta posibles complicaciones. Se realiza en distintos momentos del embarazo.",
    "preparacion":"En el primer trimestre puede pedirse vejiga llena. En etapas avanzadas no requiere preparación especial. Sigue las indicaciones que te den al agendar.",
    "comoSeRealiza":"Se aplica gel sobre el abdomen y se desliza un transductor para obtener imágenes del bebé en tiempo real. Es indoloro y seguro para la madre y el bebé.",
    "incluye":["Evaluación del desarrollo fetal","Medición y posición del bebé","Revisión de placenta y líquido amniótico","Reporte médico"]
  },
  {
    "slug":"ultrasonido-mamario","nombre":"Ultrasonido Mamario","categoria":"Imagen",
    "precioMin":330,"precioMax":400,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"El mismo día",
    "sinonimos":["ecografía mamaria","ultrasonido de mama","USG mamario"],
    "queEs":"El ultrasonido mamario es un estudio de imagen que examina el tejido de las mamas con ondas de sonido. Complementa a la mastografía, especialmente en mujeres jóvenes con tejido mamario denso.",
    "paraQueSirve":"Ayuda a evaluar bultos o masas en las mamas, distinguir entre quistes y tumores sólidos, y complementar el estudio de mama. Útil en mujeres menores de 40 años.",
    "preparacion":"No requiere preparación especial. No uses cremas ni talco en el área el día del estudio.",
    "comoSeRealiza":"Te recuestas y el técnico aplica gel sobre las mamas, deslizando el transductor para obtener imágenes detalladas del tejido mamario.",
    "incluye":["Evaluación de ambas mamas","Detección de quistes y masas","Interpretación por radiólogo","Reporte médico"]
  },
  {
    "slug":"ultrasonido-tiroideo","nombre":"Ultrasonido Tiroideo","categoria":"Imagen",
    "precioMin":300,"precioMax":450,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"El mismo día",
    "sinonimos":["ecografía de tiroides","ultrasonido de cuello","USG tiroideo"],
    "queEs":"El ultrasonido tiroideo es un estudio de imagen que examina la glándula tiroides y las estructuras del cuello mediante ondas de sonido, sin radiación.",
    "paraQueSirve":"Detecta nódulos, quistes, inflamación o crecimiento de la tiroides. Complementa al perfil tiroideo cuando hay sospecha de alteraciones estructurales.",
    "preparacion":"No requiere preparación especial ni ayuno.",
    "comoSeRealiza":"Te recuestas con el cuello ligeramente extendido. El técnico aplica gel y desliza el transductor sobre el cuello para obtener imágenes de la tiroides.",
    "incluye":["Evaluación de la glándula tiroides","Detección de nódulos y quistes","Interpretación por radiólogo","Reporte médico"]
  },
  {
    "slug":"ultrasonido-renal","nombre":"Ultrasonido Renal","categoria":"Imagen",
    "precioMin":330,"precioMax":365,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"El mismo día",
    "sinonimos":["ecografía renal","ultrasonido de riñones","USG renal","ultrasonido de vías urinarias"],
    "queEs":"El ultrasonido renal es un estudio de imagen que examina los riñones y las vías urinarias con ondas de sonido, para detectar cálculos, quistes y otras alteraciones.",
    "paraQueSirve":"Evalúa dolor lumbar, detecta cálculos renales (piedras), quistes, tumores y obstrucciones en las vías urinarias. Útil en infecciones urinarias recurrentes.",
    "preparacion":"Acude con la vejiga llena: bebe agua una hora antes y no orines. En algunos casos se pide ayuno; sigue las indicaciones al agendar.",
    "comoSeRealiza":"Te recuestas y el técnico aplica gel en la zona lumbar y el abdomen, deslizando el transductor para obtener imágenes de los riñones.",
    "incluye":["Evaluación de ambos riñones","Detección de cálculos y quistes","Revisión de vías urinarias","Reporte médico"]
  },
  {
    "slug":"mastografia","nombre":"Mastografía","categoria":"Imagen",
    "precioMin":280,"precioMax":450,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"Entre 4 y 12 horas",
    "sinonimos":["mamografía","mastografía digital","estudio de mama","mastografía bilateral"],
    "queEs":"La mastografía (también llamada mamografía) es un estudio de imagen por rayos X de baja dosis que permite detectar tempranamente el cáncer de mama y otras anomalías en el tejido mamario, incluso antes de que aparezcan síntomas.",
    "paraQueSirve":"Es la herramienta principal para la detección temprana del cáncer de mama. Se recomienda anualmente a partir de los 40 años, o antes si hay antecedentes familiares.",
    "preparacion":"No uses desodorante, talco ni cremas en axilas o senos el día del estudio. Usa ropa de dos piezas. Si tienes implantes o cirugías previas, avísalo al personal.",
    "comoSeRealiza":"Te colocarás de pie frente al mastógrafo. Una técnica colocará cada mama entre dos placas que la comprimen brevemente para obtener imágenes claras. Dura entre 10 y 20 minutos.",
    "incluye":["Imágenes por rayos X de ambas mamas","Interpretación por radiólogo certificado","Reporte médico","Consulta de resultados en línea"]
  },
  {
    "slug":"resonancia-magnetica","nombre":"Resonancia Magnética","categoria":"Imagen",
    "precioMin":2500,"precioMax":4500,"ayuno":False,"ordenMedica":True,
    "tiempoResultado":"De 1 a 3 días",
    "sinonimos":["RM","resonancia magnética nuclear","IRM","resonancia"],
    "queEs":"La resonancia magnética es un estudio de imagen avanzado que usa campos magnéticos y ondas de radio (sin radiación) para obtener imágenes muy detalladas de órganos, tejidos blandos, articulaciones y el sistema nervioso.",
    "paraQueSirve":"Permite diagnosticar con gran detalle lesiones de articulaciones, columna, cerebro, tumores y muchas otras condiciones que otros estudios no muestran con claridad.",
    "preparacion":"Generalmente requiere orden médica. Avisa si tienes marcapasos, prótesis metálicas o implantes. Retira objetos metálicos. Algunos estudios requieren ayuno o medio de contraste.",
    "comoSeRealiza":"Te recuestas en una camilla que se desliza dentro del equipo de resonancia. Debes permanecer inmóvil. El estudio puede durar de 20 a 60 minutos y es indoloro.",
    "incluye":["Imágenes detalladas de la zona estudiada","Interpretación por radiólogo","Reporte médico","Medio de contraste si es necesario"]
  },
  {
    "slug":"tomografia","nombre":"Tomografía Computarizada","categoria":"Imagen",
    "precioMin":900,"precioMax":2500,"ayuno":True,"ordenMedica":True,
    "tiempoResultado":"De 1 a 2 días",
    "sinonimos":["TAC","tomografía axial computarizada","TC","escáner"],
    "queEs":"La tomografía computarizada (TAC) es un estudio de imagen que combina múltiples radiografías para crear imágenes transversales detalladas del cuerpo. Permite ver huesos, órganos y tejidos con gran precisión.",
    "paraQueSirve":"Diagnostica fracturas complejas, tumores, hemorragias, problemas pulmonares y abdominales. Es muy útil en urgencias y para planear tratamientos.",
    "preparacion":"Puede requerir ayuno de 4 a 6 horas, especialmente si se usa contraste. Suele necesitar orden médica. Avisa si eres alérgico al medio de contraste.",
    "comoSeRealiza":"Te recuestas en una camilla que se desliza a través de un anillo (el tomógrafo). Debes permanecer inmóvil. El estudio dura pocos minutos y es indoloro.",
    "incluye":["Imágenes transversales de la zona estudiada","Interpretación por radiólogo","Reporte médico","Medio de contraste si es necesario"]
  },
  {
    "slug":"rayos-x","nombre":"Rayos X","categoria":"Imagen",
    "precioMin":150,"precioMax":400,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"El mismo día",
    "sinonimos":["radiografía","placa de rayos X","estudio radiográfico","radiografía simple"],
    "queEs":"La radiografía (rayos X) es un estudio de imagen que usa una pequeña dosis de radiación para ver huesos y algunas estructuras internas. Es rápido, económico y muy útil.",
    "paraQueSirve":"Detecta fracturas, problemas pulmonares (como neumonía), alteraciones óseas y articulares. Es uno de los estudios de imagen más usados.",
    "preparacion":"No requiere ayuno. Retira objetos metálicos y joyas de la zona a estudiar. Avisa si estás o podrías estar embarazada.",
    "comoSeRealiza":"Te colocas frente o sobre la placa según la zona a estudiar. La toma dura segundos. Es indoloro.",
    "incluye":["Imagen radiográfica de la zona indicada","Interpretación por radiólogo","Reporte médico"]
  },
  {
    "slug":"densitometria-osea","nombre":"Densitometría Ósea","categoria":"Imagen",
    "precioMin":400,"precioMax":700,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"El mismo día",
    "sinonimos":["densitometría","DEXA","DXA","densitometría con DXA","estudio de osteoporosis"],
    "queEs":"La densitometría ósea es un estudio que mide la densidad mineral de los huesos mediante una técnica de rayos X de muy baja dosis (DEXA). Evalúa la fortaleza ósea.",
    "paraQueSirve":"Detecta osteoporosis y osteopenia, midiendo el riesgo de fracturas. Se recomienda en mujeres postmenopáusicas y adultos mayores.",
    "preparacion":"No tomes suplementos de calcio 24 horas antes. Usa ropa cómoda sin metales. No requiere ayuno.",
    "comoSeRealiza":"Te recuestas en una camilla mientras un brazo del equipo pasa sobre tu cuerpo escaneando columna y cadera. Es indoloro y dura entre 10 y 20 minutos.",
    "incluye":["Medición de densidad en columna y cadera","Comparación con valores de referencia","Interpretación médica","Reporte médico"]
  },
  # ---------- ESPECIALIDAD / CARDIO / NEURO ----------
  {
    "slug":"electrocardiograma","nombre":"Electrocardiograma","categoria":"Especialidad",
    "precioMin":120,"precioMax":300,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"El mismo día",
    "sinonimos":["ECG","EKG","electro","cardiograma","electrocardiograma en reposo"],
    "queEs":"El electrocardiograma (ECG) registra la actividad eléctrica del corazón mediante electrodos colocados en la piel. Es un estudio rápido, indoloro y no invasivo.",
    "paraQueSirve":"Detecta arritmias, infartos previos, crecimiento del corazón y otras alteraciones cardíacas. Es básico en chequeos cardiovasculares y prequirúrgicos.",
    "preparacion":"No requiere ayuno. Evita cremas en el pecho el día del estudio. Usa ropa fácil de retirar.",
    "comoSeRealiza":"Te recuestas y se colocan electrodos en pecho, brazos y piernas. El equipo registra la actividad eléctrica del corazón durante unos minutos. Es indoloro.",
    "incluye":["Registro de 12 derivaciones","Interpretación por médico","Reporte médico"]
  },
  {
    "slug":"ecocardiograma","nombre":"Ecocardiograma","categoria":"Especialidad",
    "precioMin":800,"precioMax":1200,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"El mismo día",
    "sinonimos":["eco de corazón","ultrasonido de corazón","ecocardiograma transtorácico"],
    "queEs":"El ecocardiograma es un ultrasonido del corazón que muestra su estructura y funcionamiento en movimiento, evaluando las cavidades, válvulas y la fuerza de bombeo.",
    "paraQueSirve":"Evalúa la función del corazón, detecta problemas en las válvulas, insuficiencia cardíaca y malformaciones. Complementa al electrocardiograma.",
    "preparacion":"No requiere ayuno ni preparación especial. Usa ropa cómoda.",
    "comoSeRealiza":"Te recuestas de lado y el médico aplica gel en el pecho, deslizando un transductor para obtener imágenes del corazón en movimiento. Dura de 20 a 40 minutos.",
    "incluye":["Evaluación de cavidades y válvulas","Medición de la función cardíaca","Interpretación por cardiólogo","Reporte médico"]
  },
  {
    "slug":"prueba-de-esfuerzo","nombre":"Prueba de Esfuerzo","categoria":"Especialidad",
    "precioMin":600,"precioMax":1200,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"El mismo día",
    "sinonimos":["ergometría","test de esfuerzo","prueba de esfuerzo en banda"],
    "queEs":"La prueba de esfuerzo registra la actividad del corazón mientras haces ejercicio (en banda o bicicleta), para ver cómo responde el corazón al esfuerzo físico.",
    "paraQueSirve":"Detecta problemas cardíacos que solo aparecen con el esfuerzo, como isquemia o arritmias. Útil para evaluar dolor de pecho y capacidad funcional.",
    "preparacion":"Acude con ropa y calzado deportivo. Come ligero 2-3 horas antes. Evita cafeína y tabaco el día del estudio. Consulta sobre tus medicamentos.",
    "comoSeRealiza":"Caminas en una banda o pedaleas en bicicleta mientras se registra tu electrocardiograma y presión arterial, aumentando la intensidad gradualmente.",
    "incluye":["Monitoreo cardíaco durante el ejercicio","Registro de presión arterial","Interpretación por cardiólogo","Reporte médico"]
  },
  {
    "slug":"holter","nombre":"Holter","categoria":"Especialidad",
    "precioMin":600,"precioMax":1200,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"De 1 a 3 días",
    "sinonimos":["holter 24 horas","monitoreo holter","holter de ritmo","electrocardiograma ambulatorio"],
    "queEs":"El Holter es un dispositivo portátil que registra la actividad eléctrica del corazón durante 24 horas o más, mientras realizas tus actividades normales.",
    "paraQueSirve":"Detecta arritmias y alteraciones cardíacas que aparecen de forma intermitente y no se captan en un electrocardiograma normal de pocos minutos.",
    "preparacion":"Acude con el pecho limpio y sin cremas. Podrás hacer vida normal con el dispositivo, pero no debes mojarlo (evita bañarte mientras lo usas).",
    "comoSeRealiza":"Se colocan electrodos en el pecho conectados a un pequeño aparato que llevas contigo 24 horas. Anotas tus actividades y síntomas. Luego se analiza el registro.",
    "incluye":["Monitoreo continuo de 24 horas","Análisis del registro","Interpretación por cardiólogo","Reporte médico"]
  },
  {
    "slug":"electroencefalograma","nombre":"Electroencefalograma","categoria":"Especialidad",
    "precioMin":400,"precioMax":900,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"De 1 a 3 días",
    "sinonimos":["EEG","encefalograma","estudio de actividad cerebral"],
    "queEs":"El electroencefalograma (EEG) registra la actividad eléctrica del cerebro mediante electrodos colocados en el cuero cabelludo. Es indoloro y no invasivo.",
    "paraQueSirve":"Ayuda a diagnosticar epilepsia, convulsiones, trastornos del sueño y otras alteraciones neurológicas. Evalúa el funcionamiento eléctrico del cerebro.",
    "preparacion":"Lava tu cabello la noche anterior sin aplicar productos. Puede pedirse dormir pocas horas la noche previa (privación de sueño). Sigue las indicaciones al agendar.",
    "comoSeRealiza":"Se colocan varios electrodos en el cuero cabelludo. Te recuestas relajado y se registra la actividad cerebral, a veces con estímulos de luz o respiración. Dura de 30 a 60 minutos.",
    "incluye":["Registro de actividad cerebral","Pruebas de activación","Interpretación por neurólogo","Reporte médico"]
  },
  {
    "slug":"audiometria","nombre":"Audiometría","categoria":"Especialidad",
    "precioMin":200,"precioMax":400,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"El mismo día",
    "sinonimos":["audiometría tonal","examen de audición","estudio auditivo","audiometría laboral"],
    "queEs":"La audiometría es una prueba que mide tu capacidad auditiva, evaluando qué tan bien escuchas distintos tonos e intensidades de sonido.",
    "paraQueSirve":"Detecta pérdida auditiva y su grado. Se usa en chequeos, exámenes laborales y ante problemas de audición.",
    "preparacion":"Evita exponerte a ruidos fuertes 12-16 horas antes. Si tienes tapones de cerumen, conviene retirarlos antes del estudio.",
    "comoSeRealiza":"Dentro de una cabina insonorizada, usas audífonos y vas indicando cuándo escuchas cada sonido. Es indoloro y dura unos 20-30 minutos.",
    "incluye":["Evaluación de vía aérea y ósea","Audiograma","Interpretación profesional","Reporte"]
  },
  {
    "slug":"espirometria","nombre":"Espirometría","categoria":"Especialidad",
    "precioMin":250,"precioMax":450,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"El mismo día",
    "sinonimos":["prueba de función pulmonar","espirometría con broncodilatador","prueba respiratoria"],
    "queEs":"La espirometría es una prueba que mide cuánto aire puedes inhalar y exhalar y a qué velocidad. Evalúa el funcionamiento de los pulmones.",
    "paraQueSirve":"Diagnostica y controla enfermedades respiratorias como asma y EPOC. Útil en exámenes laborales y ante tos crónica o falta de aire.",
    "preparacion":"No fumes 1 hora antes. Evita comidas pesadas y ejercicio intenso antes del estudio. Consulta si debes suspender inhaladores.",
    "comoSeRealiza":"Soplas con fuerza a través de una boquilla conectada al espirómetro siguiendo las indicaciones del técnico. Se repite varias veces. Dura unos 15-30 minutos.",
    "incluye":["Medición de capacidad y flujo pulmonar","Prueba con broncodilatador (según caso)","Interpretación profesional","Reporte médico"]
  },
  {
    "slug":"endoscopia","nombre":"Endoscopia","categoria":"Endoscopia",
    "precioMin":1000,"precioMax":2000,"ayuno":True,"ordenMedica":False,
    "tiempoResultado":"El mismo día",
    "sinonimos":["panendoscopia","endoscopia digestiva","gastroscopia","endoscopia superior"],
    "queEs":"La endoscopia es un estudio que permite ver el interior del esófago, estómago y duodeno mediante un tubo delgado y flexible con una cámara (endoscopio).",
    "paraQueSirve":"Diagnostica gastritis, úlceras, reflujo, sangrados y otras alteraciones digestivas. Puede tomar biopsias durante el procedimiento.",
    "preparacion":"Requiere ayuno de al menos 8 horas (sólidos y líquidos). Si se usa sedación, lleva acompañante. Avisa si tomas anticoagulantes o eres alérgico a anestésicos.",
    "comoSeRealiza":"Generalmente con sedación, se introduce el endoscopio por la boca para revisar el tracto digestivo superior. Dura entre 15 y 30 minutos.",
    "incluye":["Revisión de esófago, estómago y duodeno","Toma de biopsia (con costo adicional)","Interpretación médica","Reporte"]
  },
  {
    "slug":"colonoscopia","nombre":"Colonoscopia","categoria":"Endoscopia",
    "precioMin":1500,"precioMax":2500,"ayuno":True,"ordenMedica":False,
    "tiempoResultado":"El mismo día",
    "sinonimos":["colonoscopía","estudio de colon","colonoscopia preventiva","colonoscopia diagnóstica"],
    "queEs":"La colonoscopia es un estudio que examina el interior del colon y el recto mediante un tubo flexible con cámara, para detectar pólipos, inflamación y cáncer.",
    "paraQueSirve":"Detecta cáncer de colon, pólipos, inflamaciones y la causa de sangrados o cambios en el hábito intestinal. Es clave en la prevención del cáncer colorrectal.",
    "preparacion":"Requiere dieta líquida 24-48 horas antes, limpieza del colon con el preparado indicado y ayuno total 8 horas antes. Lleva acompañante por la sedación.",
    "comoSeRealiza":"Con sedación, se introduce el colonoscopio por el recto para revisar todo el colon. Puede tomar biopsias o quitar pólipos. Dura de 30 a 60 minutos.",
    "incluye":["Revisión completa de colon y recto","Toma de biopsia o extracción de pólipos","Interpretación médica","Reporte"]
  },
  {
    "slug":"papanicolaou","nombre":"Papanicolaou","categoria":"Ginecología",
    "precioMin":120,"precioMax":200,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"De 3 a 7 días",
    "sinonimos":["papanicolau","citología cervical","prueba de Papanicolaou","PAP"],
    "queEs":"El Papanicolaou es una prueba que toma una muestra de células del cuello del útero para detectar cambios anormales que podrían indicar cáncer cervicouterino o lesiones previas.",
    "paraQueSirve":"Es la prueba clave para la detección temprana del cáncer de cuello uterino y del virus del papiloma humano (VPH). Se recomienda anualmente en mujeres de 21 a 65 años.",
    "preparacion":"No estés menstruando. Evita relaciones sexuales, duchas vaginales, óvulos o cremas vaginales 48 horas antes.",
    "comoSeRealiza":"En posición ginecológica, el personal toma una muestra de células del cuello uterino con un cepillo o espátula. Dura pocos minutos y la molestia es mínima.",
    "incluye":["Toma de muestra cervical","Análisis citológico","Interpretación","Reporte médico"]
  },
  {
    "slug":"colposcopia","nombre":"Colposcopia","categoria":"Ginecología",
    "precioMin":500,"precioMax":900,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"El mismo día",
    "sinonimos":["colposcopía","estudio de colposcopia"],
    "queEs":"La colposcopia es un estudio que examina con aumento el cuello del útero, la vagina y la vulva para identificar lesiones que el Papanicolaou pudo señalar.",
    "paraQueSirve":"Se realiza cuando el Papanicolaou sale anormal, para observar de cerca las lesiones y tomar biopsia si es necesario. Detecta lesiones precancerosas.",
    "preparacion":"No estés menstruando. Evita relaciones sexuales, óvulos o duchas vaginales 48 horas antes.",
    "comoSeRealiza":"En posición ginecológica, se usa un colposcopio (lente con aumento) para observar el cuello uterino. Puede aplicarse una solución que resalta zonas anormales.",
    "incluye":["Observación con aumento","Toma de biopsia si es necesario","Interpretación","Reporte médico"]
  },
  {
    "slug":"prueba-de-adn","nombre":"Prueba de ADN","categoria":"Especialidad",
    "precioMin":2000,"precioMax":6000,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"De 1 a 3 semanas",
    "sinonimos":["prueba de paternidad","test de ADN","prueba de paternidad ADN","examen de ADN"],
    "queEs":"La prueba de ADN compara el material genético de dos o más personas para determinar parentesco, principalmente paternidad, con altísima precisión.",
    "paraQueSirve":"Confirma o descarta relaciones de parentesco (paternidad, maternidad). Puede tener fines informativos o legales según el tipo de prueba.",
    "preparacion":"No requiere ayuno. Para la versión legal, se requiere identificación oficial de los participantes y una cadena de custodia.",
    "comoSeRealiza":"Se toma una muestra de saliva con un hisopo bucal (o sangre) de las personas involucradas. Se analiza el ADN en laboratorio especializado.",
    "incluye":["Toma de muestra de los participantes","Análisis genético","Reporte de resultados","Versión legal disponible (con costo distinto)"]
  },
  {
    "slug":"perfil-hormonal","nombre":"Perfil Hormonal","categoria":"Laboratorio",
    "precioMin":300,"precioMax":900,"ayuno":True,"ordenMedica":False,
    "tiempoResultado":"De 1 a 3 días",
    "sinonimos":["perfil hormonal femenino","perfil hormonal masculino","perfil hormonal completo","estudios hormonales"],
    "queEs":"El perfil hormonal es un conjunto de análisis de sangre que miden distintas hormonas del cuerpo (sexuales, tiroideas, etc.) para evaluar el equilibrio hormonal.",
    "paraQueSirve":"Evalúa problemas de fertilidad, alteraciones menstruales, menopausia, andropausia y desequilibrios hormonales. Existen paquetes femeninos y masculinos.",
    "preparacion":"Suele requerir ayuno de 8 horas. En mujeres, algunas hormonas se miden en días específicos del ciclo menstrual; consulta al agendar.",
    "comoSeRealiza":"Se toma una muestra de sangre de una vena del brazo y se miden las distintas hormonas según el paquete solicitado.",
    "incluye":["Hormonas sexuales","Hormonas tiroideas (según paquete)","Interpretación","Reporte médico"]
  },
  {
    "slug":"perfil-hepatico","nombre":"Perfil Hepático","categoria":"Laboratorio",
    "precioMin":150,"precioMax":400,"ayuno":True,"ordenMedica":False,
    "tiempoResultado":"El mismo día (24 horas)",
    "sinonimos":["pruebas de función hepática","perfil hepático completo","examen de hígado"],
    "queEs":"El perfil hepático es un conjunto de análisis de sangre que evalúan el funcionamiento del hígado, midiendo enzimas, bilirrubinas y proteínas.",
    "paraQueSirve":"Detecta daño o enfermedades del hígado como hepatitis, hígado graso o cirrosis. Útil en control de personas que toman ciertos medicamentos o alcohol.",
    "preparacion":"Requiere ayuno de 8 horas. Evita alcohol 24-48 horas antes del estudio.",
    "comoSeRealiza":"Se toma una muestra de sangre en ayunas de una vena del brazo y se analizan las enzimas y sustancias relacionadas con el hígado.",
    "incluye":["Transaminasas (TGO, TGP)","Bilirrubinas","Fosfatasa alcalina","Proteínas totales y albúmina"]
  },
  {
    "slug":"dental","nombre":"Servicios Dentales","categoria":"Dental",
    "precioMin":150,"precioMax":3000,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"Según el tratamiento",
    "sinonimos":["dentista","consulta dental","limpieza dental","endodoncia","extracción dental"],
    "queEs":"Salud Digna ofrece servicios dentales que incluyen consulta, limpieza, resinas, extracciones, endodoncias (tratamiento de conducto) y radiografías dentales, a precios accesibles.",
    "paraQueSirve":"Atiende la salud bucal: caries, dolor dental, limpieza, tratamientos de conducto y extracciones. La consulta inicial permite valorar qué tratamiento necesitas.",
    "preparacion":"No requiere ayuno. Acude con buena higiene bucal. Para algunos tratamientos puede pedirse una radiografía previa.",
    "comoSeRealiza":"En el consultorio dental, el odontólogo valora tu caso y realiza el tratamiento correspondiente (limpieza, resina, endodoncia, etc.).",
    "incluye":["Consulta dental","Limpieza y profilaxis","Resinas, extracciones, endodoncia (según necesidad)","Radiografía dental"]
  },
  {
    "slug":"examen-de-la-vista","nombre":"Examen de la Vista","categoria":"Óptica",
    "precioMin":0,"precioMax":150,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"El mismo día",
    "sinonimos":["examen de la vista gratis","examen visual","optometría","graduación de la vista"],
    "queEs":"El examen de la vista evalúa tu agudeza visual y detecta la necesidad de lentes. En Salud Digna el examen suele ser gratuito al adquirir lentes o realizar otros estudios.",
    "paraQueSirve":"Determina si necesitas lentes y con qué graduación. Detecta miopía, astigmatismo, hipermetropía y presbicia. Permite obtener una receta para lentes.",
    "preparacion":"No requiere preparación. Si usas lentes, llévalos contigo. No requiere cita previa en muchos casos.",
    "comoSeRealiza":"Con equipos automatizados y la guía de un optometrista, lees letras y se prueban distintos lentes para determinar tu graduación. Es rápido e indoloro.",
    "incluye":["Evaluación de agudeza visual","Medición de graduación","Receta para lentes","Promoción gratis con compra de lentes"]
  },
  {
    "slug":"check-up-general","nombre":"Check-Up General","categoria":"Paquetes",
    "precioMin":200,"precioMax":800,"ayuno":True,"ordenMedica":False,
    "tiempoResultado":"De 1 a 2 días",
    "sinonimos":["chequeo general","paquete preventivo","check up básico","revisión médica completa"],
    "queEs":"El check-up general es un paquete de estudios que evalúa tu estado de salud general combinando varios análisis (sangre, orina, etc.) a un precio más accesible que por separado.",
    "paraQueSirve":"Permite una revisión preventiva integral para detectar a tiempo problemas como diabetes, colesterol alto, anemia o alteraciones renales. Ideal hacerlo una vez al año.",
    "preparacion":"Requiere ayuno de 8 a 12 horas porque incluye estudios de sangre. Acude por la mañana e hidrátate con agua.",
    "comoSeRealiza":"Se toman muestras de sangre y orina, y según el paquete pueden incluirse otros estudios. Los resultados se entregan integrados.",
    "incluye":["Biometría hemática","Química sanguínea","Examen general de orina","Otros estudios según el paquete"]
  },
  {
    "slug":"antidoping","nombre":"Antidoping","categoria":"Laboratorio",
    "precioMin":150,"precioMax":400,"ayuno":False,"ordenMedica":False,
    "tiempoResultado":"El mismo día (24 horas)",
    "sinonimos":["examen antidoping","prueba antidoping","examen toxicológico","prueba de drogas"],
    "queEs":"El antidoping es una prueba que detecta la presencia de sustancias o drogas en la orina (o sangre). Suele incluir un panel de 3, 5 o más sustancias.",
    "paraQueSirve":"Se usa principalmente para fines laborales, escolares o legales, para detectar consumo reciente de drogas como marihuana, cocaína, anfetaminas, entre otras.",
    "preparacion":"No requiere ayuno. Para fines laborales, lleva identificación oficial. Acude preparado para dar muestra de orina.",
    "comoSeRealiza":"Recolectas una muestra de orina en condiciones controladas. Se analiza con pruebas que detectan distintas sustancias según el panel solicitado.",
    "incluye":["Panel de sustancias (3, 5 o más)","Análisis de muestra","Reporte con validez laboral"]
  },
]

# ====== cargar lo existente para conservar sucursales/telefono/horarios ======
path = os.path.join(ROOT, 'data', 'estudios.json')
base = json.load(open(path, encoding='utf-8'))

base['estudios'] = ESTUDIOS

json.dump(base, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f"OK dataset completo: {len(ESTUDIOS)} estudios")
from collections import Counter
cats = Counter(e['categoria'] for e in ESTUDIOS)
for c, n in cats.most_common():
    print(f"  {c}: {n}")
