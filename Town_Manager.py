import random
import copy

class Town:

    def __init__(self):
        self.name = None
        self.coordinates = (None,None)
    
class Population :

    townList = []
    graph = {}
    listPath = set()

    def __init__(self,nbTowns,complexityNb,populationSize):
        for n in range (1,nbTowns + 1):
            town = Town()
            town.name = f"Town #{n}"
            self.townList.append(town)
        self.complexityNb = complexityNb
        self.graph = {x.name : [] for x in self.townList}
        self.generatePredecessors(self.townList,complexityNb)
        rand = random.choice(self.townList).name
        self.generatePaths(rand,populationSize)

    

    def generatePredecessors(self,townList,complexityNb):
        for town in townList:
            nbPredec = random.randint(2,complexityNb)
            while len(self.graph[town.name]) != nbPredec:
                sample = random.choice(townList)
                listPredec = [x[0] for x in self.graph.get(town.name,[])]
                if (sample.name not in listPredec and sample != town):
                    distance = random.randint(50,200)
                    if(town.name in [x[0] for x in (self.graph.get(sample.name,[]))]):
                        distance = next((x for x in self.graph[sample.name] if x[0] == town.name), None)[1]
                    self.graph[town.name].append((sample.name,distance))

        #completing the predecessors

        for key in self.graph.keys():
            for predec in self.graph[key]:
                if (key not in [x[0] for x in self.graph[predec[0]]]):
                    self.graph[predec[0]].append((key,predec[1]))
    
    def generatePaths(self,startingTown,size):
        path = [startingTown]
        selection = [x.name for x in self.townList if x.name != startingTown]
        counter = 0
        while counter != size:
            weight = 0
            random.shuffle(selection)
            path.extend(selection)
            path.append(startingTown)
            self.listPath.add(tuple(copy.deepcopy(path)))
            path = [startingTown]
            counter += 1

