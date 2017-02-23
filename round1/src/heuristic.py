import numpy as np

inDir = '../in/'
fileNames = ['big_trending_today.in','large_kittens.in','medium_videos_worth_spreading.in','small_me_at_the_zoo.in']

def readInput(filename):
    # read input file output:
    # list of videos (size)
    # list of enpoints (default time, list((cache, time)))
    # list of caches (list(endpoint))
    # list of requests (vid, ep, number)
    with open(inDir+filename,'r') as fyle:
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
        
print(readInput(fileNames[3]))