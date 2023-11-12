import bs4
print('hui')


def main():
    print("hi")



def start():
    global __commands
    __commands = {
        'task': 'задач',
        'hello': 'прив|здрав',
        'open': 'открыть',
        'close': 'закрыть',
        'is_open': '(.*открыт.*лаб.*)|(.*лаб.*открыт.*)|(.*закрыт.*лаб.*)|(.*лаб.*закрыт.*)|(.*лаб.*ест.*)|(.*ест.*лаб.*)',
        'about_club': 'что такое robotic?',
        'projects': 'проекты и мероприятия',
        'join_club': 'как попасть в robotic?',
        'remind': 'напомни'
    }
