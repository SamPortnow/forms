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
                    'typ':'page',
                    '_id':'Page1',
                    'order':'',
                    'page':1,
                    'questions':
                        [
                            {
                                '_id':'Question1',
                                'typ':'mc',
                                'text':'How are you feeling?',
                                'options':['','Bad', 'Neutral', 'Good', 'Great'],
                                'value':'',
                                'if_statement': [
                                        {
                                            'logic':'greater',
                                            'value':'10',
                                            'do':'Page2'
                                        },
                                        {
                                            'logic':'less',
                                            'value':'10',
                                            'do':'Page3'
                                        }
                                      ]
                            }
                        ],
                    },
                    {
                    'typ':'page',
                    'page':2,
                    '_id':"Page2",
                    'order':'',
                    'questions':
                        [
                            {
                                '_id':'Question2',
                                'type':'mc',
                                'text': 'How were you feeling yesterday?',
                                'options':['','Bad','Neutral', 'Good'],
                                'value':'',
                                'if_statement': [
                                      ]
                            }
                        ]
                    },

                    {
                        'typ':'page',
                        '_id': 'Page3',
                        'page':3,
                        'order': '',
                        'questions': questions
                    }
            ]
    }]
    form_data = json.dumps(form_data)
    return render_template('form.html', form_data=form_data)

if __name__ == '__main__':
    app.run()