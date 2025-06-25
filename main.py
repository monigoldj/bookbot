import sys
from stats import get_and_print_report

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
    return get_and_print_report(filepath)
if __name__ == "__main__":
    main()