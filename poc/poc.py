# coding: utf-8
from odf.opendocument import OpenDocumentText as ODT
from odf.style import Style, TextProperties
from odf.text import H, P, Span
odt = ODT()
s = odt.styles
h1s = Style(name="Heading 1", family="paragraph")
h1s.addElement(TextProperties(attributes={'fontsize':"24pt", 'fontweight':"bold"}))
s.addElement(h1s)
h = H(outlinelevel=1, stylename=h1s, text="Textão")
odt.text.addElement(h)
odt.save("meuarq.odt")
