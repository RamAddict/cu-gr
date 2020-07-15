import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import sys
from matplotlib.patches import Rectangle
from matplotlib.colors import to_rgba

test_name = 'ispd19_test9.ascendingHP.csv'
baseline = 'ispd18_test8.ascendingHP.csv'

# This script reads data from the csvs and reports statistics and creates a graph.
# It should be run by giving numbers 1-3 or nothing in the command line.
# CSV files should be in the same directory.
# Some functions use the above variables to determine which tests to evaluate.


def PlotViaComparison():
    baseline_csv = pd.read_csv(baseline, names=['net', 'hp', 'NPins', 'WireLength', 'NVias'])
    test_csv = pd.read_csv(test_name, names=['net', 'hp', 'NPins', 'WireLength', 'NVias'])
    baseline_csv.columns=['net', 'hp', 'NPins', 'WireLength', 'NVias']
    test_csv.columns=['net', 'hp', 'NPins', 'WireLength', 'NVias']

    plt.rc('font', size=16)
    plt.ylabel('Frequency')
    plt.xlabel('Number of Vias per Net')

    plt.hist(test_csv['NVias'], bins=[x for x in range(1,40)], alpha=0.8, fc=(1, 0, 0, 0.5))
    plt.hist(baseline_csv['NVias'], bins=[x for x in range(1,40)], alpha=0.5, fc=(0, 0, 1, 0.5))
    
    # test_csv.NVias.hist(bins=[x for x in range(1,40)], alpha=0.9, color='b')
    # baseline_csv.NVias.hist(bins=[x for x in range(1,40)], alpha=0.7, color='r')
    # plt.suptitle(test_name[4:-4] + ' # of vias per net')
    labels = [test_name[13:-6], baseline[13:-6], 'overlap']
    handles = [Rectangle((0,0),1,1,color=c,ec="k") for c in ['r', 'cornflowerblue', 'purple']]
    plt.legend(handles, labels)
    plt.show()

def plotEveryHist():
    # name, hp, NPins, WL, Vias
    csv = pd.read_csv(test_name, names=['net', 'hp', 'NPins', 'WireLength', 'NVias'])
    print(csv.describe())

    csv.columns=['net', 'hp', 'NPins', 'WireLength', 'NVias']

    fig, axes = plt.subplots(nrows=2, ncols=2)

    HPHist = csv.hp.hist(bins=[x for x in range(1,40)], ax=axes[0,0])
    NPinsHist = csv.NPins.hist(bins=[x for x in range(1,40)], ax=axes[0,1])
    WireLength = csv.WireLength.hist(bins=[x*10 for x in range (1,40)], ax=axes[1,0])
    NVias = csv.NVias.hist(bins=[x for x in range(1,40)], ax=axes[1,1])

    plt.suptitle(test_name[4:-4])

    axes[0,0].text(0, -3000,'hp', horizontalalignment='center',
                verticalalignment='center')
    axes[0,1].text(0, -2000,'NPins', horizontalalignment='center',
                verticalalignment='center')
    axes[1,0].text(0, -2000,'WireLength', horizontalalignment='center',
                verticalalignment='center')
    axes[1,1].text(0, -2000,'NVias', horizontalalignment='center',
                verticalalignment='center')
    plt.show()


def plotASingleHist():
    # name, hp, NPins, WL, Vias
    csv = pd.read_csv(test_name, names=['net', 'hp', 'NPins', 'WireLength', 'NVias'])
    print(csv.describe(percentiles=[.25, .5, .75, .8, .9, 1]))

    csv.columns=['net', 'hp', 'NPins', 'WireLength', 'NVias']

    # fig, axes = plt.subplots(nrows=2, ncols=2)

    # HPHist = csv.hp.hist(bins=[x for x in range(1,40)], ax=axes[0,0])
    # NPinsHist = csv.NPins.hist(bins=[x for x in range(1,40)], ax=axes[0,1])
    # WireLength = csv.WireLength.hist(bins=[x*10 for x in range (1,40)], ax=axes[1,0])
    # NVias = csv.NVias.hist(bins=[x for x in range(1,40)], ax=axes[1,1])
    plt.rc('font', size=20)
    NVias = csv.hp.hist(bins=[x for x in range(1,80)])
    plt.ylabel('Frequency')
    plt.xlabel('Semiperimeter of Net')

    
    # plt.suptitle(test_name[4:-4])

    # axes[0,0].text(0, -3000,'hp', horizontalalignment='center',
    #             verticalalignment='center')
    # axes[0,1].text(0, -2000,'NPins', horizontalalignment='center',
    #             verticalalignment='center')
    # axes[1,0].text(0, -2000,'WireLength', horizontalalignment='center',
    #             verticalalignment='center')
    # axes[1,1].text(0, -2000,'NVias', horizontalalignment='center',
                # verticalalignment='center')
    plt.show()

def plot2Hist():

    baseline_csv = pd.read_csv(baseline, names=['net', 'hp', 'NPins', 'WireLength', 'NVias'])
    test_csv = pd.read_csv(test_name, names=['net', 'hp', 'NPins', 'WireLength', 'NVias'])
    baseline_csv.columns=['net', 'hp', 'NPins', 'WireLength', 'NVias']
    test_csv.columns=['net', 'hp', 'NPins', 'WireLength', 'NVias']

    fig, axes = plt.subplots(nrows=1, ncols=2)

    plt.rc('font', size=16)
    Nvias1 = baseline_csv.hp.hist(bins=[x for x in range(1,40)], ax=axes[0])
    Nvias2 = test_csv.hp.hist(bins=[x for x in range(1,40)], ax=axes[1])
    plt.ylabel('Frequency')
    plt.xlabel('Semiperimeter of Net')

    plt.show()

if (sys.argv[1] == '1'):
    plotEveryHist()
elif (sys.argv[1] == '2'):
    PlotViaComparison()
elif (sys.argv[1] == '3'):
    plotASingleHist()
else:
    plot2Hist()