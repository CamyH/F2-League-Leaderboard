# Cameron Hunt 20/09/2020
# F1 2020 F2 League
# The purpose of this python script is to keep track of how well me and my two friends do in our Formula 2 league
# Requries two text files as data sources
# Sample files are provided

import pandas as pd

# Add names of drivers here
driver_names = ["Cameron", "Yossi", "Carter"]
# Driver 1 = Cameron
driver_results_feature_1 = []
driver_results_sprint_1 = []
wins_driver_1 = 0
podiums_driver_1 = 0
poles_driver_1 = 0
fastest_laps_driver_1 = 0
# Driver 2 = Yossi
driver_results_feature_2 = []
driver_results_sprint_2 = []
wins_driver_2 = 0
podiums_driver_2 = 0
poles_driver_2 = 0
fastest_laps_driver_2 = 0
# Driver 3 = Carter
driver_results_feature_3 = []
driver_results_sprint_3 = []
wins_driver_3 = 0
podiums_driver_3 = 0
poles_driver_3 = 0
fastest_laps_driver_3 = 0
# Race Data
feature_race_data = []
sprint_race_data = []

# Points System
# Driver 1 = Cameron
score_driver_feature_1 = 0
score_driver_sprint_1 = 0
# Driver 2 = Yossi
score_driver_feature_2 = 0
score_driver_sprint_2 = 0
# Driver 3 = Carter
score_driver_feature_3 = 0
score_driver_sprint_3 = 0
# feature_race_points = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
# sprint_race_points = [15, 12, 10, 8, 6, 4, 2, 1]
fastest_lap_points = 2
pole_position_points = 4


def input_feature_race_data():
    file = open("feature_races_results.txt", "r")
    for line in file:
        for word in line.split():
            feature_race_data.append(word)


def input_sprint_race_data():
    file = open("sprint_races_results.txt", "r")
    for line in file:
        for word in line.split():
            sprint_race_data.append(word)


def input_feature_race_data_driver_1():
    global score_driver_feature_1
    global poles_driver_1
    global fastest_laps_driver_1
    # Iterating through input file data for the feature race and giving appropriate points
    for idx in range(0, len(feature_race_data)):
        if feature_race_data[idx] == driver_names[0]:
            position = feature_race_data[idx + 1]
            if feature_race_data[idx + 2] == "pole":
                score_driver_feature_1 = score_driver_feature_1 + 4
                poles_driver_1 = poles_driver_1 + 1
            if feature_race_data[idx + 3] == "fl":
                score_driver_feature_1 = score_driver_feature_1 + 2
                fastest_laps_driver_1 = fastest_laps_driver_1 + 1
            if position == "p1":
                score_driver_feature_1 = score_driver_feature_1 + 25
                driver_results_feature_1.append(position)
            elif position == "p2":
                score_driver_feature_1 = score_driver_feature_1 + 18
                driver_results_feature_1.append(position)
            elif position == "p3":
                score_driver_feature_1 = score_driver_feature_1 + 15
                driver_results_feature_1.append(position)
            elif position == "p4":
                score_driver_feature_1 = score_driver_feature_1 + 12
                driver_results_feature_1.append(position)
            elif position == "p5":
                score_driver_feature_1 = score_driver_feature_1 + 10
                driver_results_feature_1.append(position)
            elif position == "p6":
                score_driver_feature_1 = score_driver_feature_1 + 8
                driver_results_feature_1.append(position)
            elif position == "p7":
                score_driver_feature_1 = score_driver_feature_1 + 6
                driver_results_feature_1.append(position)
            elif position == "p8":
                score_driver_feature_1 = score_driver_feature_1 + 4
                driver_results_feature_1.append(position)
            elif position == "p9":
                score_driver_feature_1 = score_driver_feature_1 + 2
                driver_results_feature_1.append(position)
            elif position == "p10":
                score_driver_feature_1 = score_driver_feature_1 + 1
                driver_results_feature_1.append(position)

    return score_driver_feature_1


def input_feature_race_data_driver_2():
    global score_driver_feature_2
    global poles_driver_2
    global fastest_laps_driver_2
    # Iterating through input file data for the feature race and giving appropriate points
    for idx in range(0, len(feature_race_data)):
        if feature_race_data[idx] == driver_names[1]:
            position = feature_race_data[idx + 1]
            if feature_race_data[idx + 2] == "pole":
                score_driver_feature_2 = score_driver_feature_2 + 4
                poles_driver_2 = poles_driver_2 + 1
            if feature_race_data[idx + 3] == "fl":
                score_driver_feature_2 = score_driver_feature_2 + 2
                fastest_laps_driver_2 = fastest_laps_driver_2 + 1
            if position == "p1":
                score_driver_feature_2 = score_driver_feature_2 + 25
                driver_results_feature_2.append(position)
            elif position == "p2":
                score_driver_feature_2 = score_driver_feature_2 + 18
                driver_results_feature_2.append(position)
            elif position == "p3":
                score_driver_feature_2 = score_driver_feature_2 + 15
                driver_results_feature_2.append(position)
            elif position == "p4":
                score_driver_feature_2 = score_driver_feature_2 + 12
                driver_results_feature_2.append(position)
            elif position == "p5":
                score_driver_feature_2 = score_driver_feature_2 + 10
                driver_results_feature_2.append(position)
            elif position == "p6":
                score_driver_feature_2 = score_driver_feature_2 + 8
                driver_results_feature_2.append(position)
            elif position == "p7":
                score_driver_feature_2 = score_driver_feature_2 + 6
                driver_results_feature_2.append(position)
            elif position == "p8":
                score_driver_feature_2 = score_driver_feature_2 + 4
                driver_results_feature_2.append(position)
            elif position == "p9":
                score_driver_feature_2 = score_driver_feature_2 + 2
                driver_results_feature_2.append(position)
            elif position == "p10":
                score_driver_feature_2 = score_driver_feature_2 + 1
                driver_results_feature_2.append(position)

    return score_driver_feature_2


def input_feature_race_data_driver_3():
    global score_driver_feature_3
    global poles_driver_3
    global fastest_laps_driver_3
    # Iterating through input file data for the feature race and giving appropriate points
    for idx in range(0, len(feature_race_data)):
        if feature_race_data[idx] == driver_names[2]:
            position = feature_race_data[idx + 1]
            if feature_race_data[idx + 2] == "pole":
                score_driver_feature_3 = score_driver_feature_3 + 4
                poles_driver_3 = poles_driver_3 + 1
            if feature_race_data[idx + 3] == "fl":
                score_driver_feature_3 = score_driver_feature_3 + 2
                fastest_laps_driver_3 = fastest_laps_driver_3 + 1
            if position == "p1":
                score_driver_feature_3 = score_driver_feature_3 + 25
                driver_results_feature_3.append(position)
            elif position == "p2":
                score_driver_feature_3 = score_driver_feature_3 + 18
                driver_results_feature_3.append(position)
            elif position == "p3":
                score_driver_feature_3 = score_driver_feature_3 + 15
                driver_results_feature_3.append(position)
            elif position == "p4":
                score_driver_feature_3 = score_driver_feature_3 + 12
                driver_results_feature_3.append(position)
            elif position == "p5":
                score_driver_feature_3 = score_driver_feature_3 + 10
                driver_results_feature_3.append(position)
            elif position == "p6":
                score_driver_feature_3 = score_driver_feature_3 + 8
                driver_results_feature_3.append(position)
            elif position == "p7":
                score_driver_feature_3 = score_driver_feature_3 + 6
                driver_results_feature_3.append(position)
            elif position == "p8":
                score_driver_feature_3 = score_driver_feature_3 + 4
                driver_results_feature_3.append(position)
            elif position == "p9":
                score_driver_feature_3 = score_driver_feature_3 + 2
                driver_results_feature_3.append(position)
            elif position == "p10":
                score_driver_feature_3 = score_driver_feature_3 + 1
                driver_results_feature_3.append(position)

    return score_driver_feature_3


def input_sprint_race_data_driver_1():
    global score_driver_sprint_1
    global fastest_laps_driver_1
    # Iterating through input file data for the sprint race and giving appropriate points
    for idx in range(0, len(sprint_race_data)):
        if sprint_race_data[idx] == driver_names[0]:
            position = sprint_race_data[idx + 1]
            if sprint_race_data[idx + 2] == "fl":
                score_driver_sprint_1 = score_driver_sprint_1 + 2
                fastest_laps_driver_1 = fastest_laps_driver_1 + 1
            if position == "p1":
                score_driver_sprint_1 = score_driver_sprint_1 + 15
                driver_results_sprint_1.append(position)
            elif position == "p2":
                score_driver_sprint_1 = score_driver_sprint_1 + 12
                driver_results_sprint_1.append(position)
            elif position == "p3":
                score_driver_sprint_1 = score_driver_sprint_1 + 10
                driver_results_sprint_1.append(position)
            elif position == "p4":
                score_driver_sprint_1 = score_driver_sprint_1 + 8
                driver_results_sprint_1.append(position)
            elif position == "p5":
                score_driver_sprint_1 = score_driver_sprint_1 + 6
                driver_results_sprint_1.append(position)
            elif position == "p6":
                score_driver_sprint_1 = score_driver_sprint_1 + 4
                driver_results_sprint_1.append(position)
            elif position == "p7":
                score_driver_sprint_1 = score_driver_sprint_1 + 2
                driver_results_sprint_1.append(position)
            elif position == "p8":
                score_driver_sprint_1 = score_driver_sprint_1 + 1
                driver_results_sprint_1.append(position)

    return score_driver_sprint_1


def input_sprint_race_data_driver_2():
    global score_driver_sprint_2
    global fastest_laps_driver_2
    # Iterating through input file data for the sprint race and giving appropriate points
    for idx in range(0, len(sprint_race_data)):
        if sprint_race_data[idx] == driver_names[1]:
            position = sprint_race_data[idx + 1]
            if sprint_race_data[idx + 2] == "fl":
                score_driver_sprint_2 = score_driver_sprint_2 + 2
                fastest_laps_driver_2 = fastest_laps_driver_2 + 1
            if position == "p1":
                score_driver_sprint_2 = score_driver_sprint_2 + 15
                driver_results_sprint_2.append(position)
            elif position == "p2":
                score_driver_sprint_2 = score_driver_sprint_2 + 12
                driver_results_sprint_2.append(position)
            elif position == "p3":
                score_driver_sprint_2 = score_driver_sprint_2 + 10
                driver_results_sprint_2.append(position)
            elif position == "p4":
                score_driver_sprint_2 = score_driver_sprint_2 + 8
                driver_results_sprint_2.append(position)
            elif position == "p5":
                score_driver_sprint_2 = score_driver_sprint_2 + 6
                driver_results_sprint_2.append(position)
            elif position == "p6":
                score_driver_sprint_2 = score_driver_sprint_2 + 4
                driver_results_sprint_2.append(position)
            elif position == "p7":
                score_driver_sprint_2 = score_driver_sprint_2 + 2
                driver_results_sprint_2.append(position)
            elif position == "p8":
                score_driver_sprint_2 = score_driver_sprint_2 + 1
                driver_results_sprint_2.append(position)

    return score_driver_sprint_2


def input_sprint_race_data_driver_3():
    global score_driver_sprint_3
    global fastest_laps_driver_3
    # Iterating through input file data for the sprint race and giving appropriate points
    for idx in range(0, len(sprint_race_data)):
        if sprint_race_data[idx] == driver_names[2]:
            position = sprint_race_data[idx + 1]
            if sprint_race_data[idx + 2] == "fl":
                score_driver_sprint_3 = score_driver_sprint_3 + 2
                fastest_laps_driver_3 = fastest_laps_driver_3 + 1
            if position == "p1":
                score_driver_sprint_3 = score_driver_sprint_3 + 15
                driver_results_sprint_3.append(position)
            elif position == "p2":
                score_driver_sprint_3 = score_driver_sprint_3 + 12
                driver_results_sprint_3.append(position)
            elif position == "p3":
                score_driver_sprint_3 = score_driver_sprint_3 + 10
                driver_results_sprint_3.append(position)
            elif position == "p4":
                score_driver_sprint_3 = score_driver_sprint_3 + 8
                driver_results_sprint_3.append(position)
            elif position == "p5":
                score_driver_sprint_3 = score_driver_sprint_3 + 6
                driver_results_sprint_3.append(position)
            elif position == "p6":
                score_driver_sprint_3 = score_driver_sprint_3 + 4
                driver_results_sprint_3.append(position)
            elif position == "p7":
                score_driver_sprint_3 = score_driver_sprint_3 + 2
                driver_results_sprint_3.append(position)
            elif position == "p8":
                score_driver_sprint_3 = score_driver_sprint_3 + 1
                driver_results_sprint_3.append(position)

    return score_driver_sprint_3


# Calling main functions
input_feature_race_data()
input_sprint_race_data()
input_feature_race_data_driver_1()
input_feature_race_data_driver_2()
input_feature_race_data_driver_3()
input_sprint_race_data_driver_1()
input_sprint_race_data_driver_2()
input_sprint_race_data_driver_3()

# Calculating final total of points
# Adding feature race points with sprint drivers points
total_points_driver_1 = score_driver_feature_1 + score_driver_sprint_1
total_points_driver_2 = score_driver_feature_2 + score_driver_sprint_2
total_points_driver_3 = score_driver_feature_3 + score_driver_sprint_3

# Calculating total number of podiums & wins achieved for the first driver
for position in driver_results_feature_1:
    if position == "p1":
        wins_driver_1 = wins_driver_1 + 1
    if position == "p1" or position == "p2" or position == "p3":
        podiums_driver_1 = podiums_driver_1 + 1

for position in driver_results_sprint_1:
    if position == "p1":
        wins_driver_1 = wins_driver_1 + 1
    if position == "p1" or position == "p2" or position == "p3":
        podiums_driver_1 = podiums_driver_1 + 1
# Calculating total number of podiums & wins achieved for the second driver
for position in driver_results_feature_2:
    if position == "p1":
        wins_driver_2 = wins_driver_2 + 1
    if position == "p1" or position == "p2" or position == "p3":
        podiums_driver_2 = podiums_driver_2 + 1

for position in driver_results_sprint_2:
    if position == "p1":
        wins_driver_2 = wins_driver_2 + 1
    if position == "p1" or position == "p2" or position == "p3":
        podiums_driver_2 = podiums_driver_2 + 1

# Calculating total number of podiums & wins achieved for the third driver
for position in driver_results_feature_3:
    if position == "p1":
        wins_driver_3 = wins_driver_3 + 1
    if position == "p1" or position == "p2" or position == "p3":
        podiums_driver_3 = podiums_driver_3 + 1

for position in driver_results_sprint_3:
    if position == "p1":
        wins_driver_3 = wins_driver_3 + 1
    if position == "p1" or position == "p2" or position == "p3":
        podiums_driver_3 = podiums_driver_3 + 1

# Output Table
league_results = {"Driver": [driver_names[0], driver_names[1], driver_names[2]],
                  "Points": [total_points_driver_1, total_points_driver_2, total_points_driver_3],
                  "Wins": [wins_driver_1, wins_driver_2, wins_driver_3],
                  "Podiums": [podiums_driver_1, podiums_driver_2, podiums_driver_3],
                  "Poles": [poles_driver_1, poles_driver_2, poles_driver_3],
                  "Fastest Laps": [fastest_laps_driver_1, fastest_laps_driver_2, fastest_laps_driver_3]}


def output_data_to_table():
    df = pd.DataFrame(league_results, columns=["Driver", "Points", "Wins", "Podiums", "Poles", "Fastest Laps"])
    # Sort output table by ascending order
    df = df.sort_values(["Points"], ascending=[0])
    try:
        df.to_csv('results.csv')
        print("Results file successfully created!")
    except IOError:
        print("Error generating results file. Try again.")


# Calling Output Table Function
output_data_to_table()
