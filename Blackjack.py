#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:22:26 2020

@author: meeps360
"""
import random

class Player(object):
    
    def __init__(self, name, value): #initializes user
        self.value = value
        self.name = name
                
    def __str__(self): #prints player info
        return "Player name: " + str(self.name) + "\nHand: " + str(self.value)
            
    def addValue(self, input):
        self.value += input
        return self.value
    
    def getValue(self):
        return self.value
    
    def deal(self): #deals the card to the player
        deal = random.choice([2, 3, 4, 5, 6, 7, 8, 9 ,10, 11])
        if deal == 11:
            if (self.value + deal > 21):
                self.addValue(1)
            else:
                self.addValue(11)
        else:
            self.addValue(deal)


class CPU(object): #initializes CPU
    def __init__(self, value):
        self.value = value
    
    def deal(self): #deals the card to the CPU
        deal = random.choice([2, 3, 4, 5, 6, 7, 8, 9 ,10, 11])
        if deal == 11:
            if (self.value + deal > 21):
                self.addValue(1)
            else:
                self.addValue(11)
        else:
            self.addValue(deal)
            
    def getValue(self):
        return self.value
    
    def addValue(self, input):
        self.value += input
        return self.value
            
            
print("Welcome to Blackjack")
name = input("What is your name? ")
player = Player(name, 0)
print("Hello " + name)
print("To play, type in \"1\" to draw a card. If you do not wish to draw and want to pass it onto the computer, type in \"2\"")

while True:
    enter = int(input("Hit or Pass? "))
    if enter == 1:
        player.deal()
        print(player)
    elif enter == 2:
        print("You choose to pass, moving on the CPU's turn")
        break
    else:
        print("Input was not registered, try again")
    
    if player.getValue() > 21:
        print("You went over 21 and got ", player.getValue())
        break
    elif player.getValue() == 21:
        print("You got 21!")
        break
        
if player.getValue() == 21:
    print("You win")
elif player.getValue() < 21:
    print("")
else:
    print("You lose")

cpu = CPU(0)
if player.getValue() < 21:
    while True:
        cpu.deal()
        if cpu.getValue() > 21:
            print("You won, the CPU has a hand of ", cpu.getValue())
            break
        elif cpu.getValue() == 21:
            print("You lose, the CPU has a hand of 21")
            break
        if cpu.getValue() < 21 and cpu.getValue() > player.getValue():
            print("You lose, the CPU has a hand of ", cpu.getValue(), " and you have a hand of ", player.getValue())
            break
        
        
        
        
        
        
        
        
