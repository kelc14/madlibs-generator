from flask import Flask, request, render_template
from stories import Story, story1, story2

app = Flask(__name__)

# story_prompt = []
# story_text = ""

# story_1_prompts = ['food', 'name', 'adjective', 'noun', 'plural_noun'],
# story_1_text = """It was {food} day at school, and {name} was super {adjective} for lunch. 
# But when she went outside to eat, a {noun} stole her {plural_noun}!"""

# story_2_prompts = ["place", "noun", "verb", "adjective", "plural_noun"]
# story_2_text = """Once upon a time in a long-ago {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plural_noun}."""

# story_prompts = {'story1': story_1_prompts, 'story2': story_2_prompts}
# story_text = {'story1': story_1_text, 'story2': story_2_text}


chosen_story = ""

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/form')
def form_page():
    chosen_story = request.args['s']
    if chosen_story == 'story1':
        prompts = story1.prompts
    elif chosen_story =='story2':
        prompts = story2.prompts
    return render_template('form.html', prompts=prompts, chosen_story=chosen_story)

@app.route('/story1')
def make_story1():
    story_dict = {}
    prompts = story1.prompts
    print('prompts', prompts)
    for prompt in prompts:
        val = request.args[prompt]
        story_dict[prompt] = val
    story_text = story1.generate(story_dict)
    print('text', story_text)

    return render_template('story.html', story_text=story_text)
    # return '<h1>is this working</h1>'

@app.route('/story2')
def make_story2():
    story_dict = {}
    prompts = story2.prompts
    for prompt in prompts:
        val = request.args[f"{prompt}"]
        story_dict[prompt] = val
    story_text = story2.generate(story_dict)
    return render_template('story.html', story_text=story_text)