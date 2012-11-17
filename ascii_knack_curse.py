#!/usr/bin/env python
# coding: utf-8
'''
    Simon ANDRÉ ©copyright
    Knack Computer ©copyright
    This file is part of ascii_gimp.

    Foobar is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Foobar is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
'''
from knack.gimp.ascii.Gen import GenAscii
from knack.gimp.ascii.utils import KnackError

try:
    generator = GenAscii('file')
    generator.load_char(None, [96,25,76,200])
    generator.generate_ascii([96,25,76,200,96,25,76,200])
    
except KnackError as e:
    print e.__str__()