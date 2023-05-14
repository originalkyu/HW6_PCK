import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import csv

def main():
    datafile = open('q4.csv', 'r', encoding='utf-8-sig')
    datareader = csv.reader(datafile)
        # [3] : 역 이름
        # [10]: 07:00:00~07:59:59
        #   [10] : 승차
        #   [11] : 하차
        # [12]: 08:00:00~08:59:59 
        #   [12] : 승차
        #   [13] : 하차

    header1 = next(datareader)
    header2 = next(datareader)



    ###
    titles = ['최대 승차역 30개', '최대 하차역 30개', '최대 승하차역 30개']
    dic = {}
    for row in datareader:
        replaced_nums = list(map(lambda num : int(num.replace(",", "")), row[10:14]))
        # print(replaced_nums)
        if row[3] in dic:
            newValues = dic[row[3]]
            newValues[0] = (newValues[0] + replaced_nums[0] + replaced_nums[2])
            newValues[1] = (newValues[1] + replaced_nums[1] + replaced_nums[3])
            newValues[2] = (newValues[2] + sum(replaced_nums))
            dic[row[3]] = newValues
        else:
            newValues = []
            newValues.append(replaced_nums[0] + replaced_nums[2])
            newValues.append(replaced_nums[1] + replaced_nums[3])
            newValues.append(sum(replaced_nums))
            dic[row[3]] = newValues


    rc('font', family='AppleGothic')
    plt.rcParams['axes.unicode_minus'] = False
    fig = plt.figure(figsize=(8,12))
    plt.subplots_adjust(hspace=0.99, top=0.95, bottom=0.15,wspace=0.4)

    for i in range(3):
        sortedList = sorted(dic.items(), key = lambda x : x[1][i])
        sortedList.reverse()

        indices = range(30)
        label = [el[0] for el in sortedList]
        numList = [el[1][i] for el in sortedList]

    # print(label)
    # print(numList)
    # matplotlib('font', family='AppleGothic')
    ###
        plt.subplot(3,1,i+1)
        bars =plt.bar(indices, numList[:30])
        # print(numList[:5])
        plt.title(titles[i]+"(x축: 역 이름)")
        plt.xticks(indices, label[:30], rotation=90)
        plt.yticks(ticks=range(0,900000,100000), labels=range(0,90,10))
        plt.ylabel('(단위: 10,000 명)')
        # for i, bar in enumerate(bars):
            # plt.text(bar.get_x(), bar.get_y(),  numList[:30][i])
    # xticks, title, ylabel
    # hspace, wspace


    plt.show()
if __name__=="__main__":
    main()