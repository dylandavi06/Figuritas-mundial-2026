"""Generador de figuritas individuales."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from loguru import logger
from config.config import FIGURITA_CONFIG, FONT_CONFIG, COLOR_CONFIG, PAGE_CONFIG
from src.image_processor import ImageProcessor
from src.data_loader import Figurita


class FigoritaGenerator:
    """Genera renderizados de figuritas."""
    
    def __init__(self):
        self.width_px = PAGE_CONFIG.mm_to_px(FIGURITA_CONFIG.WIDTH_MM)
        self.height_px = PAGE_CONFIG.mm_to_px(FIGURITA_CONFIG.HEIGHT_MM)
        self.processor = ImageProcessor()
    
    def generate_figurita(self, figurita: Figurita, image_path: Path) -> Image.Image:
        """Genera una figurita con imagen y datos."""
        try:
            # Cargar y procesar imagen
            img = self.processor.load_image(image_path)
            img = self.processor.crop_to_face(img)
            img = self.processor.enhance_image(img)
            img = self.processor.resize_to_figurita(img, self.width_px - 20, self.height_px - 40)
            
            # Crear lienzo
            canvas = Image.new('RGB', (self.width_px, self.height_px), 'white')
            
            # Pegar imagen centrada
            img_pil = Image.fromarray(img)
            x_offset = (self.width_px - img_pil.width) // 2
            y_offset = 10
            canvas.paste(img_pil, (x_offset, y_offset))
            
            # Añadir texto
            draw = ImageDraw.Draw(canvas)
            
            # Nombre
            y_text = self.height_px - 50
            draw.text((self.width_px // 2, y_text), figurita.nombre,
                     fill='black', anchor='mm', align='center')
            
            # Equipo
            draw.text((self.width_px // 2, y_text + 20), figurita.equipo,
                     fill='gray', anchor='mm', align='center')
            
            # Número
            draw.text((self.width_px - 10, 10), str(figurita.numero),
                     fill='red', anchor='rt')
            
            logger.info(f"Figurita {figurita.numero} ({figurita.nombre}) generada")
            return canvas
        except Exception as e:
            logger.error(f"Error generando figurita {figurita.numero}: {e}")
            return self._create_placeholder(figurita)
    
    def _create_placeholder(self, figurita: Figurita) -> Image.Image:
        """Crea una figurita placeholder."""
        canvas = Image.new('RGB', (self.width_px, self.height_px), '#f0f0f0')
        draw = ImageDraw.Draw(canvas)
        draw.text((self.width_px // 2, self.height_px // 2), 
                 f"#{figurita.numero}", fill='black', anchor='mm')
        return canvas
