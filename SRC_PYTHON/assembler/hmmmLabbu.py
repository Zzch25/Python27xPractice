# Lab assignment - HmmmIntro!

import sys

# Example1 is an example program that
#   1) asks the user for two inputs
#   2) computes the product of the inputs
#   3) prints out the result (with write)
#   4) stops

Example1 = """
00 read r1          # get # from user to r1
01 read r2          # ditto, for r2
02 mul r3 r1 r2     # r3 = r1 * r2
03 write r3         # print what's in r3
04 halt             # stop.
"""


# Problem1 is an example program that
#   1) asks the user for an input
#   2) counts up from that input
#   3) keeps going and going...


#designed to loop, although one can cheat4 ;)

#REG 5 sets the exponent -1 = 1/0 = 2

Problem1 = """ 
00 read r1
01 copy r2 r1
02 setn r4 1
03 setn r5 1
04 copy r3 r5
05 jltz r3 9          
06 mul r1 r1 r2
07 sub r3 r3 r4
08 jumpn 05
09 write r1
10 halt
"""

Power = """ 
00 read r1
01 read r2
02 copy r3 r1
03 setn r4 1
04 sub r2 r2 r4
05 jeqzn r2 9          
06 mul r1 r1 r3
07 sub r2 r2 r4
08 jumpn 05
09 write r1
10 halt
"""

# Lab task #1: Change Problem1 to "CubicCountdown" as
# described on the lab web page.

# Lab task #2: (Not Part 2 on the web page.) Make another
# program, "Power", that reads integers x and y, computes
# the exponent x^y in r13, and prints that value.
# Use a loop, similar to the factorial program we did
# in lecture.


# These statements are to set up Hmmm...
# You'll need the files that are in this folder.

if __name__ == "__main__" : 
    import hmmmAssembler ; reload(hmmmAssembler)
    import hmmmSimulator ; reload(hmmmSimulator)
    hmmmAssembler.main(Problem1) # assemble input into machine code
    hmmmSimulator.main()   # run that machine code

# to change the function being run by the assembler and simulator, change to
#   hmmmAssembler.main(Function_name)
#
# to avoid debugging mode without asking, replace the last line with
#     hmmmSimulator.main(['-n'])
#
# to enter debugging mode without asking, replace the last line with
#     hmmmSimulator.main(['-d'])
#
# to have the program ask you whether or not you want to debug, use
#     hmmmSimulator.main()

