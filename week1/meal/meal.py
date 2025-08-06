def main():
    time = input("What time is it? ")
    converted = convert(time)
    if 7.0 <= converted <= 8.0:
        print ("breakfast time")
    elif 12.0 <= converted <= 13.0:
        print ("lunch time")
    elif 18.0 <= converted <= 19.0:
        print ("dinner time")
    else:
        print ("Nothing")
def convert(time):
   hours, mins = time.split(":")
   hours = int(hours)
   mins = int(mins)
   return hours + mins / 60

if __name__ == "__main__":
    main()
