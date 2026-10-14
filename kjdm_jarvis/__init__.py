"""KJDM Jarvis — Local-first AI agent for Kyle Johnson Digital Marketing.

Brand: #090911 background · #F97316 orange · #F0F0FF text
Powered by OpenJarvis (Stanford) × copilot.kljj365.com
"""

__version__ = "1.0.0"
__author__ = "Kyle Johnson Digital Marketing"
__brand__ = {
    "name": "KJDM",
    "background": "#090911",
    "primary": "#F97316",
    "accent": "#F97316",
    "text": "#F0F0FF",
    "font": "Inter",
}

from .config import KJDMConfig
from .client import KJDMClient

__all__ = ["KJDMConfig", "KJDMClient", "__brand__"]
