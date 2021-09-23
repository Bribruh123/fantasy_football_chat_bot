from .constant import ACTIVITY_MAP
import datetime

class Activity(object):
    def __init__(self, data, player_map, get_team_data, player_info):
        self.actions = [] # List of tuples (Team, action, Player)
        
        self.date = data['date']
        
        
        
        epoch_time = self.date
        print(epoch_time)
        # using the datetime.fromtimestamp() function  
        date_time = datetime.datetime.fromtimestamp( epoch_time/1000 ) 
        
        current = datetime.datetime.now()
        
        print(date_time, current)
        
        for msg in data['messages']:
            team = ''
            action = 'UNKNOWN'
            player = None
            bid_amount = 0
            msg_id = msg['messageTypeId']
            if msg_id == 244:
                team = get_team_data(msg['from'])
            elif msg_id == 239:
                team = get_team_data(msg['for'])
            else:
                team = get_team_data(msg['to'])
            if msg_id in ACTIVITY_MAP:
                action = ACTIVITY_MAP[msg_id]
            if action == 'WAIVER ADDED':
                bid_amount = msg.get('from', 0)
            if team:
                for team_player in team.roster:
                    if team_player.playerId == msg['targetId']:
                        player = team_player
                        break
            if not player:
                player = player_info(playerId=msg['targetId'])
            self.actions.append((team, action, player, bid_amount, str(date_time)))

    def __repr__(self):
    for a in self.actions:
        pfint(a[0:5])
        return 'Activity(' + ' '.join("(%s,%s,%s,%s)" % tup[0:5] for tup in self.actions) + ')'





