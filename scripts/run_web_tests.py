#!/usr/bin/python
#
# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Test assumptions that web fonts rely on."""

import unittest

from nototools import font_data
from nototools.unittests import font_tests

FONTS = font_tests.load_fonts(
    ['out/web/*.ttf'],
    expected_count=18)

class TestItalicAngle(font_tests.TestItalicAngle):
    loaded_fonts = FONTS
    expected_italic_angle = -12.0


class TestMetaInfo(font_tests.TestMetaInfo):
    loaded_fonts = FONTS
    mark_heavier_as_bold = True

    # Since different font files are hinted at different times, the actual
    # outlines differ slightly. So we are keeping the version numbers as a hint.
    test_version_numbers = None

    # fsType of 0 marks the font free for installation, embedding, etc.
    expected_os2_fsType = 0
    expected_os2_achVendID = 'GOOG'


class TestNames(font_tests.TestNames):
    """Bugs:
    https://github.com/google/roboto/issues/37
    """

    loaded_fonts = FONTS
    family_name = 'Roboto'
    mark_heavier_as_bold = True
    expected_copyright = 'Copyright 2011 Google Inc. All Rights Reserved.'

    def expected_unique_id(self, full_name):
        return full_name


class TestDigitWidths(font_tests.TestDigitWidths):
    loaded_fonts = FONTS
    # disable this test while *.frac and *superior glyphs are separate
    # the webfont glyph subset contains *.frac but not *superior
    test_superscript_digits = False


class TestCharacterCoverage(font_tests.TestCharacterCoverage):
    loaded_fonts = FONTS

    include = frozenset([
        0xEE01, 0xEE02, 0xF6C3])  # legacy PUA

    exclude = frozenset([
        0x2072, 0x2073, 0x208F] +  # unassigned characters
        range(0xE000, 0xF8FF + 1) + range(0xF0000, 0x10FFFF + 1)  # other PUA
        ) - include  # don't exclude legacy PUA


class TestVerticalMetrics(font_tests.TestVerticalMetrics):
    loaded_fonts = FONTS

    expected_head_yMin = -555
    expected_head_yMax = 2163

    expected_hhea_descent = -500
    expected_hhea_ascent = 1900
    expected_hhea_lineGap = 0

    expected_os2_sTypoDescender = -512
    expected_os2_sTypoAscender = 1536
    expected_os2_sTypoLineGap = 102
    expected_os2_usWinDescent = 512
    expected_os2_usWinAscent = 1946


class TestLigatures(font_tests.TestLigatures):
    loaded_fonts = FONTS


class TestHints(font_tests.TestHints):
    loaded_fonts = FONTS


if __name__ == '__main__':
    unittest.main()
