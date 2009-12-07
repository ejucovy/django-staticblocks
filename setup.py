from setuptools import setup, find_packages
import sys, os

version = '0.2'

readme = open('README.txt').read()

setup(name='django-staticblocks',
      version=version,
      description="use django flatpages as static page block snippets",
      long_description=readme,
      classifiers=['Framework :: Django'],
      keywords='django template static',
      author='Ethan Jucovy, Rob Marianski',
      author_email='ethan.jucovy@gmail.com',
      url='',
      license='GPLv3 or greater',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'djangohelpers',
      ],
      entry_points="""
      """,
      )
