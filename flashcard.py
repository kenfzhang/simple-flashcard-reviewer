# Basic flashcard reader

# Author: Kenneth Zhang
# https://www.github.com/kenfzhang

# Usage:
# $ python flashcard.py <csv file>

# csv file rows have the format:
# <front of card>, <back of card>

import csv
import random
import sys
import os

def load_flashcards(path, topic):
  with open(path) as csvfile:
    cards = []
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
      if len(row) == 2 or row[2] in topic or len(topic) == 0:
        cards.append(row)
    return cards

# Limits columns taken by text
def format_text(s,n):
  s_new = ""
  i = 0
  new_lined = False
  lines = 1
  while i < len(s):
    if s[i] == ' ' and lines * n < i:
      s_new += "\n            "
      lines += 1
    else:
      s_new += s[i]
    i += 1
  return s_new

def main():
  cards = load_flashcards(sys.argv[1], sys.argv[2:len(sys.argv)] if len(sys.argv) >= 3 else [])
  random.shuffle(cards)

  state = 'p'
  os.system('cls' if os.name == 'nt' else 'clear')
  i = 0
  while i < len(cards) and state != 'q':
    print("\n\n  QUESTION: "+format_text(cards[i][0],50)+"\n")

    
    state = input('')
    print("    |")
    print("    v\n")
    print("\n  ANSWER:   "+format_text(cards[i][1],50)+"\n")
    if len(cards[i]) > 2:
      print("  ["+cards[i][2]+"]\n")
    state = input('\n>============ ('+str(i+1)+' / '+str(len(cards))+')')
    i += 1

if __name__ == "__main__":
    # execute only if run as a script
    main()