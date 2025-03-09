from setuptools import setup

APP = ['main.py']  # Replace with your script name if different
DATA_FILES = ['logo.png']  # Include any images or files your app uses
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter', 'os', 'sys']
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['setuptools', 'py2app'],
)

