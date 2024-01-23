#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['werkzeug',
 'werkzeug.datastructures',
 'werkzeug.debug',
 'werkzeug.middleware',
 'werkzeug.routing',
 'werkzeug.sansio',
 'werkzeug.wrappers']

package_data = \
{'': ['*'], 'werkzeug.debug': ['shared/*']}

package_dir = \
{'': 'src'}

install_requires = \
['MarkupSafe>=2.1.1']

extras_require = \
{'watchdog': ['watchdog>=2.3']}

setup(name='Werkzeug',
      version='3.0.2',
      description='The comprehensive WSGI web application library.',
      author=None,
      author_email=None,
      url=None,
      packages=packages,
      package_data=package_data,
      package_dir=package_dir,
      install_requires=install_requires,
      extras_require=extras_require,
      python_requires='>=3.8',
     )
