# -*- coding: utf-8 -*-
#
# Poio Tools for Linguists
#
# Copyright (C) 2009-2013 Poio Project
# Author: Peter Bouda <pbouda@cidles.eu>
# URL: <http://media.cidles.eu/poio/>
# For license information, see LICENSE

import unicodedata

def first_word_character(string):
    for i, ch in enumerate(string):
        if is_word_character(ch):
            return i

    return -1

def last_word_character(string):
    result = first_word_character(reverse(string))
    if result == -1:
        return -1
    return len(string) - result

def is_word_character(char):
    if unicodedata.category(char)[0] == "C":
        return True
    return False
