"""Utilidades generales."""

import json
from pathlib import Path
from typing import Any, Dict, List
from loguru import logger


class DataLoader:
    """Carga datos JSON."""
    
    @staticmethod
    def load_json(filepath: Path) -> Dict[str, Any]:
        """Carga un archivo JSON."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error cargando {filepath}: {e}")
            raise
    
    @staticmethod
    def save_json(data: Dict[str, Any], filepath: Path) -> None:
        """Guarda datos a JSON."""
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


class PathManager:
    """Gestiona rutas del proyecto."""
    
    @staticmethod
    def ensure_dirs(base_path: Path) -> None:
        """Crea directorios necesarios."""
        dirs = [
            base_path / "input" / "fotos",
            base_path / "output" / "pdf",
            base_path / "output" / "preview",
            base_path / "data",
            base_path / "assets" / "fonts",
            base_path / "logs",
        ]
        for d in dirs:
            d.mkdir(parents=True, exist_ok=True)
            logger.info(f"Directorio asegurado: {d}")
