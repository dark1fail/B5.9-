import time


def time_this(num_runs):
    """
    функция которая считает время работы других функций
    """
    def function(func):
        def another_func(a):
            avg_time = 0
            for _ in range(num_runs):
                t0 = time.time()

                ### <<полезный>> код
                func(a)

                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= num_runs
            print("Выполнение в среднем заняло %.5f секунд" % avg_time)
        return another_func
    return function


@time_this(num_runs=10)
def fib(n):
    """
    считает n-ое число Фибоначчи
    """
    fib1 = 1
    fib2 = 1
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1

    print(fib2)


fib(10000)