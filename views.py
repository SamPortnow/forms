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
                                'options':['Bad', 'Neutral', 'Good', 'Great', 4, 5],
                                'caption': 'Choose...',
                                'if_statement': [
                                        {
                                            'logic':'equals',
                                            'value':'Neutral',
                                            'do':'Page2'
                                        },
                                        {
                                            'logic':'equals',
                                            'value':'Bad',
                                            'do':'Page3'
                                        },

                                        {
                                            'logic': 'greater than',
                                            'value':4,
                                            'do':'Page3'

                                        },

                                        {
                                            'logic':'between',
                                            'value':[3,5],
                                            'do': 'Page3',
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
                                'options':['Bad','Neutral', 'Good'],
                                'caption': 'Choose...',
                                'if_statement': [
                                      ]
                            },
                        ]
                    }
            ]
    }]
    form_data = json.dumps(form_data)
    return render_template('form.html', form_data=form_data)

if __name__ == '__main__':
    app.run()