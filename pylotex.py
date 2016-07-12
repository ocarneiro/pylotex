#!/usr/bin/env python3

import odt

""" pylotex """

# TODO opens TeX file


# TODO creates odt file
def convert(text):
    odt_file = odt.Odt()
    odt_file.add_text("It works!")
    odt_file.save("didit.odt")

# TODO finds \begin{document}

# TODO iterates through TeX file and adds text to odt file

# TODO finds \end{document}

# TODO saves odt file

# sandbox
if __name__ == "__main__":
    convert("new text")
