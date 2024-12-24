
def add_valid_stats(stats):
    result = 0
    for stat in stats :
        if stat is not None:
            result = result + stat
    return result