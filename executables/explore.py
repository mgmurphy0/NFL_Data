'''Plots Fantasy Football trends based on metrics from pro football reference.'''

from prep.parse_sites import pull_qb_data, pull_rb_data, pull_rec_data, pull_fantasy_data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def plot_scatter(position, filter_cats, x_cat, y_cat):

    """
    Inputs:
    position(str) - player position
    filter_cats(list) - categories to use for filtering
    x_cat(str) - category for x axis
    y_cat(str) - category for y axis
    """

    if position == 'qb':
        data = pull_qb_data()
    elif position == 'rb':
        data = pull_rb_data()
    elif position == 'wr':
        data = pull_rec_data(None)
    elif position == 'fantasy':
        data = pull_fantasy_data()

    categories = [filter_cats, x_cat, y_cat]

    # Convert data to numerical (floats) values
    if 'Ctch%' in categories:
        data['Ctch%'] = data['Ctch%'].str.replace('%', '')
    for i in categories:
        data[i] = pd.to_numeric(data[i])
    print(data.head())

    # Filter by passing yards
    if position is 'fantasy':
        data = data.sort_values(filter_cats,ascending=False)
        data = data.head(30)
    else:
        data = data[(data[filter_cats] > 800)]
        data = data.reset_index(drop=True)

    # Create data subset
    plot_data = data[['Player', 'Tm'] + categories]

    # Remove ornamental characters for achievements (pro bowl / All pro)
    plot_data['Player'] = plot_data['Player'].str.replace('*', '')
    plot_data['Player'] = plot_data['Player'].str.replace('+', '')

    # Split first and last names
    plot_data.insert(1, 'First','N/A')
    plot_data.insert(1, 'Last','N/A')
    for i in plot_data.index:
        plot_data['First'][i] = plot_data['Player'][i].split(' ')[0]
        plot_data['Last'][i] = plot_data['Player'][i].split(' ')[1]

    # team colors from this link: https://teamcolorcodes.com/nfl-team-color-codes/
    team_colors = {'ARI':'#97233f', 'ATL':'#a71930', 'BAL':'#241773', 'BUF':'#00338d', 'CAR':'#0085ca', 'CHI':'#0b162a', 'CIN':'#fb4f14', 'CLE':'#311d00', 'DAL':'#041e42', 'DEN':'#002244', 'DET':'#0076b6', 'GNB':'#203731', 'HOU':'#03202f', 'IND':'#002c5f', 'JAX':'#006778', 'KAN':'#e31837', 'LAC':'#002a5e', 'LAR':'#003594', 'MIA':'#008e97', 'MIN':'#4f2683', 'NWE':'#002244', 'NOR':'#d3bc8d', 'NYG':'#0b2265', 'NYJ':'#125740', 'LVR':'#000000', 'PHI':'#004c54', 'PIT':'#ffb612', 'SFO':'#aa0000', 'SEA':'#002244', 'TAM':'#d50a0a', 'TEN':'#0c2340', 'WAS':'#773141', '2TM':'#020202'}

    #best fit line
    m, b = np.polyfit(plot_data[x_cat], plot_data[y_cat], 1)

    plt.figure(figsize=(9,14))
    plt.grid()
    #plt.scatter(plot_data[x_cat],plot_data[y_cat],color=team_colors[plot_data['Tm']])
    for i in plot_data.index:
        plt.scatter(plot_data[x_cat][i],plot_data[y_cat][i],color=team_colors[plot_data['Tm'][i]],label=plot_data['Last'])
        plt.annotate(i, (plot_data[x_cat][i],plot_data[y_cat][i]))
    plt.plot(plot_data[x_cat], m*plot_data[x_cat] + b)
    plt.xlabel(x_cat),plt.ylabel(y_cat)
    plt.legend(loc='upper left', bbox_to_anchor=(1.02, 1.1))
    left  = 0.125  # the left side of the subplots of the figure
    right = 0.774    # the right side of the subplots of the figure
    bottom = 0.11   # the bottom of the subplots of the figure
    top = 0.917     # the top of the subplots of the figure
    wspace = 0.2   # the amount of width reserved for blank space between subplots
    hspace = 0.2   # the amount of height reserved for white space between subplots
    plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)
    plt.show()

    #lgd = ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5,-0.1))
    #fig.savefig('samplefigure', bbox_extra_artists=(lgd,text), bbox_inches='tight')


if __name__ == "__main__":

    #plot_scatter('wr','Yds','Ctch%','Y/R')
    #plot_scatter('qb','Yds','Y/A','TD')
    plot_scatter('fantasy','VBD','Age','PPR')