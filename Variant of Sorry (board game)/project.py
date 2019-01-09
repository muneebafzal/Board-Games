
# BEFORE READING THE CODE. read READ ME.



import random

fp = open('mainboard.csv', 'r')

header = fp.readline()
header = header.strip().split(',')
board = []

for i in fp:
    line = i.strip()
    line = line.split(',')

    rowdict = {}

    # add coordinates to CSV file
    for i in range(len(header)):
        key = header[i]
        value = line[i]
        rowdict[key] = value
    rowdict['Occupants'] = []

    board.append(rowdict)

fp.close()
# print(board)
################
#Making Yellow's Homeboard
fp = open('yellowhome.csv', 'r')

header = fp.readline()
header = header.strip().split(',')
yellow_home_board = []

for i in fp:0
    line = line.split(',')

    rowdict = {}

    for i in range(len(header)):
        key = header[i]
        value = line[i]
        rowdict[key] = value
    yellow_home_board.append(rowdict)

fp.close()
for rowdict in yellow_home_board:
    rowdict['HomeOccupants'] = []
############################
# Green home board
fp = open('greenhome.csv', 'r')

header = fp.readline()
header = header.strip().split(',')
green_home_board = []

for i in fp:
    line = i.strip()
    line = line.split(',')

    rowdict = {}

    for i in range(len(header)):
        key = header[i]
        value = line[i]
        rowdict[key] = value
    green_home_board.append(rowdict)

fp.close()
for rowdict in green_home_board:
    rowdict['HomeOccupants'] = []


##################################
# Red home board
fp = open('redhome.csv', 'r')

header = fp.readline()
header = header.strip().split(',')
red_home_board = []

for i in fp:
    line = i.strip()
    line = line.split(',')

    rowdict = {}

    for i in range(len(header)):
        key = header[i]
        value = line[i]
        rowdict[key] = value
    red_home_board.append(rowdict)

fp.close()
for rowdict in red_home_board:
    rowdict['HomeOccupants'] = []
# ############################################

# Blue home board
fp = open('bluehome.csv', 'r')

header = fp.readline()
header = header.strip().split(',')
blue_home_board = []

for i in fp:
    line = i.strip()
    line = line.split(',')

    rowdict = {}

    for i in range(len(header)):
        key = header[i]
        value = line[i]
        rowdict[key] = value
    blue_home_board.append(rowdict)

fp.close()
for rowdict in blue_home_board:
    rowdict['HomeOccupants'] = []

# Since the Occupants list contain objects, we have created  functions to print the name attributes of the objects in order
# to locate the objects
########################################################
# for printing the particular home boards.
def print_home_board(board):
    lis = []
    for i in board:
        s = []
        if i['HomeOccupants'] != 0:
            for element in i['HomeOccupants']:
                s.append(element.name)
        var1= 'Position: '+ i['position']
        var2 = 'HomeOccupants: ' + str(s)
        listt = [var1,var2]
        lis.append(listt)
    print(lis)

# for the printing of the BIG board
def print_board():
    lis = []
    for i in board:
        s = []
        if i['Occupants'] != 0:
            for element in i['Occupants']:
                s.append(element.name)
        var1= 'Position: '+ i['position']
        var2 = 'Occupants: ' + str(s)
        listt = [var1,var2]
        lis.append(listt)
    print(lis)
# print('Greens Home board:')
# print_home_board(green_home_board)
# Creating a class of player that can be used as an object for various players
class Player:
    def __init__(self,name,token_type):
        self.name = name
        # token_type attribute is used later to implement the kiling of the token. We use the fact that if the token type is the same for two tokens, then they
        #can not kill each other and the token that comes afterwards is just added to occupants list. Otherwise, the previous occupants is killed(sent to yardlist)
        self.token_type = token_type
        # yard_list attribute is used along with self.in_the_baord boolean attribute( which tell u if the token is in the board, if a token is not in the board it is either in
        # home_list or yard_list
        self.yard_list = []

        # home_list is used to decide the winner. If its length is 4 the players wins. and when this self.active is set equal to False and the player is no longer active.
        self.home_list = []
        self.active = True



class Token:

    def __init__(self, name,player):
        self.name = name

        # player is the object instantiated from the player class. So we will be able to use all the attricute of the Player class.
        self.player = player
        # self.in_the_baord boolean attribute( which tell u if the token is in the board, if a token is not in the board it is either in
        # home_list or yard_list

        self.in_the_board = False

        # this attribute is set to the list of dictionaries of either the mainboard or the home_boards.
        self.location = 'Yard'

    ################## Processing things
    # def make(self, x, y):
    #     ellipseMode(RADIUS)
    #     fill(0,0,0)
    #     ellipse(x+20, y+20, 7, 7)


        # processing only!
###################################################
    def come_in_the_board(self):
        # whenever 6 comes, we use this method
        # Setting the the starting position for each player according to the
        # indexing of the board

        # We will set the loops in such a way that whenever 6 comes and the player want to get a new token in into the baord
        #this method is callled.


        # see the picture 2. attached.
        if self.player == yellow_player:
            z = 0
        if self.player == green_player:
            z = 13
        if self.player == red_player:
            z =26
        if self.player == blue_player:
            z = 39

        # this can only happen if the token is in the Yardlist
        self.in_the_board = False
        for i in self.player.yard_list:
            if i == self:
                self.in_the_board = True
        # setting it True so that token can come in the board

        for i in self.player.home_list:
            if i == self:
                self.in_the_board = False

        if not self.in_the_board:
            print('this token is not on the yardlist')

        if self.in_the_board:
            self.player.yard_list.remove(self)#remove the object(itself) from the yard_list
            self.location = board[z] # getting the approriate indexed dictionary on the baord
            self.location['Occupants'].append(self)
        # Here location is a dictionary inside the board. We use this extensively in the code for updating the baord at various situations

    def move(self, board, spaces):
        '''moves a particular token of the player number of spaces on the given board'''
        # the below thing is done to make the boolean of in_the_board false after
        # sending a token in the yard.
        ############################3
        # print_yard_list(self.player)
        # print('testing')
        # print(self.player.yard_list)
        # print(self)
        # print(self.in_the_board)
        # print(self.name)
        # print(self)
        # printed things for testing
        ########################
        for i in self.player.yard_list:
            if i == self:
                self.in_the_board = False

        for i in self.player.home_list:
            if i == self:
                self.in_the_board = False
        # print(self.in_the_board)

#############################################################
        # NO IDEA why  THE BELOW thing ooes not work
        # if self in (self.player.yard_list):
        #     print('why are u running?')
        #     self.in_the_board = False
        # if self in self.player.home_list:
        #     self.in_the_board = False

        # print(self.in_the_board)
        # print_yard_list(self.player)
#######################################################################
        if not self.in_the_board:
            print("Sorry. You can't move this. This token is not on the board.")
        #######might want sth here

        else:

            # BASIC MOVEMENT

            now = self.location
            original_position = int(self.location['position'])

            n = (int(now['position']) + spaces) % len(board) # n is the new index where the token will go.
##############################################################
            # Implementing the home row thing for YELLOW.
            # these position are used for transition from main baord to respective home baord
            # SEE PICTURE 2( in the main folder) with indexed board for more clarity
            initial_position_conditions_yellow = original_position >= 46
            final_position_condition_yellow = n == 51 or n >= 0
###################################################
            # Initial position conditions for green
            initial_position_conditions_green = original_position >= 7 and original_position <= 11
            final_position_condition_green = n >= 12
##############################################################
            # Initial position conditions for red
            initial_position_conditions_red = original_position >= 20 and original_position <= 24
            final_position_condition_red = n >= 25
####################################################################################
            # Initial position conditions for blue
            initial_position_conditions_blue = original_position >= 33 and original_position <= 37
            final_position_condition_blue = n >= 38

#####################################################################################
            ##########YELLOW PLAYER CONDITIONS#################
            # Transition from big board to the individual YELLOW home board....
            if self.player == yellow_player and initial_position_conditions_yellow and final_position_condition_yellow:
                if self in self.location['Occupants']:
                    self.location['Occupants'].remove(self)

                new_position_in_home_row = original_position + spaces -50


                # After this the self.location will always point towards the yellow_home_row
                self.location = yellow_home_board[new_position_in_home_row-1]
                # appending the token(object) in the new location..inside the yellow_home_board
                self.location['HomeOccupants'].append(self)

            # If the token is ALREADY in the yellow_home_board
            # the RULE is this IF the token GETS PAST the index 6, then token gets into the homelist.

            elif self.location in yellow_home_board:

                # this means the token is OUT of the board. It has REACHED the home.
                # removing the old object from the Occupants list.
                self.location['HomeOccupants'].remove(self)
                n = (int(self.location['position']) + spaces)
                # not sure about n-1
                self.location = yellow_home_board[n-1]
                self.location['HomeOccupants'].append(self)

                if int(self.location['position']) >= 6:

                    print('this token is going to the homelist')
                    self.in_the_board = False
                    if not self.in_the_board:
                        print('I am no longer in the game.')
                    self.player.home_list.append(self)


            #################################################
            ##########GREEN PLAYER CONDITIONS#################
            # Transition from big board to the individual GREEN home board....
            elif self.player == green_player and initial_position_conditions_green and final_position_condition_green:
                if self in self.location['Occupants']:
                    self.location['Occupants'].remove(self)
                #Could have done with spaces new_poisitio = 46 + spaces -50
                new_position_in_home_row = original_position + spaces -11

                # After this the self.location will always point towards the green_home_board
                self.location = green_home_board[new_position_in_home_row-1]
                # appending the token(object) in the new location..inside the green_home_board
                self.location['HomeOccupants'].append(self)

            # If the token is ALREADY in the green_home_board
            # the RULE is this IF the token GETS PAST the index 6

            elif self.location in green_home_board:

                # removing the old object from the Occupants list.
                self.location['HomeOccupants'].remove(self)
                # this means the token is OUT of the board. It has REACHED the home.
                n = (int(self.location['position']) + spaces)
                # not sure about n-1
                self.location = green_home_board[n-1]
                self.location['HomeOccupants'].append(self)

                if int(self.location['position']) >= 6:
                    # as long as the token is in a position greater than or equal to 6, it means it is in its home.

                    print('this token is going to the homelist')
                    self.in_the_board = False
                    if not self.in_the_board:
                        print('I am no longer in the game.')
                    self.player.home_list.append(self)






            #################################################
            ########## RED PLAYER CONDITIONS################# REMAINING
            # Transition from big board to the individual RED home board....
            elif self.player == red_player and initial_position_conditions_red and final_position_condition_red:
                if self in self.location['Occupants']:
                    self.location['Occupants'].remove(self)
                #Could have done with spaces new_poisitio = 46 + spaces -50
                new_position_in_home_row = original_position + spaces - 24

                # After this the self.location will always point towards the red_home_board
                self.location = red_home_board[new_position_in_home_row-1]
                # appending the token(object) in the new location..inside the red_home_board
                self.location['HomeOccupants'].append(self)

            # If the token is ALREADY in the red_home_board
            # the RULE is this IF the token GETS PAST the index 6

            elif self.location in red_home_board:

                # removing the old object from the Occupants list.
                self.location['HomeOccupants'].remove(self)
                # this means the token is OUT of the board. It has REACHED the home.
                n = (int(self.location['position']) + spaces)
                # not sure about n-1
                self.location = red_home_board[n-1]
                self.location['HomeOccupants'].append(self)

                if int(self.location['position']) >= 6:
                    # as long as the token is in a position greater than or equal to 6, it means it is in its home.
                    print('this token is going to the homelist')
                    self.in_the_board = False
                    if not self.in_the_board:
                        print('I am no longer in the game.')
                    self.player.home_list.append(self)

            #################################################
            ########## BLUE PLAYER CONDITIONS################# REMAINING
            # Transition from big board to the individual RED home board....
            elif self.player == blue_player and initial_position_conditions_blue and final_position_condition_blue:
                if self in self.location['Occupants']:
                    self.location['Occupants'].remove(self)
                #Could have done with spaces new_poisitio = 46 + spaces -50
                new_position_in_home_row = original_position + spaces - 37

                # After this the self.location will always point towards the blue_home_board
                self.location = blue_home_board[new_position_in_home_row-1]
                # appending the token(object) in the new location..inside the blue_home_board
                self.location['HomeOccupants'].append(self)

            # If the token is ALREADY in the blue_home_board
            # the RULE is this IF the token GETS PAST the index 6

            elif self.location in blue_home_board:

                # removing the old object from the Occupants list.
                self.location['HomeOccupants'].remove(self)
                # this means the token is OUT of the board. It has REACHED the home.
                n = (int(self.location['position']) + spaces)
                # not sure about n-1
                self.location = blue_home_board[n-1]
                self.location['HomeOccupants'].append(self)

                if int(self.location['position']) >= 6:
                    # as long as the token is in a position greater than or equal to 6, it means it is in its home.
                    print('this token is going to the homelist')
                    self.in_the_board = False
                    if not self.in_the_board:
                        print('I am no longer in the game.')
                    self.player.home_list.append(self)

#############################################################################################################################

            # ELSE:
            # else put the normal movement without the home board thing  in the ELSE statement

            else:
                if self in self.location['Occupants']:
                    self.location['Occupants'].remove(self)



                self.location = board[n] # now we reach the new box where the token reaches.

                # NOW ACCOMODATING THE CONDITION FOR THE KILLING OF THE TOKEN
                if len(self.location['Occupants']) != 0:# i.e if the boxes are not vacant, tnen no n
                    if (n == 0 or n == 13 or n == 26 or n == 39):# killing can not be done on these boxes
                        self.location['Occupants'].append(self)


                    else:

                        original_list = self.location['Occupants']
                        original_list_type_wise = []
                        for obj in original_list:
                            s = obj.player.token_type
                            original_list_type_wise.append(s)

                        new_token_list = []
                        # Here we check if the occupants are of the same type..if e.g [r1,r2] then we will simply append the 3rd token..so it'll become [r1,r2,r3]
                        # if we have [b1,b2] then new result will be [r3]..and b1,b2 go to their yard_list.
                        for j in set(original_list_type_wise):


                            if j == self.player.token_type:


                                break
                            else:
                                # sending the killed token(s) to their yard list

                                if j == 'y':
                                    # other_player = yellow_player
                                    yellow_player.yard_list = yellow_player.yard_list + original_list

                                if j == 'g':
                                    # other_player = green_player
                                    green_player.yard_list = green_player.yard_list + original_list
                                if j == 'r':
                                    # other_player = red_player
                                    red_player.yard_list = red_player.yard_list + original_list
                                if j == 'b':
                                    # other_player = blue_player
                                    blue_player.yard_list = blue_player.yard_list + original_list


                                # emptying the list
                                self.location['Occupants'] = []

                                # print('i shouldnt be here')

                # when the box is vacant then just append it
                else:
                    self.location['Occupants'].append(self)




# initializing the players
yellow_player = Player('Yellow_Player','y')
green_player = Player('Green_Player','g')
red_player = Player('Red_Player','r')
blue_player = Player('Blue_Player','b')

# initializing all the 16 tokens
# Yellow tokens
y1 = Token('y1',yellow_player)
y2 = Token('y2',yellow_player)
y3 = Token('y3',yellow_player)
y4 = Token('y4',yellow_player)
yellow_tokens_list = [y1,y2,y3,y4]
# Green tokens
g1 = Token('g1',green_player)
g2 = Token('g2',green_player)
g3 = Token('g3',green_player)
g4 = Token('g4',green_player)
green_tokens_list = [g1,g2,g3,g4]
# Red tokens
r1 = Token('r1',red_player)
r2 = Token('r2',red_player)
r3 = Token('r3',red_player)
r4 = Token('r4',red_player)
red_tokens_list = [r1,r2,r3,r4]
# Blue tokens
b1 = Token('b1',blue_player)
b2 = Token('b2',blue_player)
b3 = Token('b3',blue_player)
b4 = Token('b4',blue_player)
blue_tokens_list = [b1,b2,b3,b4]

#Putting the token objects inside the player Class yard_list
for object in yellow_tokens_list:
    yellow_player.yard_list.append(object)
for object in green_tokens_list:
    green_player.yard_list.append(object)
for object in red_tokens_list:
    red_player.yard_list.append(object)
for object in blue_tokens_list:
    blue_player.yard_list.append(object)




##############################################################
## Initializing the token manually for testing

# g1.in_the_board = True
# g1.come_in_the_board()
# g2.in_the_board = True
#
# g2.come_in_the_board()
# y1.come_in_the_board()
# y1.in_the_board = True
#
# r1.come_in_the_board()
# r2.come_in_the_board()

# b1.come_in_the_board()
# b2.come_in_the_board()
# b3.come_in_the_board()
# b4.come_in_the_board()

#########################################################################


######################################################33


def print_yard_list(x):
    l = []
    for obj in x.yard_list:

        l.append(obj.name)
    print(l)

def print_home_list(x):
    l = []
    for obj in x.home_list:

        l.append(obj.name)
    print(l)

# printing yellow yard list for testing
# print('Yellows players yarlist')
# print_yard_list(yellow_player)
# # printing green yard_list for testing
# print('Greens Players yardlist')
# print_yard_list(green_player)
#
# # printing board that shows the names of the objects


turn_counter = 0

print('LET THE GAME BEGIN!!')
print('Printing the big board:')
print_board()
print()
print()

print('PRINTING ALL THE HOME BOARDS')
print('Printing yellows home board:')
print_home_board(yellow_home_board)
print('Printing Greens home board:')
print_home_board(green_home_board)
print('Printing reds home board:')
print_home_board(red_home_board)
print('Printing blues home board:')
print_home_board(blue_home_board)

print()
print()
print('PRINTING ALL THE YARDLISTS: ')
print('Yellows yardlist:')
print_yard_list(yellow_player)
print('Greens yardlist:')
print_yard_list(green_player)
print('Reds yardlist:')
print_yard_list(red_player)
print('Blues yardlist:')
print_yard_list(blue_player)
print()
print()
print('PRINTING ALL HOME LISTS: ')
print('Yellows homelist:')
print_home_list(yellow_player)
print('Greens homelist:')
print_home_list(green_player)
print('Reds homelist:')
print_home_list(red_player)
print('Blues homelist:')
print_home_list(blue_player)
print()

print(100*'-')
while True:
    ######################YELLOW PLAYER##########################################################


    if turn_counter%4 == 0:
        # if a player has won, he is no longer active. so he won't get any turn.
        if not yellow_player.active:

            break
    # Yellow Player's Turn
        print("Yellow Player's turn: ")
        roll_dice = int(input('To roll your dice please enter 0'))
        if roll_dice == 0:
            die = random.randint(1, 6)
            # die = 6
            print('You rolled', die)
            if die == 6:
                print('You rolled 6. You can only take your token(if any)out of the yardlist. ')
                print('Which token you want to take out?')
                token_choice = int(input('Which token you want to take out of yardlist(press 1,2,3,4)'))
                if token_choice == 1:
                    y1.come_in_the_board()
                if token_choice == 2:
                    y2.come_in_the_board()
                if token_choice == 3:
                    y3.come_in_the_board()
                if token_choice == 4:
                    y4.come_in_the_board()
            else:
                token_choice = int(input('Which token you want to move(press 1,2,3,4)'))
                if token_choice == 1:
                    y1.move(board,die)
                if token_choice == 2:
                    y2.move(board,die)
                if token_choice == 3:
                    y3.move(board,die)
                if token_choice == 4:
                    y4.move(board,die)
            print('Printing the big board:')
            print_board()
            print()
            print()

            print('PRINTING ALL THE HOME BOARDS')
            print('Printing yellows home board:')
            print_home_board(yellow_home_board)
            print('Printing Greens home board:')
            print_home_board(green_home_board)
            print('Printing reds home board:')
            print_home_board(red_home_board)
            print('Printing blues home board:')
            print_home_board(blue_home_board)

            print()
            print()
            print('PRINTING ALL THE YARDLISTS: ')
            print('Yellows yardlist:')
            print_yard_list(yellow_player)
            print('Greens yardlist:')
            print_yard_list(green_player)
            print('Reds yardlist:')
            print_yard_list(red_player)
            print('Blues yardlist:')
            print_yard_list(blue_player)
            print()
            print()
            print('PRINTING ALL HOME LISTS: ')
            print('Yellows homelist:')
            print_home_list(yellow_player)
            print('Greens homelist:')
            print_home_list(green_player)
            print('Reds homelist:')
            print_home_list(red_player)
            print('Blues homelist:')
            print_home_list(blue_player)
            print()

            print(100*'-')





            # implementing the WINNING CONDITION for YELLOW
            if len(yellow_player.home_list)==4:
                yellow_player.active = False
    #             print('Yellow Player Wins. Yellow players game is over.')
    if turn_counter%4 == 1:
        # if a player has won, he is no longer active. so he won't get any turn.
        if not green_player.active:

            break
        ##################GREEN PLAyer#####################################################################
        #Green Player's Turn
        print()
        print()
        print("Green Player's turn: ")
        roll_dice = int(input('To roll your dice please enter 0'))
        if roll_dice == 0:
            die = random.randint(1, 6)
            # die = 5
            print('You rolled', die)
            if die == 6:
                print('You rolled 6. You can only take your token(if any)out of the yardlist. ')
                print('Which token you want to take out?')
                token_choice = int(input('Which token you want to take out of yardlist(press 1,2,3,4)'))
                if token_choice == 1:
                    g1.come_in_the_board()
                if token_choice == 2:
                    g2.come_in_the_board()
                if token_choice == 3:
                    g3.come_in_the_board()
                if token_choice == 4:
                    g4.come_in_the_board()
            else:
                token_choice = int(input('Which token you want to move(press 1,2,3,4)'))
                if token_choice == 1:
                    g1.move(board,die)
                if token_choice == 2:
                    g2.move(board,die)
                if token_choice == 3:
                    g3.move(board,die)
                if token_choice == 4:
                    g4.move(board,die)
            print('Printing the big board:')
            print_board()
            print()
            print()

            print('PRINTING ALL THE HOME BOARDS')
            print('Printing yellows home board:')
            print_home_board(yellow_home_board)
            print('Printing Greens home board:')
            print_home_board(green_home_board)
            print('Printing reds home board:')
            print_home_board(red_home_board)
            print('Printing blues home board:')
            print_home_board(blue_home_board)

            print()
            print()
            print('PRINTING ALL THE YARDLISTS: ')
            print('Yellows yardlist:')
            print_yard_list(yellow_player)
            print('Greens yardlist:')
            print_yard_list(green_player)
            print('Reds yardlist:')
            print_yard_list(red_player)
            print('Blues yardlist:')
            print_yard_list(blue_player)
            print()
            print()
            print('PRINTING ALL HOME LISTS: ')
            print('Yellows homelist:')
            print_home_list(yellow_player)
            print('Greens homelist:')
            print_home_list(green_player)
            print('Reds homelist:')
            print_home_list(red_player)
            print('Blues homelist:')
            print_home_list(blue_player)
            print()

            print(100*'-')

            # implementing the WINNING CONDITION for GREEN
            if len(green_player.home_list)==4:
                green_player.active = False
                print('Green Player Wins. Green players game is over.')
                print()
                print()
                #################RED PLAYER#################################################
    if turn_counter%4 == 2:
        # if a player has won, he is no longer active. so he won't get any turn.
        if not red_player.active:

            break

        #Red Player's Turn
        print()
        print()
        print("Red Player's turn: ")
        roll_dice = int(input('To roll your dice please enter 0'))
        if roll_dice == 0:
            die = random.randint(1, 6)
            # die = 6
            print('You rolled', die)
            if die == 6:
                print('You rolled 6. You can only take your token(if any)out of the yardlist. ')
                print('Which token you want to take out?')
                token_choice = int(input('Which token you want to take out of yardlist(press 1,2,3,4)'))
                if token_choice == 1:
                    r1.come_in_the_board()
                if token_choice == 2:
                    r2.come_in_the_board()
                if token_choice == 3:
                    r3.come_in_the_board()
                if token_choice == 4:
                    r4.come_in_the_board()
            else:
                token_choice = int(input('Which token you want to move(press 1,2,3,4)'))
                if token_choice == 1:
                    r1.move(board,die)
                if token_choice == 2:
                    r2.move(board,die)
                if token_choice == 3:
                    r3.move(board,die)
                if token_choice == 4:
                    r4.move(board,die)
            print('Printing the big board:')
            print_board()
            print()
            print()

            print('PRINTING ALL THE HOME BOARDS')
            print('Printing yellows home board:')
            print_home_board(yellow_home_board)
            print('Printing Greens home board:')
            print_home_board(green_home_board)
            print('Printing reds home board:')
            print_home_board(red_home_board)
            print('Printing blues home board:')
            print_home_board(blue_home_board)

            print()
            print()
            print('PRINTING ALL THE YARDLISTS: ')
            print('Yellows yardlist:')
            print_yard_list(yellow_player)
            print('Greens yardlist:')
            print_yard_list(green_player)
            print('Reds yardlist:')
            print_yard_list(red_player)
            print('Blues yardlist:')
            print_yard_list(blue_player)
            print()
            print()
            print('PRINTING ALL HOME LISTS: ')
            print('Yellows homelist:')
            print_home_list(yellow_player)
            print('Greens homelist:')
            print_home_list(green_player)
            print('Reds homelist:')
            print_home_list(red_player)
            print('Blues homelist:')
            print_home_list(blue_player)
            print()

            print(100*'-')

            # implementing the WINNING CONDITION for RED
            if len(red_player.home_list)==4:
                red_player.active = False
                print('Red Player Wins. Red players game is over.')
                print()
                print()

    ###################################################################################################################
    if turn_counter%4 == 3:
        # if a player has won, he is no longer active. so he won't get any turn.
        if not blue_player.active:

            break

        #Blue Player's Turn
        print()
        print()
        print("Blue Player's turn: ")
        roll_dice = int(input('To roll your dice please enter 0'))
        if roll_dice == 0:
            die = random.randint(1, 6)
            # die = 6
            print('You rolled', die)
            if die == 6:
                print('You rolled 6. You can only take your token(if any)out of the yardlist. ')
                print('Which token you want to take out?')
                token_choice = int(input('Which token you want to take out of yardlist(press 1,2,3,4)'))
                if token_choice == 1:
                    b1.come_in_the_board()
                if token_choice == 2:
                    b2.come_in_the_board()
                if token_choice == 3:
                    b3.come_in_the_board()
                if token_choice == 4:
                    b4.come_in_the_board()

            else:
                token_choice = int(input('Which token you want to move(press 1,2,3,4)'))
                if token_choice == 1:
                    b1.move(board,die)
                if token_choice == 2:
                    b2.move(board,die)
                if token_choice == 3:
                    b3.move(board,die)
                if token_choice == 4:
                    b4.move(board,die)
            print('Printing the big board:')
            print_board()
            print()
            print()

            print('PRINTING ALL THE HOME BOARDS')
            print('Printing yellows home board:')
            print_home_board(yellow_home_board)
            print('Printing Greens home board:')
            print_home_board(green_home_board)
            print('Printing reds home board:')
            print_home_board(red_home_board)
            print('Printing blues home board:')
            print_home_board(blue_home_board)

            print()
            print()
            print('PRINTING ALL THE YARDLISTS: ')
            print('Yellows yardlist:')
            print_yard_list(yellow_player)
            print('Greens yardlist:')
            print_yard_list(green_player)
            print('Reds yardlist:')
            print_yard_list(red_player)
            print('Blues yardlist:')
            print_yard_list(blue_player)
            print()
            print()
            print('PRINTING ALL HOME LISTS: ')
            print('Yellows homelist:')
            print_home_list(yellow_player)
            print('Greens homelist:')
            print_home_list(green_player)
            print('Reds homelist:')
            print_home_list(red_player)
            print('Blues homelist:')
            print_home_list(blue_player)
            print()

            print(100*'-')

            # implementing the WINNING CONDITION for BLUE
            if len(blue_player.home_list)==4:
                blue_player.active = False
                print('Blue Player Wins. Blue players game is over.')
                print()
                print()


    turn_counter += 1

# normally the game just ends when 1 player is left. But theoratically if he keeps playing alone, then he can finish the game.
print('The game is over now that all the 16 tokens have reached their home.')


#################

# def draw():
#     background(255, 255, 255)
#     for b in board:
#         fill(b['r'],b['g'],b['b'])
#         rect(b['x'], b['y'], 40, 40)
#         for o in b['Occupants']:
#             o.make(b['x'], b['y'])

#################