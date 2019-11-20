import pytest
from datetime import datetime
from sitemap import Urlset, Url


def test_urlset():
    urlset = Urlset()
    url = Url('https://www.example.com/', priority=0.1)
    urlset.add_url(url)

    expected = '''<?xml version='1.0' encoding='utf-8'?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"><url><loc>https://www.example.com/</loc><priority>0.1</priority></url></urlset>'''
    assert urlset.to_string() == expected
