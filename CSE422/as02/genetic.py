#!/usr/bin/env python3



########################################################
##### Name     : Abir Ahammed Bhuiyan    ###############
##### ID       : 20101197                ###############
##### Course   : CSE422                  ###############
##### Section  : 05                      ###############
##### Semester : Spring 2024             ###############
##### Lab No   : 02-Strange Bank Problem ###############
########################################################



from pprint import pprint
import random



class StrangeBankProblem:
    def __init__(self, fileName="./input.txt", num_iterations=1000):
        self.fileName = fileName
        self.num_iterations = num_iterations
        self.register = []
        self.sequence_length = None
        self.population = []
        self.population_fitness = []
        self.quantity = 4


    def run(self):
        self.TakeInput(self.fileName)
        self.CreateGeneration(self.quantity)
        Solution = None

        for _ in range(self.num_iterations):
            self.CalculatePopulationFitness()
            sequence = self.FindZero()
            if sequence and sequence != "0"*self.sequence_length:
                Solution = sequence
                break
            self.SelectFittest()
            self.Crossover()
            self.Mutation()
            
        print(Solution) if Solution else print("-1")


    def Mutation(self):
        for i in range(len(self.population)):
            index_to_flip = random.randint(0, self.sequence_length-1)
            self.population[i] = self.population[i][:index_to_flip] + \
                     ('0' if self.population[i][index_to_flip] == '1' else '1') + \
                     self.population[i][index_to_flip+1:]
            

    def FindZero(self):
        for group in self.population_fitness:
            if group[1] == 0:
                return group[0]
        return False


    def Crossover(self):
        children = []
        num_parents = len(self.population)
        for _ in range(2):
            parent1, parent2 = random.sample(self.population, 2)
            crossover_point = random.randint(1, len(parent1) - 1)
            child1 = parent1[:crossover_point] + parent2[crossover_point:]
            child2 = parent2[:crossover_point] + parent1[crossover_point:]
            children.extend([child1, child2])

        self.population = children


    def CreateGeneration(self, quantity):
        for _ in range(quantity):
            self.population.append(''.join([random.choice('01') for _ in range(self.sequence_length)]))


    def CalculatePopulationFitness(self):
        self.population_fitness = []
        for chromosome in self.population:
            self.population_fitness.append((chromosome, abs(self.CalculateFitness(chromosome))))

        
    def SelectFittest(self):
        worst_fitness = max(self.population_fitness, key=lambda x: x[1])
        self.population_fitness.remove(worst_fitness)


    def CalculateFitness(self, sequence):
        total = 0
        for index, char in enumerate(sequence):
            if int(char):
                category, amount = self.register[index]
                
                if category == 'd':
                    total += amount
                else:
                    total -= amount 

        return total


    def Mapper(self, sequence):
        for index, char in enumerate(sequence):
            if int(char):
                print(f"{self.register[index][0]} {self.register[index][1]}")


    def TakeInput(self, fileName):
        with open(fileName, 'r') as fi:
            self.sequence_length = int(fi.readline())

            for _ in range(self.sequence_length):
                category, amount = fi.readline().split()
                self.register.append((category, int(amount)))



if __name__ == "__main__":
    StrangeBankProblem().run()

