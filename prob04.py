# static 메소드에 대해 알 수 있는 예제

import functools

class StringUtil:
    @staticmethod
    def concatenate(str_list):
        return functools.reduce(lambda acc, x: acc+x, str_list)

if __name__ == '__main__':
    str_list = ["SuperMan", "BatMan", "SpiderMan"]
    result_str = StringUtil.concatenate(str_list)

    print("결과 문자열 :", result_str)