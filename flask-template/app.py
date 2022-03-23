# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import correct_answers, grade_answers

# Team:
# Trent Gaylord
# Angel Otero

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods=['GET','POST'])
def results():
    if request.method =='GET':
        return 'You have not taken the test'

    answers = {'NY': request.form['New York'],
    'CA': request.form['California'],
    'TX': request.form['Texas'],
    'FL': request.form['Florida'],
    'CO': request.form['Colorado']
    }
    
    grade = grade_answers(answers)
    results = correct_answers(answers)
    
    return render_template('results.html', results=results, grade=grade)
