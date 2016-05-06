import dice

sq_names_dict = dict()
sq_names_dict['GO'] = '00'
sq_names_dict['A1'] = '01'
sq_names_dict['CC1'] = '02'
sq_names_dict['A2'] = '03'
sq_names_dict['T1'] = '04'
sq_names_dict['R1'] = '05'
sq_names_dict['B1'] = '06'
sq_names_dict['CH1'] = '07'
sq_names_dict['B2'] = '08'
sq_names_dict['B3'] = '09'
sq_names_dict['JAIL'] = '10'
sq_names_dict['C1'] = '11'
sq_names_dict['U1'] = '12'
sq_names_dict['C2'] = '13'
sq_names_dict['C3'] = '14'
sq_names_dict['R2'] = '15'
sq_names_dict['D1'] = '16'
sq_names_dict['CC2'] = '17'
sq_names_dict['D2'] = '18'
sq_names_dict['D3'] = '19'
sq_names_dict['FP'] = '20'
sq_names_dict['E1'] = '21'
sq_names_dict['CH2'] = '22'
sq_names_dict['E2'] = '23'
sq_names_dict['E3'] = '24'
sq_names_dict['R3'] = '25'
sq_names_dict['F1'] = '26'
sq_names_dict['F2'] = '27'
sq_names_dict['U2'] = '28'
sq_names_dict['F3'] = '29'
sq_names_dict['G2J'] = '30'
sq_names_dict['G1'] = '31'
sq_names_dict['G2'] = '32'
sq_names_dict['CC3'] = '33'
sq_names_dict['G3'] = '34'
sq_names_dict['R4'] = '35'
sq_names_dict['CH3'] = '36'
sq_names_dict['H1'] = '37'
sq_names_dict['T2'] = '38'
sq_names_dict['H2'] = '39'
community_chest = ['CC1', 'CC2', 'CC3']
chance = ['CH1', 'CH2', 'CH3']
railroad = ['R1', 'R2', 'R3', 'R4']

# given that the values above are unique
inv_names_dict = {int(v): k for k, v in sq_names_dict.items()}
count_dict = {int(v): 0 for k, v in sq_names_dict.items()}

total_count = 0
where_at = 0
consecutive_doubles = 0
for i in range(1, 100000):
    #roll = dice.roll('2d6')
    roll = dice.roll('2d4')
    double = (roll[0] == roll[1])
    if double and consecutive_doubles == 2:
        where_at = int(sq_names_dict["G2J"])
    else:
        if double:
            consecutive_doubles += 1
        else:
            consecutive_doubles = 0
            where_at = where_at + roll[0] + roll[1]
            if where_at > 39:
                where_at %= 40

    where_at_name = inv_names_dict[where_at]
    if where_at_name == "G2J":
        where_at = int(sq_names_dict["JAIL"])
    elif where_at_name in community_chest:
        card = dice.roll('1d16')
        if card[0] == 1:
            where_at = int(sq_names_dict["GO"])
        elif card[0] == 2:
            where_at = int(sq_names_dict["JAIL"])
            # else stay on community chest:
    elif where_at_name in chance:
        card = dice.roll('1d16')
        if card[0] == 1:
            where_at = int(sq_names_dict["GO"])
        elif card[0] == 2:
            where_at = int(sq_names_dict["JAIL"])
        elif card[0] == 3:
            where_at = int(sq_names_dict["C1"])
        elif card[0] == 4:
            where_at = int(sq_names_dict["E3"])
        elif card[0] == 5:
            where_at = int(sq_names_dict["H2"])
        elif card[0] == 6:
            where_at = int(sq_names_dict["R1"])
        elif card[0] == 7 or card[0] == 8:
            # go to next railroad
            if where_at_name == 'CH1':
                where_at = int(sq_names_dict["R2"])
            elif where_at_name == 'CH2':
                where_at = int(sq_names_dict["R3"])
            else:
                where_at = int(sq_names_dict["R1"])
        elif card[0] == 9:
            # go to next utility
            if where_at_name == 'CH1':
                where_at = int(sq_names_dict["U1"])
            elif where_at_name == 'CH2':
                where_at = int(sq_names_dict["U2"])
            else:
                where_at = int(sq_names_dict["U1"])
        elif card[0] == 10:
            # go back 3
            where_at -= 3

    count_dict[where_at] += 1
    total_count += 1

for k in sorted(count_dict, key=count_dict.get, reverse=True):
    val = count_dict[k]
    print("For cell {} we landed {} times or {} pct".format(inv_names_dict[k], val, val / total_count))

i = 1
modalstring = ""
for k in sorted(count_dict, key=count_dict.get, reverse=True):
    name = inv_names_dict[k]
    modalstring = modalstring + sq_names_dict[name]
    i += 1
    if i == 4:
        break

print("Modal string is {}".format(modalstring))
