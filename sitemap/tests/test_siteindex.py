import pytest
from sitemap import Siteindex, Sitemap


def test_siteindex():
    siteindex = Siteindex()
    sitemap = Sitemap('https://www.example.com/sitemap.xml')
    siteindex.add_sitemap(sitemap)


    expected = '''<?xml version=\'1.0\' encoding=\'utf-8\'?>\n<siteindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/siteindex.xsd"><sitemap><loc>https://www.example.com/sitemap.xml</loc></sitemap></siteindex>'''
    assert siteindex.to_string() == expected
