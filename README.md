# NBA MVP Prediction

## Overview  
This project focuses on analyzing and predicting NBA MVP candidates based on player statistics and team performance. It includes data analysis techniques to identify top performers and trends over different eras.

## Project Structure  
nba-mvp-prediction/  
├── data/                     # Directory for datasets  
│   └── NBA_Dataset.csv       # NBA dataset used for the analysis  
├── src/                      # Source code directory  
│   └── mvp_prediction.py      # Main script for MVP prediction  
├── requirements.txt          # Dependencies required for the project  
├── README.md                 # Project description and instructions  
└── .gitignore                # Files to ignore (e.g., __pycache__/, .DS_Store)  

## Dataset  
The dataset used for this project contains various statistics for NBA players, including points per game, assists per game, rebounds per game, and Player Efficiency Rating (PER). The data is stored in the `data/NBA_Dataset.csv` file.

**Columns:**  
- `player`: The name of the player.  
- `pts_per_g`: Points scored per game.  
- `ast_per_g`: Assists per game.  
- `trb_per_g`: Rebounds per game.  
- `per`: Player Efficiency Rating.  
- `team_id`: Identifier for the team.

## Getting Started  

### Prerequisites  
- Python 3.7 or higher  
- The following Python libraries:  
  - pandas  

### Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/yourusername/nba-mvp-prediction.git  
   cd nba-mvp-prediction  
2.  Install the required packages:
bash
pip install -r requirements.txt

3.  Place the NBA_Dataset.csv file in the data/ directory.
### Running the Script
1  Navigate to the src/ directory:
bash
Copy code
cd src  
2.  Run the mvp_prediction.py script:
bash
Copy code
python mvp_prediction.py  

This script will perform the following steps:
Load and analyze the NBA dataset.
Compare player statistics and identify top performers.
Provide insights on MVP candidates and team championships.
### Current Status
The current version includes basic analysis with player statistics comparisons.
Future improvements may include implementing predictive models and expanding data analysis.

### Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for suggestions.

### License
This project is licensed under the MIT License. See the LICENSE file for details.
