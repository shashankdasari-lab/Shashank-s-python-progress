#wap to ask the user to enter names of their 3 movies and store them in a list 
movie=[]
m=str(input("Enter your first favorite movie:"))
movie.append(m)
m=str(input("Enter your second favorite movie:"))
movie.append(m)
m=str(input("Enter your third favorite movie:"))
movie.append(m)

print(movie)
print(type(movie))
