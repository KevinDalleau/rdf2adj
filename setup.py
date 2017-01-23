from setuptools import setup

setup(name='rdf2adj',
      version='0.1',
      description='A module to transform rdf files to adjacency lists',
      url='http://github.com/KevinDalleau/rdf2adj',
      author='Kevin Dalleau',
      author_email='',
      license='GNU GENERAL PUBLIC LICENSE',
      py_modules = ['rdf2adj'],
      install_requires=['numpy','rdflib'])
