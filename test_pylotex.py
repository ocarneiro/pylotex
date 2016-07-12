from odt import Odt
from unittest import mock
from odf.opendocument import OpenDocumentText as ODT

def test_generate_odt():
    """Tests if an odt file is properly generated"""
    odt = Odt()

def test_add_text_to_odt():
    """Tests if add method is called on odt"""
    mock_generator = mock.MagicMock()
    odt = Odt(generator=mock_generator)
    odt.add_text("Testing")
    mock_generator.text.addElement.assert_called_with("Testing")
