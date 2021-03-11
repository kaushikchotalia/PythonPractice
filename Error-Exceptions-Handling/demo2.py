try:
    f = open('testfile','r')
    f.write("Wire a test line")
except TypeError:
    print("There was a type error")
except OSError:
    print("Hey you have an OS error")
except:
    print("All other exception!")
finally:
    print("I always run")