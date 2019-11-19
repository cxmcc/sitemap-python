import pytest
from datetime import datetime
from sitemap import UrlSet, Url, Sitemap, SiteIndex


def test_urlset():
    urlset = UrlSet()
    url = Url('https://www.example.com/', priority=0.1)
    urlset.add_url(url)

    expected = '''<?xml version='1.0' encoding='utf-8'?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"><url><loc>https://www.example.com/</loc><priority>0.1</priority></url></urlset>'''
    assert urlset.to_string() == expected


class TestUrl(object):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.loc = 'https://www.example.com/'
        self.lastmod = datetime.utcnow()
        self.changefreq = 'hourly'
        self.priority = 0.3

    def test_invalid_url_input(self):
        with pytest.raises(AssertionError):
            Url(loc=self.loc, lastmod=123)
        with pytest.raises(AssertionError):
            Url(loc=self.loc, changefreq='unknown')
        with pytest.raises(AssertionError):
            Url(loc=self.loc, priority=2.0)

    def test_happy_path(self):
        url = Url(
            loc=self.loc,
            lastmod=self.lastmod,
            changefreq=self.changefreq,
            priority=self.priority
        )
        assert isinstance(url, Url)


class TestSitemap(object):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.loc = 'https://www.example.com/'
        self.lastmod = datetime.utcnow()

    def test_invalid_sitemap_input(self):
        with pytest.raises(AssertionError):
            Sitemap(loc=self.loc, lastmod=123)

    def test_happy_path(self):
        sitemap = Sitemap(
            loc=self.loc,
            lastmod=self.lastmod
        )
        assert isinstance(sitemap, Sitemap)