"""Interfaz de línea de comandos."""

import click
from pathlib import Path
from loguru import logger
from config.config import PATH_CONFIG
from src.utils import PathManager, DataLoader
from src.data_loader import FigoritasDataset
from src.sheet_builder import SheetBuilder
from src.pdf_renderer import PDFRenderer


@click.group()
def cli():
    """Generador de figuritas coleccionables - Mundial 2026."""
    pass


@cli.command()
@click.option('--data', type=click.Path(), default='data/figuritas.json', help='Archivo JSON de figuritas')
@click.option('--fotos', type=click.Path(), default='input/fotos', help='Directorio de fotos')
@click.option('--output', type=click.Path(), default='output/pdf', help='Directorio de salida')
def generate(
    data: str,
    fotos: str,
    output: str
) -> None:
    """Genera hojas de figuritas en PDF."""
    logger.info("Iniciando generación de figuritas...")
    
    # Validar directorios
    data_path = Path(data)
    fotos_path = Path(fotos)
    output_path = Path(output)
    
    if not data_path.exists():
        logger.error(f"Archivo no encontrado: {data_path}")
        return
    
    if not fotos_path.exists():
        logger.error(f"Directorio no encontrado: {fotos_path}")
        return
    
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Cargar datos
    dataset = FigoritasDataset(data_path)
    figuritas = dataset.get_all()
    
    if not figuritas:
        logger.warning("No hay figuritas para procesar")
        return
    
    # Generar hojas
    builder = SheetBuilder()
    sheets = builder.build_multiple_sheets(figuritas, fotos_path)
    
    # Renderizar PDFs
    renderer = PDFRenderer()
    pdf_files = []
    
    for idx, sheet in enumerate(sheets, 1):
        pdf_path = output_path / f"hoja_{idx:03d}.pdf"
        renderer.image_to_pdf(sheet, pdf_path)
        pdf_files.append(pdf_path)
    
    # Combinar PDFs
    if len(pdf_files) > 1:
        final_pdf = output_path / "coleccion_completa.pdf"
        renderer.merge_pdfs(pdf_files, final_pdf)
        logger.info(f"PDF final generado: {final_pdf}")
    
    logger.success(f"¡Generación completada! Archivos en: {output_path}")


@cli.command()
def init():
    """Inicializa la estructura del proyecto."""
    logger.info("Inicializando estructura...")
    PathManager.ensure_dirs(PATH_CONFIG.BASE_DIR)
    logger.success("Estructura creada exitosamente")


if __name__ == '__main__':
    cli()
