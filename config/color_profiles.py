"""
Perfiles de color ICC y espacios de color.
"""

from enum import Enum


class ColorSpace(Enum):
    """Espacios de color soportados."""
    RGB = "RGB"
    CMYK = "CMYK"


class ColorManagement:
    """Gestión de color para PDF."""
    
    @staticmethod
    def hex_to_rgb(hex_color: str) -> tuple:
        """Convierte HEX a RGB (0-255)."""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    @staticmethod
    def rgb_to_hex(r: int, g: int, b: int) -> str:
        """Convierte RGB a HEX."""
        return f"#{r:02x}{g:02x}{b:02x}"
    
    @staticmethod
    def rgb_to_cmyk(r: int, g: int, b: int) -> tuple:
        """Convierte RGB (0-255) a CMYK (0-100)."""
        if (r, g, b) == (0, 0, 0):
            return (0, 0, 0, 100)
        
        r, g, b = r / 255.0, g / 255.0, b / 255.0
        k = 1 - max(r, g, b)
        
        c = (1 - r - k) / (1 - k) if k < 1 else 0
        m = (1 - g - k) / (1 - k) if k < 1 else 0
        y = (1 - b - k) / (1 - k) if k < 1 else 0
        
        return (
            int(c * 100),
            int(m * 100),
            int(y * 100),
            int(k * 100)
        )
