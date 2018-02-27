#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import takewhile
import os, sys, string
nominative = ['li','ish','is','il','i','hash','has'] #subject pronouns
accusative = ['sa','si','chi','pi','hachi']
dative = ['am','sam','s'+u"\u00E3", u"\u00E3", 'chim','ch'+u"\u00EF", 'im',u"\u00EF",'pim','p'+u"\u00EF", 'hachim','hach'+u"\u00EF"]
benefactive = ['ami','sami','chimi','imi','pimi','hachimi']