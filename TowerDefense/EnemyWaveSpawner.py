import pygame, math, random
from Vector2 import Vector2
from TowerDefense.Enemies.Robber import Robber
from TowerDefense.Enemies.HorseRobber import HorseRobber

class EnemyWaveSpawner():

    def __init__(self, levelReference, waveNumber):
        self.levelReference = levelReference
        self.waveNumber = waveNumber
        self.spawnTimer = 0
        self.spawnEnemyInterval = 1.3

        self.spawnedEnemies = 0
        self.enemiesToSpawn = 14

    def update(self, deltaTime):

        if self.spawnedEnemies < self.enemiesToSpawn:
            self.spawnTimer += deltaTime
            if self.spawnTimer >= self.spawnEnemyInterval:
                self.spawnTimer = 0

                robberHealth = math.floor(22 + (22 / 100 * (self.waveNumber * 28)))
                robberGoldOnKill = math.floor(15 + (15 / 100 * (self.waveNumber * 16)))
                robberScoreOnKill = math.floor(10 + (10 / 100 * (self.waveNumber * 10)))
                robberGoldToSteal = math.floor(30 + (30 / 100 * (self.waveNumber * 20)))

                if robberGoldToSteal > 700:
                    robberGoldToSteal = 700

                horseHealth = math.floor(14 + (14 / 100 * (self.waveNumber * 28)))
                horseGoldOnKill = math.floor(8 + (8 / 100 * (self.waveNumber * 14)))
                horseScoreOnKill = math.floor(10 + (10 / 100 * (self.waveNumber * 10)))

                if self.waveNumber < 3:
                    self.spawnedEnemies += 1
                    Robber(robberHealth, robberGoldOnKill, robberScoreOnKill, robberGoldToSteal, self.levelReference.level1LinePositions, self.levelReference, self.levelReference.allSprites, self.levelReference.enemySprites)
                else:
                    chanceToSpawnOnlyRobber = math.floor(70 - (70 / 100 * (self.waveNumber * 1)))

                    if chanceToSpawnOnlyRobber <= 40:
                        chanceToSpawnOnlyRobber = 40

                    if random.randint(0, 100) < chanceToSpawnOnlyRobber:
                        self.spawnedEnemies += 1
                        Robber(robberHealth, robberGoldOnKill, robberScoreOnKill, robberGoldToSteal,
                               self.levelReference.level1LinePositions, self.levelReference,
                               self.levelReference.allSprites, self.levelReference.enemySprites)
                    else:
                        self.spawnedEnemies += 2  # de robber en de horse dus 2
                        robber = Robber(robberHealth, robberGoldOnKill, robberScoreOnKill, robberGoldToSteal,
                                        self.levelReference.level1LinePositions, self.levelReference)
                        HorseRobber(horseHealth, horseGoldOnKill, horseScoreOnKill, robber,
                                    self.levelReference.level1LinePositions, self.levelReference,
                                    self.levelReference.allSprites, self.levelReference.enemySprites)


