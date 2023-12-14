# Performance monitor by ceon
import time

def execStart():
    startTime = time.time()
    return startTime

def exeStop():
    stopTime = time.time()
    return stopTime

def execTime(startTime, stopTime):
    return f"Execution Time: {startTime - stopTime} seconds.\n"