# Snake_Ladder
A sample non GUI based two player Snake &amp; Ladder scenario using random module.

dice.py
----------
Input : We have taken two player names as input.

Output : Message specifying a user has won the game.

We use randint() from random module to get a random dice throw. Total scores of players is initialized to 0. User is requested to provide an input ("Y" is preferred) for calling randint(). Random dice throw ( 1 to 6 ) is returned which gets accumulated to respective player's total score. If player's input is other than "Y", he looses a chance to throw dice.

We need to continue this random throw until - One of their scores reach Game Total (Let, it be 10). Once player's total score reaches Game Total, a message specifying that player has won the game is displayed. 

Player's total scores must be less than Game Total to proceed this scenario.

The function randint() should be given two parameters 1 and 6 so that it specifies a dice throw.

User must provide an input ("Y") to give a dice throw (we can set it to anything). Else, user looses a chance.

If player's total exceeds the Game Total(Let it be 10), his dice throw becomes invalid and score won't update for that throw.

