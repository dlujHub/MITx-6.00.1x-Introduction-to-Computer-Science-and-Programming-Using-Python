"""
How do we need to modify Accio so that print(Accio()) will print the following description?

Summoning Charm Accio
This charm summons an object to the caster, potentially over a significant distance.

"""


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

    def getDescription(self):
        return 'This charm summons an object to the caster, potentially over a significant distance.'
