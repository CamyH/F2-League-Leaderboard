# Cameron Hunt 12/10/2020
# F1 2020 F2 League
# The purpose of this python script is to keep track of how well me and my two friends do in our Formula 2 league
# Requires two text files as data sources
# Sample files are provided

import pandas as pd

# Driver 1
feature_wins_driver_1 = 0
sprint_wins_driver_1 = 0
podiums_driver_1 = 0
poles_driver_1 = 0
fastest_laps_driver_1 = 0
# Driver 2
feature_wins_driver_2 = 0
sprint_wins_driver_2 = 0
podiums_driver_2 = 0
poles_driver_2 = 0
fastest_laps_driver_2 = 0
# Driver 3
feature_wins_driver_3 = 0
sprint_wins_driver_3 = 0
podiums_driver_3 = 0
poles_driver_3 = 0
fastest_laps_driver_3 = 0
# Race Data
feature_race_data = []
sprint_race_data = []

# Points System
# Driver 1
score_driver_feature_1 = 0
score_driver_sprint_1 = 0
season_results_driver1 = []
# Driver 2
score_driver_feature_2 = 0
score_driver_sprint_2 = 0
season_results_driver2 = []
# Driver 3
score_driver_feature_3 = 0
score_driver_sprint_3 = 0
season_results_driver3 = []


class Driver:

    def __init__(self):
        # self.name = name
        self.feature_race = feature_race_data
        # for word in feature_race_data:
        #   print(word)

    def input_feature_race_data(self):
        file = open("feature_races_results.txt", "r")
        for line in file:
            for word in line.split():
                feature_race_data.append(word)
                # print(word)

    def input_sprint_race_data(self):
        file = open("sprint_races_results.txt", "r")
        for line in file:
            for word in line.split():
                sprint_race_data.append(word)
                # print(word)

    def calculate_feature_race_points(self, name, driver_score, driver_poles, driver_fastest_laps,
                                      driver_results_feature):
        driver = Driver()
        driver.input_feature_race_data()
        self.driver_name = name
        self.driver_score_feature = driver_score
        self.driver_poles_feature = driver_poles
        self.driver_fastest_laps_feature = driver_fastest_laps
        self.driver_results_feature = driver_results_feature
        for idx in range(0, len(feature_race_data)):
            if feature_race_data[idx] == self.driver_name:
                position = feature_race_data[idx + 1]
                if feature_race_data[idx + 2] == "pole":
                    self.driver_score_feature = self.driver_score_feature + 4
                    self.driver_poles_feature = self.driver_poles_feature + 1
                if feature_race_data[idx + 3] == "fl":
                    self.driver_score_feature = self.driver_score_feature + 2
                    self.driver_fastest_laps_feature = self.driver_fastest_laps_feature + 1
                if position == "p1":
                    self.driver_score_feature = self.driver_score_feature + 25
                    position_feature = position + "f"
                    self.driver_results_feature.append(position_feature)
                elif position == "p2":
                    self.driver_score_feature = self.driver_score_feature + 18
                    self.driver_results_feature.append(position)
                elif position == "p3":
                    self.driver_score_feature = self.driver_score_feature + 15
                    self.driver_results_feature.append(position)
                elif position == "p4":
                    self.driver_score_feature = self.driver_score_feature + 12
                    self.driver_results_feature.append(position)
                elif position == "p5":
                    self.driver_score_feature = self.driver_score_feature + 10
                    self.driver_results_feature.append(position)
                elif position == "p6":
                    self.driver_score_feature = self.driver_score_feature + 8
                    self.driver_results_feature.append(position)
                elif position == "p7":
                    self.driver_score_feature = self.driver_score_feature + 6
                    self.driver_results_feature.append(position)
                elif position == "p8":
                    self.driver_score_feature = self.driver_score_feature + 4
                    self.driver_results_feature.append(position)
                elif position == "p9":
                    self.driver_score_feature = self.driver_score_feature + 2
                    self.driver_results_feature.append(position)
                elif position == "p10":
                    self.driver_score_feature = self.driver_score_feature + 1
                    self.driver_results_feature.append(position)
                else:
                    self.driver_results_feature.append(position)

    def calculate_sprint_race_points(self, name, driver_score, driver_fastest_laps,
                                     driver_results_sprint):
        driver = Driver()
        driver.input_sprint_race_data()
        self.driver_name = name
        self.driver_score_sprint = driver_score
        self.driver_fastest_laps_sprint = driver_fastest_laps
        self.driver_results_sprint = driver_results_sprint
        for idx in range(0, len(sprint_race_data)):
            if sprint_race_data[idx] == self.driver_name:
                position = sprint_race_data[idx + 1]
                if sprint_race_data[idx + 2] == "fl":
                    self.driver_score_sprint = self.driver_score_sprint + 2
                    self.driver_fastest_laps_sprint = self.driver_fastest_laps_sprint + 1
                if position == "p1":
                    self.driver_score_sprint = self.driver_score_sprint + 15
                    position_sprint = position + "s"
                    self.driver_results_sprint.append(position_sprint)
                elif position == "p2":
                    self.driver_score_sprint = self.driver_score_sprint + 12
                    self.driver_results_sprint.append(position)
                elif position == "p3":
                    self.driver_score_sprint = self.driver_score_sprint + 10
                    self.driver_results_sprint.append(position)
                elif position == "p4":
                    self.driver_score_sprint = self.driver_score_sprint + 8
                    self.driver_results_sprint.append(position)
                elif position == "p5":
                    self.driver_score_sprint = self.driver_score_sprint + 6
                    self.driver_results_sprint.append(position)
                elif position == "p6":
                    self.driver_score_sprint = self.driver_score_sprint + 4
                    self.driver_results_sprint.append(position)
                elif position == "p7":
                    self.driver_score_sprint = self.driver_score_sprint + 2
                    self.driver_results_sprint.append(position)
                elif position == "p8":
                    self.driver_score_sprint = self.driver_score_sprint + 1
                    self.driver_results_sprint.append(position)
                else:
                    self.driver_results_sprint.append(position)


# numOfDrivers = 5

# a = Driver()
# b = Driver()
# "a={a}, b={b}, a+b={c}".format(a=a, b=b, c=a+b)

# for i in range(0, numOfDrivers):
#    'driver{0}'.format(i) = Driver()

driver1 = Driver()
driver2 = Driver()
driver3 = Driver()

# Feature Races
driver1.calculate_feature_race_points("Cameron", 0, 0, 0, [])
for i in range(0, len(feature_race_data)):
    del feature_race_data[0]
driver2.calculate_feature_race_points("Yossi", 0, 0, 0, [])
for i in range(0, len(feature_race_data)):
    del feature_race_data[0]
driver3.calculate_feature_race_points("Carter", 0, 0, 0, [])

# Sprint Races
driver1.calculate_sprint_race_points("Cameron", 0, 0, [])
for i in range(0, len(sprint_race_data)):
    del sprint_race_data[0]
driver2.calculate_sprint_race_points("Yossi", 0, 0, [])
for i in range(0, len(sprint_race_data)):
    del sprint_race_data[0]
driver3.calculate_sprint_race_points("Carter", 0, 0, [])
for i in range(0, len(sprint_race_data)):
    del sprint_race_data[0]

# Add both results arrays together for all drivers and store in new array driver1_results
driver1_results = (*driver1.driver_results_feature, *driver1.driver_results_sprint)
driver2_results = (*driver2.driver_results_feature, *driver2.driver_results_sprint)
driver3_results = (*driver3.driver_results_feature, *driver3.driver_results_sprint)
# Get fastest laps for each driver
fastest_laps_driver_1 = driver1.driver_fastest_laps_feature + driver1.driver_fastest_laps_sprint
fastest_laps_driver_2 = driver2.driver_fastest_laps_feature + driver2.driver_fastest_laps_sprint
fastest_laps_driver_3 = driver3.driver_fastest_laps_feature + driver3.driver_fastest_laps_sprint
# Get total points for each driver
total_points_driver_1 = driver1.driver_score_feature + driver1.driver_score_sprint
total_points_driver_2 = driver2.driver_score_feature + driver2.driver_score_sprint
total_points_driver_3 = driver3.driver_score_feature + driver3.driver_score_sprint

# Calculating total number of podiums & wins achieved
for position in driver1_results:
    if position == "p1s":
        sprint_wins_driver_1 = sprint_wins_driver_1 + 1
    elif position == "p1f":
        feature_wins_driver_1 = feature_wins_driver_1 + 1
    if position == "p1s" or position == "p1f" or position == "p2" or position == "p3":
        podiums_driver_1 = podiums_driver_1 + 1

for position in driver2_results:
    if position == "p1s":
        sprint_wins_driver_2 = sprint_wins_driver_2 + 1
    elif position == "p1f":
        feature_wins_driver_2 = feature_wins_driver_2 + 1
    if position == "p1s" or position == "p1f" or position == "p2" or position == "p3":
        podiums_driver_2 = podiums_driver_2 + 1

for position in driver3_results:
    if position == "p1s":
        sprint_wins_driver_3 = sprint_wins_driver_3 + 1
    elif position == "p1f":
        feature_wins_driver_3 = feature_wins_driver_3 + 1
    if position == "p1s" or position == "p1f" or position == "p2" or position == "p3":
        podiums_driver_3 = podiums_driver_3 + 1

# Output Table
# FR = Feature Race
# SR = Sprint Race
league_results = {"Driver": [driver1.driver_name, driver2.driver_name, driver3.driver_name],
                  "FR Wins": [feature_wins_driver_1, feature_wins_driver_2, feature_wins_driver_3],
                  "SR Wins": [sprint_wins_driver_1, sprint_wins_driver_2, sprint_wins_driver_3],
                  "Podiums": [podiums_driver_1, podiums_driver_2, podiums_driver_3],
                  "Poles": [driver1.driver_poles_feature, driver2.driver_poles_feature, driver3.driver_poles_feature],
                  "FLaps": [fastest_laps_driver_1, fastest_laps_driver_2, fastest_laps_driver_3],
                  "Points": [total_points_driver_1, total_points_driver_2, total_points_driver_3]}

race_results = {"Driver": [driver1.driver_name, driver2.driver_name, driver3.driver_name],
                "Feature Race Results": [driver1.driver_results_feature, driver2.driver_score_feature, driver3.driver_score_feature],
                "Sprint Race Results": [driver1.driver_results_sprint, driver2.driver_results_sprint, driver3.driver_results_sprint]}

# Output function
def output():
    df = pd.DataFrame(league_results, columns=["Driver", "FR Wins", "SR Wins", "Podiums", "Poles", "FLaps", "Points"])
    driver_results_output = pd.DataFrame(race_results, columns=["Driver", "Feature Race Results", "Sprint Race Results"])
    #driver2_results_output = pd.DataFrame(driver2_results, columns=["Race Results for "][driver2_name])
    #driver3_results_output = pd.DataFrame(driver3_results, columns=["Race Results for "][driver3_name])

    # Sort output table by ascending order
    df = df.sort_values(["Points"], ascending=[0])
    #print(driver2_results_output)
    #print(driver3_results_output)
    try:
        df.to_csv('results.csv')
        print("Results file successfully created!")
    except IOError:
        print("Error generating results file. Try again.")


# Call function
output()
