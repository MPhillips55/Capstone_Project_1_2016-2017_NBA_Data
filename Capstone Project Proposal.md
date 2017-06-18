# Capstone Project 1 Proposal
## 2016-2017 NBA Season Data

Successful strategies in the NBA morph over time as teams adjust to rule changes that are often subtle, but can have a dramatic impact on the most efficient way to play the game. Currently, there are some hallmarks of the teams that consistently win - playing at a fast pace, spreading the floor with four or five players capable of knocking down 3-point shots, and defensive schemes formulated around long, fast players that cover each other's weaknesses. 

Sports analytics is fascinating to me. The whole Moneyball phenomena has entered pop culture, but underneath the hype, sports analytics appears to be here to stay and for good reason. These developing techniques have had profound impacts on everything from salary cap management to the prevalance of the 3-point shot in the NBA and I expect in the years to come using them effectively will become necessary to even field a team capable of winning.

### 1. What is the problem you want to solve?

> Winning and losing is paramount in pro sports. Jobs are on the line every day, from individual players to executives who shape strategy and build teams. Identifying exactly what sets the winning teams apart from the losing teams and providing concrete examples of what needs to change could impact an organization at every level. Based on results, you could tell an individual player to shoot more corner 3's, change the team's defensive scheme to guard against the pick-and-roll in different ways, provide the coach with information that could help design higher-percentage plays, and assist the executives with finding players that fit the new model.  

### 2. Who is your client and why do they care about this problem?

> I envision my client being a team General Manager who is responsible for building a team and working with the coach to decide which strategies to pursue. As mentioned, winning or losing is paramount to these people keeping their job.

### 3. What data are you going to use?

> I selected three datasets obtained from an NBA data warehousing site affiliated with the well-known NBAstuffer.com. This site has provided analytics to the general public for over a decade and recently began selling their data to interested parties. Using a student discount the data was obtained for a reasonable price and is provided in nicely-formatted csv files.

> The three datasets encompass the 2016-2017 NBA season and include full team and player box scores for every game, as well as play-by-play data for every game including shot coordinates that allow mapping of shot charts.

### 4. In brief, outline your approach to solving this problem?

> My preliminary plan is to focus on a few key areas: game pace by team, shot choice efficiency by player, team, and league-wide, assist rate per shot attempt at a team level, and rebounding/steal rates by team. 

> I will compile these metrics and combine them with the win or loss information associated with that team and game. By feeding this information to machine learning algorithms (initially random forest and k-means clustering, with further investigation as necessary) a minimum baseline to achieve success should be outlined. I also plan to experiment with PCA to see if the algorithm will decide on different metrics to predict success then the ones that I have picked.

### 5. What are your deliverables?

> I plan on delivering project code, a series of slides explaining what the system does, an explanation of why this is important to the stakeholders, and a working model that can take in stats, from a real game or hypothetical, and predict whether the team should have won or lost. 

> The ability to deal with hypotheticals is important because the team can test how much change in a certain direction is needed to improve performance as well.




