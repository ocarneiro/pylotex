from odf.opendocument import OpenDocumentText as ODT


class Odt(object):

    def __init__(self, generator=None):
        self.generator = generator or ODT()

    def add_text(self, text):
        self.generator.text.addElement(text)
