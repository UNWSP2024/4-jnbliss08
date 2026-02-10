# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many
# tickets are desired for each movie.
# At the end of the program it prints out the total number of tickets desired by the user.
# Use either a "for loop" or "while loop" to accomplish this.
total_tickets = 0
movies = ['Cars', 'Tron', 'Star Wars', 'Lord of the Rings', 'Black Hawk Down']
for movie in movies:
    tickets = int(input(f'how many tickets do you want for {movie}? '))
    while tickets < 0: 
        tickets = int(input('Error please enter a positive number: '))    
    total_tickets += tickets

print(f'you want {total_tickets} tickets')