class SchipholMapper:
  def __init__(self):
    self.__flights = None
    self._airlines = None
    self._destinations = None
    self._aircraftTypes = None

  def load_from_contents(self, contents):
    for content in contents:

        key = list(content.keys())[0]
        value = list(content.values())[0]

        if key == 'flights':
          self.__flights = value
        elif key == 'airlines':
          self._airlines = value
        elif key == 'destinations':
          self._destinations = value
        elif key == 'aircraftTypes':
          self._aircraftTypes = value
        else:
          raise ValueError(f"Chave invalida! {key}")

    return {'flights': self.__flights, 'airlines': self._airlines,
            'destinations': self._destinations, 'aircraftTypes': self._aircraftTypes}
