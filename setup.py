from setuptools import setup, find_packages

setup(name='demo',
     version = '0.1',
     description = "A great Fortune Teller",
     author = 'Julia, Madeleine, Leah',
     license = 'LICENSE.txt',
     packages = find_packages(),
      install_requires=['pandas','numpy'],)
