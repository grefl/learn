

def format_duration(seconds):
    time_values = {
        'second': {'val':0, 'ranking': 4},
        'minute':{'val':0, 'ranking': 3},
        'hour':{'val':0, 'ranking': 2},
        'day':{'val':0, 'ranking': 1},
        'year':{'val':0, 'ranking': 0},
    }
    time_values['second']['val'] = seconds % 60
    time_values['minute']['val'] = seconds // 60
    time_values['hour']['val']  = time_values['minute']['val'] // 60
    time_values['minute']['val'] = time_values['minute']['val'] % 60
    time_values['day']['val'] = time_values['hour']['val'] //  24
    time_values['hour']['val'] = time_values['hour']['val'] % 24 
    time_values['year']['val'] = time_values['day']['val'] // 365
    time_values['day']['val'] = time_values['day']['val'] % 365
    sorted_values = sorted(time_values.items(), key=lambda x : x[1]['ranking'])
    new_values = []
    for key, val in sorted_values:
        if val['val'] > 0:
            if val['val'] > 1:
                new_values.append((key + 's', val['val']))
            else:
                new_values.append((key, val['val']))
    if len(new_values) == 1:
        key, value = new_values.pop()
        return f"{value} {key}" 
    last = len(new_values) -1
    new_string = []
    for idx, (key, value) in enumerate(new_values):
        if idx == last:
            new_string.append(f"and {value} {key}")
        else:
            comma = ',' if idx < last -1 else ''
            new_string.append(f"{value} {key}{comma} ")
    return ''.join(new_string)

print(format_duration((3601 * 24) * 364))
