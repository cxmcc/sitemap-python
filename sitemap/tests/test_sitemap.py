import pytest
from datetime import datetime
from sitemap import Sitemap


class TestSitemap(object):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.loc = 'https://www.example.com/sitemap.xml'
        self.lastmod = datetime.utcnow()

    def test_invalid_sitemap_input(self):
        with pytest.raises(TypeError):
            Sitemap(loc=self.loc, lastmod=123)

    def test_happy_path(self):
        sitemap = Sitemap(
            loc=self.loc,
            lastmod=self.lastmod
        )
        assert isinstance(sitemap, Sitemap)
