from most_retweeted import most_retweeted
from top_users import top_users
from top_days import top_days
from top_hashtags import top_hashtags

while True:
    input_number = input('''
Ingresa la opción que deseas ver:
1. Top 10 tweets más retweeted
2. Top 10 con más tweets
3. Top 10 días con más tweets
4. Top 10 hashtags más usados
Input: ''')

    if input_number == '1':
        most_retweeted()

    elif input_number == '2':
        top_users()

    elif input_number == '3':
        top_days()

    elif input_number == '4':
        top_hashtags()

    else:
        print('''
Por favor ingresa una opción válida''')
