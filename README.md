# SimpleTuner Theme Template

A template for creating custom themes for SimpleTuner WebUI.

<img width="1916" height="1010" alt="image" src="https://github.com/user-attachments/assets/a02fc138-522b-4ff4-83dc-8fab3b0cc619" />

## Installation Methods

### Method 1: Pip Install (Recommended)

Install via pip for automatic discovery:

```bash
pip install git+https://github.com/yourusername/your-theme-name.git
```

Or for local development:

```bash
cd simpletuner-theme-template
pip install -e .
```

### Method 2: Local Theme Folder

Copy your theme to `~/.simpletuner/themes/yourtheme/`:

```
~/.simpletuner/themes/yourtheme/
├── theme.json    # Theme manifest
├── theme.css     # CSS overrides
└── assets/       # Optional: images and sounds
    ├── images/
    │   └── logo.svg
    └── sounds/
        └── notification.wav
```

**theme.json format:**
```json
{
    "id": "yourtheme",
    "name": "Your Theme Name",
    "description": "A custom theme with your colors",
    "author": "Your Name",
    "version": "1.0.0",
    "assets": {
        "images": {
            "logo": "assets/images/logo.svg",
            "favicon": "assets/images/favicon.ico"
        },
        "sounds": {
            "success": "assets/sounds/success.wav",
            "error": "assets/sounds/error.wav",
            "info": "assets/sounds/info.wav",
            "hover": "assets/sounds/hover.wav"
        }
    }
}
```

## Creating Your Theme

### 1. Edit tokens.yaml

The `src/simpletuner_theme_template/tokens.yaml` file contains all design tokens. Edit colors to match your theme:

```yaml
colors:
  primary:
    purple: "#your-color"
  accent:
    blue: "#your-color"
```

### 2. Build CSS

Run the build script to generate theme.css:

```bash
python build_theme.py
```

### 3. Add Custom Assets (Optional)

#### Images
Place images in `assets/images/` and declare them in your theme manifest or `get_assets()` method:
- `logo` - Custom logo image
- `favicon` - Custom favicon
- `sidebar-bg` - Sidebar background image

#### Sounds
Place sounds in `assets/sounds/` and declare them:
- `success` - Played on successful operations
- `error` - Played on errors
- `warning` - Played for warnings
- `info` - Played for notifications
- `hover` - Played on UI hover (retro mode)

**Supported formats:**
- Images: `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`, `.webp`, `.ico`
- Sounds: `.wav`, `.mp3`, `.ogg`, `.m4a`

### 4. Test Your Theme

Install locally and refresh the theme list in SimpleTuner's UI Settings.

## Theme CSS Structure

Your theme.css should override CSS custom properties defined in SimpleTuner's `tokens.css`. Only override what you want to change:

```css
:root {
    /* Core palette */
    --colors-primary-purple: #9333ea;
    --colors-accent-blue: #38bdf8;

    /* Text colors */
    --colors-text-primary: #ffffff;
    --colors-text-secondary: #94a3b8;

    /* Surfaces */
    --colors-dark-bg: #0a0a0a;
    --colors-card-bg: rgba(255, 255, 255, 0.04);
}
```

## Available Token Categories

- **colors**: Primary, accent, semantic, text, surface colors
- **spacing**: xs through 3xl spacing scale
- **typography**: Font families, sizes, weights, line heights
- **border-radius**: sm, md, lg, xl, full
- **shadows**: Various shadow depths
- **z-index**: Layering system

See SimpleTuner's `static/css/tokens.css` for the complete list of variables.

## Package Structure

```
simpletuner-theme-template/
├── setup.py                 # Package setup with entry_points
├── build_theme.py           # Build script for generating CSS
├── README.md
└── src/
    └── simpletuner_theme_template/
        ├── __init__.py      # Theme class with get_css_path() and get_assets()
        ├── tokens.yaml      # Design tokens (edit this!)
        ├── theme.css        # Generated CSS (don't edit directly)
        ├── tokens.json      # Generated JSON
        └── assets/          # Optional: theme assets
            ├── images/
            └── sounds/
```

## Entry Point Registration

Pip-installed themes are discovered via the `simpletuner.themes` entry point group:

```python
# setup.py
entry_points={
    "simpletuner.themes": [
        "mytheme = my_theme_package:MyTheme",
    ],
}
```

Your theme class must have:
- `id`: Unique theme identifier
- `name`: Display name
- `description`: Short description
- `author`: Author name
- `get_css_path()`: Class method returning Path to CSS file
- `get_assets()`: Optional class method returning dict of asset declarations

## Asset Security

SimpleTuner validates all asset requests:
- Asset names must be alphanumeric with hyphens/underscores only
- Path traversal attempts (`../`) are blocked
- Only whitelisted file extensions are allowed
- Assets must be declared in the theme manifest
- Resolved paths must stay within the theme directory
