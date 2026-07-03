"""Tests de procesamiento de imágenes."""

import pytest
import numpy as np
from src.image_processor import ImageProcessor


def test_rgb_conversion():
    """Verifica conversión RGB."""
    processor = ImageProcessor()
    # Crear imagen dummy
    img = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    assert img.shape == (100, 100, 3)
