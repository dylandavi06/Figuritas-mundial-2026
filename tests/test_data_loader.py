"""Tests del cargador de datos."""

import pytest
from pathlib import Path
from src.data_loader import Figurita


def test_figurita_model():
    """Verifica modelo de Figurita."""
    fig = Figurita(
        id=1,
        numero=1,
        nombre="Test",
        equipo="Team",
        pais="Country",
        imagen_path="test.jpg"
    )
    assert fig.numero == 1
    assert fig.nombre == "Test"
