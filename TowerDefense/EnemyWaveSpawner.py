import pygame, math, random
from Vector2 import Vector2
from TowerDefense.Enemies.Robber import Robber
from TowerDefense.Enemies.HorseRobber import HorseRobber

class EnemyWaveSpawner():

    def __init__(self, levelReference, waveNumber):
        self.levelReference = levelReference
        self.waveNumber = waveNumber
        self.spawnTimer = 0
        self.spawnEnemyInterval = 1

        numberOf3Rounds = 0
        k = waveNumber
        while k >= 3:
            k -= 3
            numberOf3Rounds += 1

        self.robberBonusSpeed = 0 + (numberOf3Rounds * 3)
        self.horseBonusSpeed = 0 + (numberOf3Rounds * 3)

        self.spawnedEnemies = 0
        self.enemiesToSpawn = 10 + numberOf3Rounds

        if self.robberBonusSpeed >= 30:
            self.robberBonusSpeed = 30

        if self.horseBonusSpeed >= 60:
            self.horseBonusSpeed = 60


    def update(self, deltaTime):

        if self.spawnedEnemies < self.enemiesToSpawn:
            self.spawnTimer += deltaTime
            if self.spawnTimer >= self.spawnEnemyInterval:
                self.spawnTimer = 0

                robberHealth = math.floor(10 + (10 / 100 * (self.waveNumber * 60)))
                robberGoldOnKill = math.floor(14 + (14 / 100 * (self.waveNumber * 12)))
                robberScoreOnKill = math.floor(10 + (10 / 100 * (self.waveNumber * 10)))
                robberGoldToSteal = math.floor(25 + (25 / 100 * (self.waveNumber * 65)))

                horseHealth = math.floor(6 + (6 / 100 * (self.waveNumber * 35)))
                horseGoldOnKill = math.floor(6 + (6 / 100 * (self.waveNumber * 12)))
                horseScoreOnKill = math.floor(10 + (10 / 100 * (self.waveNumber * 10)))

                if self.waveNumber < 3:
                    self.spawnedEnemies += 1
                    Robber(self.robberBonusSpeed, robberHealth, robberGoldOnKill, robberScoreOnKill, robberGoldToSteal, self.levelReference.level1LinePositions, self.levelReference, self.levelReference.allSprites, self.levelReference.enemySprites)
                else:
                    chanceToSpawnOnlyRobber = math.floor(62 - (62 / 100 * (self.waveNumber * 1)))

                    if chanceToSpawnOnlyRobber <= 40:
                        chanceToSpawnOnlyRobber = 40

                    if random.randint(0, 100) < chanceToSpawnOnlyRobber:
                        self.spawnedEnemies += 1
                        Robber(self.robberBonusSpeed, robberHealth, robberGoldOnKill, robberScoreOnKill, robberGoldToSteal,
                               self.levelReference.level1LinePositions, self.levelReference,
                               self.levelReference.allSprites, self.levelReference.enemySprites)
                    else:
                        self.spawnedEnemies += 2  # de robber en de horse dus 2
                        robber = Robber(self.robberBonusSpeed, robberHealth, robberGoldOnKill, robberScoreOnKill, robberGoldToSteal,
                                        self.levelReference.level1LinePositions, self.levelReference)
                        HorseRobber(self.horseBonusSpeed, horseHealth, horseGoldOnKill, horseScoreOnKill, robber,
                                    self.levelReference.level1LinePositions, self.levelReference,
                                    self.levelReference.allSprites, self.levelReference.enemySprites)


