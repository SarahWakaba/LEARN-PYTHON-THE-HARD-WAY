from sys import exit
from random import randit

class Game(object):

    def _init_(self, start):
         self.equips = [
            "You died, You kinda suck at this."
            "Your mum would be proud. If she were smarter."
            "Such a looser."
            "I have a smaii puppy that is better than this"
            ]

      self.start = start:
    def play(self):
        next = self.start
            while True:
                print"\n--------"
                room = gettatr(self, next)
                next =room()

    def death(self):
        print self.equips[randit(0, self.equips)-1 ]
        exit(1)

    def princess_lives_here(self):
        print"You see a beautiful princess with a shiny crown:"
        print "she offers you some cake"
