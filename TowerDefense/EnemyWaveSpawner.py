import pygame, math, random
from Vector2 import Vector2
from TowerDefense.Enemies.Robber import Robber
from TowerDefense.Enemies.HorseRobber import HorseRobber

class EnemyWaveSpawner():

    def __init__(self, levelReference, waveNumber):
        self.levelReference = levelReference
        self.waveNumer = waveNumber

        self.spawnTimer = 0
        self.spawnEnemyInterval = 1.3

        self.spawnedEnemies = 0
        self.enemiesToSpawn = 10

    def update(self, deltaTime):

        if self.spawnedEnemies < self.enemiesToSpawn:
            self.spawnTimer += deltaTime
            if self.spawnTimer >= self.spawnEnemyInterval:
                self.spawnTimer = 0
                if random.randint(0, 100) < 70:
                    self.spawnedEnemies += 1
                    Robber(self.levelReference.level1LinePositions, self.levelReference, self.levelReference.allSprites, self.levelReference.enemySprites)
                else:
                    self.spawnedEnemies += 2 # de robber en de horse dus 2
                    robber = Robber(self.levelReference.level1LinePositions, self.levelReference)
                    HorseRobber(robber, self.levelReference.level1LinePositions, self.levelReference, self.levelReference.allSprites, self.levelReference.enemySprites)


