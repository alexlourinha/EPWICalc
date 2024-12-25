
def mastery_calc(character):
    mastery = 0.00
    buffs = character.get("active_buffs")
    if any("Axe and Hammer Mastery - 1" in x for x in buffs):
        mastery = 1.00
    if any("Axe and Hammer Mastery - 2" in x for x in buffs):
        mastery = 1.00
    if any("Axe and Hammer Mastery - 3" in x for x in buffs):
        mastery = 1.00
    if any("Axe and Hammer Mastery - 4" in x for x in buffs):
        mastery = 1.00
    if any("Axe and Hammer Mastery - 5" in x for x in buffs):
        mastery = 1.00
    if any("Axe and Hammer Mastery - 6" in x for x in buffs):
        mastery = 1.00
    if any("Axe and Hammer Mastery - 7" in x for x in buffs):
        mastery = 1.00
    if any("Axe and Hammer Mastery - 8" in x for x in buffs):
        mastery = 1.00
    if any("Axe and Hammer Mastery - 9" in x for x in buffs):
        mastery = 1.00
    if any("Axe and Hammer Mastery - 10" in x for x in buffs):
        mastery = 1.00
    if any("Axe and Hammer Mastery - Sage" in x for x in buffs):
        mastery = 1.00
    if any("Axe and Hammer Mastery - Demon" in x for x in buffs):
        mastery = 1.00

    return mastery