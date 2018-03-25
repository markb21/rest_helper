from setuptools import setup

setup(name='rest_helper',
      version='0.1',
      description='Rest helper - helping you parsing',
      author='Mark Budiak',
      author_email='mark.budiak@gmail.com',
      packages=['rest_helper'],
      install_requires=[
          'docopt',
      ],
      zip_safe=False)