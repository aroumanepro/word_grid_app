from setuptools import setup, find_packages

setup(
    name='word_grid_app',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'tk'
    ],
    entry_points={
        'console_scripts': [
            'word_grid_app = word_grid_app.app:main',
        ],
    },
    author='ROUMANE Abderrahmane',
    author_email='abderrahmane.roumane.pro@gmail.com',
    description='A word grid application built with Tkinter',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/aroumanepro/word_grid_app',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
