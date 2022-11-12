"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    current_file = open(filename)
    species = set()
    for line in current_file:
        words = line.split("|")
        current_s = words[1]
        species.add(current_s)

    current_file.close()
    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    current_file = open(filename)
    for line in current_file:
        words = line.split("|")
        current_s = words[1]
        if current_s == search_string:
            villagers_name = words[0]
            villagers.append(villagers_name)

    current_file.close()

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code
    current_file = open(filename)
    set_find_hobbies = set()
    hobby_list = []

    #Parse through current_file and add all hobbies to create a complete set of distinct hobbies
    for line in current_file:
        words = line.split("|")
        current_hobby = words[3]
        #Make sure all hobbies exist in this set
        #{'Music', 'Fitness', 'Fashion', 'Education', 'Nature', 'Play'}
        set_find_hobbies.add(current_hobby)

    #Turn the set into a list
    for unique_hobby in set_find_hobbies:
        hobby_list.append(unique_hobby, [])
        #output: ['Music', [] , 'Fitness', 'Fashion', 'Education', 'Nature', 'Play']
    
    #Loop through list and add each name to a list, for a hobby
    for line in current_file:
        words = line.split("|")
        current_hobby = words[3]
        villager_name = words[0]
        
        #if current_hobby matches a hobby in hobby_list, add villages name to matching list and append it
        if current_hobby in hobby_list:
            hobby_list[current_hobby + 1].append(villager_name)


    return hobby_list
all_names_by_hobby("villagers.csv")

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code

#get_villagers_by_species("villagers.csv", "Anteater")