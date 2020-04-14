from lxml import etree

xslRoot = etree.fromstring(open("template.xsl", 'rb').read())
transform = etree.XSLT(xslRoot)
xmlRoot = etree.fromstring(open("xmldata.xml", 'rb').read())
transRoot = transform(xmlRoot)
print(etree.tostring(transRoot))
