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
            eps.append((defaultT, links))
        # fill request list
        for i in range(nbReq):
            l = fyle.readline()
            requests.append([int(i) for i in l.split()])

        return vidSizes, eps, caches, requests, cacheSize

def caculate_sum(num_video, eps, num_cache, request):
    requestnum = len(request)
    #print requestnum
    #print len(num_cache)
    sum_time = np.zeros(shape=(len(num_cache),len(num_video)), dtype=int)
    
    num_end = np.zeros(shape=(len(num_cache),len(num_video)), dtype=int)
    
    for req in range(requestnum):
        #print req
        onereq = request[req]
        ep = eps[onereq[1]]
        cache_time = ep[1]
        default_time = ep[0]
        for cache, time in cache_time:
            sum_time[cache][onereq[0]] += (default_time-time)*onereq[2]
            #!!!!! reduce
            num_end[cache][onereq[0]] += 1
    return sum_time,num_end
#print(readInput(fileNames[3]))

vidSizes, eps, caches, requests, cacheSize = readInput(fileNames[3]);
print len(requests)
s_time, num_ep = caculate_sum(vidSizes,eps,caches,requests);
print num_ep