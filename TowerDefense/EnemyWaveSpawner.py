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
        self.enemiesToSpawn = 10

    def update(self, deltaTime):

        if self.spawnedEnemies < self.enemiesToSpawn:
            self.spawnTimer += deltaTime
            if self.spawnTimer >= self.spawnEnemyInterval:
                self.spawnTimer = 0

                robberHealth = math.floor(28 + (30 / 100 * (self.waveNumber * 16)))
                print("LVL: " + str(self.waveNumber) + " Robber: " + str(robberHealth))
                robberGoldOnKill = 20
                robberScoreOnKill = 10
                robberGoldToSteal = 20

                horseHealth = math.floor(12 + (12 / 100 * (self.waveNumber * 16)))
                print("LVL: " + str(self.waveNumber) + "Horse: " + str(horseHealth))
                horseGoldOnKill = 10
                horseScoreOnKill = 10

                if self.waveNumber < 5:
                    self.spawnedEnemies += 1
                    Robber(robberHealth, robberGoldOnKill, robberScoreOnKill, robberGoldToSteal, self.levelReference.level1LinePositions, self.levelReference, self.levelReference.allSprites, self.levelReference.enemySprites)
                else:
                    if random.randint(0, 100) < 70:
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


