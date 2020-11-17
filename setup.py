from pathlib import Path
from setuptools import setup


__here__ = Path(__file__).absolute().parent


README  = (__here__ / "README.rst").read_text().strip()
VERSION = "1.0.0"


setup(
  name="lazy-string",
  version=VERSION,
  description="Python library for defining strings with delayed evaluation",
  long_description=README,
  long_description_content_type="text/x-rst",
  keywords=[
    "lazy", "string", "strings", "lazy-evaluation", "library", "libraries",
  ],
  license="MIT",
  url=f"https://github.com/oblalex/lazy-string/tree/v{VERSION}",

  author="Oleksandr Oblovatnyi",
  author_email="oblovatniy@gmail.com",

  python_requires=">=3.7",
  py_modules=[
    "lazy_string",
  ],

  classifiers=[
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX",
    "Programming Language :: Python :: 3",
    "Topic :: Software Development :: Libraries",
  ],

  zip_safe=True,
)
