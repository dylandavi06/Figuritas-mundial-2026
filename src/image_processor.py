"""Procesamiento de imágenes."""

import cv2
import numpy as np
from pathlib import Path
from loguru import logger
from config.config import PROCESSING_CONFIG


class ImageProcessor:
    """Procesamiento y mejora de imágenes."""
    
    @staticmethod
    def load_image(image_path: Path) -> np.ndarray:
        """Carga una imagen."""
        img = cv2.imread(str(image_path))
        if img is None:
            raise ValueError(f"No se pudo cargar: {image_path}")
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    @staticmethod
    def resize_to_figurita(image: np.ndarray, width: int = 440, height: int = 500) -> np.ndarray:
        """Redimensiona imagen a tamaño de figurita."""
        return cv2.resize(image, (width, height), interpolation=cv2.INTER_LANCZOS4)
    
    @staticmethod
    def enhance_image(image: np.ndarray) -> np.ndarray:
        """Mejora la imagen con CLAHE y filtros."""
        # CLAHE
        if PROCESSING_CONFIG.ENABLE_CLAHE:
            lab = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)
            l, a, b = cv2.split(lab)
            clahe = cv2.createCLAHE(clipLimit=PROCESSING_CONFIG.CLAHE_CLIP_LIMIT, tileGridSize=(8, 8))
            l = clahe.apply(l)
            image = cv2.cvtColor(cv2.merge([l, a, b]), cv2.COLOR_LAB2RGB)
        
        # Bilateral Filter
        if PROCESSING_CONFIG.ENABLE_BILATERAL_FILTER:
            image = cv2.bilateralFilter(image, PROCESSING_CONFIG.BILATERAL_DIAMETER, 75, 75)
        
        # Unsharp Mask
        if PROCESSING_CONFIG.ENABLE_UNSHARP_MASK:
            blur = cv2.GaussianBlur(image, (0, 0), 2.0)
            image = cv2.addWeighted(image, 1.5, blur, -0.5, 0)
        
        return np.clip(image, 0, 255).astype(np.uint8)
    
    @staticmethod
    def detect_faces(image: np.ndarray) -> list:
        """Detecta rostros en la imagen."""
        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        return faces.tolist()
    
    @staticmethod
    def crop_to_face(image: np.ndarray, margin: int = 50) -> np.ndarray:
        """Recorta la imagen al rostro detectado."""
        faces = ImageProcessor.detect_faces(image)
        if not faces:
            return image
        
        x, y, w, h = faces[0]
        y_start = max(0, y - margin)
        y_end = min(image.shape[0], y + h + margin)
        x_start = max(0, x - margin)
        x_end = min(image.shape[1], x + w + margin)
        
        return image[y_start:y_end, x_start:x_end]
