'''Analyzes NFL data for specific positions. Visualizes data for comparison.'''

from prep.parse_sites import pull_qb_data, pull_rb_data, pull_rec_data
from analysis.clean_radar_data import clean_qb_data, clean_rb_data, clean_rec_data
from visualization.polar_charts import polar_charts

position = 'qb'

if position == 'qb': ## Analyze QB
    data = pull_qb_data()

    categories = ['Cmp%', 'Yds', 'TD', 'Int', 'Y/A', 'Rate']

    qb_data = clean_qb_data(data,categories)

    players = ['Mahomes','Watson','Brady','Rodgers','Wilson','Allen']

    polar_charts(qb_data,categories,players)
    print(qb_data)

if position == 'rb':## Analyze RB
    data = pull_rb_data()

    # Select stat categories
    categories = ['Att', 'Yds', 'TD', 'Y/A', 'Age']

    rb_data = clean_rb_data(data,categories)

    # Select players to analyze
    players = ['Henry','Dobbins','Elliott','Taylor','Cook','Jones']

    polar_charts(rb_data,categories,players)
    print(rb_data)

if position == 'wr':## Analyze WR
    data = pull_rec_data(None)

    # Select stat categories
    categories = ['Tgt', 'Rec', 'Ctch%', 'Yds', 'Y/R', 'TD']

    rec_data = clean_rec_data(data,categories)

    # Select players to analyze
    players = ['Adams','Diggs','Kelce','Hopkins','Waller','Metcalf']

    polar_charts(rec_data,categories,players)
    print(rec_data)