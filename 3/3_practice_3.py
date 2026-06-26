"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime
import lorem
from collections import Counter

messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение 
        #является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    },

    ]

def generate_chat_history():
    messages_amount = random.randint(20, 100)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, max(1, len(users_ids) // 2 + 1))
),
            "text": lorem.sentence(),
        })
    return messages    
    
if __name__ == "__main__":
    # print(generate_chat_history())
    messages = generate_chat_history()

# 1. Вывести айди пользователя, который написал больше всех сообщений.
def max_sender():
    senders = []    
    for message in messages:
        senders.append(message.get("sent_by"))

    count = Counter(senders)
    print(count)

    max_sent_message = 0
    for sender in count:
        times_sent = count.get(sender)
        # print (f'Пользователь {sender}: {times_sent} cообщений')
        # who_max_sender[sender] = [times_sent]
        # print
        if times_sent > max_sent_message:
            max_sent_message = times_sent
            max_sender = sender 
    print(f'Пользователь {max_sender}: {max_sent_message} cообщений')
        
# max_sender()

# 2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
from pprint import pprint
def max_replied():
    dict_of_replies = {}
    for message in messages:
        rep = 0
        for message2 in messages:
            if message2.get("reply_for") == message.get("id"):
                rep += 1
            dict_of_replies[message.get("id")] = rep
    
    max_dict = {}
    max_replied_message = 0
    for id in dict_of_replies:
        times_replied = dict_of_replies.get(id)
        
        if times_replied > max_replied_message:
            max_replied_message = times_replied
            max_dict[id] = max_replied_message
            
        elif times_replied == max_replied_message:
            max_dict[id] = times_replied
        
    pprint(max_dict)
# max_replied()

# 3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
from collections import Counter
messages = generate_chat_history()
# print([len(m.get('seen_by', [])) for m in messages[:5]])

def max_seen_unique():
    dict_of_sent_messaes = {}
    for message in messages:
        seen = message.get("seen_by", [])
        seen = set(seen)
        sent_by = message.get("sent_by")
        if sent_by not in dict_of_sent_messaes:
            dict_of_sent_messaes[sent_by] = seen
        else: dict_of_sent_messaes.get(sent_by).update(seen)
    pprint(dict_of_sent_messaes)    


    sorted_senders = sorted(dict_of_sent_messaes.items(), key=lambda item: len(item[1]), reverse=True)
    top_3 = sorted_senders[:3]
    for i, (sender, viewers) in enumerate(top_3, start=1):
        print(f"{i}. Отправитель: {sender}:")
        print(f"   Направил: {len(viewers)} уникальных сообщений")  # или сами ID
                    
    # for sender, viewers in dict_of_sent_messaes.items():
    #     print(f"{sender}: {len(viewers)} уникальных зрителей")                  
# max_seen_unique()  
        
# 4. Определить, когда в чате больше всего сообщений: 
# утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
from datetime import datetime
time_list = []
def the_most_active_time():
    for message in messages:
        date_time = message.get("sent_at") 
        time_ = int(date_time.strftime('%H'))
        # print(time_)
        time_list.append(time_)
    print(time_list)
    
    morning = 0
    noon = 0
    evening = 0
    
    for time in time_list:
        if time < 12:
            morning += 1
        elif time < 18:
            noon += 1
        elif time >= 18:
            evening += 1
        
    if morning > noon and morning > evening:
        print(f'\nБольше всего сообщений утром - {morning} \n\nднем - {noon} сообщений \nвечером - {evening} cообщений\n')
    elif evening > noon and evening > morning:
        print(f'\nБольше всего сообщений вечером - {evening} \n\nднем - {noon} сообщений \nутром - {morning} cообщений\n')
    elif noon > morning and noon > evening:
        print(f'\nБольше всего сообщений днем - {noon} \n\nутром - {morning} сообщений \nвечером - {evening} cообщений\n')
    # обработка случаев с = (от ДИПСИКА)
    # max_count = max(morning, noon, evening)
    # periods = []
    # if morning == max_count: periods.append("утром")
    # if noon == max_count: periods.append("днём")
    # if evening == max_count: periods.append("вечером")
    # print(f"Больше всего сообщений: {', '.join(periods)} – {max_count} сообщений") 
# the_most_active_time()

# 5. Вывести идентификаторы сообщений, который стали началом для 
# самых длинных тредов (цепочек ответов).

def lognest_chain():
    children = {}
    parents = []
    for message in messages:
        reply_for = message.get("reply_for")
        id = message.get("id")
        if reply_for is not None:
            child_id = message.get("id")
            if reply_for not in children:
                children[reply_for] = [child_id]
            else: children[reply_for].append(child_id)
        if reply_for is None:
            parents.append(id)
    
    def count_chain(msg_id):
    # если у сообщения нет детей, длина = 1
    
        # 1. Проверяем, есть ли msg_id в ключах словаря children
        if msg_id not in children:
            # Если нет → сообщение не является родителем
        # → у него нет детей → это конец цепочки
        # → длина цепочки, начинающейся с него, равна 1
            return 1
    
         # 2. Если msg_id есть в ключах → у него есть дети
        total = 1
        # 3. Перебираем всех прямых детей (список из children[msg_id])
        for child in children[msg_id]:
        # 4. Для каждого ребёнка рекурсивно считаем длину его цепочки
            total += count_chain(child)
                # Результат прибавляем к total
        # 5. Возвращаем общую длину цепочки
        return total
    

    results = {}
    for parent in parents:
        results[parent] = count_chain(parent)
    print("Длины цепочек для каждого корня:")
    pprint(results)

    results = sorted(results.items(), key= lambda item: item[1], reverse=True)
    print('Топ 5 тредов:')
    pprint(results[:5])
lognest_chain()

