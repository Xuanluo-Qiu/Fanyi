import sys

from fy_http import *
from display import *

args = sys.argv[:]

word = args[1]

display(word, get_word(word))