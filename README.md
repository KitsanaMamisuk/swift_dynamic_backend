# School REST API System

โปรเจคนี้เป็นระบบ REST API สำหรับจัดการข้อมูลโรงเรียน พัฒนาด้วย Django REST Framework และใช้ PostgreSQL เป็นฐานข้อมูล รันบน Docker เพื่อความสะดวกในการพัฒนาและ deployment

## 🚀 ขั้นตอนการติดตั้ง

### ข้อกำหนดเบื้องต้น
- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/get-started) และ [Docker Compose](https://docs.docker.com/compose/install/) (ถ้าใช้วิธีติดตั้งแบบ Docker)
- [Python](https://www.python.org/downloads/) เวอร์ชัน 3.8 หรือสูงกว่า (ถ้าใช้วิธีติดตั้งแบบไม่ใช้ Docker)
- [PostgreSQL](https://www.postgresql.org/download/) (ถ้าใช้วิธีติดตั้งแบบไม่ใช้ Docker)

### 1. โคลนโปรเจค
```bash
git clone https://github.com/KitsanaMamisuk/swift_dynamic_backend.git
cd swift_dynamic_backend/5_rest_api
```

## 🚀 เริ่มต้นใช้งาน (Quick Start)

### สำหรับผู้ใช้ Docker (แนะนำ)
```bash
# 1. โคลนโปรเจค
git clone https://github.com/KitsanaMamisuk/swift_dynamic_backend.git
cd swift_dynamic_backend/5_rest_api

# 2. สร้างและรันคอนเทนเนอร์
make build
make up

# 3. รันการ migrate และเริ่มใช้งาน
make migrate

# 4. เพิ่มข้อมูลเริ่มต้น (ถ้าต้องการ)
make init_data
make run-backend
```

### สำหรับผู้ไม่ใช้ Docker
```bash
# 1. โคลนโปรเจค
git clone https://github.com/KitsanaMamisuk/swift_dynamic_backend.git
cd swift_dynamic_backend/5_rest_api

# 2. ตั้งค่า virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# หรือ
venv\Scripts\activate     # Windows

# 3. ติดตั้ง dependencies
pip install -r requirements.txt

# 4. ตั้งค่าฐานข้อมูล PostgreSQL และสร้างไฟล์ .env

# 5. รัน migrate และเริ่มเซิร์ฟเวอร์
python manage.py migrate

# 6. เพิ่มข้อมูลเริ่มต้น (ถ้าต้องการ)
python manage.py init_data
python manage.py runserver
```

เข้าถึง API ที่ http://localhost:8000/api/v1/ และเอกสาร API ที่ [api-documentation.html](./api-documentation.html)

## 📋 คำสั่งที่มีให้ใช้งาน

### คำสั่งสำหรับ Docker (Makefile)
| คำสั่ง | คำอธิบาย |
|-------|----------|
| `make up` | สร้างและเริ่มต้นคอนเทนเนอร์แบบ detached mode |
| `make down` | หยุดและลบคอนเทนเนอร์ พร้อมทั้งลบ orphaned containers |
| `make build` | สร้าง Docker image ใหม่ |
| `make run-backend` | รัน Django application ด้วย uvicorn พร้อม hot-reload |
| `make migrations` | สร้างไฟล์ migrations สำหรับการเปลี่ยนแปลงโมเดล |
| `make migrate` | อัพเดทฐานข้อมูลตาม migrations |
| `make delete-migrations` | ลบไฟล์ migrations ทั้งหมด (ยกเว้น __init__.py) |
| `make reset-db` | รีเซ็ตฐานข้อมูลและรัน migrations ใหม่ทั้งหมด |
| `make init_data` | สร้างข้อมูลเริ่มต้นในฐานข้อมูล |
| `make gen-swagger-json` | สร้างไฟล์ Swagger JSON สำหรับ API documentation |
| `make collectstatic` | รวบรวมไฟล์ static สำหรับ production |

### คำสั่งสำหรับการพัฒนาแบบไม่ใช้ Docker (Django Management Commands)
| คำสั่ง | คำอธิบาย |
|-------|----------|
| `python manage.py runserver` | รัน Django development server |
| `python manage.py makemigrations` | สร้างไฟล์ migrations สำหรับการเปลี่ยนแปลงโมเดล |
| `python manage.py migrate` | อัพเดทฐานข้อมูลตาม migrations |
| `python manage.py init_data` | สร้างข้อมูลเริ่มต้นในฐานข้อมูล |
| `python manage.py generate_swagger --format json --output api-docs.json` | สร้างไฟล์ Swagger JSON สำหรับ API documentation |
| `python manage.py collectstatic` | รวบรวมไฟล์ static สำหรับ production |
| `python manage.py createsuperuser` | สร้าง superuser สำหรับ admin interface |

## 🏗️ โครงสร้างของโปรเจค

```
.
├── api_exam.md              # เอกสารข้อกำหนดสำหรับการพัฒนา API
├── api-docs.json            # เอกสาร Swagger JSON สำหรับ API
├── api-documentation.html   # เอกสาร HTML สำหรับ API
├── apis                     # แอปพลิเคชัน Django สำหรับ API endpoints
│   ├── __init__.py
│   ├── admin.py             # การกำหนดค่า Django admin
│   ├── apps.py              # การกำหนดค่าแอปพลิเคชัน
│   ├── choices.py           # ค่าคงที่และตัวเลือกต่างๆ
│   ├── filters.py           # ฟิลเตอร์สำหรับ API
│   ├── management           # คำสั่งเฉพาะสำหรับการจัดการ
│   │   ├── __init__.py
│   │   └── commands
│   │       ├── __init__.py
│   │       ├── generate_swagger.py    # คำสั่งสำหรับสร้าง Swagger documentation
│   │       └── init_data.py           # คำสั่งสำหรับเพิ่มข้อมูลเริ่มต้น
│   ├── migrations           # ไฟล์ migrations สำหรับฐานข้อมูล
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   ├── models.py            # โมเดลฐานข้อมูล
│   ├── serializers.py       # Serializers สำหรับ API
│   ├── tests.py             # การทดสอบ
│   ├── urls.py              # URL routing
│   └── views                # API views ตามเวอร์ชัน
│       ├── __init__.py
│       └── v1
│           ├── __init__.py
│           ├── classroom.py # Endpoints เกี่ยวกับห้องเรียน
│           ├── school.py    # Endpoints เกี่ยวกับโรงเรียน
│           ├── student.py   # Endpoints เกี่ยวกับนักเรียน
│           └── teacher.py   # Endpoints เกี่ยวกับครู
├── docker-compose.yml       # การกำหนดค่า Docker Compose
├── Dockerfile               # การกำหนดค่า Docker image
├── exam_app                 # แพ็คเกจหลักของแอปพลิเคชัน Django
│   ├── __init__.py
│   ├── asgi.py              # ASGI configuration
│   ├── settings.py          # การตั้งค่าโปรเจค
│   ├── urls.py              # URL routing หลัก
│   └── wsgi.py              # WSGI configuration
├── Makefile                 # คำสั่งสำหรับอำนวยความสะดวก
├── manage.py                # Django command-line utility
└── requirements.txt         # Python dependencies
```

## 🔑 Environments

ตัวแปรสภาพแวดล้อมหลักที่ใช้ในโปรเจคนี้:

| ตัวแปร | คำอธิบาย |
|-------|----------|
| `POSTGRES_USER` | ชื่อผู้ใช้สำหรับฐานข้อมูล PostgreSQL (default: postgres) |
| `POSTGRES_PASSWORD` | รหัสผ่านสำหรับฐานข้อมูล PostgreSQL (default: P@ssw0rd) |
| `POSTGRES_DB` | ชื่อฐานข้อมูล PostgreSQL (default: db_school) |


## 📚 API Documentation

โปรเจคนี้มีเอกสาร API ให้แล้วในไฟล์ต่อไปนี้:

1. `api-docs.json` - เอกสาร Swagger JSON
2. `api-documentation.html` - เอกสาร HTML ที่แสดงผลลัพธ์จาก Swagger JSON

หากต้องการสร้างเอกสาร Swagger JSON ใหม่ ใช้คำสั่ง:
```bash
# ถ้าใช้ Docker
make gen-swagger-json

# ถ้าไม่ใช้ Docker
python manage.py generate_swagger --format json --output api-docs.json
```

### API Endpoints ที่สำคัญ

โปรเจคนี้มี API endpoints แบ่งตามหมวดหมู่ดังนี้:

#### School
- `GET /api/v1/schools/` - รายการโรงเรียนทั้งหมด
- `POST /api/v1/schools/` - สร้างโรงเรียนใหม่
- `GET /api/v1/schools/{id}/` - ดูรายละเอียดโรงเรียน
- `PUT /api/v1/schools/{id}/` - อัพเดทโรงเรียน
- `DELETE /api/v1/schools/{id}/` - ลบโรงเรียน

#### Classroom
- `GET /api/v1/classrooms/` - รายการห้องเรียนทั้งหมด
- `POST /api/v1/classrooms/` - สร้างห้องเรียนใหม่
- `GET /api/v1/classrooms/{id}/` - ดูรายละเอียดห้องเรียน
- `PUT /api/v1/classrooms/{id}/` - อัพเดทห้องเรียน
- `DELETE /api/v1/classrooms/{id}/` - ลบห้องเรียน

#### Teacher
- `GET /api/v1/teachers/` - รายการครูทั้งหมด
- `POST /api/v1/teachers/` - สร้างครูใหม่
- `GET /api/v1/teachers/{id}/` - ดูรายละเอียดครู
- `PUT /api/v1/teachers/{id}/` - อัพเดทครู
- `DELETE /api/v1/teachers/{id}/` - ลบครู

#### Student
- `GET /api/v1/students/` - รายการนักเรียนทั้งหมด
- `POST /api/v1/students/` - สร้างนักเรียนใหม่
- `GET /api/v1/students/{id}/` - ดูรายละเอียดนักเรียน
- `PUT /api/v1/students/{id}/` - อัพเดทนักเรียน
- `DELETE /api/v1/students/{id}/` - ลบนักเรียน

รายละเอียดเพิ่มเติมของ API สามารถดูได้ในเอกสาร API ที่อยู่ในโปรเจค
