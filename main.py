import file_operations

def main():
    # TODO: 添加用戶界面和主要的執行邏輯
    # 測試代碼
    #寫入文件
    file_operations.write_file('test.txt', 'Hello, GitHub!')

    # 讀取文件
    content = file_operations.read_file('test.txt')
    print(content)  # 應該輸出 'Hello, GitHub!'
    pass

if __name__ == "__main__":
    main()
