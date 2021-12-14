# create a simple graph png file from a text file 
# containing 2 values (separated by semicolons) of volts over time (in ms converted to minutes)

import matplotlib.pyplot as plt
import os
import easygui

path = easygui.diropenbox("Choix du dossier")
graph_dir_path = path + "_graph"
os.mkdir(graph_dir_path)

count = 0

for i in os.listdir(path):
    f = open(os.path.join(path, i), "r")
    values = f.readlines()
    f.close()
    value_volt = []
    value_time = []
    for value in values:
        value_volt.append(float(value.split(";")[0]))
        _temp = value.split(";")[1]
        value_time.append(float(_temp.split("\n")[0]) / 60000)

    f.close()
    plt.plot(value_time, value_volt)
    plt.ylabel('Batterie(Volt)')
    plt.xlabel('Temps(minutes)')
    min_value_time = value_time[value_volt.index(min(value_volt))]
    min_value_volt = min(value_volt)
    plt.text(min_value_time, min_value_volt, "X")

    #plt.annotate('{}V at {:.2f}min'.format(min_value_volt, min_value_time), xy = (min_value_time, min_value_volt), xytext = ((max(value_time)/min(value_time)), min_value_volt + 0.5))
    #annotate with an arrowprops
    #plt.annotate('{}V at {:.2f}min'.format(min_value_volt, min_value_time), xy = (min_value_time, min_value_volt), xytext = (min_value_time, min_value_volt + 0.5),arrowprops = dict(facecolor='black', shrink=0.05))
    plt.annotate('Minimum {}V at {:.2f}min'.format(min_value_volt, min_value_time),
                 xy = (min_value_time, min_value_volt),
                 xycoords = 'data',
                 xytext = (0.8, 0.95),
                 textcoords = 'axes fraction',
                 horizontalalignment = 'right',
                 verticalalignment = 'bottom',)

    plt.grid(True)
    plt.savefig('{}/{}.png'.format(graph_dir_path, i), dpi=200)
    plt.close()
    count += 1

easygui.msgbox("{} graphs créés".format(count))
