def main():
  pitching = open("MLB_Pitching.csv", 'r')
  team_data = []

  #get the import info out of pitching and store into team_data

  pitching.close()

  hitting = open("MLB_Hitting.csv", 'r')

  #process all the data in hitting and add to the correct portion of the team_data

  hitting.close()


  outFile = open("mlb_output.csv", 'w')

  #process each line of the team_data and save to the output file.
  output = ""
  outFile.write(output)

  outFile.close()

  import os

# Define file names
hitting_file = "MLB_Hitting.csv"
pitching_file = "MLB_Pitching.csv"
combined_file = "MLB_Combined.csv"

# Step 1: Read hitting data
hitting_data = {}
with open(hitting_file, 'r') as hf:
    # Read the header
    header = hf.readline().strip().split(",")
    # Get indices for relevant columns
    team_index = header.index("Tm")
    runs_per_game_index = header.index("R/G")

    for line in hf:
        row = line.strip().split(",")
        team_name = row[team_index]
        runs_per_game = float(row[runs_per_game_index])  # Runs scored per game
        hitting_data[team_name] = runs_per_game

# Step 2: Read pitching data and combine
combined_data = []
with open(pitching_file, 'r') as pf:
    # Read the header
    header = pf.readline().strip().split(",")
    # Get indices for relevant columns
    team_index = header.index("Tm")
    runs_allowed_per_game_index = header.index("RA/G")
    wins_index = header.index("W")
    losses_index = header.index("L")
    era_index = header.index("ERA")

    for line in pf:
        row = line.strip().split(",")
        team_name = row[team_index]
        if team_name in hitting_data:  # Ensure team exists in hitting data
            runs_allowed_per_game = float(row[runs_allowed_per_game_index])  # Runs allowed per game
            wins = int(row[wins_index])
            losses = int(row[losses_index])
            era = float(row[era_index])

            # Prepare the combined row
            combined_row = [
                team_name,
                hitting_data[team_name],
                runs_allowed_per_game,
                wins,
                losses,
                era
            ]
            combined_data.append(combined_row)

# Step 3: Save the combined data to a new CSV file
with open(combined_file, 'w', newline='') as cf:
    # Write the header
    cf.write("Team Name,Runs Scored Per Game,Runs Allowed Per Game,Wins,Losses,ERA\n")
    for data in combined_data:
        # Join the data list into a comma-separated string and write to the file
        cf.write(",".join(map(str, data)) + "\n")

print(f"Combined data saved to {combined_file}.")


if __name__ == '__main__':
  main()
