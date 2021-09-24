import pandas as pd

main_data_set = pd.read_csv("athlete_events.csv")

print(main_data_set.Sport.unique())
