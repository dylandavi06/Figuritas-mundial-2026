"""Generador de PDFs con WeasyPrint."""

from pathlib import Path
from typing import List
from weasyprint import HTML, CSS
from PIL import Image
from loguru import logger
from config.config import PDF_CONFIG, PAGE_CONFIG


class PDFRenderer:
    """Renderiza PDFs profesionales."""
    
    def __init__(self):
        self.pdf_config = PDF_CONFIG
    
    def render_sheet_to_pdf(self, sheet_html: str, output_path: Path) -> None:
        """Renderiza HTML a PDF."""
        try:
            HTML(string=sheet_html).write_pdf(
                str(output_path),
                zoom=1.0,
                uncompressed_pdf=not self.pdf_config.COMPRESS
            )
            logger.info(f"PDF guardado: {output_path}")
        except Exception as e:
            logger.error(f"Error renderizando PDF: {e}")
            raise
    
    def image_to_pdf(self, image: Image.Image, output_path: Path) -> None:
        """Convierte imagen PIL a PDF."""
        try:
            # Convertir a RGB si es necesario
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Guardar como PDF
            image.save(str(output_path), 'PDF')
            logger.info(f"PDF generado desde imagen: {output_path}")
        except Exception as e:
            logger.error(f"Error convirtiendo imagen a PDF: {e}")
            raise
    
    def merge_pdfs(self, pdf_list: List[Path], output_path: Path) -> None:
        """Combina múltiples PDFs."""
        try:
            from PyPDF2 import PdfMerger
            
            merger = PdfMerger()
            for pdf_path in pdf_list:
                merger.append(str(pdf_path))
            
            merger.write(str(output_path))
            merger.close()
            logger.info(f"PDFs combinados en: {output_path}")
        except Exception as e:
            logger.error(f"Error combinando PDFs: {e}")
            raise
