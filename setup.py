from setuptools import setup, find_packages
import sys, os

version = '0.3'

readme = open('README.txt').read()

setup(name='django-staticblocks',
      version=version,
      description="staticblocks provides you with tools for content managers to easily include flatpage content as a snippet in your templates while retaining structured control over the templates themselves",
      long_description=readme,
      classifiers=['Framework :: Django'],
      keywords='django template static',
      author='Ethan Jucovy, Rob Marianski',
      author_email='ethan.jucovy@gmail.com',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'djangohelpers',
      ],
      entry_points="""
      """,
      )
