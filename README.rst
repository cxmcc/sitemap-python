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

Urlset
^^^^^^

.. code:: python

    from sitemap import Url, Urlset
    
    urlset = Urlset()
    url = Url('https://www.example.com/', changefreq='weekly')
    
    urlset.add_url(url)

    # urlset.to_string()
    urlset.write_xml('sitemap.xml')

Siteindex
^^^^^^^^^

.. code:: python

    from sitemap import Sitemap, Siteindex
    
    siteindex = Siteindex()
    sitemap = Sitemap('https://www.example.com/sitemap.xml')
    
    siteindex.add_sitemap(sitemap)

    # siteindex.to_string()
    siteindex.write_xml('sitemap.xml')

