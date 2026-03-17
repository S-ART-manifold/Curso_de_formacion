# Análisis de Telemetría - CASE-01
## Bloque B0.3

### Eventos Detectados

Se detectaron **3 anomalías** durante la sesión de telemetría:

1. **EPS_LOW (360s → 450s)**: Voltaje de batería por debajo del umbral
   - Voltaje mínimo: 3.38V (umbral: 3.5V)
   - Duración: 90 segundos

2. **COMMS_DROP (600s → 620s)**: Pérdida de comunicaciones
   - Señal mínima: -93.7 dBm (umbral: -85 dBm)
   - Duración: 20 segundos

3. **THERMAL_HIGH (734s → 775s)**: Temperatura elevada
   - Temperatura máxima: 48.09°C (umbral: 45°C)
   - Duración: 41 segundos

### Análisis por Subsistema

**EPS (Sistema de Energía):**
El voltaje de batería descendió por debajo del umbral seguro durante 90 segundos. Esto indica que el sistema de potencia estaba bajo estrés, posiblemente por consumo excesivo o reducción de generación solar. Un voltaje sostenido bajo podría comprometer el funcionamiento de otros subsistemas.

**TT&C (Comunicaciones):**
Se detectó una pérdida de enlace de 20 segundos aproximadamente. La señal descendió a -93.7 dBm, lo que representa una degradación significativa. Este evento podría deberse a ocultación del satélite, interferencia, o desalineación de antenas.

**Térmico:**
La temperatura interna alcanzó 48.09°C, superando el umbral de 45°C durante 41 segundos. Aunque el evento fue puntual y de corta duración, indica que el control térmico fue insuficiente en ese período. Esto podría deberse a intensa radiación solar o actividad computacional.

### Acción del Operador

Como operador de la misión, **mi primera acción sería: Activar modo de ahorro de energía.**

Justificación: La anomalía de voltaje bajo es la más crítica porque afecta a todos los subsistemas. Activar el modo de ahorro reduciría el consumo, permitiendo que la batería se recupere. Las anomalías de comunicaciones y térmica parecen ser eventos puntuales y transitorios, por lo que no requieren acción inmediata.

### Conclusiones

El satélite experimentó estrés en sus subsistemas principales durante esta ventana de operación, pero ninguno de los eventos fue catastrófico. Los umbrales de detección fueron efectivos para identificar degradaciones. Se recomienda monitoreo continuo y posible ajuste del modo de operación si los eventos se repiten.