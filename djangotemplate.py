class Person(object):
    def say_hellop(self):
        print('hello')

person = Person()
people = {'Tom':10, 'Steve':20}

#python code
people['Tom']
person.say_hello()

#django template engine
{{people.Tom}}
{{person.say_hello}}

# #한줄 주석
# '''
# 주석1
# 주석2
# '''

# {#한줄 주석#}

# #여러 줄 주석
# {% comment "왜 주석처리 했는지 적어도 됨 옵션" %}
#  주석1
#  주석2
# {% endcomment %}


#---------------------------------------------------

# python에서 실행 할 경우 

# athelete_list = []

# if athelete_list:
#     for athelete in athelete_list:
#         print(athelete.name)
# else:
#     print("empty")

# Django template 에서 실행할 경우

# {% for athelete in athelete_list %}
#     {{athelete.name}}
# {% empty %}
#     empty
# {% endfor %}


# empty 사용 안할 경우 

# {% if athelete_list %}
#     {% for athelete in athelete_list %}
#         {{athelete.name}}
#     {% endfor %}
# {%else%}
#     empty
# {% endif %}
