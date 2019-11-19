sitemap
=======

Sitemap library for dynamically generating ``sitemap.xml``

.. image:: https://img.shields.io/pypi/v/sitemap.svg
    :target: https://pypi.python.org/pypi/sitemap

Installation
------------

.. code:: bash

    pip install sitemap

Usage
-----

.. code:: python

    from sitemap import Url, UrlSet
    
    urlset = UrlSet()
    url = Url('https://www.example.com/', changefreq='weekly')
    
    urlset.add_url(url)
    
    urlset.write_xml('sitemap.xml')
