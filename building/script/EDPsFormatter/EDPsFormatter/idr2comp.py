# -*- coding: utf-8 -*-
import os
import pandas as pd

__all__ = ['idr2comp']


def idr2comp(edps, att):
    filedir = os.path.dirname(__file__).replace('\\', '/')

    stories = att['stories']
    IM = att['IM']
    IDRs = edps[:stories]
    otherEdps = edps[stories:]

    # Decide curve name
    cType = 'c'  # 丙类
    if IM <= 7:
        cIM = 7
    else:
        cIM = 8
    if stories <= 4:
        cStories = 4
    elif stories <= 6:
        cStories = 6
    elif stories <= 8:
        cStories = 8
    else:
        cStories = 10

    key = cType + '_' + str(cIM) + '_' + str(cStories)
    curves = []
    for dir in os.listdir(filedir + '/curves'):
        # print(dir)
        if key in dir:
            curves.append(dir)
    print('Matched curves:', curves)

    # idr to component rotation
    newEdps = []
    for i in range(len(IDRs)):
        floor = i + 1
        if floor > 10:
            floor = 10  # 大于10层按10层取值
        # print(floor)
        idr = IDRs[i]
        bRots = []
        cRots = []
        for curve in curves:
            # print(curve)
            # beam
            csvFileb = curve + '-ib-f' + str(floor) + '.csv'
            dfb = pd.read_csv(filedir + '/curves/' + curve + '/' + csvFileb)
            bRot = _interpolation(idr, dfb)
            bRots.append(bRot)
            # column
            csvFilec = curve + '-ic-f' + str(floor) + '.csv'
            dfc = pd.read_csv(filedir + '/curves/' + curve + '/' + csvFilec)
            cRot = _interpolation(idr, dfc)
            cRots.append(cRot)

        # use average value for more than one matched curves
        bRot = sum(bRots) / len(bRots)
        cRot = sum(cRots) / len(cRots)
        newEdps.append(bRot)
        newEdps.append(cRot)

    newEdps = IDRs + newEdps + otherEdps
    # print(len(newEdps))
    return newEdps


def _interpolation(x, df):
    df.columns = ['x', 'y']
    ind = df[df['x'] > x].index.tolist()
    if ind:  # not empty, need interpolation
        ind2 = ind[0]
        ind1 = ind2 - 1
        # print(ind1, ind2)
        if ind1 >= 0:
            x1 = df.loc[ind1]['x']
            y1 = df.loc[ind1]['y']
        else:
            x1 = 0
            y1 = 0
        x2 = df.loc[ind2]['x']
        y2 = df.loc[ind2]['y']
        y = (x - x1) / (x2 - x1) * (y2 - y1) + y1
    else:  # empty, select last value
        y = df.tail(1)['y'].values[0]
    return y
