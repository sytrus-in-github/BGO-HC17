#!/usr/bin/env python3

import sys

def showError(msg):
    print(msg)
    sys.exit(1)


def showHelp():
    showError('format: checker.py input_file output_file\n'
              'example: ./checker.py ../in/example.in ../out/example.out')


def getInput(inputFilename):
    def showInputError(msg, lineno=None):
        msg = 'invalid input file {filename}{line}: {msg}'.format(
                filename=inputFilename,
                line=' on line {}'.format(lineno) if lineno!=None else '',
                msg=msg)
        showError(msg)


    with open(inputFilename, 'r') as f:
        nRow, nCol, minGradient, maxCell = [int(x) for x in f.readline().split()]
        pizza = []
        for i,line in enumerate(f):
            i += 2
            line = line.rstrip()

            if not set(line).issubset(set('TM')):
                showInputError('invalid char', lineno=i)

            if len(line) != nCol:
                showInputError('invalid line length', lineno=i)

            pizza.append(line)

        if len(pizza) != nRow:
            showInputError('invalid number of lines')

        return nRow, nCol, minGradient, maxCell, pizza



def getAnswer(answerFilename):
    def showOutputError(msg, lineno=None):
        msg = 'invalid answer file {filename}{line}: {msg}'.format(
                filename=answerFilename,
                line=' on line {}'.format(lineno) if lineno!=None else '',
                msg=msg)
        showError(msg)


    with open(answerFilename, 'r') as f:
        nSlice = int(f.readline())
        slices = []
        for i in range(nSlice):
            row0, col0, row1, col1 = [int(x) for x in f.readline().split()]
            slices.append([row0, col0, row1, col1])

    return nSlice, slices


def new2dArray(nRow, nCol, init):
    return [[init for y in range(nCol)] for x in range(nRow)]


def subsum(a, r0, c0, r1, c1):
    return a[r1][c1] - a[r1][c0-1] - a[r0-1][c0] + a[r0-1][c0-1]


def main():
    if len(sys.argv) != 3:
        showHelp()

    R, C, L, H, pizza = getInput(sys.argv[1])
    nSlice, slices = getAnswer(sys.argv[2])

    count = {x:new2dArray(R+1, C+1, 0) for x in 'TM'}

    for i in range(R):
        for j in range(C):
            count[pizza[i][j]][i+1][j+1] = 1

    for c in 'TM':
        for i in range(1,R+1):
            for j in range(1,C+1):
                count[c][i][j] += count[c][i-1][j]+count[c][i][j-1]-count[c][i-1][j-1]

    sliceCount = new2dArray(R+2, C+2, 0)
    score = 0

    for r0,c0,r1,c1 in slices:
        if (r1-r0+1)*(c1-c0+1) > H:
            showError('too much cells in slice {},{},{},{}'.format(r0, c0, r1, c1))

        for c in 'TM':
            if subsum(count[c], r0+1, c0+1, r1+1, c1+1) < L:
                showError('not enough {} in slice {},{},{},{}'.format(c, r0, c0, r1, c1))

        sliceCount[r0+1][c0+1] += 1
        sliceCount[r0+1][c1+2] -= 1
        sliceCount[r1+2][c0+1] -= 1
        sliceCount[r1+2][c1+2] += 1

        score += (r1-r0+1)*(c1-c0+1)

    for i in range(1, R+1):
        for j in range(1, C+1):
            sliceCount[i][j] += sliceCount[i-1][j]+sliceCount[i][j-1]-sliceCount[i-1][j-1]
            assert 0 <= sliceCount[i][j]
            if sliceCount[i][j] > 1:
                showError('multiple slice covering cell ({},{})'.format(i-1, j-1))

    print('Score: {}'.format(score))


if __name__=='__main__':
    main()
else:
    showError('???')
