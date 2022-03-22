command = input()

players_pool = {}  # tier {player: {position: skill}}

while command != "Season end":

    if ' -> ' in command:
        player, position, skill = command.split(' -> ')

        if player not in players_pool:
            players_pool[player] = {position: int(skill)}

        elif position not in players_pool[player].keys():
            players_pool[player][position] = int(skill)

        else:
            players_pool[player][position] = max(players_pool[player][position], int(skill))

    elif ' vs ' in command:
        player_1, player_2 = command.split(' vs ')

        if player_1 in players_pool.keys() and player_2 in players_pool.keys():  # both players exist in the tier
            for p1_position in players_pool[player_1].keys():
                if p1_position in players_pool[player_2].keys():  # If they got at least one position in common
                    p1_skill = sum(players_pool[player_1].values())
                    p2_skill = sum(players_pool[player_2].values())
                    if p1_skill < p2_skill:  # player with better total skill points wins
                        players_pool.pop(player_1)  # and the other is demoted from the tier -> remove him
                    elif p2_skill < p1_skill:
                        players_pool.pop(player_2)
                    break

    command = input()

player_pts = [(p, sum(players_pool[p].values())) for p in players_pool.keys()]
player_ranking = [rank for rank in sorted(player_pts, key=lambda item: (-item[1], item[0]))]

for rank in player_ranking:
    player, skill = rank
    print(f"{player}: {skill} skill")
    position_ranking = [rank for rank in sorted(players_pool[player].items(), key=lambda item: (-item[1], item[0]))]
    output = [f'- {pos} <::> {skill}' for pos, skill in position_ranking]
    print(*output, sep='\n')