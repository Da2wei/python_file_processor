import argparse
import file_operations

def main():
    parser = argparse.ArgumentParser(description="Python File Processor")
    
    # 定義命令行參數
    parser.add_argument("-r", "--read", help="Read a file", action="store", dest="read_file")
    parser.add_argument("-w", "--write", help="Write to a file", action="store", dest="write_file")
    parser.add_argument("-c", "--content", help="Content to write", action="store", dest="content")
    
    # 解析命令行參數
    args = parser.parse_args()

    # 執行對應的操作
    if args.read_file:
        print(file_operations.read_file(args.read_file))
    elif args.write_file and args.content:
        file_operations.write_file(args.write_file, args.content)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
