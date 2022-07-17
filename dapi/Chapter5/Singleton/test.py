from threading import Thread
import time
import unittest
from singleton.singleton import SafeSingleton

class SingletonTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass is called")

    def test_singleton_get_set_value(self):
        print("test_singleton_get_set_value")

        s = SafeSingleton()
        s.delete_instance()
        s1 = SafeSingleton("hi")
        self.assertEqual(s1.value, "hi")
        s2 = SafeSingleton()
        self.assertEqual(s1, s2)
        s2.set_value("hihi")
        self.assertEqual(s2.value, "hihi")
        self.assertEqual(s1.value, "hihi")

    def test_singleton_multithread_safe(self):
        print("test_singleton_multithread_safe")

        def test_singleton(value, results, index):
            singleton = SafeSingleton(value)
            # singleton.set_value(value)
            print(singleton.value)
            results[index] = singleton.value

        s = SafeSingleton()
        s.delete_instance()
        results = [None] * 2
        process1 = Thread(target=test_singleton, args=("FOO", results, 0, ))
        process2 = Thread(target=test_singleton, args=("BAR", results, 1, ))
        process1.start()
        process2.start()
        print(results[0], results[1])
        time.sleep(0.25)
        self.assertEqual(results[0], results[1])


if __name__ == "__main__":
    unittest.main()
