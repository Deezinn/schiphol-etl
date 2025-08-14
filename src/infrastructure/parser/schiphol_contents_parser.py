class SchipholContentsParser:
  def __init__(self):
    self.__flights = None
    self.__airlines = None
    self.__destinations = None
    self.__aircraftTypes = None

  def load_from_contents(self, contents):
    for content in contents:

        key = list(content.keys())[0]
        value = list(content.values())[0]

        if key == 'flights':
          self.__flights = value
        elif key == 'airlines':
          self.__airlines = value
        elif key == 'destinations':
          self.__destinations = value
        elif key == 'aircraftTypes':
          self.__aircraftTypes = value
        else:
          raise ValueError(f"Chave invalida! {key}")

    return {'flights': self.__flights, 'airlines': self.__airlines,
            'destinations': self.__destinations, 'aircraftTypes': self.__aircraftTypes}
