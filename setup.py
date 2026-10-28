from pathlib import Path

from setuptools import find_packages, setup

BASE_DIR = Path(__file__).resolve().parent

setup(
    # Package identity
    name="mcq_generator",
    version="0.1.0",

    # Package metadata
    author="Mensa Loveable",
    author_email="abdullahi.adedayo@gmail.com",
    description="A Python package for generating multiple-choice questions (MCQs) from text.",
    long_description=(BASE_DIR / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",

    # Package discovery
    packages=find_packages(),

    # Dependencies
    install_requires=[
        "openai",
        "langchain-core",
        "langchain-google-genai",
        "langchain",
        "python-dotenv",
        "streamlit",
        "pypdf",
    ],

    # Python compatibility
    python_requires=">=3.10",
)