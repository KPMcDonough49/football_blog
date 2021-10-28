import pandas as pd 

def return_pass_df(data):

    periods = data['periods']

    events = []
    for i in range(0, len(periods)):
        num_events = len(periods[i]['pbp'])
        for j in range(0, num_events):
            events.append((periods[i]['pbp'][j]))

    drives = []
    for event in events:
        if event['type'] == 'drive':
            drives.append(event)

    events_df = pd.DataFrame()
    for drive in drives:
        new_df = pd.json_normalize(drive['events'])
        new_df['sequence'] = drive['sequence']
        events_df = events_df.append(new_df)

    clean_df = events_df[['type', 'id', 'sequence', 'clock', 'home_points', 'away_points',
       'play_type', 'description', 'screen_pass', 'hash_mark', 'play_action',
       'run_pass_option', 'statistics', 'details',
       'start_situation.down', 'start_situation.yfd', 'start_situation.possession.alias',
       'start_situation.location.alias',
       'start_situation.location.yardline',
       'end_situation.down', 'end_situation.yfd',
       'end_situation.possession.alias',
       'end_situation.location.alias',
       'end_situation.location.yardline', 'players_rushed', 'men_in_box',
       'blitz', 'play_direction',
       'pocket_location', 'qb_at_snap', 'huddle', 'pass_route', 'running_lane',
       'scoring_play','score.points', 'statistics']]

    clean_df = clean_df.drop('statistics', axis=1)
    clean_df = clean_df.rename(columns={'id': 'play_id'})

    events = []
    for drive in drives:
        events.append(drive['events'])

    plays = []
    for event in events:
        num_plays = len(event)
        for i in range(0, num_plays):
            plays.append(event[i])

    stats_df = pd.DataFrame()
    for play in plays:
        if 'statistics' in play:
            play_df = pd.json_normalize(play['statistics'])
            play_df['play_id'] = play['id']
        stats_df = stats_df.append(play_df)
    
    pass_df = stats_df[stats_df['stat_type'] == 'pass']
    rel_cols = ['stat_type','attempt','complete','yards','att_yards','firstdown','sack','blitz','hurry','knockdown','pocket_time','on_target_throw','batted_pass', 'team.alias', 'sack_yards', 'interception', 'touchdown', 'play_id', 'nullified']
    pass_df = pass_df[([col for col in rel_cols if col in pass_df.columns])]
    pass_df = pass_df.drop_duplicates()
    pass_df = pass_df[pass_df['nullified'] != True]

    pass_clean_df = clean_df[['play_id', 'sequence', 'description', 'screen_pass', 'hash_mark', 'play_action', 'run_pass_option', 'players_rushed', 'men_in_box', 'pass_route', 'running_lane', 'qb_at_snap', 'start_situation.down', 'start_situation.yfd', 'start_situation.possession.alias']]
    pass_df = pass_df.merge(pass_clean_df, how='inner', on='play_id')

    return pass_df

def return_rush_df(data):

    periods = data['periods']

    events = []
    for i in range(0, len(periods)):
        num_events = len(periods[i]['pbp'])
        for j in range(0, num_events):
            events.append((periods[i]['pbp'][j]))

    drives = []
    for event in events:
        if event['type'] == 'drive':
            drives.append(event)

    events_df = pd.DataFrame()
    for drive in drives:
        new_df = pd.json_normalize(drive['events'])
        new_df['sequence'] = drive['sequence']
        events_df = events_df.append(new_df)

    clean_df = events_df[['type', 'id', 'sequence', 'clock', 'home_points', 'away_points',
       'play_type', 'description', 'screen_pass', 'hash_mark', 'play_action',
       'run_pass_option', 'statistics', 'details',
       'start_situation.down', 'start_situation.yfd', 'start_situation.possession.alias',
       'start_situation.location.alias',
       'start_situation.location.yardline',
       'end_situation.down', 'end_situation.yfd',
       'end_situation.possession.alias',
       'end_situation.location.alias',
       'end_situation.location.yardline', 'players_rushed', 'men_in_box',
       'blitz', 'play_direction',
       'pocket_location', 'qb_at_snap', 'huddle', 'pass_route', 'running_lane',
       'scoring_play','score.points', 'statistics']]

    clean_df = clean_df.drop('statistics', axis=1)
    clean_df = clean_df.rename(columns={'id': 'play_id'})

    events = []
    for drive in drives:
        events.append(drive['events'])

    plays = []
    for event in events:
        num_plays = len(event)
        for i in range(0, num_plays):
            plays.append(event[i])

    stats_df = pd.DataFrame()
    for play in plays:
        if 'statistics' in play:
            play_df = pd.json_normalize(play['statistics'])
            play_df['play_id'] = play['id']
        stats_df = stats_df.append(play_df)
    
    rush_df = stats_df[stats_df['stat_type'] == 'rush']
    rel_cols = ['stat_type','yards','firstdown', 'yards_after_contact','touchdown', 'play_id', 'nullified']
    rush_df = rush_df[(rel_cols)]
    rush_df = rush_df.drop_duplicates()
    rush_df = rush_df[rush_df['nullified'] != True]

    rush_clean_df = clean_df[['play_id', 'sequence', 'description', 'run_pass_option', 'players_rushed', 'men_in_box', 'running_lane', 'qb_at_snap', 'start_situation.down', 'start_situation.yfd', 'start_situation.possession.alias']]
    rush_df = rush_df.merge(rush_clean_df, how='inner', on='play_id')

    return rush_df

def return_penalty_df(data):

    periods = data['periods']

    events = []
    for i in range(0, len(periods)):
        num_events = len(periods[i]['pbp'])
        for j in range(0, num_events):
            events.append((periods[i]['pbp'][j]))

    drives = []
    for event in events:
        if event['type'] == 'drive':
            drives.append(event)

    events_df = pd.DataFrame()
    for drive in drives:
        new_df = pd.json_normalize(drive['events'])
        new_df['sequence'] = drive['sequence']
        events_df = events_df.append(new_df)

    clean_df = events_df[['type', 'id', 'sequence', 'clock', 'home_points', 'away_points',
       'play_type', 'description', 'screen_pass', 'hash_mark', 'play_action',
       'run_pass_option', 'statistics', 'details',
       'start_situation.down', 'start_situation.yfd', 'start_situation.possession.alias',
       'start_situation.location.alias',
       'start_situation.location.yardline',
       'end_situation.down', 'end_situation.yfd',
       'end_situation.possession.alias',
       'end_situation.location.alias',
       'end_situation.location.yardline', 'players_rushed', 'men_in_box',
       'blitz', 'play_direction',
       'pocket_location', 'qb_at_snap', 'huddle', 'pass_route', 'running_lane',
       'scoring_play','score.points', 'statistics']]

    clean_df = clean_df.drop('statistics', axis=1)
    clean_df = clean_df.rename(columns={'id': 'play_id'})

    events = []
    for drive in drives:
        events.append(drive['events'])

    plays = []
    for event in events:
        num_plays = len(event)
        for i in range(0, num_plays):
            plays.append(event[i])

    stats_df = pd.DataFrame()
    for play in plays:
        if 'statistics' in play:
            play_df = pd.json_normalize(play['statistics'])
            play_df['play_id'] = play['id']
        stats_df = stats_df.append(play_df)
    
    penalty_df = stats_df[stats_df['stat_type'] == 'penalty']
    rel_cols = ['stat_type', 'yards', 'player.name', 'play_id', 'team.alias']
    penalty_df = penalty_df[(rel_cols)]
    penalty_df = penalty_df.drop_duplicates()
    penalty_clean_df = clean_df[['play_id', 'sequence', 'description','start_situation.down', 'start_situation.yfd', 'start_situation.possession.alias', 'end_situation.down']]
    penalty_df = penalty_df.merge(penalty_clean_df, how='inner', on='play_id')

    return penalty_df