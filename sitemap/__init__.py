import datetime
import io
import xml.etree.cElementTree as etree


VALID_CHANGEFREQ = ['always', 'hourly', 'daily', 'weekly',
                    'monthly', 'yearly', 'never']
ATTR_XMLNS_XSI = 'http://www.w3.org/2001/XMLSchema-instance'
ATTR_XSI_SCHEMALOCATION_SITEMAP = (
    'http://www.sitemaps.org/schemas/sitemap/0.9 '
    'http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd'
)
ATTR_XSI_SCHEMALOCATION_SITEINDEX = (
    'http://www.sitemaps.org/schemas/sitemap/0.9 '
    'http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd'
)
ATTR_XMLNS = 'http://www.sitemaps.org/schemas/sitemap/0.9'


class Url:
    def __init__(self, loc, lastmod=None, changefreq=None, priority=None):
        if lastmod is not None:
            assert isinstance(lastmod, datetime.datetime)
        if changefreq is not None:
            assert changefreq in VALID_CHANGEFREQ
        if priority is not None:
            assert 0.0 <= priority <= 1.0
        self.loc = loc
        self.lastmod = lastmod
        self.changefreq = changefreq
        self.priority = priority

    def fill_doc(self, doc):
        etree.SubElement(doc, 'loc').text = self.loc
        if self.lastmod is not None:
            lastmod = self.lastmod.strftime('%Y-%m-%d')
            etree.SubElement(doc, 'lastmod').text = lastmod
        if self.changefreq is not None:
            etree.SubElement(doc, 'changefreq').text = self.changefreq
        if self.priority is not None:
            etree.SubElement(doc, 'priority').text = '%0.1f' % self.priority


class UrlSet:
    def __init__(self):
        self.urls = []

    def add_url(self, url):
        assert isinstance(url, Url)
        self.urls.append(url)

    def _to_etree(self):
        root = etree.Element('urlset')
        root.attrib['xmlns:xsi'] = ATTR_XMLNS_XSI
        root.attrib['xsi:schemaLocation'] = ATTR_XSI_SCHEMALOCATION_SITEMAP
        root.attrib['xmlns'] = ATTR_XMLNS
        for url in self.urls:
            doc = etree.SubElement(root, 'url')
            url.fill_doc(doc)
        tree = etree.ElementTree(root)
        return tree

    def to_string(self):
        tree = self._to_etree()
        with io.BytesIO() as f:
            tree.write(f, encoding='utf-8', xml_declaration=True)
            return f.getvalue().decode('utf-8')

    def write_xml(self, filename):
        tree = self._to_etree()
        tree.write(filename, encoding='utf-8', xml_declaration=True)


class Sitemap:
    def __init__(self, loc, lastmod=None):
        if lastmod is not None:
            assert isinstance(lastmod, datetime.datetime)
        self.loc = loc
        self.lastmod = lastmod

    def fill_doc(self, doc):
        etree.SubElement(doc, 'loc').text = self.loc
        if self.lastmod is not None:
            lastmod = self.lastmod.strftime('%Y-%m-%d')
            etree.SubElement(doc, 'lastmod').text = lastmod


class SiteIndex:
    def __init__(self):
        self.sitemaps = []

    def add_sitemap(self, sitemap):
        assert isinstance(sitemap, Sitemap)
        self.urls.append(sitemap)

    def _to_etree(self):
        root = etree.Element('siteindex')
        root.attrib['xmlns:xsi'] = ATTR_XMLNS_XSI
        root.attrib['xsi:schemaLocation'] = ATTR_XSI_SCHEMALOCATION_SITEINDEX
        root.attrib['xmlns'] = ATTR_XMLNS
        for sitemap in self.sitemaps:
            doc = etree.SubElement(root, 'sitemap')
            sitemap.fill_doc(doc)
        root = self._to_etree()
        tree = etree.ElementTree(root)
        return tree

    def to_string(self):
        tree = self._to_etree()
        with io.BytesIO() as f:
            tree.write(f, encoding='utf-8', xml_declaration=True)
            return f.getvalue().decode('utf-8')

    def write_xml(self, filename):
        tree = self._to_etree()
        tree.write(filename, encoding='utf-8', xml_declaration=True)
