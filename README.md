# gRPC-Calculator

**gRPC-Calculator** es una implementacion academica para el entendimiento de la arquitectura basada en microservicios. Es una calculadora distribuida utilizando gRPC y RabbitMQ. Cada operación aritmética básica (suma, resta, multiplicación y división) se maneja mediante un microservicio independiente, lo que permite escalabilidad y mantenimiento modular.

## Tabla de Contenidos

- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Notas Adicionales](#notas-adicionales)
- [Licencia](#licencia)

## Estructura del Proyecto

El proyecto está organizado en los siguientes directorios y archivos principales:

- **client_rest/**: Cliente REST construido con FastAPI que interactúa con el gateway para realizar operaciones aritméticas.
- **gateway/**: Puerta de enlace que recibe solicitudes del cliente REST y las dirige a los microservicios correspondientes a través de RabbitMQ.
- **sum_service/**: Microservicio que maneja operaciones de suma.
- **sub_service/**: Microservicio que maneja operaciones de resta.
- **mul_service/**: Microservicio que maneja operaciones de multiplicación.
- **div_service/**: Microservicio que maneja operaciones de división.
- **rabbitmq/**: Configuración y consumidor de RabbitMQ para manejar la cola de mensajes entre el gateway y los microservicios.
- **docker-compose.yml**: Archivo de configuración para Docker Compose que orquesta todos los servicios del proyecto.

## Requisitos Previos

Antes de instalar y ejecutar el proyecto, asegúrate de tener instalados los siguientes componentes:

- **Docker**: Para crear y gestionar contenedores.
- **Docker Compose**: Para orquestar múltiples contenedores.

Además, si estás utilizando **Windows**, es necesario:

- **WSL2 (Windows Subsystem for Linux 2)**: Para ejecutar entornos Linux en Windows y permitir la integración con Docker.

## Instalación

Sigue estos pasos para instalar y ejecutar el proyecto:

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/joseduquep/gRPC-Calculator.git
