"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started



story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)
story2 = Story(
    ['food', 'name', 'adjective', 'noun', 'plural_noun'],
"""It was {food} day at school, and {name} was super {adjective} for lunch. 
But when she went outside to eat, a {noun} stole her {plural_noun}!""")

story3 = Story(
    ['number', 'noun', 'adjective', 'activity', 'clothing', 'food', 'noun'],
"""One very nice morning near the end of summer, my mother woke me up at {number}:00 A.M. and said, "Wake up and smell the {noun}, {adjective} head! Today is your first day of {activity} and you can't be late." I groaned in my bed for twenty seconds, but eventually I got dressed. I wore a {clothing}. She said, "I made you the breakfast of champions, your favorite, {food}! Have a great day, you are a {noun}!" And off I went. """)

story_data = {1: story1, 2: story2, 3: story3}
stories = {1:'Ancient Times', 2: "Lunch Time", 3: "First Day", 4: "Story4", 5: "Story5", 6: "Story6"}


