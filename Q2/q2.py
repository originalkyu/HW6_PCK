import random
import matplotlib.pyplot as plt
import numpy as np
import csv
import math

def makeListDic(count):
    lists = [[], {}]
    for i in range(count):
        num = random.randrange(1,7)
        lists[0].append(num)
        if num in lists[1]:
            lists[1][num] = lists[1][num] + 1
        else:
            lists[1][num] = 1
    return lists
def main():
    testcounts = [100, 1000, 10000, 100000]
    datas = []
    deviations = []

    # 데이터 만들기    
    for i in testcounts:
        datas.append(makeListDic(i))

    # 데이터 csv파일로 저장하기
    newfile = open('q2result.csv', 'w', encoding='utf-8')
    wr = csv.writer(newfile)

    header = [i for i in range(1,7)]
    header.insert(0,"")
    header.append("Deviations of Max Abs Nomalization")
    wr.writerow(header)
    for i, cnt in enumerate(testcounts):
        writeData = [str(cnt)]
        for j in range(1, 7):
            writeData.append(datas[i][1][j])
        datanp = np.array(list(datas[i][1].values()))
        min_datanp = np.min(datanp)
        max_datanp = np.max(datanp)
        # norm_datanp = (datanp - min_datanp) / (max_datanp - min_datanp)
        norm_datanp = datanp / max_datanp
        print(norm_datanp)
        deviations.append(np.std(norm_datanp))
        writeData.append(np.std(norm_datanp))
        wr.writerow(writeData)


    # 데이터 그리기
    fig = plt.figure(figsize=(10,10))
    plt.subplots_adjust(hspace=1,wspace=0.4)
    for i,l in enumerate(datas):
        plt.subplot(4,1,i+1)
        counts, edges, bars = plt.hist(l[0], bins=6)
        plt.bar_label(bars)

        # ylim, yticks, ylabel
        # plt.ylim(top=math.floor(testcounts[i]/3))
        plt.title(str(testcounts[i])+' Rounds Plot')
        plt.xlabel('Number')
        plt.yticks(range(0,int(testcounts[i]/2.5),int(testcounts[i]/10)))
        plt.ylabel('Frequency')
        plt.text(2.4, testcounts[i]/4, "Deviations of Max Abs Nomalization: {:.4f}".format(deviations[i]))
    plt.show()

if __name__ =="__main__":
    main()