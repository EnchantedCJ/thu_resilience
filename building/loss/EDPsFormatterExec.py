# -*- coding: utf-8 -*-
# from EDPsFormatter.idr2comp import idr2comp
from building.loss.EDPsFormatter.idr2comp import idr2comp


def main(config):
    numEQ = config['numEQ']
    ifTrans = config['idr2comp']

    # input
    print('------ Input ------')
    blg = []  # 输出文件每栋建筑的记录
    edp = []  # 输入文件每行的记录
    with open('../tha/Results/EDPs.txt', 'r', encoding='utf-8') as f:
        i = 0
        for line in f.readlines():
            edp.append(line.split())
            i += 1
    numBlg = int(i / numEQ)
    print('Number of buildings:', numBlg)

    blgAtts = []
    with open('../tha/inputs/BlgAttributes.txt', 'r', encoding='utf-8') as f:
        numBlg1 = int(f.readline().strip())
        print('Number of buildings:', numBlg1)
        # check
        if not numBlg == numBlg1:
            print('The number of buildings does not match!')
            exit(0)
        else:
            print('Match!')
        f.readline()
        for line in f.readlines():
            temp = line.strip('\n').split()
            blgAtt = {}
            blgAtt['stories'] = int(temp[1])
            blgAtt['IM'] = float(temp[7])
            blgAtt['stype'] = int(temp[16])
            blgAtts.append(blgAtt)

    # format
    print('------ Format ------')
    edpMax = []
    for i in range(numBlg):
        blg.append([])
        edpMax.append([])
        numEDP = len(edp[numEQ * i])

        # 输出文件每块的第一行
        if ifTrans and blgAtts[i]['stype'] == 0:
            # blg[i].append(
            #     '{nEQ} {nEDP}\n'.format(nEQ=1, nEDP=numEDP + 2 * blgAtts[i]['stories']))  # 取numEQ=1,多条地震动取最大EDP
            blg[i].append(
                '{nEQ} {nEDP}\n'.format(nEQ=numEQ, nEDP=numEDP + 2 * blgAtts[i]['stories']))
        else:
            # blg[i].append('{nEQ} {nEDP}\n'.format(nEQ=1, nEDP=numEDP))  # 取numEQ=1,多条地震动取最大EDP
            blg[i].append('{nEQ} {nEDP}\n'.format(nEQ=numEQ, nEDP=numEDP))

        # # 每个EDP取多条地震动结果的最大值
        # for k in range(numEDP):
        #     tempList = [float(edp[numEQ * i + j][k]) for j in range(numEQ)]
        #     tempListAbs = list(map(abs, tempList))
        #     ind = tempListAbs.index(max(tempListAbs))
        #     edpAbsMax = tempList[ind]
        #     edpMax[i].append(edpAbsMax)
        #
        # # idr2comp
        # if ifTrans and blgAtts[i]['stype'] == 0:
        #     # print('IDR to component rotation.')
        #     edpMax[i] = idr2comp(edpMax[i], blgAtts[i])
        # else:
        #     print('Keep IDR.')
        #
        # # 组成输出文件块
        # edpMax[i] = list(map(lambda x: format(x, '.4E'), edpMax[i]))
        # blg[i].append('\t'.join(edpMax[i]) + '\n')
        # # print(len(edpMax[i]))

        # 保留多条地震动的EDP
        for j in range(numEQ):
            edp1 = [float(edp[numEQ * i + j][k]) for k in range(numEDP)]

            # idr2comp
            if ifTrans and blgAtts[i]['stype'] == 0:
                # print('IDR to component rotation.')
                edp1 = idr2comp(edp1, blgAtts[i])
            else:
                print('Keep IDR.')

            # 组成输出文件块
            edp1 = list(map(lambda x: format(x, '.4E'), edp1))
            blg[i].append('\t'.join(edp1) + '\n')
            # print(len(edpMax[i]))

    # counting each type
    print('------ Counting ------')
    numBlgf = 0
    numBlgfw = 0
    numBlgurm = 0
    numBlgrm = 0
    for blgAtt in blgAtts:
        if blgAtt['stype'] == 0:
            numBlgf += 1
        elif blgAtt['stype'] == 1:
            numBlgfw += 1
        elif blgAtt['stype'] == 2:
            numBlgurm += 1
        elif blgAtt['stype'] == 3:
            numBlgrm += 1
        else:
            print('No such type!')
            exit(0)
    print('Frame:', numBlgf)
    print('Framewall:', numBlgfw)
    print('URM:', numBlgurm)
    print('RM:', numBlgrm)

    # output
    print('------ Output ------')

    # ff = open('./LossEstimator/f/input/Edps.txt', 'w', encoding='utf-8')
    # ffw = open('./LossEstimator/fw/input/Edps.txt', 'w', encoding='utf-8')
    # furm = open('./LossEstimator/urm/input/Edps.txt', 'w', encoding='utf-8')
    # frm = open('./LossEstimator/rm/input/Edps.txt', 'w', encoding='utf-8')
    #
    # ff.writelines('{nBlg}\n'.format(nBlg=numBlgf))
    # ffw.writelines('{nBlg}\n'.format(nBlg=numBlgfw))
    # furm.writelines('{nBlg}\n'.format(nBlg=numBlgurm))
    # frm.writelines('{nBlg}\n'.format(nBlg=numBlgrm))
    #
    # for i in range(numBlg):
    #     if blgAtts[i]['stype'] == 0:
    #         ff.writelines(blg[i])
    #     elif blgAtts[i]['stype'] == 1:
    #         ffw.writelines(blg[i])
    #     elif blgAtts[i]['stype'] == 2:
    #         furm.writelines(blg[i])
    #     elif blgAtts[i]['stype'] == 3:
    #         frm.writelines(blg[i])
    #     else:
    #         print('No such type!')
    #         exit(0)
    #
    # ff.close()
    # ffw.close()
    # furm.close()
    # frm.close()

    f = open('./LossEstimator/input/Edps.txt', 'w', encoding='utf-8')
    f.writelines('{nBlg}\n'.format(nBlg=numBlg))
    for i in range(numBlg):
        f.writelines(blg[i])
    f.close()


if __name__ == '__main__':
    config = {'numEQ': 1,
              'idr2comp': True}
    main(config)
