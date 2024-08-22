import argparse
import sys

def fizzbuzz(start, end, fizz_num, buzz_num, fizz_word, buzz_word, reverse, step):
    sequence = range(start, end + 1, step)
    if reverse:
        sequence = reversed(sequence)
    
    for num in sequence:
        msg = ''
        if num % fizz_num == 0:
            msg += fizz_word
        if num % buzz_num == 0:
            msg += buzz_word
        print(msg or num)

def main():
    parser = argparse.ArgumentParser(description="Enhanced FizzBuzz")
    parser.add_argument('-s', '--start', type=int, default=1, help="Starting number")
    parser.add_argument('-e', '--end', type=int, default=100, help="Ending number")
    parser.add_argument('-f', '--fizz-num', type=int, default=3, help="Number for Fizz")
    parser.add_argument('-b', '--buzz-num', type=int, default=5, help="Number for Buzz")
    parser.add_argument('--fizz-word', type=str, default="Fizz", help="Word for Fizz")
    parser.add_argument('--buzz-word', type=str, default="Buzz", help="Word for Buzz")
    parser.add_argument('-r', '--reverse', action='store_true', help="Reverse the sequence")
    parser.add_argument('-t', '--step', type=int, default=1, help="Step increment")
    args = parser.parse_args()

    fizzbuzz(args.start, args.end, args.fizz_num, args.buzz_num, args.fizz_word, args.buzz_word, args.reverse, args.step)

if __name__ == "__main__":
    sys.exit(main())
