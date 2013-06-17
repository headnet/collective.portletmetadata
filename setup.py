from setuptools import setup, find_packages
import os

setup(name='collective.portletmetadata',
      version='0.1',
      description="",
      long_description="",
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Bo Simonsen',
      author_email='bo@headnet.dk',
      url='http://github.com/collective/collective.portletmetadata',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.jbot',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
)
