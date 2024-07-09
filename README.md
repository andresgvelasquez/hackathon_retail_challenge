# Hackathon Retail Challenge Edition

Este proyecto está diseñado para hacer análisis estadístico en segmentación de clientes y así facilitar el filtrado de un universo de compradores a audiencias que realmente pueden convertirse en compradores y generar leads de ventas.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Fases del Proyecto](#fases-del-proyecto)
  - [Análisis del Dataset](#análisis-del-dataset)
  - [Estadística Descriptiva](#estadística-descriptiva)
  - [Segmentación](#segmentación)
  - [Predicción](#predicción)
  - [Clustering](#clustering)
  - [Conclusiones](#conclusiones)
  - [Visualización](#visualización)
- [Contribuir](#contribuir)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Instalación

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    cd tu-repositorio
    ```

2. Crear y activar un entorno virtual (opcional pero recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. Instalar las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para ejecutar el proyecto, sigue estos pasos:

1. Construir y levantar los contenedores de Docker:
    ```bash
    docker-compose up --build
    ```

2. Acceder a la web de Django para cargar el archivo CSV:
    - La aplicación web estará disponible en `http://localhost:8000`, se aloja en el contenedor *django*. 
    - Sube el archivo CSV a través de la interfaz web. La ubicación es: ./datasets/input/Online_Retail.csv

3. El archivo CSV será procesado y cargado en una base de datos PostgreSQL alojada en otro contenedor *postgresql*.

4. Visualizar la base de datos a través de pgAdmin:
    - pgAdmin estará disponible en `http://localhost:5050`, se aloja en el contendor *pgadmin*.
    - Accede con las credenciales configuradas y verifica los datos cargados en la base de datos PostgreSQL.

## Fases del Proyecto

### Análisis del Dataset

- Descripción del dataset y su estructura.
- Análisis inicial para comprender las características principales de los datos.

### Estadística Descriptiva

- Aplicación de técnicas de estadística descriptiva para resumir y entender los datos.

### Segmentación

- Metodologías de segmentación utilizadas para dividir los datos en grupos significativos.

### Predicción

- Uso de modelos predictivos para anticipar comportamientos y tendencias futuras.

### Clustering

- Aplicación de técnicas de clustering para agrupar datos similares.

### Conclusiones

- Resumen de los hallazgos y conclusiones derivadas del análisis.

### Visualización

- Generación de gráficos y visualizaciones para ilustrar los resultados del análisis.

## Contribuir

Las contribuciones son bienvenidas. Sigue estos pasos para contribuir:

1. Hacer un fork del proyecto.
2. Crear una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Hacer commit de tus cambios (`git commit -m 'Agregar nueva característica'`).
4. Hacer push a la rama (`git push origin feature/nueva-caracteristica`).
5. Abrir un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

- Andrés González  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/andres946/)
[![Correo Electrónico](https://img.shields.io/badge/Correo%20Electrónico-andresgvelasquez8@gmail.com-red?style=for-the-badge&logo=mail.ru)](mailto:andresgvelasquez8@gmail.com) 