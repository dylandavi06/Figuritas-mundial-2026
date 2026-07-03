#!/usr/bin/env python
"""Script de benchmark de performance."""

import time
from pathlib import Path
from loguru import logger
from config.config import PATH_CONFIG
from src.data_loader import FigoritasDataset
from src.sheet_builder import SheetBuilder


def benchmark():
    """Ejecuta benchmark."""
    logger.info("Iniciando benchmark...")
    
    # Cargar dataset
    start = time.time()
    dataset = FigoritasDataset(PATH_CONFIG.FIGURITAS_JSON)
    load_time = time.time() - start
    logger.info(f"Tiempo carga: {load_time:.2f}s")
    
    # Generar hojas
    start = time.time()
    builder = SheetBuilder()
    figuritas = dataset.get_all()[:16]  # Solo primeras 16
    
    if figuritas:
        sheets = builder.build_multiple_sheets(figuritas, PATH_CONFIG.INPUT_FOTOS_DIR)
        generation_time = time.time() - start
        logger.info(f"Tiempo generación (16 figuritas): {generation_time:.2f}s")
        logger.info(f"Tiempo promedio por figurita: {generation_time/16:.3f}s")


if __name__ == "__main__":
    benchmark()
