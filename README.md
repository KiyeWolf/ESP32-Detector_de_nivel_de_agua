Sistema de Monitoreo de Nivel de Agua con ESP32  

Este proyecto implementa un sistema de monitoreo de nivel de agua utilizando un **ESP32**, un **sensor ultrasónico**, un **servo motor** y un **display de 7 segmentos**. Además, cuenta con conectividad WiFi mediante **MQTT Adafruit**, permitiendo visualizar los datos desde un celular y activar una descarga del tanque de forma remota.  
---
**Componentes Utilizados**  
- ESP32 
- Sensor Ultrasónico HC-SR04 (para medir el nivel de agua)  
- Servo Motor (simula la válvula de descarga del tanque)  
- Display de 7 segmentos (TM1637) (muestra el nivel de agua)  
- Conexión WiFi (MQTT Adafruit para enviar datos al celular)  
---
**¿Cómo funciona?**  
1. El **sensor de ultrasonido** mide la distancia del agua al sensor y calcula el nivel de profundidad del tanque.  
2. El **display** muestra el nivel de agua en tiempo real.  
3. Los datos se envían a la **plataforma MQTT de Adafruit**, donde pueden ser consultados desde un celular.  
4. Si el usuario envía una señal desde su celular, el **servo motor** gira, simulando la descarga del tanque.  
---
Pruebas y Resultados
Se realizaron pruebas con los componentes físicos y la comunicación con MQTT, exceptuando el display de 7 segmentos porque en ese momento no había disponibilidad para utilizarlo (Sin embargo es funcional todo lo demás).
En la carpeta .pruebas se incluyen imágenes y un video mostrando el funcionamiento del servo y la conexión wifi en tiempo real.

Si quieres usarlo puedes:
Clonar el repositorio y carga el código en el ESP32 usando una herramienta como Thonny o Wokwi.
Conéctalo a una red WiFi y configúralo en Adafruit IO para la conexión MQTT.
¡Listo! Visualiza el nivel de agua desde tu celular y activa la descarga con un solo click.


Este proyecto fue realizado para la materia Fundamentos de los sistemas embebidos de la carrera Ingeniería informática, en la Universidad Nacional de La Matanza.
