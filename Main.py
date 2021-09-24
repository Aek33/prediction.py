import pandas as pd

main_data_set = pd.read_csv("athlete_events.csv")

print('Вопрос 1:')
q_1_frame = main_data_set.loc[(main_data_set.Year == 1992), ['Sex', 'Age']].groupby(['Sex']).Age.min()
q_1 = "Мужчина: " + str(int(q_1_frame[1])) + " лет;" + "\n" \
      + "Женщина: " + str(int(q_1_frame[0])) + " лет."
print(q_1)

print('Вопрос 2:')
q_2_frame = main_data_set.loc[(main_data_set.Year == 2012), ["ID", "Name", 'Sex', "Sport"]]
q_2_frame = q_2_frame.loc[(q_2_frame.Sex == "M"), ["ID", "Name", "Sport"]]
q_2_frame = q_2_frame.drop_duplicates(subset="Name", keep="first")
q_2_all = len(q_2_frame.index)
q_2_basketball = len(q_2_frame.loc[(q_2_frame.Sport == "Basketball"), ["ID", "Name", "Sport"]].index)
q_2 = q_2_basketball * 100 / q_2_all
print(round(q_2, 2), " %")

