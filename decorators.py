# decorators.py

import time

def timer_decorator(func):
    """
    裝飾器用於測量函數的執行時間。

    參數:
    - func: 被裝飾的函數

    返回:
    - wrapper: 修改後的函數
    """
    def wrapper(*args, **kwargs):
        # 記錄函數開始執行的時間
        start_time = time.time()
        
        # 調用被裝飾的函數並獲取結果
        result = func(*args, **kwargs)
        
        # 記錄函數結束執行的時間
        end_time = time.time()
        
        # 計算並打印函數的執行時間
        print(f"{func.__name__} took {end_time - start_time} seconds to run.")
        
        # 返回被裝飾的函數的結果
        return result

    return wrapper


def log_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} was called with {args} and returned {result}")
        return result
    return wrapper
