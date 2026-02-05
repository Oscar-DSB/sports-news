# 📰 SportsNews (Django Web App)

SportsNews es una aplicación web desarrollada con **Django** que permite consultar información deportiva organizada por deportes y partidos.

Proyecto realizado como práctica universitaria dentro de la asignatura de **Programación Web con Django**.

---

## 🚀 Funcionalidades principales

- Página principal con deportes disponibles mediante tarjetas visuales
- Visualización de partidos/eventos organizados por estado:
  - Partidos anteriores
  - Partidos de hoy
  - Próximos eventos
- Vista especial para Fórmula 1 con clasificación de pilotos y calendario de grandes premios
- Sistema de autenticación integrado (login/logout)
- Vista **Members** accesible únicamente para administradores, mostrando la actividad de usuarios

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Django 5.2
- HTML5 + CSS3
- SQLite (modo desarrollo)
- Django Templates (arquitectura MVT)

---

## 📂 Estructura del proyecto

El proyecto está dividido en dos apps principales:

- `sports/` → lógica principal de deportes y partidos
- `social/` → autenticación y vista Members (solo admins)

---

## ⚙️ Instalación y ejecución (entorno virtual obligatorio)

Para ejecutar correctamente el proyecto es necesario crear un entorno virtual.

### 1. Clonar el repositorio

git clone https://github.com/Oscar-DSB/sports-news.git
cd sports-news

---

### 2. Crear entorno virtual (myworld)

python -m venv myworld

---

### 3. Activar entorno virtual

En Windows (PowerShell):

myworld\Scripts\Activate

Cuando esté activado verás:

(myworld) PS C:\...

---

### 4. Instalar dependencias

pip install -r requirements.txt

---

### 5. Aplicar migraciones

python manage.py migrate

---

### 6. Crear superusuario (opcional)

Para acceder al panel admin:

python manage.py createsuperuser

---

### 7. Ejecutar servidor

python manage.py runserver

Abrir en el navegador:

http://127.0.0.1:8000/

---

## 🔑 Roles de usuario

- Usuario normal → puede navegar por la aplicación
- Administrador (`is_staff`) → puede acceder a:
  - /admin/
  - /members/

---

## 📄 Documentación y demostración

- 📘 Memoria del proyecto (PDF):
  👉 [Descargar Memoria SportsNews](/docs/Memoria_Practica4_SportsNews_Oscar.pdf)

- 🎥 Vídeo de demostración:
  👉 [Descargar Video SportsNews](/docs/Video%20SportsNews.mp4)

---

## 👤 Autor

Desarrollado por **Oscar De Simone**  
Universidad Francisco de Vitoria (UFV)  
Ingeniería de la Industria Conectada 4.0
