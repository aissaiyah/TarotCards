import random
#imports library

#In each function there is a 1 in 2 choice for the card to be reversed
def theFool():
    roll = random.randint(1,2)
    if roll == 1:
        card = "The Fool"
        info = "Represents: New beginnings, innocence, adventure"
    if roll == 2:
        card = "The Reversed Fool"
        info = "Represents: Recklessness, fearlessness, risk" 
    return card + "\n" +info
#if the roll lands on that number change the information in the variables card and info to those values and return those values with spacing
def theHighPriestess():
    roll = random.randint(1,2)
    if roll == 1:
        card = "The High Priestess"
        info = "Represents: Inner voice, unconscious, divine feminine, and security"
    if roll == 2:
        card = "The Reversed High Priestess"
        info = "Represents: Repressed feelings, withdrawal, and silence " 
    return card + "\n" +info
def theEmpress():
    roll = random.randint(1,2)
    if roll == 1:
        card = "The Empress"
        info = "Represents: Femininity, nurturing, fertility, abundance, and celebration"
    if roll == 2:
        card = "The Reversed Empress"
        info = "Represents: Dependence, smothering, and emptiness" 
    return card + "\n" +info
def theEmporer():
    roll = random.randint(1,2)
    if roll == 1:
        card = "The Emporer"
        info = "Represents:  Authority, structure, a father figure, and change"
    if roll == 2:
        card = "The Reversed Emporer"
        info = "Represents: Excessive control, rigidity, and domination" 
    return card + "\n" +info
def theHierophant():
    roll = random.randint(1,2)
    if roll == 1:
        card = "The Hierophant"
        info = "Represents: Spiritual wisdom, tradition, conformity, morality, and ethics"
    if roll == 2:
        card = "The Reversed Hierophant"
        info = "Represents: Rebellion, subversiveness, freedom, and personal beliefs" 
    return card + "\n" +info
def theLovers():
    roll = random.randint(1,2)
    if roll == 1:
        card = "The Lovers"
        info = "Represents: Love, harmony, partnerships, and choices"
    if roll == 2:
        card = "The Reversed Lovers"
        info = "Represents: Disbalance, one-sidedness, and disharmony" 
    return card + "\n" +info
def theChariot():
    roll = random.randint(1,2)
    if roll == 1:
        card = "The Chariot"
        info = "Represents: Direction, control, willpower, determination, success, action, and security"
    if roll == 2:
        card = "The Reversed Chariot"
        info = "Represents: Lack of control, opposition, lack of direction, and self-discipline" 
    return card + "\n" +info
def theStrength():
    roll = random.randint(1,2)
    if roll == 1:
        card = "Strength"
        info = "Represents:  Strength, courage, compassion, focus, persuasion, and influence"
    if roll == 2:
        card = "Reversed Strength"
        info = "Represents:  Self-doubt, weakness, insecurity, low energy, and raw emotion" 
    return card + "\n" +info
def theHermit():
    roll = random.randint(1,2)
    if roll == 1:
        card = "The Hermit"
        info = "Represents: Wisdom, soul searching, solitude, spiritual enlightenment, receiving/giving guidance, and intuition"
    if roll == 2:
        card = "The Reversed Hermit"
        info = "Represents: Loneliness, isolation, paranoia, sadness, being overcome or paralyzed by fear" 
    return card + "\n" +info
def Justice():
    roll = random.randint(1,2)
    if roll == 1:
        card = "Justice"
        info = "Represents: Fairness, integrity, legal disputes, cause and effect, and life lessons"
    if roll == 2:
        card = "Reversed Justice"
        info = "Represents: Injustice, dishonesty, failure to take responsibility, deceitful practices, and negative karma" 
    return card + "\n" +info
def Death():
    roll = random.randint(1,2)
    if roll == 1:
        card = "Death"
        info = "Represents: Ending of a cycle, transitions, getting rid of excess, powerful movement, resolutions, and intuition"
    if roll == 2:
        card = "Reversed Death"
        info = "Represents: Resisting change, fear of new beginnings, dependency, and negative patterns" 
    return card + "\n" +info
def wheelOfFortune():
    roll = random.randint(1,2)
    if roll == 1:
        card = "Wheel Of Fortune"
        info = "Represents: Chance, destiny and fate, karma, turning points, and a resolved conflict"
    if roll == 2:
        card = "Reversed Wheel Of Fortune"
        info = "Represents: Upheaval, lousy luck, unwelcome changes, and setbacks" 
    return card + "\n" +info
def theMagician():
    roll = random.randint(1,2)
    if roll == 1:
        card = "The Magician"
        info = "Represents: Willpower, creation, inner strength, and manifestation"
    if roll == 2:
        card = "The Reversed Magician"
        info = "Represents: Manipulation and illusions" 
    return card + "\n" +info
def theHangedMan():
    roll = random.randint(1,2)
    if roll == 1:
        card = "The Hanged Man"
        info = "Represents: Letting go, sacrificing, pausing to reflect, uncertainty, and spiritual awakening"
    if roll == 2:
        card = "The Reversed Hanged Man"
        info = "Represents: Discontentment, stagnation, negativity, no solution, and fear of sacrifice" 
    return card + "\n" +info
def Temperance():
    roll = random.randint(1,2)
    if roll == 1:
        card = "Temperance"
        info = "Represents: Balance, moderation, good health, cooperating with others, and diligence"
    if roll == 2:
        card = "Reversed Temperance"
        info = "Represents: Imbalance, discord, hastiness, overindulgence, and risky behavior" 
    return card + "\n" +info
def TheDevil():
    roll = random.randint(1,2)
    if roll == 1:
        card = "The Devil"
        info = "Represents: Material focus, material possessions, trapped in bondage, addictions, depression, negative thinking, and betrayal"
    if roll == 2:
        card = "The Reversed Devil"
        info = "Represents: Overcoming addiction, independence, reclaiming power, detachment, and freedom" 
    return card + "\n" +info
def TheTower():
    roll = random.randint(1,2)
    if roll == 1:
        card = "The Tower"
        info = "Represents: Intense and sudden change, release, painful loss, tragedy, and revelation"
    if roll == 2:
        card = "The Reversed Tower"
        info = "Represents: Resisting change, avoiding tragedy, a narrow escape, and delaying what is inevitable" 
    return card + "\n" +info
def TheStar():
    roll = random.randint(1,2)
    if roll == 1:
        card = "The Star"
        info = "Represents: Hope, renewal, creativity and inspiration, generosity, healing, and change"
    if roll == 2:
        card = "The Reversed Star"
        info = "Represents: Despair, lack of hope, creative block, boredom, and focusing on the negative" 
    return card + "\n" +info
def TheMoon():
    roll = random.randint(1,2)
    if roll == 1:
        card = "The Moon"
        info = "Represents: Fear, anxiety, confusion, delusion, risk, and grief"
    if roll == 2:
        card = "The Reversed Moon"
        info = "Represents: Overcoming fear, emotional stability, finding the truth, conquering anxiety, and gaining clarity" 
    return card + "\n" +info
def TheSun():
    roll = random.randint(1,2)
    if roll == 1:
        card = "The Sun"
        info = "Represents: Happiness, fertility, success, optimism, truth, and diligence"
    if roll == 2:
        card = "The Reversed Sun"
        info = "Represents: Sadness, procrastination, pessimism, lies, and failure" 
    return card + "\n" +info
def Judgement():
    roll = random.randint(1,2)
    if roll == 1:
        card = "Judgement"
        info = "Represents: Reflection, inner calling, reckoning, awakening, rebirth, and absolution"
    if roll == 2:
        card = "Reversed Judgement"
        info = "Represents: Feeling down, self-doubt, and missing the call for fearlessness" 
    return card + "\n" +info
def theWorld():
    roll = random.randint(1,2)
    if roll == 1:
        card = "The World"
        info = "Represents: Fulfillment, harmony, completion, integration, travel, and unity"
    if roll == 2:
        card = "The Reversed World"
        info = "Represents: Incompletion, shortcuts, delays, and emptiness" 
    return card + "\n" +info
#list of cards in the deck
deck = [theFool(),theHighPriestess(),theEmpress(),theEmporer(),theHierophant(),theLovers(),theChariot(),theStrength(),Justice(),Death(),wheelOfFortune(),theHermit(),theMagician(),theHangedMan(),Temperance(),TheDevil(),TheTower(),TheStar(),TheMoon(),TheSun(),Judgement(),theWorld()]


