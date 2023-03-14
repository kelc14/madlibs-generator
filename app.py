from flask import Flask, request, render_template
from stories import story_data, stories

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html', stories=stories)

@app.route('/form')
def form_page():
    story_id = int(request.args['story_id'])
    chosen_story = story_data[story_id]
    prompts = chosen_story.prompts
    print('this is the story ID', story_id)
    return render_template('form.html', prompts=prompts, story_id=story_id )

@app.route('/story/<story_id>')
def generate_story(story_id):
    story_id = int(story_id)

    story_dict = {}
    prompts = story_data[story_id].prompts
    print('prompts', prompts)
    for prompt in prompts:
        val = request.args[prompt]
        story_dict[prompt] = val
    story_text = story_data[story_id].generate(story_dict)
    print('text', story_text)

    return render_template('story.html', story_text=story_text)


