# Proyecto: Calculadora simple basada en microservicios

## Info de la materia

**Materia:** ST0263: Tópicos Especiales en Telemática  
**Estudiantes:**
- Jose Alejandro Duque Piedrahita - jaduquep@eafit.edu.co
- Pedro Saldarriaga Fontan - psaldarrif@eafit.edu.co
- Juan Pablo Zuluaga Pelaez - jpzuluagap@eafit.edu.co

**Profesor:** Alvaro Enrique Ospina Sanjuan - aeospinas@eafit.edu.co

---

# 1. Nombre del proyecto

**Calculadora Distribuida basada en Microservicios usando gRPC, REST y RabbitMQ**

## 1.1 Breve descripción de la actividad

Implementación de una aplicación distribuida con:
- Cliente REST
- API Gateway
- Microservicios gRPC
- Middleware orientado a mensajes (RabbitMQ)
- Contenerización completa con Docker

## 1.2 Aspectos cumplidos (requerimientos funcionales y no funcionales)

- Cliente REST funcional con FastAPI
- API Gateway desarrollado en FastAPI
- Microservicios independientes para suma, resta, multiplicación y división usando gRPC
- Integración de RabbitMQ como Message-Oriented Middleware (MOM)
- Implementación de consumidor RabbitMQ para operaciones fallidas
- Contenerización de todos los componentes con Docker
- Documentación automática de APIs con Swagger (FastAPI)
- Arquitectura desacoplada y escalable

## 1.3 Aspectos NO cumplidos

- El proyecto se completó con exito todos los aspectos.

---

# 2. Información general de diseño de alto nivel

- Arquitectura basada en microservicios
- API Gateway Pattern para centralización de solicitudes
- Comunicación eficiente entre servicios usando gRPC + Protocol Buffers
- RabbitMQ como broker de mensajes para tolerancia a fallos (MOM)
- Docker + Docker Compose para contenerización y orquestación
- Principios de bajo acoplamiento y alta cohesión

---

# 3. Ambiente de desarrollo y detalles técnicos

## 3.1 Tecnologías utilizadas

- **Lenguaje:** Python 3.11
- **Frameworks:**
  - FastAPI (REST y Gateway)
  - gRPC (microservicios)
  - RabbitMQ (MOM)
- **Librerías:**
  - grpcio, grpcio-tools
  - pika
- **Contenerización:** Docker 24.0
- **Broker:** RabbitMQ 3.9-management

## 3.2 Cómo se compila y ejecuta

```bash
git clone https://github.com/joseduquep/gRPC-Calculator.git
cd gRPC-Calculator
docker-compose up --build
docker-compse up
```

Servicios disponibles:
- Cliente REST: [http://localhost:8000/docs](http://localhost:8000/docs)
- RabbitMQ Admin: [http://localhost:15672](http://localhost:15672) (admin/admin)

## 3.3 Configuración de parámetros

Variables de entorno:
- `RABBIT_HOST=rabbitmq-broker`
- `RABBIT_USER=admin`
- `RABBIT_PASS=admin`

Puertos expuestos:
- Cliente REST: `8000`
- RabbitMQ AMQP: `5672`, Web: `15672`

## 3.4 Estructura de directorios

```bash
.
├── client_rest
├── gateway
├── sum_service
├── sub_service
├── mul_service
├── div_service
├── rabbitmq
├── docker-compose.yml
└── README.md
```

---

# 4. Ambiente de ejecución (producción)

## 4.1 Tecnologías utilizadas en producción

- Python 3.11
- Docker 24.0
- Docker Compose
- RabbitMQ 3.9-management


## 4.2 Cómo lanzar el servidor

```bash
git clone https://github.com/joseduquep/gRPC-Calculator.git
cd gRPC-Calculator
docker-compose up -d
```

## 4.3 Mini guía de uso
![image](https://github.com/user-attachments/assets/f94eedf7-5a75-4470-a7f4-e1f06d914f23)


1. Ingresar a [http://18.208.223.92:8000/docs](http://18.208.223.92:8000/docs)
2. Ejecutar operaciones:
   - `/sum` suma
   - `/sub` resta
   - `/mul` multiplicación
   - `/div` división
3. Consultar mensajes pendientes en [http://18.208.223.92:15672](http://18.208.223.92:15672)

---

# 5. Credenciales de Acceso en AWS

- jpzuluagap@eafit.edu.co
- Aws1234*

![image](https://github.com/user-attachments/assets/cbb46cc0-528f-4f02-8a3a-16d00fc262f3)


  ![image](https://github.com/user-attachments/assets/b5b7a06f-a17e-4fe6-9d2a-b0d52a35bb9e)

---

# 6. Referencias

- Curso Fundamentos Básicos de Docker - Platzi
- FastAPI & Swagger - Documentación oficial y asistencia ChatGPT
- [gRPC Python Documentation](https://grpc.io/docs/languages/python/)
- [RabbitMQ Documentation](https://www.rabbitmq.com/documentation.html)
- "Middleware for Communications" - Qusay H. Mahmoud

---

