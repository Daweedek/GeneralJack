# -*- coding: utf-8 -*- 
class Car:
    def __init__(self):
        self.speed = 0
        self.armor = 0
        self.inventoryLvl = 0
        self.inventory = {
        }

    def repair(self):
        self.nextLevel = 15000

    def upgrade(self, what):
        pass
