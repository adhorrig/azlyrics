# -*- coding: utf-8 -*-
from setuptools import setup, Command
import sys
import os
from shutil import rmtree

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

here = os.path.abspath(os.path.dirname(__file__))

class PublishCommand(Command):
    """Support setup.py publish."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        sys.exit()

setup(
  name = 'azlyrics',
  packages = ['azlyrics'],
  version = '1.0',
  description = 'An API wrapper for azlyrics which allows you to programatically extract data',
  long_description=long_descr,
  author = 'Adam Horrigan',
  author_email = 'adhorrig@gmail.com',
  url = 'https://github.com/adhorrig/azlyrics',
  download_url = 'https://github.com/adhorrig/azlyrics/archive/0.1.tar.gz',
  keywords = ['azlyrics', 'lyrics', 'albums', 'artists', 'songs', 'music', 'api'],
  classifiers = [],
  cmdclass={
          'publish': PublishCommand,
      }
)