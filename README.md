# 🎮 FastAPI Games CRUD

Este es un proyecto simple que implementa un **CRUD de videojuegos** utilizando [FastAPI](https://fastapi.tiangolo.com/) como framework backend y **Firebase Firestore** como base de datos NoSQL.

Es ideal para practicar el uso de FastAPI y la integración con Firebase mediante el SDK Admin de Python.

Puedes ver la documentacion desplegada aqui:

- [FastApiCrud /docs](https://fast-api-crud-zeta.vercel.app/docs)
- [FastApiCrud /redoc](https://fast-api-crud-zeta.vercel.app/redoc)

## 📁 Estructura del Proyecto

```
├── main.py # Contiene todas las rutas y lógica del CRUD
├── requirements.txt # Dependencias necesarias para el entorno
├── README.md # Este archivo 📝
└── .env
```

## ⚙️ Instalación

1. Clona el repositorio:

```
git clone git@github.com:JSebastianMarin/FastApiCRUD.git
```

2. (Opcional) Crea un entorno virtual:

```
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:

```
pip install -r requirements.txt
```

4. Guarda tus credenciales de firebase firestore en tu archivo `.env`, donde debe estar guardado como un string de solo una linea. Puedes hacerlo siguiendo este comando

```
cat [tu_archivo_credenciales].json
```

La salida la puedes copiar y pegar directamente en el `.env`

## ▶️ Ejecución

Corre la aplicación con:

```
fastapi dev main.py
```

Esto iniciará el servidor en http://127.0.0.1:8000

También puedes acceder a la documentación interactiva generada automáticamente en:

- 📚 http://127.0.0.1:8000/docs
- 📚 http://127.0.0.1:8000/redoc

## 📚 Endpoints disponibles

| Metodo | Endpoint           | Descripcion                   |
| ------ | ------------------ | ----------------------------- |
| GET    | `/games/`          | Obtener todos los juegos      |
| GET    | `/games/{game_id}` | Obtener un juego por ID       |
| POST   | `/games/`          | Crear un nuevo juego          |
| PUT    | `/games/{game_id}` | Actualizar un juego existente |
| DELETE | `/games/{game_id}` | Eliminar un juego             |

## 🧠 Aprendizajes

Este proyecto es una buena práctica para:

- Crear APIs REST con FastAPI
- Validar datos con Pydantic
- Conectarse a Firebase Firestore desde Python
- Organizar rutas y modelos en un único archivo

## Integrantes

- [Jose Luis Ramos Arango](https://github.com/RamSterB) - [Email](mailto:jose.luis.ramos@correounivalle.edu.co)
- [Juan Sebastian Marin Serna](https://github.com/JSebastianMarin) - [Email](mailto:juan.marin.serna@correounivalle.edu.co)
