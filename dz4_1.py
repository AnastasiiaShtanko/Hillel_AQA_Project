australia_blacklist = {'Alex', 'Max', 'Joe'}
poker_blacklist = {'Anastasiia', 'Maria', 'Joe', 'Oliver', 'Max'}
alcohol_blacklist = {'Joe', 'Harry', 'Jack', 'Alex', 'Max'}

winners = australia_blacklist.intersection(poker_blacklist, alcohol_blacklist)
#winners_string = ', '.join(str(element) for element in winners)

if not winners:
    print("There are no winners :(")
else:
    print("Jackpot winners: ", winners)
