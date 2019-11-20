import datetime
import io
import xml.etree.cElementTree as etree


__all__ = ['Url', 'Urlset', 'Sitemap', 'Siteindex']


VALID_CHANGEFREQ = ['always', 'hourly', 'daily', 'weekly',
                    'monthly', 'yearly', 'never']
ATTR_XMLNS_XSI = 'http://www.w3.org/2001/XMLSchema-instance'
ATTR_XSI_SCHEMALOCATION_SITEMAP = (
    'http://www.sitemaps.org/schemas/sitemap/0.9 '
    'http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd'
)
ATTR_XSI_SCHEMALOCATION_SITEINDEX = (
    'http://www.sitemaps.org/schemas/sitemap/0.9 '
    'http://www.sitemaps.org/schemas/sitemap/0.9/siteindex.xsd'
)
ATTR_XMLNS = 'http://www.sitemaps.org/schemas/sitemap/0.9'


class Root:
    def to_string(self):
        tree = self._to_etree()
        with io.BytesIO() as f:
            tree.write(f, encoding='utf-8', xml_declaration=True)
            return f.getvalue().decode('utf-8')

    def write_xml(self, filename):
        tree = self._to_etree()
        tree.write(filename, encoding='utf-8', xml_declaration=True)


class Url:
    def __init__(self, loc, lastmod=None, changefreq=None, priority=None):
        if lastmod is not None:
            if not isinstance(lastmod, datetime.datetime):
                raise TypeError
        if changefreq is not None:
            if not isinstance(changefreq, str):
                raise TypeError
            if changefreq not in VALID_CHANGEFREQ:
                raise ValueError
        if priority is not None:
            if not isinstance(priority, (int, float)):
                raise TypeError
            if not 0.0 <= priority <= 1.0:
                raise ValueError
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


class Urlset(Root):
    def __init__(self):
        self.urls = []

    def add_url(self, url):
        if not isinstance(url, Url):
            raise TypeError
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


class Sitemap:
    def __init__(self, loc, lastmod=None):
        if lastmod is not None:
            if not isinstance(lastmod, datetime.datetime):
                raise TypeError
        self.loc = loc
        self.lastmod = lastmod

    def fill_doc(self, doc):
        etree.SubElement(doc, 'loc').text = self.loc
        if self.lastmod is not None:
            lastmod = self.lastmod.strftime('%Y-%m-%d')
            etree.SubElement(doc, 'lastmod').text = lastmod


class Siteindex(Root):
    def __init__(self):
        self.sitemaps = []

    def add_sitemap(self, sitemap):
        if not isinstance(sitemap, Sitemap):
            raise TypeError
        self.sitemaps.append(sitemap)

    def _to_etree(self):
        root = etree.Element('siteindex')
        root.attrib['xmlns:xsi'] = ATTR_XMLNS_XSI
        root.attrib['xsi:schemaLocation'] = ATTR_XSI_SCHEMALOCATION_SITEINDEX
        root.attrib['xmlns'] = ATTR_XMLNS
        for sitemap in self.sitemaps:
            doc = etree.SubElement(root, 'sitemap')
            sitemap.fill_doc(doc)
        tree = etree.ElementTree(root)
        return tree
