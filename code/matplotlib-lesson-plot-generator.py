#!/usr/bin/env python3


import os
img_dir = "../img"
img_type = "png"




## This is how the data is loaded in the first example of the lesson

import pandas as pd
# this is loaded from the network, because at the time of writing this is
# the source used in the matplotlib lesson example. This could probably
# use somethin from this repository's /data directory.
# df = pd.read_csv('../data/surveys.csv',
df = pd.read_csv('https://ndownloader.figshare.com/files/2292172',
                  index_col='record_id')

import matplotlib.pyplot as plt

small_dataset = df[:50]
plot_data = small_dataset['plot_id']








def section_simple_plotting():
    plt.figure()
    plt.plot(plot_data, label='My Data')
    plt.savefig(os.path.join(img_dir, '06_simple_plotting_myplot.png'))




def section_plot_essentials():
    ## setup
    plt.figure()
    plt.plot(plot_data, label='My Data')

    ## example code
    plt.xlabel('Index')
    plt.ylabel('Plot Value')
    plt.title('The Plot Value From surveys.csv')
    plt.savefig(os.path.join(img_dir, '06_plot_essentials.png'))



def section_managing_figures():
    plt.figure(figsize=(10, 8)) # no need for actual 200 dpi
    plt.subplots_adjust(left=0.1, bottom=0.2, right=0.99, top=0.99)
    plt.plot(plot_data, label='My Data')
    plt.savefig(os.path.join(img_dir, '06_managing_figures.png'))



def section_managing_styles_colors():
    plt.figure()
    plt.plot(plot_data, color='#aa5599')
    plt.savefig(os.path.join(img_dir, '06_managing_styles_colors.png'))



def section_managing_styles_line_style():
    plt.figure()
    plt.plot(plot_data, linewidth=3)
    plt.savefig(os.path.join(img_dir, '06_managing_styles_line_style.png'))



def section_managing_styles_other_styles_dot():
    plt.figure()
    plt.plot(plot_data, 'o')
    plt.savefig(os.path.join(img_dir, '06_managing_styles_other_styles_dot.png'))



def section_plot_range():
    plt.figure()
    plt.plot(plot_data)
    plt.xlim(-10, 15)
    plt.savefig(os.path.join(img_dir, '06_plot_range.png'))


def section_plot_scale():
    plt.figure()
    plt.plot(plot_data)
    plt.loglog()
    plt.savefig(os.path.join(img_dir, '06_plot_scale.png'))


def section_two_independent_axes():
    plt.figure()
    plt.bar(plot_data.index, plot_data.values)
    plt.twinx()
    plt.plot(1/ plot_data, color='k')
    plt.savefig(os.path.join(img_dir, '06_two_independent_axes.png'))



def section_a_realistic_example():
    plt.figure()
    grouped_plot_data = small_dataset.groupby('sex')

    colors = ['r', 'g'] #we'll be cycling through these colors
    color_index = 0
    for group in grouped_plot_data:
        color = colors[color_index]
        group_label = group[0]
        group_data = group[1]
        plt.plot(group_data['plot_id'], color=color, label=group_label)
        color_index += 1
    plt.legend()
    plt.savefig(os.path.join(img_dir, '06_a_realistic_example.png'))

def section_describing_the_plot_leged_ticks_labels():
    plt.figure()
    plt.plot(plot_data, label='Some Sescription')
    plt.legend(loc='best')

    plt.xticks([1,2,3,5,8,13,21,34,55]) # put ticks in given locations of X-axis
    plt.yticks([0,10,20,30], ['A', 'B', 'C', 'D']) # put ticks in given locations on Y-axis, denote them with letters

    plt.grid()

    plt.xlabel('X-axis label')
    plt.ylabel('Y-axis label')

    plt.title('Plot title')
    plt.savefig(os.path.join(img_dir, '06_describing_the_plot_leged_ticks_labels.png'))


def section_plot_variations_bar_plot():
    plt.figure()
    plt.bar(plot_data.index, plot_data.values)
    plt.savefig(os.path.join(img_dir, '06_plot_variations_bar_plot.png'))


def section_plot_variations_wisker_plot():
    plt.figure()
    plt.boxplot(plot_data.index, plot_data.values)
    plt.savefig(os.path.join(img_dir, '06_plot_variations_wisker_plot.png'))


if __name__ == '__main__':
    section_simple_plotting()
    section_plot_essentials()
    section_managing_figures()
    section_managing_styles_colors()
    section_managing_styles_line_style()
    section_managing_styles_other_styles_dot()
    section_plot_range()
    section_plot_scale()
    section_two_independent_axes()
    section_a_realistic_example()
    section_describing_the_plot_leged_ticks_labels()
    section_plot_variations_bar_plot()
    section_plot_variations_wisker_plot()
