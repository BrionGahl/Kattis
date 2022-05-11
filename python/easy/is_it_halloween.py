#!/usr/bin/env python

def is_hallow(date):
    return date == "OCT 31" or date == "DEC 25"
def main():
    date = input()
    if (is_hallow(date)):
        print("yup")
        return
    print("nope")    
    return    

if __name__ == "__main__":
    main()