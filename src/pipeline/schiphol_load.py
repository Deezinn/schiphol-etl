

def save_in_csv(dataframe, tag):
  match tag:
      case "aircraftTypes":
        dataframe.to_csv(f"src/data/raw/{tag}.csv")
      case "airlines":
        dataframe.to_csv(f"src/data/raw/{tag}.csv")
      case "destinations":
        dataframe.to_csv(f"src/data/raw/{tag}.csv")
      case "flights":
        dataframe.to_csv(f"src/data/raw/{tag}.csv")
      case _:
        print("Tag invalida!")
