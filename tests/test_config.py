"""Tests de configuración."""

import pytest
from config.config import PAGE_CONFIG, FIGURITA_CONFIG


def test_page_config_dimensions():
    """Verifica dimensiones de página."""
    assert PAGE_CONFIG.WIDTH_MM == 210
    assert PAGE_CONFIG.HEIGHT_MM == 297
    assert PAGE_CONFIG.DPI_EXPORT == 300


def test_figurita_config():
    """Verifica configuración de figurita."""
    assert FIGURITA_CONFIG.WIDTH_MM == 50
    assert FIGURITA_CONFIG.HEIGHT_MM == 70


def test_mm_to_px_conversion():
    """Verifica conversión mm a píxeles."""
    px = PAGE_CONFIG.mm_to_px(50, 300)
    assert isinstance(px, int)
    assert px > 0
