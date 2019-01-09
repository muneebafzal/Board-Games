import random
__author__ = 'Muneeb'

fp = open('orgsolarquest.csv', 'r')

header = fp.readline()
header = header.strip().split(',')
board = []

for i in fp:
    line = i.strip()
    line = line.split(',')

    rowdict = {}

    for i in range(len(header)):
        key = header[i]
        value = line[i]
        rowdict[key] = value
    board.append(rowdict)

fp.close()
for rowdict in board:
    rowdict['Fuel_station'] = False
    rowdict['Occupants'] = []
    rowdict['Owner'] = False


# Creating a class of player that can be used as an object for various players
class Player:

    def __init__(self, name, location):
        self.name = name
        self.location = location
        # Here location is a dictionary inside the board. We use this extensively in the code for updating the baord at various situations
        self.money = 1500
        self.fuel = 12
        self.fuel_stations = 3
        #initially, the number of fuel stations available to the player
        self.owned = []
        self.active = True
        self.location['Occupants'].append(self.name)

    def move(self, board, spaces):
        '''moves a player number of spaces on the given board'''
# it also checks if a player is out of the game

        purchase = int(rowdict['purchase'])
        if self.fuel <= spaces:
            property_type = self.location['type'] == 'planet' or self.location['type'] == 'moon'
            eligibility_to_buy_property = self.money >= purchase and property_type
            availability_fuel_station = self.location['Fuel_station']
            if not eligibility_to_buy_property and not availability_fuel_station:
                self.active = False

            return

        # ADVANCE MOVEMENT
        self.location['Occupants'].remove(self.name)
        i = int(self.location['position'])
        for j in range(i+1, i+spaces +1):
            n = self.location['next']
            l = n.split(';')
            if len(l) > 1:
                pos_1 = board[int(l[0])]
                pos_2 = board[int(l[1])]
                pos_1_name = pos_1['name']
                pos_2_name = pos_2['name']
                choose = int(input("Which route you want to go thru?\nPress 1 to go to thru: "+str(pos_1_name) + "\nPress 2 to go to thru: " + str(pos_2_name) ))
                if choose ==1:
                    # self.location['Occupants'].remove(self.name)
                    self.location = pos_1
                    # print('a', self.location['name'])

                if choose ==2:
                    self.location = pos_2
                    # print('b', self.location['name'])
            else:
                self.location = board[int(l[0])]
                # print('c', self.location['name'])

        # BASIC MOVEMENT
        # now = self.location
        # n = (int(now['position']) + spaces) % len(board)
        #
        # self.fuel -= spaces
        # #NOT sure abt this
        # if self.name in self.location['Occupants']:
        #     self.location['Occupants'].remove(self.name)
        #
        # self.location = board[n]
        # self.location['Occupants'].append(self.name)

        self.fuel -= spaces

        self.location['Occupants'].append(self.name)



    def pay_rent(self):
        '''Given a certain location(self.location), it calculates the location's rental amount. That amount is deducted from the players
        If , after paying, a player's account is below zero, the players '''
       # this method takes rent from a player when he lands on an owned palce. Also, in case the rent is in minus, it gives free money to the player.
        rowdict = self.location
        rental_amount = int(rowdict['rent'])
        self.money -= rental_amount
        if self.money <= 0:
            self.active = False
        # Giving money to the owner of the property
        if rowdict['Owner'] != False:
            other_player = rowdict['Owner']
            other_player.money += rental_amount




    def buy_fuel(self):
        # '''Given the current location(self.location), calculates the price of fuel for that location. IF the player has
        # enough money in their account, the fuel is added. IF the property has an owner, the purchase price is added
        #  to the owners account.'''

        rowdict = self.location
        fuel_price = int(rowdict['fuel'])
        if fuel_price <= self.money:
            self.money -= fuel_price
            self.fuel += 1
            if self.money <= 0:
                self.active = False
            # Giving money to the owner of the property. If a player owns a place, his money is first deducted and then paid to him back. So no change occurs.
            if rowdict['Owner']:
                other_player = rowdict['Owner']
                other_player.money += fuel_price





    def buy_property(self):
        '''IF the player has enough money to purchase the current property, deduct the sale price from the player's
        account, and set the property's owner to the current player;'''
        # for rowdict in board:
        #     if rowdict['position']  == self.location:
        rowdict = self.location
        purchase = int(rowdict['purchase'])
        if self.money >= purchase:
            self.money -= purchase
            rowdict['Owner'] = self
            self.owned.append(rowdict['name'])
        if self.money <= 0:
            self.active = False





p1 = Player('Player 1', board[0])
p2 = Player('Player 2', board[0])
p3 = Player('Player 3', board[0])
# note that this game is valid for any number of players
plist = [p1,p2,p3]
menu = 'Please note that you have to end your turn(press 6) to give turn to other players.\nOptions:\n0: Purchase property\n1: Get fuel\n2: Plant fuel station\n3: Move!\n4: Board Information\
  \n5: Player information\n6: End turn\n'

while True:
    # Checking if no. of active player are <= 1, if yes Game Over
    number_of_active_players =0
    for p in plist:
        if p.active:
            number_of_active_players += 1
    if number_of_active_players <= 1 :
        break




    for p in  plist:
        # move_counter does not allow a player to move twice
        move_counter =0
        # this checks for a winner
        number_of_active_players =0
        for b in plist:
            if b.active:
                number_of_active_players += 1
        if number_of_active_players <= 1 :
            break

        if p.active == False:
            break

        while True:
            if p.active ==False:
                    print('Sorry. Your game is over!')
                    break


            print()
            choice = int(input(menu))

            if choice == 0:

                can_be_purchased = p.location['type'] == 'moon' or p.location['type'] == 'planet'
                no_previous_owner = not p.location['Owner']
                purchase_price_greater_than_zero = p.location['purchase'] != ''
                if can_be_purchased and no_previous_owner and purchase_price_greater_than_zero:
                    p.buy_property()

                else:
                    print('You could not purchase this property now. ')


            if choice == 1:
                # Setting the limit for the max fuel. Otherwise, a player can refuel infinitely using his own fuel stations.
                if p.fuel == 12:
                    print('The fuel capactiy is full you can not get more fuel.')
                    continue


                availability_fuel_station = p.location['Fuel_station']
                if availability_fuel_station:
                    p.buy_fuel()

                else:
                    print('You could not buy the fuel.')

            if choice == 2:

                owner_of_the_property = p.location['Owner'] == p

                number_of_fuel_stations_that_a_player_can_manufacture = p.fuel_stations > 0
                vacant_place_for_fuel_station = not p.location['Fuel_station']
                if owner_of_the_property and number_of_fuel_stations_that_a_player_can_manufacture and vacant_place_for_fuel_station:
                    p.location['Fuel_station'] = True
                    p.fuel_stations -= 1

                else:
                    print('You could not plant a fuel station.')

            if choice == 3:

                if move_counter ==1:
                    print('You can not move twice.')
                    continue
                die = random.randint(2, 12)
                print('You rolled', die)
                # die = 40
                # initial_position_of_the_player = int(p.location['position'])

                before = int(p.location['position'])
                p.move(board, die)
                after = int(p.location['position'])
                # Case: Landing or moving past the Earth
                if after < before:
                    p.money += 500

                any_other_owner = p.location['Owner'] != p and p.location['Owner'] != False

                # If someone else owns this place
                if any_other_owner:
                    p.pay_rent()
                # Special case for some Federation Stations in which the rent is in minus.
                if p.location['rent'] != '':
                    if int(p.location['rent']) < 0 and p.location['name'] != 'earth':
                        p.pay_rent()


                # Case: Landing or moving past the Earth
                # final_position_of_the_player = int(p.location['position'])
                # if initial_position_of_the_player >= 79 and \
                #         (final_position_of_the_player >= 0 and final_position_of_the_player <= 11):
                #     p.money += 500

                move_counter += 1

            if choice == 4:

                print('Board Information')
                fuel_station_present = ''
                if p.location['Fuel_station']:
                    fuel_station_present += '*'
                print('Name of the place:(Note that * shows if the space contains a fuel station):',p.location['name'] + fuel_station_present)
                print('Type of the place: ', p.location['type'])
                # Printing the Occupants
                print('Occupants:', p.location['Occupants'])

            if choice == 5:

                print('Current Player Information ')
                print('Name:',p.name)
                print('Money: ', p.money,'units')
                print('Fuel: ', p.fuel)
                print('The number of fuel stations available to the player:', p.fuel_stations)
                print('List of properties owned by the player:', p.owned)
                print('Active:',p.active)

            if choice == 6:
                break
                # Move on to the next player

print()
print('Game Over!!')

for k in plist:
    if k.active:
        print(k.name, 'wins')


















































