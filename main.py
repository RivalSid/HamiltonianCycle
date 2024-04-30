from Town_Manager import *
from genetic import  *


def main():

    popSize=100
    convergenceRate = 0.4
    complexityNb = 8
    townNb = 20
    mutationRate = 0.1
    nbIteration = 10000
    pop = Population(townNb,complexityNb,popSize)
    


    for i in range (1,nbIteration + 1):
        parents = selectionFun(pop.listPath,pop.graph,5)
        kids = generateOffSprings(pop,parents)
        mututeOffspring(kids,mutationRate)
        generateNewPop(pop,parents,kids,convergenceRate)
        print(evaluationFun(pop.listPath,pop.graph))
        print(f'done iteration number [{i}]')
        print("****************************")

    best = best_Path(pop)
    print(f'best path is {best}')
    print(checkPath(best,pop.graph))













if __name__ == '__main__':
    main()