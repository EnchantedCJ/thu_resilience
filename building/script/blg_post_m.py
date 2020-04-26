# -*- coding: utf-8 -*-
__all__ = ['postprocess']

_FUNCTION = ['家庭', '政府', '医疗', '科教', '媒体', '公益', '文化', '经济']


class Building(object):
    def __init__(self):
        self.id = 0
        self.func = ''
        self.result = {0.2: {'x': {}, 'y': {}},
                       0.3: {'x': {}, 'y': {}},
                       0.4: {'x': {}, 'y': {}}}


def postprocess(blgFuncPath, resultDir):
    blgs = []
    # 读取分类
    with open(blgFuncPath, 'r', encoding='utf-8') as f:
        f.readline()
        for line in f.readlines():
            temp = line.strip('\n').split()
            blg = Building()
            try:
                blg.id = int(temp[0])
            except:
                print('建筑功能文件ID不正确！')
            try:
                blg.func = temp[1]
            except:
                blg.func = '家庭'  # 缺省
            if blg.func not in _FUNCTION:
                print('建筑功能文件Function不正确！')
            blgs.append(blg)

    # 读取结果
    for pga in [0.2, 0.3, 0.4]:
        for direction in ['x', 'y']:
            try:
                with open(resultDir + '/' + str(pga) + '/' + direction + '/basic.txt', 'r', encoding='utf-8') as f:
                    f.readline()
                    for blg in blgs:
                        temp = f.readline().strip('\n').split()
                        result = {}
                        result['lossMedian'] = float(temp[2])
                        result['lossP16'] = float(temp[5])
                        result['lossP84'] = float(temp[6])
                        result['downtimeMedian'] = float(temp[2])
                        result['downtimeP16'] = float(temp[7])
                        result['downtimeP84'] = float(temp[8])
                        result['hurtMedian'] = float(temp[9])
                        result['hurtP16'] = float(temp[10])
                        result['hurtP84'] = float(temp[11])
                        result['deathMedian'] = float(temp[12])
                        result['deathP16'] = float(temp[13])
                        result['deathP84'] = float(temp[14])
                        blg.result[pga][direction]['loss'] = result

                with open(resultDir + '/' + str(pga) + '/' + direction + '/DamageState.txt', 'r',
                          encoding='utf-8') as f:
                    f.readline()
                    numEQ = 1
                    for blg in blgs:
                        dsEQ = []
                        for i in range(numEQ):
                            temp = f.readline().strip('\n').split()
                            dsStory = [int(ds) for ds in temp[2:]]
                            dsEQ.append(max(dsStory))
                        ds = sorted(dsEQ)[int(numEQ * 0.84) - 1]  # 各地震动84%保证率的破坏状态
                        blg.result[pga][direction]['ds'] = ds
            except:
                print('读取结果失败')

    # 合并结果
    for blg in blgs:
        for pga in [0.2, 0.3, 0.4]:
            merge = {'loss': {}, 'ds': 0}
            resultx = blg.result[pga]['x']
            resulty = blg.result[pga]['y']
            merge['loss']['lossMedian'] = resultx['loss']['lossMedian'] + resulty['loss']['lossMedian']
            merge['loss']['lossP16'] = resultx['loss']['lossP16'] + resulty['loss']['lossP16']
            merge['loss']['lossP84'] = resultx['loss']['lossP84'] + resulty['loss']['lossP84']
            merge['loss']['downtimeMedian'] = max(resultx['loss']['downtimeMedian'], resulty['loss']['downtimeMedian'])
            merge['loss']['downtimeP16'] = max(resultx['loss']['downtimeP16'], resulty['loss']['downtimeP16'])
            merge['loss']['downtimeP84'] = max(resultx['loss']['downtimeP84'], resulty['loss']['downtimeP84'])
            merge['loss']['hurtMedian'] = max(resultx['loss']['hurtMedian'], resulty['loss']['hurtMedian'])
            merge['loss']['hurtP16'] = max(resultx['loss']['hurtP16'], resulty['loss']['hurtP16'])
            merge['loss']['hurtP84'] = max(resultx['loss']['hurtP84'], resulty['loss']['hurtP84'])
            merge['loss']['deathMedian'] = max(resultx['loss']['deathMedian'], resulty['loss']['deathMedian'])
            merge['loss']['deathP16'] = max(resultx['loss']['deathP16'], resulty['loss']['deathP16'])
            merge['loss']['deathP84'] = max(resultx['loss']['deathP84'], resulty['loss']['deathP84'])
            merge['ds'] = max(resultx['ds'], resulty['ds'])
            blg.result[pga]['merge'] = merge

    for pga in [0.2, 0.3, 0.4]:
        with open(resultDir + '/' + str(pga) + '/blg_result_merge_' + str(pga) + '.txt', 'w', encoding='utf-8') as f:
            f.write('ID\t'
                    'lossMedian\tlossP16\tlossP84\t'
                    'downtimeMedian\tdowntimeP16\tdowntimeP84\t'
                    'hurtMedian\thurtP16\thurtP84\t'
                    'deathMedian\tdeathP16\tdeathP84\t'
                    'damageState\n')
            for blg in blgs:
                f.write(str(blg.id))
                f.write('\t')
                for key in blg.result[pga]['merge']['loss']:
                    f.write(str(blg.result[pga]['merge']['loss'][key]))
                    f.write('\t')
                f.write(str(blg.result[pga]['merge']['ds']))
                f.write('\n')

    # 韧性指标
    for pga in [0.2, 0.3, 0.4]:
        status = _cal_status(pga, blgs)
        with open(resultDir + '/' + str(pga) + '/blg2criteria_' + str(pga) + '.txt', 'w', encoding='utf-8') as f:
            for func in _FUNCTION:
                f.write(str(status[func]['level']))
                f.write('\t')
                f.write(str(status[func]['downtime']))
                f.write('\n')


def _cal_status(pga, blgs):
    status = {}
    for func in _FUNCTION:
        status[func] = {'total': 0,
                        'usable': 0,
                        'downtimes': [], }

    for blg in blgs:
        merge = blg.result[pga]['merge']
        status[blg.func]['total'] += 1
        if merge['ds'] in [0, 1, 2]:
            status[blg.func]['usable'] += 1
        status[blg.func]['downtimes'].append(merge['loss']['downtimeP84'])

    numBlg = 0
    for func in _FUNCTION:
        numBlg += status[func]['total']
        if status[func]['total'] != 0:
            status[func]['level'] = status[func]['usable'] / status[func]['total']
        else:
            status[func]['level'] = 1.0
        if status[func]['downtimes'] != []:
            status[func]['downtime'] = sorted(status[func]['downtimes'])[int(status[func]['total'] * 0.9) - 1]
        else:
            status[func]['downtime'] = 0.0
    if numBlg != len(blgs):
        print('建筑数量不对应！')

    return status


if __name__ == '__main__':
    blgFuncPath = 'BlgFunction.txt'
    resultDir = '.'
    postprocess(blgFuncPath, resultDir)
