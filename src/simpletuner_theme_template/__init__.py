"""SimpleTuner Theme Template Package.

This package provides a template for creating custom themes for SimpleTuner WebUI.
Themes are discovered via Python entry_points and loaded dynamically.
"""

from pathlib import Path
from typing import Dict

__version__ = "0.2.0"

THEME_DIR = Path(__file__).parent


class TemplateTheme:
    """Theme class discovered via entry_points.

    SimpleTuner's ThemeService will call get_css_path() to locate the CSS file
    and get_assets() to get asset declarations.
    """

    id = "template"
    name = "Fennec Theme"
    description = "Fennec girl holds your training config"
    author = "SimpleTuner"
    version = __version__

    @classmethod
    def get_css_path(cls) -> Path:
        """Return the path to the theme's CSS file."""
        return THEME_DIR / "theme.css"

    @classmethod
    def get_tokens_path(cls) -> Path:
        """Return the path to the theme's tokens.yaml file."""
        return THEME_DIR / "tokens.yaml"

    @classmethod
    def get_assets(cls) -> Dict:
        """Return theme asset declarations.

        Assets are organized by type (images, sounds) with names mapping to
        relative paths within the theme directory.

        SimpleTuner will serve these via /api/themes/{theme_id}/assets/{type}/{name}
        with security validation (path sanitization, extension whitelist).

        Returns:
            Dict with 'images' and 'sounds' keys mapping asset names to paths.
        """
        return {
            "images": {
                "sidebar-bg": "assets/images/fennec.png",
            },
            "sounds": {},
        }
