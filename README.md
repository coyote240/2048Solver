# 2048 Solver in Python

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

I just can't seem to break that pattern.

## The Solver

Don't look for much, there are far smarter people than me playing with the
problem.  This project falls into the "procrasti-work" category.  While I have
plenty of paying or otherwise projects to work on, I'm wasting my time on this
one.  A less cynical view may be that I'm keeping a project aside for pure
enjoyment.  Yeah, let's go with that one.

Most of what will be done first is simply implementing the game.  This means
rules and the basic ability to play.  Beyond this, here is the creativity.  Is
the game to be solved as a search problem?  How else?  It remains to be seen.
