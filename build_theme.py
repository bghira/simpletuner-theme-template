#!/usr/bin/env python3
"""Build CSS custom properties from tokens.yaml

This script converts tokens.yaml into theme.css, generating CSS custom
properties that can override SimpleTuner's default tokens.css values.
"""

import json
import yaml
from pathlib import Path
from typing import Any


def generate_css_tokens(tokens: dict[str, Any]) -> str:
    """Generate CSS custom properties from tokens"""
    css_lines = ["/* Generated CSS custom properties from tokens.yaml */"]
    css_lines.append(":root {")

    variables: dict[str, str] = {}

    # Process colors
    colors = tokens.get("colors", {})

    # Dark surfaces
    if "dark" in colors:
        dark = colors["dark"]
        variables["colors-dark-bg"] = dark.get("bg", "#0a0a0a")
        variables["colors-dark-sidebar"] = dark.get("sidebar", "#0f0f0f")
        variables["colors-dark-surface"] = dark.get("surface", "#1c1f2e")
        variables["colors-card-bg"] = dark.get("card", "rgba(255, 255, 255, 0.04)")
        variables["colors-card-bg-elevated"] = dark.get(
            "card-elevated", "rgba(255, 255, 255, 0.06)"
        )
        variables["colors-card-bg-hover"] = dark.get(
            "card-hover", "rgba(255, 255, 255, 0.08)"
        )
        variables["colors-sidebar-bg-hover"] = dark.get(
            "sidebar-hover", "rgba(255, 255, 255, 0.03)"
        )

    # Dark surface opacity variants
    if "dark-surface" in colors:
        ds = colors["dark-surface"]
        for key, value in ds.items():
            variables[f"colors-dark-surface-{key}"] = value

    # Glass surfaces
    if "glass" in colors:
        glass = colors["glass"]
        variables["colors-glass-bg"] = glass.get("bg", "rgba(255, 255, 255, 0.05)")
        variables["colors-glass-border"] = glass.get(
            "border", "rgba(255, 255, 255, 0.08)"
        )
        variables["colors-glass-hover"] = glass.get(
            "hover", "rgba(102, 126, 234, 0.1)"
        )
        variables["colors-focus-ring"] = glass.get(
            "focus-ring", "rgba(102, 126, 234, 0.1)"
        )

    # Surface/panel
    if "surface" in colors:
        surface = colors["surface"]
        variables["colors-surface-panel"] = surface.get(
            "panel", "rgba(18, 21, 30, 0.92)"
        )
        variables["colors-surface-panel-border"] = surface.get(
            "panel-border", "rgba(148, 163, 184, 0.18)"
        )
        variables["colors-surface-field"] = surface.get(
            "field", "rgba(15, 18, 26, 0.85)"
        )
        variables["colors-surface-field-border"] = surface.get(
            "field-border", "rgba(148, 163, 184, 0.2)"
        )
        variables["colors-border-soft"] = surface.get(
            "border-soft", "rgba(255, 255, 255, 0.12)"
        )
        variables["colors-border-subtle"] = surface.get(
            "border-subtle", "rgba(255, 255, 255, 0.06)"
        )
        variables["colors-border-strong"] = surface.get(
            "border-strong", "rgba(255, 255, 255, 0.18)"
        )

    # Slate scale
    if "slate" in colors:
        slate = colors["slate"]
        for key, value in slate.items():
            variables[f"colors-slate-{key}"] = value

    # Modal overlays
    if "modal" in colors:
        modal = colors["modal"]
        for key, value in modal.items():
            variables[f"colors-modal-{key}"] = value

    # Primary palette
    if "primary" in colors:
        primary = colors["primary"]
        variables["colors-primary-purple"] = primary.get("purple", "#667eea")
        variables["colors-primary-gradient"] = primary.get(
            "gradient", "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
        )
        variables["colors-secondary-gradient"] = primary.get(
            "secondary-gradient", "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)"
        )

    # Accent colors
    if "accent" in colors:
        accent = colors["accent"]
        variables["colors-accent-pink"] = accent.get("pink", "#f093fb")
        variables["colors-accent-blue"] = accent.get("blue", "#60a5fa")
        variables["colors-accent-cyan"] = accent.get("cyan", "#38bdf8")
        variables["colors-purple"] = accent.get("purple", "#a855f7")
        variables["colors-purple-muted"] = accent.get("purple-muted", "#c084fc")

    # Blue scale
    if "blue" in colors:
        blue = colors["blue"]
        for key, value in blue.items():
            variables[f"colors-blue-{key}"] = value

    # Indigo scale
    if "indigo" in colors:
        indigo = colors["indigo"]
        for key, value in indigo.items():
            variables[f"colors-indigo-{key}"] = value

    # Violet scale
    if "violet" in colors:
        violet = colors["violet"]
        for key, value in violet.items():
            variables[f"colors-violet-{key}"] = value

    # Violet-400 variants
    if "violet-400" in colors:
        v400 = colors["violet-400"]
        for key, value in v400.items():
            variables[f"colors-violet-400-{key}"] = value

    # Green scale
    if "green" in colors:
        green = colors["green"]
        for key, value in green.items():
            variables[f"colors-green-{key}"] = value

    # Amber scale
    if "amber" in colors:
        amber = colors["amber"]
        for key, value in amber.items():
            variables[f"colors-amber-{key}"] = value

    # Emerald
    if "emerald" in colors:
        emerald = colors["emerald"]
        for key, value in emerald.items():
            variables[f"colors-emerald-{key}"] = value

    # Semantic colors
    if "semantic" in colors:
        sem = colors["semantic"]
        variables["colors-semantic-success"] = sem.get("success", "#22c55e")
        variables["colors-semantic-success-bg"] = sem.get(
            "success-bg", "rgba(34, 197, 94, 0.15)"
        )
        variables["colors-success-bright"] = sem.get("success-bright", "#4ade80")
        variables["colors-semantic-error"] = sem.get("error", "#ef4444")
        variables["colors-semantic-error-bg"] = sem.get(
            "error-bg", "rgba(239, 68, 68, 0.15)"
        )
        variables["colors-semantic-warning"] = sem.get("warning", "#f59e0b")
        variables["colors-semantic-warning-bg"] = sem.get(
            "warning-bg", "rgba(245, 158, 11, 0.15)"
        )
        variables["colors-semantic-info"] = sem.get("info", "#3b82f6")
        variables["colors-semantic-info-bg"] = sem.get(
            "info-bg", "rgba(59, 130, 246, 0.15)"
        )

    # Text colors
    if "text" in colors:
        text = colors["text"]
        for key, value in text.items():
            variables[f"colors-text-{key}"] = value

    # White overlays
    if "white" in colors:
        white = colors["white"]
        for key, value in white.items():
            variables[f"colors-white-{key}"] = value

    # Black overlays
    if "black" in colors:
        black = colors["black"]
        for key, value in black.items():
            variables[f"colors-black-{key}"] = value

    # Event dock
    if "event" in colors:
        event = colors["event"]
        variables["colors-event-dock-bg"] = event.get(
            "dock-bg", "rgba(15, 18, 26, 0.96)"
        )
        variables["colors-event-dock-border"] = event.get(
            "dock-border", "rgba(148, 163, 184, 0.18)"
        )
        variables["colors-event-list-bg"] = event.get(
            "list-bg", "rgba(12, 14, 22, 0.65)"
        )

    # Onboarding
    if "onboarding" in colors:
        onboard = colors["onboarding"]
        variables["colors-onboarding-overlay"] = onboard.get(
            "overlay", "rgba(8, 10, 16, 0.92)"
        )
        variables["colors-onboarding-modal"] = onboard.get(
            "modal", "rgba(13, 16, 24, 0.95)"
        )

    # Status
    if "status" in colors:
        status = colors["status"]
        variables["colors-status-connected-bg"] = status.get(
            "connected-bg", "rgba(34, 197, 94, 0.9)"
        )
        variables["colors-status-disconnected-bg"] = status.get(
            "disconnected-bg", "rgba(239, 68, 68, 0.9)"
        )
        variables["colors-status-reconnecting-bg"] = status.get(
            "reconnecting-bg", "rgba(249, 115, 22, 0.9)"
        )

    # Toast
    if "toast" in colors:
        toast = colors["toast"]
        for key, value in toast.items():
            variables[f"colors-toast-{key}"] = value

    # Overlay
    if "overlay" in colors:
        overlay = colors["overlay"]
        for key, value in overlay.items():
            variables[f"colors-overlay-{key}"] = value

    # Loader
    if "loader" in colors:
        loader = colors["loader"]
        variables["colors-spinner-track"] = loader.get("spinner-track", "#f3f3f3")
        variables["colors-spinner-head"] = loader.get("spinner-head", "#3498db")
        variables["colors-skeleton-base"] = loader.get("skeleton-base", "#f0f0f0")
        variables["colors-skeleton-highlight"] = loader.get(
            "skeleton-highlight", "#e0e0e0"
        )

    # Tabs
    if "tab" in colors:
        tab = colors["tab"]
        for key, value in tab.items():
            variables[f"colors-tab-{key}"] = value

    # Dataset badges
    if "dataset" in colors:
        dataset = colors["dataset"]
        for dtype, values in dataset.items():
            if isinstance(values, dict):
                for key, value in values.items():
                    variables[f"colors-dataset-type-{dtype}-{key}"] = value

    # Spacing
    spacing = tokens.get("spacing", {})
    for key, value in spacing.items():
        variables[f"spacing-{key}"] = value

    # Typography
    typography = tokens.get("typography", {})
    for category, values in typography.items():
        if isinstance(values, dict):
            for key, value in values.items():
                variables[f"typography-{category}-{key}"] = value

    # Border radius
    border_radius = tokens.get("border-radius", {})
    for key, value in border_radius.items():
        variables[f"border-radius-{key}"] = value

    # Layout
    layout = tokens.get("layout", {})
    for key, value in layout.items():
        variables[f"layout-{key}"] = value

    # Shadows
    shadows = tokens.get("shadows", {})
    for key, value in shadows.items():
        variables[f"shadow-{key}"] = value

    # Z-index
    z_index = tokens.get("z-index", {})
    for key, value in z_index.items():
        variables[f"z-{key}"] = value

    # Theme assets (CSS url() values)
    assets = tokens.get("assets", {})
    for key, value in assets.items():
        variables[f"asset-{key}"] = value

    # Write CSS variables sorted by key
    for key in sorted(variables.keys()):
        css_lines.append(f"  --{key}: {variables[key]};")

    css_lines.append("}")
    return "\n".join(css_lines)


def main():
    """Main build function"""
    # Read tokens
    src_dir = Path(__file__).parent / "src" / "simpletuner_theme_template"
    tokens_file = src_dir / "tokens.yaml"
    with open(tokens_file, "r") as f:
        tokens = yaml.safe_load(f)

    # Generate CSS
    css_content = generate_css_tokens(tokens)

    # Append custom CSS if present
    custom_css = tokens.get("custom_css", "")
    if custom_css:
        css_content += "\n\n/* Custom theme styles */\n" + custom_css.strip() + "\n"

    # Write CSS file in the package directory
    css_file = src_dir / "theme.css"
    with open(css_file, "w") as f:
        f.write(css_content)

    print(f"Generated {css_file}")

    # Also generate JSON for JavaScript access
    json_file = src_dir / "tokens.json"
    with open(json_file, "w") as f:
        json.dump(tokens, f, indent=2)

    print(f"Generated {json_file}")


if __name__ == "__main__":
    main()
