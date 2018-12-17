from setuptools import setup

setup(
    name='bv',
    version='0.1.2',
    author='codechenx',
    author_email='codechenx@gmail.com',
    url='https://github.com/codechenx/bv',
    description='Data Viewer in Terminal for Bioinformatician',
    python_requires='>=3.5',
    license="MIT License",
    packages=['bv'],
    install_requires=["chardet"],
    package_data={'bv': ['config/*.cfg']},
    entry_points={
        'console_scripts': [
            'bv=bv:bv'
        ]
    }
)
