def direction(facing, turn):
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    dir_look = directions.index(facing)
    look_steps = turn // 45

    if look_steps >= 0:
        while look_steps > 0:
            dir_look += 1
            if dir_look > len(directions) - 1:
                dir_look = 0
            look_steps -= 1
        return directions[dir_look]
    else:
        while look_steps < 0:
            dir_look -= 1
            if dir_look == 0:
                dir_look = len(directions) - 1
            look_steps += 1
        return directions[dir_look]
