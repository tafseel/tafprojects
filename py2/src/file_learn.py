import pandas


def fun1():
    df = pandas.DataFrame(data=[[1, 2, 3], [2, 3, 5], [10, 20, 30]], columns=["A", "B", "C"])
    print(df.head())


if __name__ == '__main__':
    fun1()
