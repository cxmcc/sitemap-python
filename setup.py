from distutils.core import setup

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
  name='sitemap',
  packages=['sitemap'],
  version='20191121',
  license='MIT',
  description='Sitemap library',
  long_description=long_description,
  author='Xiuming Chen',
  author_email='cc@cxm.cc',
  url='https://github.com/cxmcc/sitemap-python',
  keywords=['sitemap'],
  install_requires=[],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
    'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
    'Topic :: Internet :: WWW/HTTP :: Site Management',
  ],
)
