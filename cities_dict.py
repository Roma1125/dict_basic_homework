def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """
    answer={}
    for i in range(len(cities)):
        answer.setdefault(i,cities[i])

    return answer
print(cities_dict(["Bukhara", "Khiva", "Namangan", "Samarkand", "Tashkent"]))