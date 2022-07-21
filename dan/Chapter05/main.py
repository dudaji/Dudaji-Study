from singleton.singlethread import SingleThread
from singleton.multiThread import MultiThread
from multiprocessing.pool import ThreadPool


class Test:
    pass

if __name__ == "__main__":

    st1 = SingleThread()
    st2 = SingleThread()

    print("########SingleThread########\n")

    print("--------------SingleThread - Not safe--------------")
    print(f"st1 value = {st1.get_value()}")
    print(f"st2 value = {st2.get_value()}")
    print("---------------------------------------------------\n")

    pool = ThreadPool(processes=8)

    for _ in range(1, 100):
        mt1 = pool.apply_async(SingleThread)
        mt2 = pool.apply_async(SingleThread)
        mt3 = pool.apply_async(SingleThread)
        if mt1.get() != \
            mt2.get() != \
            mt3.get():
            print("--------------MultiThread - Not safe---------------")
            print(f"mt1 value = {mt1.get().get_value()}")
            print(f"mt2 value = {mt2.get().get_value()}")
            print(f"mt3 value = {mt3.get().get_value()}")
            print("---------------------------------------------------\n")
        del mt1
        del mt2
        del mt3

    st1 = MultiThread()
    st2 = MultiThread()

    print("########MultiThread########\n")

    print("--------------MultiThread - safe-------------------")
    print(f"st1 value = {st1.get_value()}")
    print(f"st2 value = {st2.get_value()}")
    print("---------------------------------------------------\n")

    pool = ThreadPool(processes=8)

    for _ in range(1, 100):
        mt1 = pool.apply_async(MultiThread)
        mt2 = pool.apply_async(MultiThread)
        mt3 = pool.apply_async(MultiThread)
        if mt1.get() != \
            mt2.get() != \
            mt3.get():
            print("--------------MultiThread -  safe------------------")
            print(f"mt1 value = {mt1.get().get_value()}")
            print(f"mt2 value = {mt2.get().get_value()}")
            print(f"mt3 value = {mt3.get().get_value()}")
            print("---------------------------------------------------\n")
        del mt1
        del mt2
        del mt3

