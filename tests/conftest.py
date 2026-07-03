"""Configuración de pytest."""

import pytest
from pathlib import Path
from config.config import PATH_CONFIG


@pytest.fixture
def test_data_dir():
    """Directorio de datos de test."""
    return Path(__file__).parent / "data"


@pytest.fixture
def sample_figurita_data():
    """Datos de ejemplo de figurita."""
    return {
        "id": 1,
        "numero": 1,
        "nombre": "Test Player",
        "equipo": "Test Team",
        "posicion": "Delantero",
        "pais": "Argentina",
        "imagen_path": "test.jpg"
    }
