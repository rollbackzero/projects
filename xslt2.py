from lxml import etree

xslRoot = etree.fromstring(open("template2.xsl", 'rb').read())
transform = etree.XSLT(xslRoot)
xmlRoot = etree.fromstring(open("xmldata2.xml", 'rb').read())
transRoot = transform(xmlRoot)
print(etree.tostring(transRoot))
