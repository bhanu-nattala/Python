  
import random


#defining our player class
class Player():
    moves = {
        1:'rock',2:'paper',3:'sissor'
    }
    def __init__(self):
        #stores the current move
        self.current_move = None
        #list of competitors for the current user
        self.competitors = []
        #calculate results after all games
        self.reviews = dict([])

    #method for player to make move
    def make_move(self):
        self.current_move = self.moves[random.randint(1,3)];

    #evaluating the player with respect to other player
    def evaluate_player(self, round):
        review = []
        for competitor in self.competitors:
            if self.current_move == 'rock':
                if competitor.current_move == 'paper':
                    review.append('LOST')
                elif competitor.current_move == 'rock':
                    review.append('DRAW')
                else:
                    review.append('WON')
            elif self.current_move == 'paper':
                if competitor.current_move == 'sissor':
                    review.append('LOST')
                elif competitor.current_move == 'paper':
                    review.append('DRAW')
                else:
                    review.append('WON')
            elif self.current_move == 'sissor':
                if competitor.current_move == 'rock':
                    review.append('LOST')
                elif competitor.current_move == 'sissor':
                    review.append('DRAW')
                else:
                    review.append('WON')

        #storing the result of round in reviews dictonary
        self.reviews[round] = review

    #finding the results for all games played
    def generate_report(self, num):
        print(f'RESULT OF PLAYER {num}:')
        for key, item in self.reviews.items():
            print(f"{key} ", end="")
            print(*item)

#initialiazing the player
p1 = Player()
p2 = Player()
p3 = Player()
p4 = Player()

#setting up competitors for each player
p1.competitors = [p2,p3,p4]
p2.competitors = [p1,p3,p4]
p3.competitors = [p1,p2,p4]
p4.competitors = [p1,p2,p3]

for round in range(50):
    #each palyer making a move
    p1.make_move()
    p2.make_move()
    p3.make_move()
    p4.make_move()

    #printing the moves in current round
    print(f"moves round {round}")
    print(f"(player 1 : {p1.current_move}) (player 2 : {p2.current_move}) (player 3 : {p3.current_move}) (player 4 : {p4.current_move})")

    #evaluating each player
    p1.evaluate_player(f'round {round}')
    p2.evaluate_player(f'round {round}')
    p3.evaluate_player(f'round {round}')
    p4.evaluate_player(f'round {round}')

#printing the results after all games
print('\nFINAL RESULTS OF ALL PLAYERS')
p1.generate_report(1)
print('\n')
p2.generate_report(2)
print('\n')
p3.generate_report(3)
print('\n')
p4.generate_report(4)
print('\n')
