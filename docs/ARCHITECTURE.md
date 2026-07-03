# Arquitectura

## Componentes principales

### 1. Config (`config/`)
- **config.py**: Configuración centralizada (dimensiones, colores, fuentes)
- **color_profiles.py**: Gestión de espacios de color
- **typography.py**: Configuración tipográfica y estilos CSS

### 2. Source (`src/`)
- **utils.py**: Utilidades generales (DataLoader, PathManager)
- **data_loader.py**: Carga dataset de figuritas desde JSON
- **image_processor.py**: Procesamiento de imágenes (detección de rostros, mejora)
- **figurita_generator.py**: Renderiza figurita individual
- **sheet_builder.py**: Construye grillas 4x4 de figuritas
- **pdf_renderer.py**: Convierte imágenes a PDF
- **cli.py**: Interfaz de línea de comandos

### 3. Templates (`templates/`)
- **figurita.html**: Template de figurita individual
- **sheet.html**: Template de hoja completa

### 4. Scripts (`scripts/`)
- **download_fonts.py**: Descarga Google Fonts
- **benchmark.py**: Mide performance

## Flujo de procesamiento

```
1. JSON -> FigoritasDataset (data_loader.py)
   |
2. Carga imágenes (image_processor.py)
   |
3. Procesa (CLAHE, bilateral filter, unsharp mask)
   |
4. Genera figurita individual (figurita_generator.py)
   |
5. Construye grilla 4x4 (sheet_builder.py)
   |
6. Convierte a PDF (pdf_renderer.py)
   |
7. Combina múltiples PDFs
```

## Dependencias externas

- **WeasyPrint**: Renderizado HTML -> PDF
- **Pillow**: Manipulación de imágenes
- **OpenCV**: Procesamiento de imágenes
- **MediaPipe**: Detección de objetos (opcional)
- **Click**: CLI framework
- **Loguru**: Logging estructurado
- **Pydantic**: Validación de modelos

## Consideraciones de performance

- Las imágenes se procesan en paralelo (posible mejora)
- PDF se renderiza con WeasyPrint (relativamete rápido)
- La detección de rostros es costosa (puede desactivarse)
