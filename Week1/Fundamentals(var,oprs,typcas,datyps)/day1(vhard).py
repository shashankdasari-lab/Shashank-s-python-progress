#ESPORTS PLAYER PERFORMANCE report 

print("\nESPORTS PLAYER PERFORMANCE TRACKER \n")

print("\nPlayer Information\n")
ply_name=str(input("Enter Player Name:"))
team_name=str(input("Enter Team Name:"))
game_name=str(input("Enter Game Name:"))

print("\nPlayer Statistics\n")
kills=int(input("Enter total kills:"))
total_assist=int(input("Enter Total Assists:"))
total_deaths=int(input("Enter Total Deaths:"))
total_headshots=int(input("Enter Total Headshot kills :"))

print("\nMATCH STATISTICS\n")
mts_pld=int(input("Enter Total Matches Played:"))
mts_won=int(input("Enter Total Matches Won:"))
mts_lost=int(input("Enter Total Matches lost:"))

print("\n\nFINANCIAL DETAILS")
tour_ear=int(input("Enter tournament earnings:"))
streaming_earnings=int(input("enter Streaming earnings:"))
sponsorship_ear=int(input("enter Sponsorship earnings:"))

win_percentage=mts_won/mts_pld*100
head_per=total_headshots/kills*100

#output 
print("\nFINAL REPORT\n")
print("\nPLAYER INFORMATION\n")
print("Player Name:",ply_name)
print("Team Name:",team_name)
print("Game Name:",game_name)


print("\nCOMBAT STATISTICS\n")
print("Kill death assist ratio:",kills+total_assist/total_deaths)
print("Win Percentage:",mts_won/mts_pld*100)
print("Average Kills:",kills/mts_pld)
print("Average Assist:",total_assist/mts_pld)
print("Headshot Percentage:",head_per)

print("\nCOMPARSION ANALYSIS\n")

print("IS total kills greater than total deaths:",kills>total_deaths)
print("Is win percentage greater than 50:",win_percentage>50)
print("Is headshot percentage greater than 40",head_per>40)
print("Are Tournament Earnings greater than Streaming Earnings:",tour_ear>streaming_earnings)

print("\nOTHER STATISTICS\n")

print("(Kills > Deaths) and (Win Percentage > 50):",kills>total_deaths and win_percentage>50)
print("(Tournament Earnings > 100000) or (Sponsorship Earnings > 50000):",tour_ear>100000 or sponsorship_ear>50000)

print("\nFINANCIAL ANALSYS\n")
print("Total Earnings: ",streaming_earnings+tour_ear+sponsorship_ear)
print("Average earnings per match:",streaming_earnings+tour_ear+sponsorship_ear/mts_pld)








