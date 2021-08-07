def co2_judge(co2_value):
    if co2_value > 1200:
        return 'red'
    if co2_value > 800:
        return 'yellow'
    return 'green'
