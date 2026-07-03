# 🎫 Figuritas Mundial 2026 - Generador Profesional de Figuritas Coleccionables

Aplicación profesional para generar hojas de figuritas estilo álbum de Mundial con **calidad de impresión (600 DPI renderizado, PDF/X-3 compliant)**.

## ✨ Características

- ✅ **Detección inteligente de rostros** con MediaPipe + OpenCV
- ✅ **Procesamiento de imagen avanzado** (restauración, CLAHE, anti-aliasing)
- ✅ **Renderizado profesional** a 600 DPI con sobremuestreo 2x
- ✅ **Tipografía perfecta** con Google Fonts (kerning, ligaduras)
- ✅ **PDF/X-3 compliant** listo para imprenta offset
- ✅ **Grilla 4×4** (16 figuritas por hoja A4 exacto)
- ✅ **Crop marks** y sangría de corte profesionales
- ✅ **Soporte CMYK** para impresión a color
- ✅ **Multipágina automática** si hay más de 16 figuritas
- ✅ **Template HTML/CSS customizable**

## 🚀 Quick Start

### 1. Instalación

```bash
git clone https://github.com/dylandavi06/Figuritas-mundial-2026.git
cd Figuritas-mundial-2026

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements-prod.txt

# Descargar Google Fonts
python scripts/download_fonts.py
```

### 2. Preparar datos

**data/figuritas.json:**
```json
{
  "album_info": {
    "titulo": "Mi Álbum Mundial 2026",
    "total_figuritas": 440,
    "ano": 2026
  },
  "figuritas": [
    {
      "numero": 1,
      "nombre": "Lionel Messi",
      "tipo": "jugador",
      "equipo": "Argentina",
      "posicion": "Delantero",
      "numero_camiseta": 10,
      "foto": "messi.jpg",
      "color_fondo": "#87CEEB",
      "especial": false
    },
    {
      "numero": 2,
      "nombre": "Mi Amigo Juan",
      "tipo": "amigo",
      "equipo": null,
      "posicion": "Portero",
      "numero_camiseta": 1,
      "foto": "juan.jpg",
      "color_fondo": "#FFD700",
      "especial": false
    }
  ]
}
```

**input/fotos/:** Coloca aquí tus JPG/PNG

### 3. Generar PDF

```bash
python -m src.cli generar
```

Output:
- `output/figuritas_mundial2026_completo.pdf` (todas las hojas)
- `output/figuritas_mundial2026_hoja-1.pdf` (hoja 1)
- `output/figuritas_mundial2026_hoja-2.pdf` (hoja 2)
- etc.

## 📋 Especificaciones Técnicas

| Parámetro | Valor |
|-----------|-------|
| **Resolución** | 600 DPI renderizado + sobremuestreo 2x |
| **Tamaño hoja** | A4 exacto (210 × 297 mm) |
| **Grilla** | 4 columnas × 4 filas |
| **Tamaño figurita** | 50 × 70 mm |
| **Espaciado** | 2.5 mm entre figuritas |
| **Márgenes** | 10 mm |
| **Sangría de corte** | 3 mm (bleed) |
| **Crop marks** | Líneas de corte profesionales |
| **Color** | RGB/CMYK (configurable) |
| **PDF Standard** | PDF/X-3 compliant |

## 📁 Estructura del Proyecto

```
Figuritas-mundial-2026/
├── src/
│   ├── cli.py                 # Interfaz de línea de comandos
│   ├── data_loader.py         # Carga y valida JSON
│   ├── image_processor.py     # Procesamiento de imágenes
│   ├── figurita_generator.py  # Renderizado de figurita
│   ├── sheet_builder.py       # Construcción de grilla
│   ├── pdf_renderer.py        # Generación de PDF
│   ├── merger.py              # Combina PDFs
│   └── utils.py               # Utilidades
├── templates/
│   ├── figurita.html          # Template de figurita
│   └── sheet.html             # Template de hoja
├── config/
│   ├── config.py              # Configuración global
│   ├── color_profiles.py      # Perfiles ICC y colores
│   └── typography.py          # Tipografía
├── data/
│   └── figuritas.json         # 👈 Tus figuritas aquí
├── input/
│   └── fotos/                 # 👈 Tus fotos aquí
├── output/                    # 👈 PDFs generados aquí
├── assets/
│   ├── fonts/                 # Google Fonts
│   ├── backgrounds/           # Texturas opcionales
│   └── flags/                 # Banderas (si las necesitas)
├── scripts/
│   ├── download_fonts.py      # Descarga Google Fonts
│   └── benchmark.py           # Mide performance
├── tests/
│   ├── conftest.py
│   ├── test_data_loader.py
│   └── test_image_processor.py
├── docs/
│   ├── SETUP.md               # Instalación detallada
│   ├── USAGE.md               # Guía de uso
│   ├── TEMPLATE_CUSTOMIZATION.md
│   └── COLOR_PROFILES.md
├── requirements-prod.txt
├── requirements-dev.txt
├── pyproject.toml
├── setup.py
└── README.md
```

## 📝 Formato de datos (figuritas.json)

### Campos obligatorios:
- `numero`: int (1-440+)
- `nombre`: string (nombre jugador/amigo)
- `tipo`: "jugador" | "amigo"
- `foto`: string (nombre archivo en input/fotos/)

### Campos opcionales:
- `equipo`: string (país/club, se usa para color automático)
- `posicion`: string (Portero, Defensa, Mediocampista, Delantero)
- `numero_camiseta`: int (1-99)
- `color_fondo`: string HEX (#RRGGBB) o nombre de equipo
- `especial`: boolean (true = efecto holográfico)

## 🎨 Colores Predefinidos por Equipo

```json
"equipo": "Argentina"     // Automático: #87CEEB (celeste)
"equipo": "Brasil"        // Automático: #00AA00 (verde)
"equipo": "Francia"       // Automático: #4169E1 (azul)
"equipo": "Alemania"      // Automático: #FFFFFF (blanco)
"equipo": "España"        // Automático: #FFC400 (amarillo)
```

O especifica color manualmente:
```json
"color_fondo": "#FF6B6B"  // Rojo personalizado
```

## 🔧 Configuración Avanzada

Edita `config/config.py` para:
- Resolución DPI (300, 600, etc.)
- Dimensiones de figuritas
- Márgenes y espaciado
- Paleta de colores
- Perfiles ICC CMYK

## 🧪 Testing

```bash
# Instalar dev dependencies
pip install -r requirements-dev.txt

# Ejecutar tests
pytest tests/ -v

# Con cobertura
pytest tests/ --cov=src
```

## 📊 Benchmarks

```bash
python scripts/benchmark.py
```

Mide:
- Tiempo de detección de rostros
- Calidad de imagen procesada
- Tiempo de renderizado PDF
- Tamaño final de archivos

## 📦 Dependencias Principales

| Librería | Uso |
|----------|-----|
| **WeasyPrint** | Renderizado HTML/CSS a PDF profesional |
| **MediaPipe** | Detección de rostros inteligente |
| **OpenCV** | Procesamiento avanzado de imágenes |
| **Pillow (PIL)** | Manipulación de imágenes |
| **scikit-image** | Filtros y restauración |
| **Click** | Interfaz CLI elegante |
| **Jinja2** | Templates HTML |
| **Pydantic** | Validación de datos |

## 🚨 Troubleshooting

### Error: "No module named 'weasyprint'"
```bash
pip install weasyprint
```

### Error: "Face not detected"
La app sigue funcionando pero usa la imagen completa. Es warning, no error.

### PDF pixelado
Asegúrate que fotos tengan al menos 150 DPI. Ver warning en consola.

### Tipografía no renderiza
Ejecuta `python scripts/download_fonts.py` nuevamente.

## 📖 Documentación Completa

- **[SETUP.md](docs/SETUP.md)** - Instalación paso a paso
- **[USAGE.md](docs/USAGE.md)** - Guía completa de uso
- **[TEMPLATE_CUSTOMIZATION.md](docs/TEMPLATE_CUSTOMIZATION.md)** - Personalizar template
- **[COLOR_PROFILES.md](docs/COLOR_PROFILES.md)** - CMYK/ICC profiles

## 📄 Licencia

**Personal use only.** No redistribuir marcas registradas de FIFA o editoriales. Usar solo para colecciones personales.

---

**Generado con ❤️ para coleccionistas de figuritas** 🎫

👉 **¿Primera vez?** Ver [docs/SETUP.md](docs/SETUP.md)
