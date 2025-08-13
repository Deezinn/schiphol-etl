class SchipholEntity:
  def __init__(self, flights = None, airlines = None, destinations = None, aircraftTypes = None):
    self.flights = flights
    self.airlines = airlines
    self.destinations = destinations
    self.aircrafttypes = aircraftTypes

  @classmethod
  def from_dict(cls, data):
    return cls(
      flights=data.get('flights'),
      airlines=data.get('airlines'),
      destinations=data.get('destinations'),
      aircraftTypes=data.get('aircraftTypes')
    )
