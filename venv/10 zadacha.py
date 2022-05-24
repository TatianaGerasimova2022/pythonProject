import requests


# def print_fun_facts():
#     url = 'https://cat-fact.herokuapp.com/facts'
#     for i in range(4):
#         print(requests.get(url).json()[i]['text'])
# print_fun_facts()

def get_currencie():
    for j in range(1, 13):
        if j < 10:
            j = '0' + str(j)
        for i in range(1, 31):
            if i < 10:
                i = '0' + str(i)
            url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/2022-' + str(j) +'-'+ str(i) + '/currencies/usd/rub.json'
        response = requests.get(url).json()
        print(response['rub'])


get_currencie()
