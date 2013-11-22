from flask import Flask, render_template
from pymongo import MongoClient
import json
client = MongoClient()
db = client.form
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    question = {
        'typ': 'mc',
        'text':''
    }
    people = ['Dan', 'Sam', 'Jeff']
    questions = []
    for person in people:
        question['text'] = 'How much do you like %s' %person
        questions.append(question.copy())
    form_data = [{
        'sections':
            [
                {
                    'type':'page',
                    'id':'Page1',
                    'order':'',
                    'page':1,
                    'questions':
                        [
                            {
                                'id':'Question1',
                                'type':'select',
                                'text':'How are you feeling?',
                                'value':'',
                                'options':['Bad', 'Neutral', 'Good', 'Great', 4, 5],
                                'caption': 'Choose...',
                                'if_statement': [
                                        {
                                            'logic':'equals',
                                            'value':'Neutral',
                                            'do':'page',
                                            'place':'Page2'
                                        },
                                        {
                                            'logic':'equals',
                                            'value':'Bad',
                                            'do':'page',
                                            'place':'Page3',
                                        },

                                        {
                                            'logic': 'greater than',
                                            'value':4,
                                            'do':'page',
                                            'place':'Page3'

                                        },

                                        {
                                            'logic':'between',
                                            'value':[3,5],
                                            'do':'page',
                                            'place': 'Page3',
                                        }


                                      ]
                            },
                            {
                                'id':'Question3',
                                'type':'textarea',
                                'text': 'How were you feeling yesterday?',
                                'if_statement': [
                                      ]
                            }
                        ],
                    },
                    {
                    'type':'page',
                    'page':2,
                    'id':"Page2",
                    'order':'',
                    'questions':
                        [
                            {
                                'id':'Question2',
                                'type':'select',
                                'text': 'How were you feeling yesterday?',
                                'forloop': 3,
                                'pre':'posttest',
                                'value':'',
                                'options':['Bad','Neutral', 'Good'],
                                'caption': 'Choose...',
                                'if_statement': [
                                      ]
                            },
                        ]
                    },
                {
                    'type':'section',
                    'page':2,
                    'id':'Section3',
                    'visible':False,
                    'order':'',
                    'questions':
                        [
                            {
                                'id':'Question4',
                                'type':'textfield',
                                'text':'Feel Better!',
                            }
                        ]
                },
                {
                    'type':'section',
                    'page': 2,
                    'id':'Section2',
                    'order':'',
                    'questions':
                        [
                            {
                                'id':'Question3',
                                'type':'select',
                                'text': "Whats up!?",
                                'value':'',
                                'options':['Bad', 'Neutral', 'Good'],
                                'if_statement': [
                                        {
                                            'logic':'equals',
                                            'value':'Neutral',
                                            'do':'section',
                                            'place':'Section3',
                                        }]
                            }
                        ],
                },
            ]
    }]
    form_data = json.dumps(form_data)
    return render_template('form.html', form_data=form_data)

@app.route('/create')
def create():
    return render_template('create_form.html')

@app.route('/logic')
def logic():
    return render_template('logic.html')

if __name__ == '__main__':
    app.run()