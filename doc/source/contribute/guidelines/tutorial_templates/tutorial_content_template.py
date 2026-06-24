# Copyright (C) 2020 - 2026 ANSYS, Inc. and/or its affiliates.
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

# _order: 1
"""
Content formatting examples
============================

This file shows how to use different RST formatting patterns inside
sphinx-gallery tutorial cells.
"""
###############################################################################
# Bullet lists
# ------------
#
# Enumerate something:
#
# - something 1;
# - something 2;
# - something 3.
#
# Enumerate something with a numbered list:
#
# #. something 1;
# #. something 2;
# #. something 3.

# Code block

###############################################################################
# Bullet lists with explanations between items
# --------------------------------------------
#
# Enumerate something and reference each item to use it as a subheading:
#
# - :ref:`Something 1<ref_something_1>`;
# - :ref:`Something 2<ref_something_2>`;
# - :ref:`Something 3<ref_something_3>`.
#
# .. _ref_something_1:
#
# Something 1
# ^^^^^^^^^^^
#
# Explanation 1

# Code block 1

###############################################################################
# .. _ref_something_2:
#
# Something 2
# ^^^^^^^^^^^
#
# Explanation 2

# Code block 2

###############################################################################
# .. _ref_something_3:
#
# Something 3
# ^^^^^^^^^^^
#
# Explanation 3

# Code block 3
