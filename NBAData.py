import pandas as pd

# Load the NBA dataset
file_path = r"C:\Users\mahlo\OneDrive\Documents\NBA_MVP\NBA_Dataset.csv"
nba_data = pd.read_csv(file_path)

# Print column names
print("Column names in the dataset:")
print(nba_data.columns)

# Adjust the grouping for individual player statistics
player_comparison = nba_data.groupby('player').mean()

# Print the results
print("\nPlayer-wise comparison of statistics:")
print(player_comparison[['pts_per_g', 'ast_per_g', 'trb_per_g']])

# Continue with the analysis
# 1. Player with the highest career points per game
highest_ppg_player = nba_data.loc[nba_data['pts_per_g'].idxmax()]

# 2. Team with the most total championships since 1981
team_championships = nba_data.groupby('team_id')['team_id'].count()
most_championships_team = team_championships.idxmax()

# 3. Player with the highest Player Efficiency Rating (PER) in a single season
highest_per_player = nba_data.loc[nba_data['per'].idxmax()]

# 4. Comparison of statistics between different eras
era_comparison = nba_data.groupby('season').mean()

# Print the results
print(f"1. Player with the highest career points per game: {highest_ppg_player['player']} with {highest_ppg_player['pts_per_g']} points per game.")
print(f"2. Team with the most total championships since 1981: {most_championships_team}.")
print(f"3. Player with the highest PER in a single season: {highest_per_player['player']} with a PER of {highest_per_player['per']}.")
print("\n4. Comparison of statistics between different eras:")
print(era_comparison[['pts_per_g', 'ast_per_g', 'trb_per_g']])

