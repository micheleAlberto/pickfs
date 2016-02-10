from distutils.core import setup

setup(name='pickfs',
      version='1.0',
      description='Pick files and folders with a simple curse based gui',
      author='Michele Alberto',
      url='https://github.com/micheleAlberto/pickfs',
      packages=['pickfs'],
      install_requires=[
          'glob','pick'
      ],
      zip_safe=False
     )
