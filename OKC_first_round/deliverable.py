import csv
import math

def inc_helper(fgm, shots_attempted, row):
  #Non Corner 3s
  if abs(float(row[2])) > 7.8 and math.sqrt(float(row[1])**2 + float(row[2])**2) >= 23.75:
    shots_attempted[2] += 1
    if row[3] == '1':
      fgm[2] += 1

  #Corner 3s
  elif abs(float(row[2])) <= 7.8 and abs(float(row[1])) >= 22:                       
    shots_attempted[1] += 1
    if row[3] == '1':
      fgm[1] += 1
  
  #2 pts
  else:                                         
    shots_attempted[0] += 1
    if row[3] == '1':
      fgm[0] += 1


def main():
  #indexed as [2 points, Corner 3s, Non Corner 3s] 
  teamA_fgm = [0,0,0]   
  teamB_fgm = [0,0,0]
  teamA_shots_attempted = [0,0,0]
  teamB_shots_attempted = [0,0,0] 
  teamA_total_shots = 0
  teamB_total_shots = 0
  with open('shots_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line = 0
    for row in csv_reader:
      if line == 0:
        line += 1
        continue
      else:
        if row[0] == 'Team A':
          teamA_total_shots += 1
          inc_helper(teamA_fgm, teamA_shots_attempted, row)
        elif row[0] == 'Team B':
          teamB_total_shots += 1
          inc_helper(teamB_fgm, teamB_shots_attempted, row)
  
  
  print(f'Team A\n2PT: (Shot Distribution: {teamA_shots_attempted[0]/teamA_total_shots*100}, eFG: {(teamA_fgm[0] + (0.5*3*2))/teamA_shots_attempted[0]*100})\nC3: (Shot Distribution: {teamA_shots_attempted[1]/teamA_total_shots*100}, eFG: {(teamA_fgm[1] + (0.5*3*3))/teamA_shots_attempted[1]*100})\nNC3: (Shot Distribution: {teamA_shots_attempted[2]/teamA_total_shots*100}, eFG: {(teamA_fgm[2] + (0.5*3*3))/teamA_shots_attempted[2]*100})')

  print(f'Team B\n2PT: (Shot Distribution: {teamB_shots_attempted[0]/teamB_total_shots*100}, eFG: {(teamB_fgm[0] + (0.5*3*2))/teamB_shots_attempted[0]*100})\nC3: (Shot Distribution: {teamB_shots_attempted[1]/teamB_total_shots*100}, eFG: {(teamB_fgm[1] + (0.5*3*3))/teamB_shots_attempted[1]*100})\nNC3: (Shot Distribution: {teamB_shots_attempted[2]/teamB_total_shots*100}, eFG: {(teamB_fgm[2] + (0.5*3*3))/teamB_shots_attempted[2]*100})')

if __name__ == '__main__':
    main()