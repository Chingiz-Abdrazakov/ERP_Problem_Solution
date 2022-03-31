import math
import os
import random
import re
import sys


class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __sub__(self, other):
        return Time(self.hour - other.hour, self.minute - other.minute)

    def __lt__(self, other):
        return (self.hour * 60 + self.minute) < (other.hour * 60 + other.minute)

    def __repr__(self):
        return str(self.hour).zfill(2) + ':' + str(self.minute).zfill(2)

    def get_time(self):
        return self.hour, self.minute


def check_time(s):
    if ':' not in s:
        print('Invalid input format, try again')
        return False
    if int(s[:s.find(':')]) < 0 or int(s[:s.find(':')]) > 23:
        print('Invalid hour, try again')
        return False
    if int(s[s.find(':') + 1:]) < 0 or int(s[s.find(':') + 1:]) > 60:
        print('Invalid minute, try again')
        return False
    return True


def create_time(s):
    return Time(int(s[:s.find(':')]), int(s[s.find(':') + 1:]))


def available_rooms(arr):
    ans = ''
    first = True
    for element in arr:
        if not first:
            ans += ', '
        ans += str(element[0])
        first = False
    return ans


def book(roomsTime, fromTime, toTime, element):
    for val in roomsTime[element[0]]:
        if val[0] < fromTime and val[1] > toTime:
            roomsTime[element[0]].remove(val)
            roomsTime[element[0]].append((val[0], fromTime))
            roomsTime[element[0]].append((toTime, val[1]))
            print('Successfully booked room #' + str(element[0]) + ' from ' + str(fromTime) +
                  ' till ' + str(toTime))
            break


def strong_password(passw):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(passw) < 5:
        return False
    numCount = 0
    lowCount = 0
    uppCount = 0
    for number in numbers:
        if number in passw:
            numCount += 1
    for symbol in lower_case:
        if symbol in passw:
            lowCount += 1
    for symbol in upper_case:
        if symbol in passw:
            uppCount += 1
    if numCount and lowCount and uppCount:
        return True
    return False


if __name__ == '__main__':
    db = {}
    books = {}
    prevQuery = ''
    firstAttempt = True

    roomsTime = {230: [(Time(0, 0), Time(23, 59))],
                 218: [(Time(0, 0), Time(23, 59))],
                 112: [(Time(0, 0), Time(23, 59))],
                 113: [(Time(0, 0), Time(23, 59))],
                 231: [(Time(0, 0), Time(23, 59))],
                 537: [(Time(0, 0), Time(23, 59))],
                 432: [(Time(0, 0), Time(23, 59))],
                 100: [(Time(0, 0), Time(23, 59))],
                 101: [(Time(0, 0), Time(23, 59))],
                 201: [(Time(0, 0), Time(23, 59))],
                 239: [(Time(0, 0), Time(23, 59))]}
    roomsMaxCapacity = {230: 4, 218: 2, 112: 6,
                        113: 7, 231: 5, 537: 10,
                        432: 9, 100: 3, 101: 5,
                        201: 7, 239: 6}

    failsCounter = 0
    while True:
        if failsCounter >= 3:
            query = input('Sign in or sign up? (i/u): ')
        else:
            if firstAttempt:
                query = input('Sign in or sign up? (i/u): ')
            else:
                query = prevQuery
        print('--------------------------------------------------------------------')
        if query == 'u':
            name = input('Please, enter your name: ')
            password = input('Please, enter your password (password must contain lowercase, uppercase and numbers): ')
            if name in db:
                print('The name is already taken, choose another')
                firstAttempt = False
                prevQuery = query
                failsCounter += 1
                continue
            else:
                isStrong = strong_password(password)
                if not isStrong:
                    print('Your password is weak, try another one')
                    continue
                else:
                    db[name] = password
                    print('Hello, ' + name + '!')

        elif query == 'i':
            name = input('Please, enter your name: ')
            password = input('Please, enter your password: ')
            if name not in db or db[name] != password:
                print('Invalid name or password')
                firstAttempt = False
                prevQuery = query
                failsCounter += 1
                continue
            else:
                print('Hello, ' + name + '!')
        else:
            print('Invalid input, try again')
            continue

        def find_free(fromTime, toTime):
            freeRooms = []
            for key, times in roomsTime.items():
                for val in times:
                    if val[0] < fromTime and val[1] > toTime:
                        freeRooms.append(key)
            return freeRooms

        def arr_greater(arr, el):
            ans = []
            for key in arr:
                value = roomsMaxCapacity[key]
                if value >= el:
                    ans.append((key, value))
            ans.sort(key=lambda x: x[1])
            return ans


        while True:
            nextquery = input('If you want to see your bookings, type s\nIf you want to book a room, type b\nIf you want to leave, type l: ')
            if nextquery == 's':
                if name not in books:
                    print('You have no booked rooms yet')
                    firstAttempt = False
                    continue
                else:
                    print('Your bookings: ')
                    for booking in books[name]:
                        print('Room #', str(booking[0]), 'from', booking[1], 'till', booking[2])
            elif nextquery == 'b':
                    fromTimeInp = input('Please enter the time you want to book from (in hh:mm format): ')
                    if not check_time(fromTimeInp):
                        continue
                    toTimeInp = input('Please enter the time you want to book till (in hh:mm format): ')
                    if not check_time(toTimeInp):
                        continue

                    fromTime = create_time(fromTimeInp)
                    toTime = create_time(toTimeInp)
                    if toTime < fromTime:
                        print('Invalid time interval, try again')
                        continue
                    allFreeInTimeInterval = find_free(fromTime, toTime)
                    personCount = int(input('Please enter the number of people '))
                    freeRooms = arr_greater(allFreeInTimeInterval, personCount)
                    print('--------------------------------------------------------------------')
                    print('Available rooms:', available_rooms(freeRooms))
                    if not available_rooms(freeRooms):
                        print('There are no rooms for this time interval')
                    isBooked = False

                    while True:
                        for element in freeRooms:
                            print('Book room #', element[0], 'from', fromTime, 'till', toTime, '?')
                            answer = input('y/n ')
                            if answer == 'n':
                                continue
                            elif answer == 'y':
                                book(roomsTime, fromTime, toTime, element)
                                if name not in books:
                                    books[name] = [(element[0], fromTime, toTime)]
                                else:
                                    books[name].append((element[0], fromTime, toTime))
                                isBooked = True
                                print('--------------------------------------------------------------------')
                                firstAttempt = True
                                break
                        if isBooked:
                            break
                        print('There are no other rooms available for this time period')
                        toContinue = input('Do you want to book a room for this interval? y/n ')
                        if toContinue == 'n':
                            firstAttempt = True
                            break
                        elif toContinue == 'y':
                            continue
                        else:
                            print('Invalid input')
                            break
            elif nextquery == 'l':
                firstAttempt = True
                failsCounter = 0
                break