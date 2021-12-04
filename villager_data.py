"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    species = set()

    # TODO: replace this with your code
    file_log = open(filename)
    for line in file_log:
      species.add(line.split('|')[1])
    return species


def get_villagers_by_species(filename, species="All"):
    """Return a list of villagers' names by species.

    Arguments:
      - filename (str): the path to a data file
      - species (str): optional, the name of a species

    Return:
      - list[list]: a list of lists
    """

    villagers = []

    # TODO: replace this with your code
    file_log = open(filename)
    for villager in file_log:
      name,animals = villager.split('|')[:2]
      if species in ("All", animals):
        villagers.append(name)
    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list that villagers' names, grouped by hobby.

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    # TODO: replace this with your code
    Fitness = []
    Play = []
    Music = []
    Nature = []
    Education = []
    Fashion = []

    file_log = open(filename)
    for villagers in file_log:
      name,hobby = villagers.split('|')[0], villagers.split('|')[-2]
      if hobby == "Fitness":
        Fitness.append(name)
      if hobby == "Play":
        Play.append(name)
      if hobby == "Fashion":
        Fashion.append(name)
      if hobby == "Music":
        Music.append(name)
      if hobby == "Nature":
        Nature.append(name)
      if hobby == "Education":
        Education.append(name)

    all_hobbies = [Fitness, Fashion, Education, Play, Music, Nature]
    # print(all_hobbies)
    print(Education)
    return [Fitness, Fashion, Education, Play, Music, Nature]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []
    
    file_log = open(filename)
    for data in file_log:
      name, species, personality, hobby,saying = data.split('|')
      data_tup = (name, species, personality, hobby, saying)
    # TODO: replace this with your code
      all_data.append(data_tup)
    return all_data


def find_motto(filename, name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """
    motto = ""
    file_log= open(filename)
    for line in file_log:
      if name == line.split('|')[0]:
        motto = line.split('|')[-1]
  
    return motto


def find_likeminded_villagers(filename, name):
    """Return a set of villagers with the same personality as the given villager."""
    villager_name, personality = '',''
    villagers =[]
    like_minded_villagers= set()

    file_log = open(filename)

    for line in file_log:
      villagers.append(line.split('|')[0:3])
      villager_name, personality = line.split('|')[0], line.split('|')[2]
     

    for names in villagers:
       print(names)
      if (names[2] == personality):
        print(personality)
        like_minded_villagers.add(names[0])
    print(like_minded_villagers, name)  

find_likeminded_villagers("villagers.csv","Audie")