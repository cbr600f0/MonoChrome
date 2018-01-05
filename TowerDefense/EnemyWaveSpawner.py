import pygame, math
from Vector2 import Vector2
from TowerDefense.Enemies.Robber import Robber

class EnemyWaveSpawner():

    def __init__(self, levelReference, waveNumber):
        self.levelReference = levelReference
        self.waveNumer = waveNumber

        self.spawnTimer = 0
        self.spawnEnemyInterval = 1.4
        self.mark = 10

        self.spawnedEnemies = 0
        self.enemiesToSpawn = 10

    def update(self, deltaTime):

        if self.spawnedEnemies < self.enemiesToSpawn:
            self.spawnTimer += deltaTime
            if self.spawnTimer >= self.spawnEnemyInterval:
                self.spawnTimer = 0
                Robber(self.levelReference.level1LinePositions, self.levelReference, self.levelReference.allSprites, self.levelReference.enemySprites)
                self.spawnedEnemies += 1


