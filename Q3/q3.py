import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
import csv

def main():
    datafile = open('JejuPopul.csv', 'r', encoding='cp949') # 전국
    datareader = csv.reader(datafile)

    header = next(datareader)
    data = next(datareader)
    print(header)
    print(data)
    indexlist = [i for i in range(3,49,5)]
    for i in range(1,20, 2):
        indexlist.insert(i,indexlist[i-1]+1)
    
    index = range(10)
    label = [str(i) for i in range(2011,2021,1)]
    male = []
    female = []
    isFemaleMore = []
    for i, item in enumerate(indexlist):
        num = int(data[item].replace(",",""))
        if i % 2 == 0:
            male.append(num)
        else:
            female.append(num)

    for i in range(10):
        if male[i] < female[i]:
            isFemaleMore.append(True)
        else:
            isFemaleMore.append(False)

    # 그리기
    rc('font', family='AppleGothic')
    plt.rcParams['axes.unicode_minus'] = False
    fig = plt.figure(figsize=(10,10))
    width = 0.35
    x = np.arange(10)
    
    bar_male = plt.bar(x - width/2,male, width, color='orange', label='male')
    bar_female = plt.bar(x + width/2,female, width, color='green', label='female')

    # figsize
    # title, xticks, xlabel, yticks, ylabel, ylim, grid, text
    plt.title('Men and Women Population')
    plt.xticks(index, label)
    plt.ylim(285000, 350000)
    plt.ylabel('(단위: 명)')
    plt.grid()
    plt.legend(loc='center left')

    for i, bar in enumerate(bar_male):
        plt.text(bar.get_x(), 281000, str(male[i]), color='orange')
    for i, bar in enumerate(bar_female):
        plt.text(bar.get_x() - width, 279500, str(female[i]), color='green')
    plt.show()


if __name__ == "__main__":
    main()