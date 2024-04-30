import random
import copy

def evaluationFun (instance,graph) :
    if isinstance(instance,tuple):
        counter = 1
        weight = [0] * 2
        change = True 
        while (counter != len(instance)):
            predecs = [x[0] for x in graph[instance[counter]]]
            if (instance[counter-1] not in predecs):
                weight[0] = weight[0] + (10000 * (len(instance) - counter))
                change = False
            else:
                weight[0] += next((x[1] for x in graph[instance[counter]] if x[0] == instance[counter-1]))
                if (change == True):
                    weight[1]+=1
            counter +=1
        return weight
    elif isinstance(instance,set):
        weight = [0] * 2
        for path in instance :
            holdList = evaluationFun(path,graph) 
            if (weight[1] < holdList[1]):
                weight[1] = holdList[1]
            weight[0] = weight[0] + holdList[0]
        return weight
    

def selectionFun(population,graph,size):
    orderList = sorted([(x,evaluationFun(x,graph)[1]) for x in population],reverse=True,key= lambda x: x[1])
    parents = set()
    counter = 0
    while(len(parents) != size):
        parents.add(orderList[counter][0])
        counter += 1
    return parents    

def generateOffSprings(pop,parents):
    offSprings = []
    best_Parent = next((x for x in parents if evaluationFun(x,pop.graph)[1] == max([evaluationFun(y,pop.graph)[1] for y in parents])))
    startingPoint = evaluationFun(best_Parent,pop.graph)[1]
    pickList = [set() for _ in range(len(best_Parent))]
    index = startingPoint
    while(index != len(best_Parent) - 1):
        for parent in parents:
            pickList[index].add(parent[index])
        index += 1
    while (len(offSprings) != len(parents)):
        offSpring = list(best_Parent)[0:startingPoint]
        index = startingPoint+1
        while (index != len(best_Parent)):
            if not pickList[index] or all(x in offSpring for x in pickList[index]):
                offSpring.append(random.choice([x.name for x in pop.townList if x.name not in offSpring]))
            else:
                choice = random.choice([x for x in pickList[index] if x not in offSpring])
                offSpring.append(choice)
                pickList[index].remove(choice)
            index+=1
        offSpring.append(best_Parent[0])
        offSprings.append(tuple(offSpring))
    return set(offSprings)





def mututeOffspring(offSprings,mutationRate):
    path = random.choice(list(offSprings))
    if (random.random() <= mutationRate):
        p1 = random.randint(1,len(path) - 2)
        p2 = random.randint(1,len(path) - 2)
        pathlist = list(path)
        pathlist[p1] , pathlist[p2] = pathlist[p2], pathlist[p1]
        offSprings.remove(path)
        offSprings.add(tuple(pathlist))

def generateNewPop (oldPop,parents,offSprings,convergenceRate):
    newPop = set()
    nbOldPop = int(len(oldPop.listPath) * (1-convergenceRate))
    evalPaths = sorted([(evaluationFun(x,oldPop.graph)[1],x) for x in oldPop.listPath],key= lambda x:x[0])
    for i in range (0,nbOldPop):
        newPop.add(evalPaths[i][1])
    parentsOffSpring = list(parents)+list(offSprings)
    for i in range(0,len(parentsOffSpring)):
        newPop.add(parentsOffSpring[i])
    oldPop.listPath = newPop


def best_Path(population):
    best = random.choice(list(population.listPath))
    for path in population.listPath:
        if evaluationFun(best,population.graph)[1] < evaluationFun(path,population.graph)[1]:
            best = path
    return best


def checkPath(path,graph):
    distance = 0
    for index in range(1,len(path)):
        if path[index] not in [x[0] for x in graph[path[index-1]]]:
            return False
        distance += next((x[1] for x in graph[path[index-1]] if x[0] == path[index]),None)
        print(f'Im at the jump number {index} for now...')
    return distance