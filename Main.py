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
print(round(q_2, 1), " %")

print('Вопрос 3:')

q_3_frame = main_data_set.loc[lambda x: (x.Sex == 'F') & (x.Year == 2000) & (x.Sport == 'Tennis') & (x.Height > 0),
                              ["Name", "Height"]].drop_duplicates(subset="Name", keep="first")

q_3_height_mean = q_3_frame.Height.mean()
q_3_dispersion = q_3_frame.Height.map(lambda x: (x - q_3_height_mean) ** 2).sum()
q_3_ms = q_3_dispersion / (len(q_3_frame.index) - 1)
q_3_std = q_3_ms ** 0.5
print("Средний квадрат отклонений: ", round(q_3_ms, 1))
print("Стандартное отклонение: ", round(q_3_std, 1))

print("Вопрос 4:")

q_4_frame = main_data_set.loc[main_data_set.Year == 2006]
q_4_frame = q_4_frame.sort_values(by="Weight", ascending=False)
print("Имя: ", q_4_frame.iloc[0, 1])
print("Вес: ", int(q_4_frame.iloc[0, 5]))
print("Вид спорта: ", q_4_frame.iloc[0, 12])

print("Вопрос 5:")

# John Aalberg
q_5_frame = main_data_set.loc[main_data_set.Name == "John Aalberg"]
print(q_5_frame.groupby("Year").ID.count())

print("Вопрос 6:")

q_6_frame = main_data_set.loc[lambda x: (x.NOC == 'SUI') & (x.Year == 2008) & (x.Sport == 'Tennis') & (x.Medal != "NA"),
                              ["Name", "Medal"]]
print(q_6_frame.groupby("Name").Medal.count())

print("Вопрос 7: ")

q_7_frame = main_data_set.loc[lambda x: (x.NOC.isin(["ITA", "ESP"])) & (x.Year == 2016) & (x.Medal.notnull()),
                              ["NOC", "Medal"]]
q_7 = q_7_frame.groupby("NOC").Medal.count()
if q_7["ESP"] < q_7["ITA"]:
    print("Правда")
else:
    print("Ложь")

print("Вопрос 8: ")

q_8_frame = main_data_set.loc[lambda x: (x.Year == 2008) & (x.Age.notnull()),
                              ["Name", 'Age']].drop_duplicates(subset="Name", keep="first")
q_8_group = q_8_frame.groupby("Age").Age.count()
print("Наименьшее:")
print(q_8_group[q_8_group == q_8_group.min()].to_string(header=False))
print("Наибольшее:")
print(q_8_group[q_8_group == q_8_group.max()].to_string(header=False))
