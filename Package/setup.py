from setuptools import setup, find_packages

setup(
    name='KKanjiRecognizer',
    version='0.1',
    packages=find_packages(exclude=['packageTests*']),
    license='MIT',
    description='Package for recognizing Kanji characters using ResNet',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/VasyaR/Bachelor_work',
    author='Vasyl Rusyn',
    author_email='vasyarusynb@gmail.com'
)