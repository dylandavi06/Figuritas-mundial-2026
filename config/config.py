"""
Configuración global de la aplicación.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class PageConfig:
    """Configuración de página A4."""
    WIDTH_MM: float = 210
    HEIGHT_MM: float = 297
    DPI_EXPORT: int = 300
    DPI_RENDER: int = 600
    OVERSAMPLE: float = 2.0
    
    def mm_to_px(self, mm: float, dpi: int = 600) -> int:
        return int(mm * dpi / 25.4)


@dataclass
class FigoritaConfig:
    """Configuración de figurita individual."""
    WIDTH_MM: float = 50
    HEIGHT_MM: float = 70


@dataclass
class GridConfig:
    """Configuración de grilla 4x4."""
    COLS: int = 4
    ROWS: int = 4
    FIGURITAS_PER_SHEET: int = 16
    MARGIN_MM: float = 10
    GUTTER_MM: float = 2.5
    CROP_MARK_OFFSET_MM: float = 3
    BLEED_MM: float = 3


@dataclass
class ColorConfig:
    """Paleta de colores predefinida."""
    COLORS: dict = None
    BACKGROUND_DARK: str = "#1a1a1a"
    BACKGROUND_LIGHT: str = "#FFFFFF"
    TEXT_PRIMARY: str = "#FFFFFF"
    TEXT_SECONDARY: str = "#333333"
    
    def __post_init__(self):
        if self.COLORS is None:
            self.COLORS = {
                "Argentina": "#87CEEB",
                "Brasil": "#00AA00",
                "Alemania": "#FFFFFF",
                "Francia": "#4169E1",
                "España": "#FFC400",
                "Italia": "#009246",
                "Portugal": "#006600",
                "default": "#B0B0B0",
            }


@dataclass
class FontConfig:
    """Configuración de tipografía."""
    FONT_TITLE: str = "Montserrat-Bold.ttf"
    FONT_BODY: str = "Roboto-Regular.ttf"
    FONT_CONDENSED: str = "Roboto-Condensed.ttf"
    
    SIZE_NOMBRE: int = 14
    SIZE_EQUIPO: int = 9
    SIZE_POSICION: int = 8
    SIZE_NUMERO_FIGURITA: int = 10


@dataclass
class PDFConfig:
    """Configuración de PDF."""
    PDF_VERSION: str = "1.4"
    COMPRESS: bool = True
    TITLE: str = "Figuritas Coleccionables - Mundial 2026"
    AUTHOR: str = "Personal Collection"
    PRODUCER: str = "Figuritas Generator Pro"
    COLOR_SPACE: str = "RGB"
    ENABLE_PDF_X3: bool = True
    ENABLE_CROP_MARKS: bool = True


@dataclass
class ProcessingConfig:
    """Configuración de procesamiento de imagen."""
    FACE_DETECTION_CONFIDENCE: float = 0.5
    ENABLE_CLAHE: bool = True
    CLAHE_CLIP_LIMIT: float = 2.0
    ENABLE_BILATERAL_FILTER: bool = True
    BILATERAL_DIAMETER: int = 9
    ENABLE_UNSHARP_MASK: bool = True
    MIN_DPI_WARNING: int = 72


@dataclass
class PathConfig:
    """Configuración de paths."""
    BASE_DIR: Path = Path(__file__).parent.parent
    
    @property
    def DATA_DIR(self) -> Path:
        return self.BASE_DIR / "data"
    
    @property
    def INPUT_FOTOS_DIR(self) -> Path:
        return self.BASE_DIR / "input" / "fotos"
    
    @property
    def OUTPUT_DIR(self) -> Path:
        return self.BASE_DIR / "output"
    
    @property
    def FONTS_DIR(self) -> Path:
        return self.BASE_DIR / "assets" / "fonts"
    
    @property
    def TEMPLATES_DIR(self) -> Path:
        return self.BASE_DIR / "templates"
    
    @property
    def FIGURITAS_JSON(self) -> Path:
        return self.DATA_DIR / "figuritas.json"


# Instancias globales
PAGE_CONFIG = PageConfig()
FIGURITA_CONFIG = FigoritaConfig()
GRID_CONFIG = GridConfig()
COLOR_CONFIG = ColorConfig()
FONT_CONFIG = FontConfig()
PDF_CONFIG = PDFConfig()
PROCESSING_CONFIG = ProcessingConfig()
PATH_CONFIG = PathConfig()
