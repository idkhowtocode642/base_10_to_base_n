def base_10_to_base_n(value: int, base: int):
    def operation(value: int, base: int, result=[]):
        if value != 0:
            print(base, value - (value % base), value % base)
            result.insert(0, value % base)
            return operation(int((value - (value % base)) / base), base)
        return result
    print("Result", operation(value, base))
