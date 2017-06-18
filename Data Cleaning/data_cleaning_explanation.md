## Capstone Project 1 - Data Wrangling

### The Data

I chose to work with 3 datasets compiled from box scores and NBA API feeds from the 2016-2017 NBA Season. The data was obtained from a website specializing in providing this type of sports data in csv and Excel files. At first glance the data seemed to be in decent shape, and a first pass at wrangling the 3 files went fairly quickly. The 3 datasets are as follows:
        
1. 'box_Score_Team_Stats.xlsx' - 2460 rows, 40 columns. 2 rows per game, 1 for the home team and one for away team. Typical NBA box score data fills out the rest of the file.
        
2. 'Player_BoxScore_Dataset.xlsx' - 26137 rows, and 23 columns. This file contains a variable number of rows per game depending on how many players entered the game (and thus generated stats), 15-24 rows total per game. Typical NBA box score data makes up the rest of this file.
        
3. 'combined-stats.csv' - 603493 rows, 44 columns. The most interesting file, at least at first glance. Many, many rows per game, each one representing a play that could be recorded as a stat. Some examples of these plays would be 'foul', 'layup', 'steal', 'assist', etc. This file also contains many other variables recorded for each play including the players that are on the court at the applicable time, the players involved in the play, shot distance from the basket, time data that shows when during the game the play took place, and court coordinate data that allows mapping where the play took place on a virtual court. 
        
### Data Cleaning

Files 1 and 2 were mostly in good shape. I did remove the 'DATASET' descriptor column as it merely identified the dataset and provided no other useful information. I also converted the 'DATE' column to a datetime object. I checked the datatypes of my other columns and they were appropriately identified by pandas as strings, ints, or floats so no other changes were necessary at this time.

File 3 had some issues when first read into pandas. The datatypes were all over the place and for my eventual project I knew I needed to make a few other changes. I'll list the steps I took to get the data into a manageable place to begin my analysis.

1. 'remaining_time', 'elapsed', and 'play_length' columns charted where in the course of the game, and shot clock, a play took place. To be able to analyze these metrics I needed to convert them all to the same scale - I chose seconds. Pandas read the columns initially as strings, so I used built-in Python packages 'time' and 'datetime' to convert to datetime and then convert that object to seconds. There were a few other wrinkles here, the full process is documented in the notebooks attached to this repository.

2. Next I noticed many of the columns that should hold numbers were imported as strings. This was due to a few instances of 'unknown' mixed into the columns. I replaced 'unknown' with NaN's and converted these columns to int's or float's as appropriate. 

3. I dropped the 'data_set' column again as it was useless.

4. 'game_id' is a unique identifier for each game that I will likely need to utilize during my project. It was unfortunately imported as a string of the Excel formula that created it. An example entry for this column was ' "=21600001" '. I removed the extra quotation marks and the equals sign and recast as int.

5. Changed the 'date' column to a datetime object.

I exported the 3 datasets to new csv's and reimported to test that the changes were all successful. With these changes I am ready to begin the analysis phase of the project.
