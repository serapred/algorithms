def fibonacci(cb, safety):
    values = []
    while(True):
        if len(values) < 2:
            values.append(1)
        else:
            values = [values[-1], values[-1] + values[-2]]

        # after calculating the nth num of the
        # fibonacci sequence, executes the
        # injected function passing it as param.

        r = cb(values[-1])
        if (r[0]):
            return(r[1])


# callback function, passed as parameter
# for function injection
# return a couple consisting of boolean flag
# that marks if a result was found
# and the result in affermative case
def check_17(v, s):

    if v % 17 == 0:
        return (True, v)

    if v > s:
        return (True, None)

    return (False,)


if __name__ == '__main__':
    res = fibonacci(check_17, 1000)
    if (res != None):
        print(res)
