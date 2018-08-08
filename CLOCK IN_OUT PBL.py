import datetime
import time
from msvcrt import getch

# import cv2

# from datetime import date, time

import os.path

save_path  = "C:\\Users\\Imam\\Documents\\PROGRAMMING PROJECTS"

print("")

filename = input("Name the File: ")

# completeName = os.path.join(save_path, name_of_file + ".txt")

completeName = os.path.join(save_path, filename + ".txt")  

with open(completeName, 'w') as file1:
	while True:

		# if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
		# 	break

		name = input('\n' + "What is your name?")

		input('\n' + "Press ENTER to start the stopwatch")
		startTime = datetime.datetime.now()
		input('\n' + "Press ENTER to stop the stopwatch")
		endTime = datetime.datetime.now()

		time_out = ('\n' + "Time Out: " + str(endTime-startTime))
		print(time_out)

		student_out = ("Student Out: " + str(name))
		print(student_out)

		time_released = ("Time Released: " + str(startTime))
		print(time_released)

		time_back = ("Time Back: " + str(endTime))
		print(time_back)

		# file1.write(str(final_list))
		file1.write("Log:" + "\n")
		file1.write(str(time_out) + "\n" + str(student_out) + "\n" + str(time_released) + "\n" + str(time_back))

		print('\n' + "Do you want to continue? (ESC to exit, ENTER to continue)")

		key = ord(getch())
		if key == 27: #ESC
			break

		# if msvcrt.kbhit():
		# 	if ord(msvcrt.getch()) == 27:
		# 		break
	file1.close()


# except 
#------------------------------------------------------------------------

# import os.path

# save_path  = "C:\\Users\\Imam\\Documents\\PROGRAMMING PROJECTS"

# print("")

# filename = input("What is the name of the file: ")

# # completeName = os.path.join(save_path, name_of_file + ".txt")

# completeName = os.path.join(save_path, filename + ".txt")  

# file1 = open(completeName, "w")

# # file1.write(str(final_list))

# file1.write("Log:" + "\n" + "\n")

# file1.write(str(time_out) + "\n" + str(student_out) + "\n" + str(time_released) + "\n" + str(time_back))

# file1.close()

# time_released = datetime.datetime.now()

#------------------------------------------------------------------------

# class Timer(object):
#     """A simple timer class"""
    
#     def __init__(self):
#         pass
    
#     def start(self):
#         """Starts the timer"""
#         self.start = datetime.datetime.now()
#         return self.start
    
#     def stop(self, message="Total: "):
#         """Stops the timer.  Returns the time elapsed"""
#         self.stop = datetime.datetime.now()
#         return message + str(self.stop - self.start)
    
#     def now(self, message="Now: "):
#         """Returns the current time with a message"""
#         return message + ": " + str(datetime.datetime.now())
    
#     def elapsed(self, message="Elapsed: "):
#         """Time elapsed since start was called"""
#         return message + str(datetime.datetime.now() - self.start)

# def stopWatchSeconds(secondCnt) :
#     """ counts second for secondCnt seconds """

#     # is there a better way to do this?
#     startTime = time.clock()
#     elapsed = 0
#     for x in range(0, secondCnt, 1) :
#         print "loop cycle time: %f, seconds cnt: %02d" % (elapsed , x)
#         elapsed = 1 - (time.clock() - startTime)
#         time.sleep(elapsed)
#         startTime = time.clock()

# def stopwatch(seconds):
#     start = time.time()
#     time.clock()
#     elapsed = 0
#     while elapsed < seconds:
#         elapsed = time.time() - start
#         print("loop cycle time: %s, seconds count: %s" % (time.clock() , elapsed))
#         time.sleep(1)

#---------------------------------------------------------------------------------------

# import os
# import time


# s=0
# m=0

# while s<=60:
#     os.system('cls')
#     print (m, 'Minutes', s, 'Seconds')
#     time.sleep(1)
#     s+=1
#     if s==60:
#         m+=1
#         s=0

#---------------------------------------------------------------------------------------

# import datetime

# class Timer(object):
#     """A simple timer class"""
    
#     def __init__(self):
#         pass
    
#     def start(self):
#         """Starts the timer"""
#         self.start = datetime.datetime.now()
#         return self.start
    
#     def stop(self, message="Total: "):
#         """Stops the timer.  Returns the time elapsed"""
#         self.stop = datetime.datetime.now()
#         return message + str(self.stop - self.start)
    
#     def now(self, message="Now: "):
#         """Returns the current time with a message"""
#         return message + ": " + str(datetime.datetime.now())
    
#     def elapsed(self, message="Elapsed: "):
#         """Time elapsed since start was called"""
#         return message + str(datetime.datetime.now() - self.start)
    
#     def split(self, message="Split started at: "):
#         """Start a split timer"""
#         self.split_start = datetime.datetime.now()
#         return message + str(self.split_start)
    
#     def unsplit(self, message="Unsplit: "):
#         """Stops a split. Returns the time elapsed since split was called"""
#         return message + str(datetime.datetime.now() - self.split_start)
        
#----------------------------------------------------------------------------------------

# import os
# import time
# second = 0
# minute = 0
# hours = 0
# while(True):
#     print('\n\n\n\n\n\n\n')
#     print('\t\t\t\t-------------')
#     print('\t\t\t\t  %d : %d : %d '%(hours,minute,second))
#     print('\t\t\t\t-------------')
#     time.sleep(1)
#     second+=1
#     if(second == 60):
#         second = 0
#         minute+=1
#     if(minute == 60):
#         minute = 0
#         hour+=1;
#     os.system('cls')
    
#---------------------------------------------------------------------------------------

# import time

# class Timer:
#     def __init__(self, func=time.perf_counter):
#         self.elapsed = 0.0
#         self._func = func
#         self._start = None

#     def start(self):
#         if self._start is not None:
#             raise RuntimeError('Already started')
#         self._start = self._func()

#     def stop(self):
#         if self._start is None:
#             raise RuntimeError('Not started')
#         end = self._func()
#         self.elapsed += end - self._start
#         self._start = None

#     def reset(self):
#         self.elapsed = 0.0

#     @property
#     def running(self):
#         return self._start is not None

#     def __enter__(self):
#         self.start()
#         return self

#     def __exit__(self, *args):
#         self.stop()
        
#---------------------------------------------------------------------------------------

# import time.time() from time
# i=1
# while True:
# 	input("Press any key to start the stopwatch")
# 	startTime = datetime.datetime.now()
# 	input("Press any key to stop the stopwatch")
# 	endTime = datetime.datetime.now()
# 	print("Time Out : ", endTime-startTime)
# 	i += 1

# 	print("Student Out: ", name)
# 	print("Time Released: ", startTime)
# 	print("Time Back: ", endTime)
# 	break

# Press Ctrl+C to stop the stopwatch

#---------------------------------------------------------------------------------------

# print("Student Out: ", name)
# print("Time Released: ", time_released)
# # print("Time Out: ", time_elapsed)
# # print(stopwatch(20))

# time_back = datetime.datetime.now()

# print("Time Back: ", time_back)
