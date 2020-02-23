#P1: Probability of winning of player with rating2
# P2: Probability of winning of player with rating1.

# P1 = (1.0 / (1.0 + pow(10, ((rating1 – rating2) / 400))));
# P2 = (1.0 / (1.0 + pow(10, ((rating2 – rating1) / 400))));
# Obviously, P1 + P2 = 1.



#rating1 = rating1 + K*(Actual Score – Expected score);

# Suppose there is a live match on chess.com between two players
# rating1 = 1200, rating2 = 1000;
# P1 = (1.0 / (1.0 + pow(10, ((1000-1200) / 400)))) = 0.76
# P2 = (1.0 / (1.0 + pow(10, ((1200-1000) / 400)))) = 0.24

# And Assume constant K=30;

# CASE-1 : Suppose Player 1 wins:
# rating1 = rating1 + k*(actual – expected) = 1200+30(1 – 0.76) = 1207.2;
# rating2 = rating2 + k*(actual – expected) = 1000+30(0 – 0.24) = 992.8;

# Case-2 : Suppose Player 2 wins:
# rating1 = rating1 + k*(actual – expected) = 1200+30(0 – 0.76) = 1177.2;
# rating2 = rating2 + k*(actual – expected) = 1000+30(1 – 0.24) = 1022.8;



# Python 3 program for Elo Rating 
import math 
  
# Function to calculate the Probability 
def Probability(rating1, rating2): 
  
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400)) 
  
  
# Function to calculate Elo rating 
# K is a constant. 
# d determines whether 
# Player A wins or Player B.  
def EloRating(Ra, Rb, K, d): 
   
  
    # To calculate the Winning 
    # Probability of Player B 
    Pb = Probability(Ra, Rb) 
  
    # To calculate the Winning 
    # Probability of Player A 
    Pa = Probability(Rb, Ra) 
  
    # Case -1 When Player A wins 
    # Updating the Elo Ratings 
    if (d == 1) : 
        Ra = Ra + K * (1 - Pa) 
        Rb = Rb + K * (0 - Pb) 
      
  
    # Case -2 When Player B wins 
    # Updating the Elo Ratings 
    else : 
        Ra = Ra + K * (0 - Pa) 
        Rb = Rb + K * (1 - Pb) 
      
  
    print("Updated Ratings:-") 
    print("Ra =", round(Ra, 6)," Rb =", round(Rb, 6)) 
  
# Driver code 
  
# Ra and Rb are current ELO ratings 
Ra = 1200
Rb = 1000
K = 30
d = 1
EloRating(Ra, Rb, K, d) 

