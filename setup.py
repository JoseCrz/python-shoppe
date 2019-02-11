from setuptools import setup

setup(
    name='shoppe',
    version='0.1',
    py_modules=['shoppe'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        shoppe=shoppe:cli
    ''',
)
