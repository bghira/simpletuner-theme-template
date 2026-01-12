from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).parent.resolve()

setup(
    name="simpletuner-theme-template",
    version="0.2.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A theme template for SimpleTuner WebUI",
    long_description=(here / "README.md").read_text(encoding="utf-8") if (here / "README.md").exists() else "",
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/simpletuner-theme-template",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "simpletuner_theme_template": ["*.yaml", "*.css", "*.json"],
    },
    python_requires=">=3.10",
    install_requires=["pyyaml>=5.0"],
    entry_points={
        "simpletuner.themes": [
            "template = simpletuner_theme_template:TemplateTheme",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
