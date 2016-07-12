from odf.opendocument import OpenDocumentText as ODT
from odf.style import Style, TextProperties
from odf.text import H, P, Span


class Odt(object):

    def __init__(self, generator=None):
        self.generator = generator or ODT()
        self.setup()

    def add_text(self, text):
        h = H(outlinelevel=1, stylename=self.h1s, text=text)
        self.generator.text.addElement(h)

    def save(self, filename):
        self.generator.save(filename)

    def setup(self):
        odt = self.generator
        s = odt.styles
        h1s = Style(name="Heading 1", family="paragraph")
        h1s.addElement(
             TextProperties(
                 attributes={'fontsize': "24pt",
                             'fontweight': "bold"}
                           )
                      )
        s.addElement(h1s)
        self.h1s = h1s
