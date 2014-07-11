from setuptools import setup, find_packages
import sys
import os

version = '0.1'

setup(name='coreproxy',
      version=version,
      description="A proxy for making requests to Brave Core API",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Sean Sanders',
      author_email='sean.d.sanders@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      namespace_packages = ['brave'],
      install_requires=[
          'ecdsa',
          'webob',
          'requests',
          'paste',
      ]
)
