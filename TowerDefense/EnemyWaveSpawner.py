import pygame, math, random
from Vector2 import Vector2
from TowerDefense.Enemies.Robber import Robber
from TowerDefense.Enemies.HorseRobber import HorseRobber

class EnemyWaveSpawner():

    def __init__(self, levelReference, waveNumber):
        self.levelReference = levelReference
        self.waveNumber = waveNumber
        self.spawnTimer = 0
        self.spawnEnemyInterval = 1.4

        numberOf5Rounds = 0
        i = waveNumber
        while i >= 3:
            i -= 3
            numberOf5Rounds += 1

        self.spawnedEnemies = 0
        self.enemiesToSpawn = 10 + numberOf5Rounds


    def update(self, deltaTime):

        if self.spawnedEnemies < self.enemiesToSpawn:
            self.spawnTimer += deltaTime
            if self.spawnTimer >= self.spawnEnemyInterval:
                self.spawnTimer = 0

                robberHealth = math.floor(18 + (18 / 100 * (self.waveNumber * 32)))
                robberGoldOnKill = math.floor(10 + (10 / 100 * (self.waveNumber * 20)))
                robberScoreOnKill = math.floor(10 + (10 / 100 * (self.waveNumber * 10)))
                robberGoldToSteal = math.floor(32 + (32 / 100 * (self.waveNumber * 20)))

                if robberGoldToSteal > 700:
                    robberGoldToSteal = 700

                horseHealth = math.floor(6 + (6 / 100 * (self.waveNumber * 32)))
                horseGoldOnKill = math.floor(6 + (6 / 100 * (self.waveNumber * 20)))
                horseScoreOnKill = math.floor(10 + (10 / 100 * (self.waveNumber * 10)))

                if self.waveNumber < 3:
                    self.spawnedEnemies += 1
                    Robber(robberHealth, robberGoldOnKill, robberScoreOnKill, robberGoldToSteal, self.levelReference.level1LinePositions, self.levelReference, self.levelReference.allSprites, self.levelReference.enemySprites)
                else:
                    chanceToSpawnOnlyRobber = math.floor(75 - (75 / 100 * (self.waveNumber * 1)))

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


