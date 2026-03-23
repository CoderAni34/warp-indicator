#!/usr/bin/env python3
"""
Setup script for WARP Indicator
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="warp-indicator",
    version="1.0.0",
    author="CoderAni34",
    author_email="coderAni34@users.noreply.github.com",
    description="System tray indicator for Cloudflare WARP VPN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CoderAni34/warp-indicator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Environment :: X11 :: Gnome",
        "Intended Audience :: End Users/Desktop",
        "Topic :: System :: Networking",
    ],
    python_requires=">=3.6",
    install_requires=[
        "PyGObject>=3.30.0",
    ],
    entry_points={
        "console_scripts": [
            "warp-indicator=warp_indicator:main",
        ],
    },
    include_package_data=True,
    license="MIT",
)
