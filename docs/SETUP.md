# Setup - Guía de Instalación

## Requisitos

- Python 3.10+
- pip o poetry
- Sistema operativo: Linux, macOS o Windows

## Instalación

### 1. Clonar repositorio

```bash
git clone https://github.com/dylandavi06/Figuritas-mundial-2026.git
cd Figuritas-mundial-2026
```

### 2. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
# Producción
pip install -r requirements-prod.txt

# Desarrollo (opcional)
pip install -r requirements-dev.txt
```

### 4. Descargar fuentes

```bash
python scripts/download_fonts.py
```

### 5. Inicializar estructura

```bash
python -m src.cli init
```

## Estructura de directorios

```
Figuritas-mundial-2026/
├── config/              # Configuración
├── src/                 # Código fuente
├── templates/           # Templates HTML
├── scripts/             # Scripts utilitarios
├── tests/               # Tests unitarios
├── docs/                # Documentación
├── data/                # Datos JSON
├── input/
│   └── fotos/          # Fotos de entrada
├── output/
│   ├── pdf/            # PDFs generados
│   └── preview/        # Previsualizaciones
└── assets/
    └── fonts/          # Fuentes descargadas
```

## Verificación

```bash
python -m pytest tests/
```
