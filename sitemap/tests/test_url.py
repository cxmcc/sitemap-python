import pytest
from datetime import datetime
from sitemap import Url


class TestUrl(object):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.loc = 'https://www.example.com/'
        self.lastmod = datetime.utcnow()
        self.changefreq = 'hourly'
        self.priority = 0.3

    def test_invalid_url_input(self):
        with pytest.raises(TypeError):
            Url(loc=self.loc, lastmod=123)
        with pytest.raises(ValueError):
            Url(loc=self.loc, changefreq='unknown')
        with pytest.raises(ValueError):
            Url(loc=self.loc, priority=2.0)

    def test_happy_path(self):
        url = Url(
            loc=self.loc,
            lastmod=self.lastmod,
            changefreq=self.changefreq,
            priority=self.priority
        )
        assert isinstance(url, Url)
