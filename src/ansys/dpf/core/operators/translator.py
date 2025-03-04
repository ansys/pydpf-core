# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


class Markdown2RstTranslator:
    """A translator class for Markdown to RST text conversion."""
    def __init__(self):
        import pypandoc

        self._convert = pypandoc.convert_text

        # import mistune
        # from mistune.renderers.rst import RSTRenderer
        #
        # md2rst_converter = mistune.create_markdown(renderer=RSTRenderer())

    def convert(self, text:str) -> str:
        """Convert the Markdown text in input to RST."""
        return self._convert(
            source=text,
            to="rst",
            format="md",
            verify_format=False,  # Improves performance but does not check validity of format
            extra_args=["--eol=lf"],
        )
        # return md2rst_converter(specification.description)
