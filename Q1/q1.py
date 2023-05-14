import csv
from matplotlib import rc
import matplotlib.pyplot as plt
import numpy as np
def getDataList(fileName):
    dataList = []

    file = open(fileName+'.csv', 'r',encoding='cp949')
    datareader = csv.reader(file)

    # 헤더 제거하기
    for i in range(8):
        next(datareader)

    for i in range(12):
        dataList.append(float(next(datareader)[2]))

    file.close()
    return dataList

def main():

    filenames = {'All':'All', 'S':'Seoul','D':'Daejeon','B':'Busan','J':'Jeju'}
    indices = range(1,13,1)
    markers = ['o','x','D','*','s']
    datas = {}
    dicSub = {}

    ### step1: 데이터 구하기
    for i,name in enumerate(filenames.keys()):
        datas[name] = getDataList(name)
        dicSub[name] = [el_name - el_All for el_name,el_All in zip(datas[name],datas['All'])]
    ### step2: 그림 그리기
  
    fig = plt.figure(figsize=(10,10))
    plt.subplots_adjust(hspace=0.9,wspace=0.4)
    gs = fig.add_gridspec(5,2)

    # xlabel, ylabel, xticks, yticks
    # legend(), title, figsize, text
    # hspace, wspace
    ax_head = fig.add_subplot(gs[0,:])
    for i,name in enumerate(filenames.keys()):
        ax_head.plot(indices, datas[name], label=filenames[name], marker=markers[i])
        if name != 'All':
            ax = fig.add_subplot(gs[i,0])
            ax.plot(indices, datas['All'], label=filenames['All'], marker=markers[0], color='c')
            ax.plot(indices, datas[name], label=filenames[name], marker=markers[2], color='orange')
            ax.set_title("All vs "+filenames[name])
            ax.set_xlabel('Month')
            ax.set_ylabel('Celsius')
            ax.set_xticks(indices)
            ax.set_yticks(range(-5,30,5))
            ax.legend(loc='center left', bbox_to_anchor=(1,0.5),fontsize=6)

            ax = fig.add_subplot(gs[i,1])
            ax.plot(indices, dicSub[name], marker=markers[0], color='black')
            ax.set_title("Value = " + filenames[name] + " - All")
            ax.set_xlabel('Month')
            ax.set_ylabel('Celsius')
            ax.set_xticks(indices)
            ax.set_yticks(range(-3,10,3))
            ax.text(4, 6, "Mean of Values: {:.1f}".format(np.mean(np.array(dicSub[name]))))
    ax_head.set_title("Temp Datas")
    ax_head.set_xlabel('Month')
    ax_head.set_ylabel('Celsius')
    ax_head.set_xticks(indices)
    ax_head.set_yticks(range(-5,30,5))
    ax_head.legend(loc='center left', bbox_to_anchor=(1,0.5),fontsize=8)


    plt.show()

    ### step3: 데이터 csv로 출력하기
    newfile = open('q1result.csv', 'w', encoding='utf-8')
    wr = csv.writer(newfile)
    header = [str(i)+'월' for i in range(1, 13, 1)]
    header.insert(0,"")
    header.append("Mean")
    wr.writerow(["\"than All\" is omitted after every content."])
    wr.writerow(header)
    # print()
    for name in filenames.keys():
        if name in dicSub and name != 'All':
            # print(dic[name],end='\t')
            writeData = []
            writeData.append(filenames[name])
            for i in range(12):
                if dicSub[name][i] > 0:
                    # print('{:.1f}도 덥다.'.format(dicSub[name][i]), end="\t")
                    writeData.append("{:.1f} hotter".format(dicSub[name][i]))
                elif dicSub[name][i] == 0:
                    # print('온도가 같다.'.format(dicSub[name][i]), end="\t")
                    writeData.append("same".format((dicSub[name][i])))
                elif dicSub[name][i]:
                    # print('{:.1f} 춥다.'.format(dicSub[name][i]), end="\t")
                    writeData.append("{:.1f} colder".format(dicSub[name][i]))
                
            # print()
            meanTemp = np.array(dicSub[name]).mean()
            if meanTemp > 0:
                writeData.append("{:.1f} hotter".format(meanTemp))
            elif meanTemp == 0:
                writeData.append("same")
            else :
                writeData.append("{:.1f} colder".format(meanTemp))
            wr.writerow(writeData)
    newfile.close()
    
if __name__ =="__main__":
    main()