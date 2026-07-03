# Uso - Guía de Utilización

## Inicio rápido

### 1. Preparar datos

Crea `data/figuritas.json` con estructura:

```json
{
  "figuritas": [
    {
      "id": 1,
      "numero": 1,
      "nombre": "Lionel Messi",
      "equipo": "Argentina",
      "posicion": "Delantero",
      "pais": "Argentina",
      "imagen_path": "path/to/image.jpg",
      "rareza": "Común",
      "brillo": false
    }
  ]
}
```

### 2. Agregar fotos

Coloca las imágenes en `input/fotos/` con nombres `{id}.jpg`

### 3. Generar PDFs

```bash
python -m src.cli generate \
  --data data/figuritas.json \
  --fotos input/fotos \
  --output output/pdf
```

### 4. Resultados

Los PDFs se guardan en `output/pdf/`:
- `hoja_001.pdf` - Primera hoja (16 figuritas)
- `hoja_002.pdf` - Segunda hoja
- `coleccion_completa.pdf` - Todas combinadas

## Opciones avanzadas

### Personalizar dimensiones

Edita `config/config.py`:

```python
@dataclass
class FigoritaConfig:
    WIDTH_MM: float = 50  # Ancho en mm
    HEIGHT_MM: float = 70  # Alto en mm
```

### Personalizar colores

Edita `config/config.py`:

```python
@dataclass
class ColorConfig:
    COLORS: dict = {
        "Argentina": "#87CEEB",
        "Brasil": "#00AA00",
        # ...
    }
```

### Mejorar imágenes

Edita `config/config.py`:

```python
@dataclass
class ProcessingConfig:
    ENABLE_CLAHE: bool = True
    ENABLE_BILATERAL_FILTER: bool = True
    ENABLE_UNSHARP_MASK: bool = True
```

## Troubleshooting

### Error: "No se puede cargar imagen"

- Verifica que las imágenes existan en `input/fotos/`
- Verifica que el nombre sea `{id}.jpg`
- Verifica que el formato sea soportado (JPG, PNG)

### Error: "Módulo no encontrado"

```bash
pip install -r requirements-prod.txt
```

### Generar lentamente

- Reduce resolución DPI en `config/config.py`
- Reduce el número de figuritas
- Desactiva filtros de imagen

## Performance

Ejecutar benchmark:

```bash
python scripts/benchmark.py
```
