my_list = []

for loop in range(3):
  if loop == 0:
    songTrack = input("CD name? ")
    my_list.append(songTrack)
    print("\n")
    
  else:
    name = input("What is the song name? ")
    start = input("Start time:")
    end = input("End time:")
    my_list.append([name, start, end])
    print("\n")
    
songnum = int(input("What song number? "))
print("\n")

print ("The title of song is " + my_list[songnum][0], "and it starts at " + my_list[songnum][1] + " and ends at " + my_list[songnum][2])
    