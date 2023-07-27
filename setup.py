from setuptools import setup, find_packages

setup(
    name="tangods_baslercamera",
    version="0.0.1",
    description="Tango device connects to Basler cameras by the serial number",
    author="Daniel Schick",
    author_email="dschick@mbi-berlin.de",
    python_requires=">=3.6",
    entry_points={"console_scripts": ["BaslerCamera = tangods_baslercamera:main"]},
    license="MIT",
    packages=["tangods_baslercamera"],
    install_requires=[
        "pytango",
        "pypylon",
    ],
    url="https://github.com/MBI-Div-b/pytango-BaslerCamera",
    keywords=[
        "tango device",
        "tango",
        "pytango",
    ],
)
