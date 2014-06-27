"""
T.S. Eliot, 1925
cat, 2014.06.27
draft1
"""

class World:
    def __str__(self):
        return "this is the way the world ends"

    def ends(self):
        return ["whimper"]

def main():
    world = World()

    for i in range(4):
        print world

    if "bang" not in world.ends():
        print "not with a bang"

    if "whimper" in world.ends():
        print "but with a whimper"

if __name__ == "__main__":
    main()
