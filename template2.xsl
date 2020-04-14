<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.example.org/routerconfig">
<xsl:template match="/">
    <xsl:for-each select="interfaces/interface">
        interface <xsl:value-of select="name"/><br />
            ip address <xsl:value-of select="ipv4addr"/><br />
    </xsl:for-each>
</xsl:template>
</xsl:stylesheet>

