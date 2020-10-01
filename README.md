# Snake_Ladder
A sample two player Snake &amp; Ladder scenario using random module.

dice.py
----------
Input : We have taken two player names as input.

Output : Message specifying a user has won the game.

We use randint() from random module to get a random dice throw. Total scores of players is initialized to 0. User is requested to provide an input ("Y" is preferred) for calling randint(). Random dice throw ( 1 to 6 ) is returned which gets accumulated to respective player's total score. If player's input is other than "Y", he looses a chance to throw dice.

We need to continue this random throw until - One of their scores reach Game Total (Let, it be 10). Once player's total score reaches Game Total, a message specifying that player has won the game is displayed. 
