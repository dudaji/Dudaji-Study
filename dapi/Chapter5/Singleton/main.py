from observer.observer import NotificationObserver
from singleton.singleton import SafeSingleton

if __name__ == "__main__":
    s = SafeSingleton("banana")

    o1 = NotificationObserver("apple")
    o2 = NotificationObserver("kiwi")
    o3 = NotificationObserver("tomato")
    print(s.value, o1.value, o2.value, o3.value)

    s.subscribe(o1)
    s.subscribe(o2)
    s.update_value("melon")

    print(s.value, o1.value, o2.value, o3.value)
