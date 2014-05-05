# Completely Inelegant 2048 Solver

I'm sure you've seen a hundred of them.  Here's one more.

I came to the 2048 game a bit late, past the hype.  It's a fun and somewhat
addictive game, but I seem to have plateaued as I'm sure many have.  I have
discovered a playable pattern that has gotten me to 15k with most games ending
in the mid-5ks.  It takes minutes to get this far, and I've not found the
pattern that gets me to the next level.

## The Pattern

The pattern I have been using is quite simple.  In fact, I think I learned much
of it from a cat on the bus heading into Denver one evening.  His words, "you
have to keep promoting your highest numbers to the top row."  And this I have
done, keeping my highest numbers to the top row, most of my moves are left to
right, combing numbers 16 and up towards the "top" of the board.

There are two problems with this:

1. Higher numbers can get isolated and can be hard to combine.
2. There seems to be an oscilating pattern that causes "promoted" higher numbers
   to occur on opposing ends of the board.

I just can't seem to break that pattern.  I would like to see the output graph
of this program point the way to a new play pattern.

## The Graph

I've had fun thinking about the problem of 2048.  I'm not especially strong at
maths, but better at logic.  Looking at any give state of the board, there are a
finite number of states that basically break down as:

valid moves * empty cells * 2

where 2 is the number of possible values of the random cell added at the end of
each turn.

As the player only has control over the valid move chosen, I do not intend to
explore the entirety of the game graph.  That means that the number of possible
next board states is limited to:

valid moves * (empty cells - 1)

## The Solver

Thus far I have implemented the game as a Board and Game class.  After a few
iterations where the state of the Board object changed with each move, I've
rewritten the Board class to be stateless.  Each mutator operation returns a new
board state, leaving the instance itself intact.  This allows for a basic search
algorithm:

For each game state:

* pull each next valid state
* evaluate each next state based upon:
    * point value of change
    * number of empty cells
