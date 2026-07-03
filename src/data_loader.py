"""Cargador de datos de figuritas."""

from pathlib import Path
from typing import List, Dict, Any
from pydantic import BaseModel, Field
from loguru import logger
import json


class Figurita(BaseModel):
    """Modelo de una figurita."""
    id: int
    numero: int
    nombre: str
    equipo: str
    posicion: str = "Jugador"
    pais: str
    imagen_path: str
    rareza: str = "Común"
    brillo: bool = False


class FigoritasDataset:
    """Gestiona el dataset de figuritas."""
    
    def __init__(self, json_path: Path):
        self.json_path = json_path
        self.figuritas: List[Figurita] = []
        self.load_data()
    
    def load_data(self) -> None:
        """Carga figuritas desde JSON."""
        try:
            with open(self.json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.figuritas = [Figurita(**fig) for fig in data.get('figuritas', [])]
            logger.info(f"Cargadas {len(self.figuritas)} figuritas")
        except Exception as e:
            logger.error(f"Error cargando dataset: {e}")
            self.figuritas = []
    
    def get_by_numero(self, numero: int) -> Figurita | None:
        """Obtiene figurita por número."""
        for fig in self.figuritas:
            if fig.numero == numero:
                return fig
        return None
    
    def get_by_equipo(self, equipo: str) -> List[Figurita]:
        """Obtiene figuritas de un equipo."""
        return [f for f in self.figuritas if f.equipo.lower() == equipo.lower()]
    
    def get_all(self) -> List[Figurita]:
        """Obtiene todas las figuritas."""
        return self.figuritas
