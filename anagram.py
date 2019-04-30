import math
import os
import random
import re
import sys
from collections import Counter

def substringAnagrams(s):
  count = 0
  substrings = []
  l = len(s)
  i = 0
  while i < l:
    j = i + 1
    while j <= len(s):
      sub = s[i:j]
      for x in substrings:
        if(areAnagrams(sub, x)):
          count = count + 1
      substrings.append(sub)
      j = j + 1
    i = i + 1
  return count

def areAnagrams(s1, s2):
  return Counter(s1) == Counter(s2)