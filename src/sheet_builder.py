"""Constructor de hojas de figuritas (4x4)."""

from pathlib import Path
from typing import List
from PIL import Image
from loguru import logger
from config.config import PAGE_CONFIG, GRID_CONFIG
from src.data_loader import Figurita
from src.figurita_generator import FigoritaGenerator


class SheetBuilder:
    """Construye hojas de figuritas en grilla 4x4."""
    
    def __init__(self):
        self.grid_config = GRID_CONFIG
        self.page_width_px = PAGE_CONFIG.mm_to_px(PAGE_CONFIG.WIDTH_MM)
        self.page_height_px = PAGE_CONFIG.mm_to_px(PAGE_CONFIG.HEIGHT_MM)
        self.generator = FigoritaGenerator()
    
    def build_sheet(self, figuritas: List[Figurita], image_dir: Path) -> Image.Image:
        """Construye una hoja con 16 figuritas."""
        sheet = Image.new('RGB', (self.page_width_px, self.page_height_px), 'white')
        
        margin_px = PAGE_CONFIG.mm_to_px(self.grid_config.MARGIN_MM)
        gutter_px = PAGE_CONFIG.mm_to_px(self.grid_config.GUTTER_MM)
        
        figurita_width_px = PAGE_CONFIG.mm_to_px(50)  # 50mm por figurita
        figurita_height_px = PAGE_CONFIG.mm_to_px(70)  # 70mm por figurita
        
        idx = 0
        for row in range(self.grid_config.ROWS):
            for col in range(self.grid_config.COLS):
                if idx >= len(figuritas):
                    break
                
                x = margin_px + col * (figurita_width_px + gutter_px)
                y = margin_px + row * (figurita_height_px + gutter_px)
                
                figurita = figuritas[idx]
                image_path = image_dir / f"{figurita.id}.jpg"
                
                fig_img = self.generator.generate_figurita(figurita, image_path)
                sheet.paste(fig_img, (x, y))
                
                idx += 1
        
        logger.info(f"Hoja construida con {idx} figuritas")
        return sheet
    
    def build_multiple_sheets(self, figuritas: List[Figurita], image_dir: Path) -> List[Image.Image]:
        """Construye múltiples hojas."""
        sheets = []
        for i in range(0, len(figuritas), self.grid_config.FIGURITAS_PER_SHEET):
            chunk = figuritas[i:i + self.grid_config.FIGURITAS_PER_SHEET]
            sheet = self.build_sheet(chunk, image_dir)
            sheets.append(sheet)
        return sheets
