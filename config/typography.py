"""
Configuración de tipografía y estilos.
"""


class Typography:
    """Gestión de fuentes y estilos tipográficos."""
    
    # Google Fonts
    FONTS = {
        "Montserrat": {
            "weights": ["Bold", "SemiBold", "Regular"],
            "url": "https://fonts.google.com/download?family=Montserrat"
        },
        "Roboto": {
            "weights": ["Bold", "Regular", "Condensed"],
            "url": "https://fonts.google.com/download?family=Roboto"
        },
        "Poppins": {
            "weights": ["Bold", "Regular"],
            "url": "https://fonts.google.com/download?family=Poppins"
        }
    }
    
    # Estilos CSS para HTML templates
    CSS_STYLES = """
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Roboto', sans-serif;
        background-color: white;
    }
    
    .figurita-card {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 50mm;
        height: 70mm;
        border: 1px solid #ddd;
        padding: 4mm;
        position: relative;
    }
    
    .figurita-image {
        width: 44mm;
        height: 50mm;
        object-fit: cover;
        border-radius: 2mm;
    }
    
    .figurita-info {
        width: 100%;
        text-align: center;
        margin-top: 2mm;
        font-size: 8pt;
    }
    
    .nombre {
        font-family: 'Montserrat', sans-serif;
        font-weight: bold;
        font-size: 11pt;
        color: #000;
        margin-bottom: 1mm;
        word-wrap: break-word;
    }
    
    .equipo {
        font-size: 8pt;
        color: #555;
        margin-bottom: 0.5mm;
    }
    
    .numero {
        position: absolute;
        top: 2mm;
        right: 2mm;
        font-weight: bold;
        font-size: 14pt;
        background: rgba(0,0,0,0.1);
        width: 6mm;
        height: 6mm;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
    }
    """
    
    @staticmethod
    def get_font_path(font_name: str, weight: str = "Regular") -> str:
        """Obtiene la ruta de la fuente."""
        return f"assets/fonts/{font_name}-{weight}.ttf"
