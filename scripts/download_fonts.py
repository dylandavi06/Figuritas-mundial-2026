#!/usr/bin/env python
"""Descarga Google Fonts necesarias."""

import requests
from pathlib import Path
from loguru import logger


FONTS_TO_DOWNLOAD = {
    "Montserrat-Bold": "https://github.com/JetBrains/JetBrainsMono/raw/master/fonts/ttf/JetBrainsMono-Bold.ttf",
    "Roboto-Regular": "https://github.com/google/roboto/raw/main/fonts/Roboto-Regular.ttf",
    "Roboto-Condensed": "https://github.com/google/roboto/raw/main/fonts/RobotoCondensed-Regular.ttf",
}


def download_fonts(output_dir: Path) -> None:
    """Descarga fuentes a directorio."""
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for font_name, url in FONTS_TO_DOWNLOAD.items():
        output_path = output_dir / f"{font_name}.ttf"
        
        if output_path.exists():
            logger.info(f"Font ya existe: {font_name}")
            continue
        
        try:
            logger.info(f"Descargando {font_name}...")
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            with open(output_path, 'wb') as f:
                f.write(response.content)
            
            logger.success(f"Descargado: {font_name}")
        except Exception as e:
            logger.error(f"Error descargando {font_name}: {e}")


if __name__ == "__main__":
    fonts_dir = Path(__file__).parent.parent / "assets" / "fonts"
    download_fonts(fonts_dir)
