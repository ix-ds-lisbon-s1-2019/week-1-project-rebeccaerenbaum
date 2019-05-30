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
        winninghandvals = {}
        stringtovals = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}

        for key,value in self.playerandcards.items():
            winninghandvals[key] = []
            for card in value:
                letter = card[:-1]
                winninghandvals[key].append(stringtovals[letter])
        maxname = []
        maxi = 0
        for key,value in winninghandvals.items():
            if max(value) > maxi:
                maxi = max(value)
                winninghandvals[key].remove(max(value))
                maxname = [key]
            elif max(value) == maxi:
                winninghandvals[key].remove(max(value))
                maxname.append(key)
        while len(maxname) > 1:
            alive = maxname
            maxname = []
            maxi = 0
            for name in alive:
                vlist = winninghandvals[name]
                if max(vlist) > maxi:
                    maxi = max(vlist)
                    winninghandvals[name].remove(max(vlist))
                    maxname = [name]
                elif max(vlist) == maxi:
                    winninghandvals[name].remove(max(vlist))
                    maxname.append(name)
        print("The winner is " + str(maxname))
                 
        #print("The winner is " + winner)
        #print("The winner is " + self.maxname[0])
                
                
                
game1 = PokerGame(6)
game1.names()
game1.dealcards()
game1.winninghand()

