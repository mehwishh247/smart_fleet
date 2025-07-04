# Smart Fleet (FastAPI Backend)

A lightweight vehicle, sensor, and driver management API built with FastAPI, using in-memory storage.

## Features
- Full CRUD routes for vehicles, drivers, and sensors
- FastAPI models and validation
- Modular project structure
- .env config and CORS enabled

## To Run
```bash
poetry install
uvicorn smart_fleet.main:app --reload
