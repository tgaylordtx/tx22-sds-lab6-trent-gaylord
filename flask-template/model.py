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

def correct_answers(answers):
    answers['NY'] = 'Correct!' if answers['NY'].lower() == 'albany' else 'Incorrect.'
    answers['CA'] = 'Correct!' if answers['CA'].lower() == 'sacramento' else 'Incorrect.'
    answers['TX'] = 'Correct!' if answers['TX'].lower() == 'austin' else 'Incorrect.'
    answers['FL'] = 'Correct!' if answers['FL'].lower() == 'tallahassee' else 'Incorrect.'
    answers['CO'] = 'Correct!' if answers['CO'].lower() == 'denver' else 'Incorrect.'

    return answers

def grade_answers(answers):
    num_correct_ans = 0

    if answers['NY'].lower() == 'albany': num_correct_ans += 1
    if answers['CA'].lower() == 'sacramento': num_correct_ans += 1
    if answers['TX'].lower() == 'austin': num_correct_ans += 1
    if answers['FL'].lower() == 'tallahasee': num_correct_ans += 1
    if answers['CO'].lower() == 'denver': num_correct_ans += 1

    return (int)(num_correct_ans / 0.05)