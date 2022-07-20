from Config import Config

def main():
    user1 = Config('Pat', 'Seoul')
    print(user1.getName())
    print(user1.getLocation())

    user2 = Config('Mat', 'Busan')
    print(user2.getName())
    print(user2.getLocation())

if __name__ == '__main__':
    main()
