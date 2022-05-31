#!/usr/bin/env python

def homework(questions):
    total = 0
    for question in questions:
        if '-' in question:
            nums = [int(x) for x in question.split("-")]
            total += (nums[1] - nums[0]) + 1
        else:
            total += 1
    return total

def main():
    questions = input().split(";")
    print(homework(questions))
    return

if __name__ == "__main__":
    main()