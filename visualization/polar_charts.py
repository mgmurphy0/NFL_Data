import pandas as pd
import numpy as np

# Import data visualization modules
import matplotlib as matplotlib
import matplotlib.pyplot as plt

def get_player_data(data, name):
    #return np.asarray(data[data['Tm'] == team])[0]
    return np.asarray(data[data['Last'] == name])[0]

def plot_data(ax,data,angles,color,categories):
    # Plot data and fill with team color #add the last value twice to complete the polar plot
    ax.plot(angles, np.append(data[-(len(angles)-1):], data[-(len(angles)-1)]), color=color, linewidth=2)
    ax.fill(angles, np.append(data[-(len(angles)-1):], data[-(len(angles)-1)]), color=color, alpha=0.2)
    # Set category labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_yticklabels([])
    # Add player name
    ax.text(np.pi/2, 1.5, data[0], ha='center', va='center', size=15, color=color)
    return ax


def polar_charts(data: pd.DataFrame, categories: list, players:list):
    # General plot parameters
    matplotlib.rcParams['font.family'] = 'Avenir'
    matplotlib.rcParams['font.size'] = 12
    matplotlib.rcParams['axes.linewidth'] = 0
    matplotlib.rcParams['xtick.major.pad'] = 5

    # team colors from this link: https://teamcolorcodes.com/nfl-team-color-codes/
    team_colors = {'ARI':'#97233f', 'ATL':'#a71930', 'BAL':'#241773', 'BUF':'#00338d', 'CAR':'#0085ca', 'CHI':'#0b162a', 'CIN':'#fb4f14', 'CLE':'#311d00', 'DAL':'#041e42', 'DEN':'#002244', 'DET':'#0076b6', 'GNB':'#203731', 'HOU':'#03202f', 'IND':'#002c5f', 'JAX':'#006778', 'KAN':'#e31837', 'LAC':'#002a5e', 'LAR':'#003594', 'MIA':'#008e97', 'MIN':'#4f2683', 'NWE':'#002244', 'NOR':'#d3bc8d', 'NYG':'#0b2265', 'NYJ':'#125740', 'LVR':'#000000', 'PHI':'#004c54', 'PIT':'#ffb612', 'SFO':'#aa0000', 'SEA':'#002244', 'TAM':'#d50a0a', 'TEN':'#0c2340', 'WAS':'#773141'}

    # Calculate angles for radar chart
    offset = np.pi/(len(categories))
    angles = np.linspace(0, 2*np.pi, len(categories) + 1) + offset

    players_comp = list()
    for player in players:
        stats = get_player_data(data, player)
        players_comp.append((stats))

    # Create figure
    fig = plt.figure(figsize=(10, 10), facecolor='white')

    # Add subplots, adjust space between subplots, plot QB data
    if len(players_comp) == 1:
        ax1 = fig.add_subplot(121, projection='polar', facecolor='#ededed')
        ax = [ax1]
    elif len(players_comp)  == 2:
        ax1 = fig.add_subplot(121, projection='polar', facecolor='#ededed')
        ax2 = fig.add_subplot(122, projection='polar', facecolor='#ededed')
        ax = [ax1,ax2]
    elif len(players_comp)  == 3:
        ax1 = fig.add_subplot(131, projection='polar', facecolor='#ededed')
        ax2 = fig.add_subplot(132, projection='polar', facecolor='#ededed')
        ax3 = fig.add_subplot(133, projection='polar', facecolor='#ededed')
        ax = [ax1,ax2,ax3]
    elif len(players_comp)  == 4:
        ax1 = fig.add_subplot(221, projection='polar', facecolor='#ededed')
        ax2 = fig.add_subplot(222, projection='polar', facecolor='#ededed')
        ax3 = fig.add_subplot(223, projection='polar', facecolor='#ededed')
        ax4 = fig.add_subplot(224, projection='polar', facecolor='#ededed')
        ax = [ax1,ax2,ax3,ax4]
    elif len(players_comp)  == 6:
        ax1 = fig.add_subplot(231, projection='polar', facecolor='#ededed')
        ax2 = fig.add_subplot(232, projection='polar', facecolor='#ededed')
        ax3 = fig.add_subplot(233, projection='polar', facecolor='#ededed')
        ax4 = fig.add_subplot(234, projection='polar', facecolor='#ededed')
        ax5 = fig.add_subplot(235, projection='polar', facecolor='#ededed')
        ax6 = fig.add_subplot(236, projection='polar', facecolor='#ededed')
        ax = [ax1,ax2,ax3,ax4,ax5,ax6]
    elif len(players_comp)  == 8:
        #matplotlib.rcParams['font.size'] = 10
        #matplotlib.rcParams['xtick.major.pad'] = 5
        ax1 = fig.add_subplot(331, projection='polar', facecolor='#ededed')
        ax2 = fig.add_subplot(332, projection='polar', facecolor='#ededed')
        ax3 = fig.add_subplot(333, projection='polar', facecolor='#ededed')
        ax4 = fig.add_subplot(334, projection='polar', facecolor='#ededed')
        ax5 = fig.add_subplot(335, projection='polar', facecolor='#ededed')
        ax6 = fig.add_subplot(336, projection='polar', facecolor='#ededed')
        ax7 = fig.add_subplot(337, projection='polar', facecolor='#ededed')
        ax8 = fig.add_subplot(338, projection='polar', facecolor='#ededed')
        ax = [ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8]
    for i in range(len(ax)):
        plot_data(ax[i],players_comp[i],angles,team_colors[players_comp[i][3]],categories)   
    plt.subplots_adjust(hspace=0.8, wspace=0.5)
    plt.show()