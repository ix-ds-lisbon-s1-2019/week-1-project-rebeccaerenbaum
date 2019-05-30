#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:59:42 2019

@author: beccaerenbaum
"""

import random
        
class PokerGame:
    
    def __init__(self, number_of_players):
        self.number_of_players = input("how many players?") #class attribute
    
    def names(self):
        self.namelist = []
        for i in range(int(self.number_of_players)):
            self.namelist.append(input("What is your name?"))
            
    def dealcards(self):
        self.possiblevalues = ["2H","2D","2C","2S", "3H", "3D", "3C", "3S", "4H", "4D", "4C", "4S", "5H", "5D", "5C", "5S", "6H", "6D", "6C", "6S","7H", "7D", "7C", "7S", "8H", "8D", "8C", "8S", "9H", "9D", "9C", "9S", "10H", "10D", "10C", "10S", "QH", "QD", "QC", "QS", "JH", "JD", "JC", "JS", "KH", "KD", "KC", "KS", "AH", "AD", "AC", "AS"]
        self.playerandcards = {}
        for player in self.namelist:
            cards = []
            for val in range(5):
                card = random.choice(self.possiblevalues)
                index = self.possiblevalues.index(card)
                self.possiblevalues.pop(index)
                cards.append(card)
                #self.possiblevalues.pop(val)
            self.playerandcards[player] = cards
                
        print(self.playerandcards)
   
    def winninghand(self):
        self.maxname = []
        for key, value in self.playerandcards.items():
            if "AH" in value or "AD" in value or "AC" in value or "AS" in value:
                self.maxname.append(key)
        print(self.maxname)
        if not self.maxname:
            for key, value in self.playerandcards.items():
                if "KH" in value or "KD" in value or "KC" in value or "KS" in value:
                    self.maxname.append(key)
        elif not self.maxname:
         for key, value in self.playerandcards.items():
                if "QH" in value or "QD" in value or "QC" in value or "QS" in value:
                    self.maxname.append(key)
        if len(self.maxname) > 1:
            count = 0
            maxcount = 0
            winner = ""
            for key, value in self.playerandcards.items():
                for card in value:
                    x = card.count("A")
                    y = card.count("K")
                    if x > count:
                        count == x
                        if count > maxcount:
                            maxcount == count
                            winner += key
                    elif y > count:
                        count == y
                        if count > maxcount:
                            maxcount == count
                            winner += key
        print("The winner is " + winner)
        #print("The winner is " + self.maxname[0])
                
                
                
game1 = PokerGame(6)
game1.names()
game1.dealcards()
game1.winninghand()

