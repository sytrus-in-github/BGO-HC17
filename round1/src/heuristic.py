import numpy as np

inDir = '../in/'
fileNames = ['big_trending_today.in','large_kittens.in','medium_videos_worth_spreading.in','small_me_at_the_zoo.in']
fileName = fileNames[3]

def readInput():
    # read input file output:
    # list of videos (size)
    # list of enpoints (default time, list((cache, time)))
    # list of caches (list(endpoint))
    # list of requests (vid, ep, number)
    with open(inDir+fileName,'r') as fyle:
        l = fyle.readline()
        # read first line, initialize lists
        nbVid, nbEp, nbReq, nbCache, cacheSize = [int(i) for i in l.split()]
        eps = []
        caches = [[]]*nbCache;
        requests = []
        # fill vidSizes
        l = fyle.readline()
        vidSizes = [int(i) for i in l.split()]
        # fill end point list and cache list
        for i in range(nbEp):
            l = fyle.readline()
            defaultT, nblink = [int(i) for i in l.split()]
            links = []
            for j in range(nblink):
                l = fyle.readline()
                cacheId, t = [int(i) for i in l.split()]
                caches[cacheId].append(i)
                links.append((cacheId, t))
            caches.append((defaultT, links))
        # fill request list
        for i in range(nbReq):
            l = fyle.readline()
            requests.append([int(i) for i in l.split()])

        return vidSizes, eps, caches, requests, cacheSize
        
def rankAll(spupMat, nbepMat, nbep, regCoeff):
    # return ranking and score as matrices of shape (nbcache, nbvid)
    nbcache = len(nbepMat)
    # score function !
    score = lambda spup, ep: spup - regCoeff * ep / nbep
    # compute and store list of list of scores
    scores = []
    for i in range(nbcache):
        scores.append([score(s, e) for (s, e) in zip(spupMat[i,:], nbepMat[i,:])])
    # sort list per cache
    ranks = []
    skores = [] # permuted scores
    for l in scores:
        lstPair = sorted(enumerate(l), key=lambda x: x[0])
        ranks.append([x[0] for x in lstPair])
        skores.append([x[1] for x in lstPair])
    return ranks, skores
    
def cacheFillAll(ranks, scores, vidSizes, cacheMem):
    # naive fill-up of caches
    nbcache = len(ranks)
    fills = [[]] * nbcache
    for i in range(nbcache):
        availableMem = cacheMem
        for r in ranks[i]:
            if vidSizes[r] <= availableMem:
                fills[i].append(r)
                availableMem -= vidSizes[r]
    return fills

outDir = '../out/'
    
def outputFile(fills):
    usefulfills = [l for l in fills in l]
    nbuseful = len(usefulfills)
    with open(outDir+fileName,'w') as out:
        out.write(str(nbuseful)+'\n')
        for l in usefulfills:
            s = ''
    
print(readInput(fileNames[3]))