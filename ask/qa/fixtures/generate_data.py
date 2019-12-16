import random
import os
filename = os.path.dirname(os.path.abspath(__file__)) + '/testdata.yaml'
with open(filename, 'w') as f:
    for i in range(1, 3):
        _str = """
- model: auth.User
  pk: {0}
  fields:
    password: password{0}
    is_superuser: 0
    username: username{0}
    first_name: first_name{0}
    last_name: last_name{0}
    email: email@email.com
    is_staff: 0
    is_active: 0
    date_joined: '2019-12-15 19:31:03'      
      """.format(i)
        print(_str, file=f)
    for i in range(1, 21):
        _str = """
- model: qa.Question
  pk: {0}
  fields:    
    title: 'Question{0}'
    text: 'text{0}'
    added_at: '2019-12-15 19:31:03'
    rating: {1}
    author_id: {2}
        """.format(i, random.randint(0, 10), random.randint(1, 2))
        print(_str, file=f)
    for i in range(1, 21):
        _str = """
- model: qa.Answer
pk: {0}
fields: 
    text: 'Answer{0}'
    added_at: '2019-12-15 19:31:03'
    author_id: {1}
    question_id: {2}
        """.format(i, random.randint(1, 2), random.randint(1, 20))
        print(_str, file=f)
