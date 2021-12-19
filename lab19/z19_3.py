# розклад руху маршрутних таксі: номер маршруту, кінцева зупинка, марка автобуса, час поїздки
def rozklad():
    taxi = {}
    taxi["номер маршруту"] = input("номер маршруту : ")
    taxi["кінцева зупинка"] = input("кінцева зупинка : ").split("  ")
    taxi["марка таксі"] = input("марка таксі : ")
    taxi["час поїздки"] = input("час поїздки : ")
    return taxi
def input_taxi():
    n = int(input("кількість таксі : "))
    return [rozklad() for i in range(n)]
def search_taxi(taxi_list, taxi_title):
    return list(filter(lambda taxi: taxi['номер маршруту'] == taxi_title, taxi_list))

taxi_list = input_taxi()

while True:
    ans = input('Do you want to search {y/n} ? : ' )
    if ans == 'n':
        break
    taxi_title = input('Taxi for search: ')
    taxi_res = search_taxi(taxi_list, taxi_title)
    if len(taxi_res) > 0:
        print(taxi_res)
    else:
        print('No song')