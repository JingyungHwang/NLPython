
import nltk
from nltk import CFG

grammer = CFG.fromstring("""
  S -> NP VP
  NP -> 'She' |  'That boy'
  VP -> 'sings a song.' | 'is reading a book.'
  """)

parser = nltk.ChartParser(grammer)

sentence = 'She!sings a song.'.split('!')
print(sentence) 
'''
위 방식은 임시 뗌빵에 가깝다. Chat GPT의 조언에 따르면 토큰화를 더욱 정교하게 하는 방식이 좋다.
예시 코드를 남긴다.
grammar = CFG.fromstring("""
  S -> NP VP
  NP -> 'She' | 'That' 'boy'
  VP -> 'sings' 'a' 'song' '.' | 'is' 'reading' 'a' 'book' '.'
""")
'''


#sentence = "That boy is reading a book."

for tree in parser.parse(sentence):
   tree.pretty_print()