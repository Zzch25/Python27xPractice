#Zachary Job
#12/4/2012
#https://www.cs.hmc.edu/twiki/bin/view/ModularCS1/DateClass!
#http://wiki.answers.com/Q/How_many_days_in_each_month

class Date:
    """ a user-defined data structure that
        stores and manipulates dates
    """

    # the constructor is always named __init__ !
    def __init__(self, month, day, year):
        """ the constructor for objects of type Date """
        self.month = month
        self.day = day
        self.year = year


    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        """
        s =  "%02d/%02d/%04d" % (self.month, self.day, self.year)
        return s


    # here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """ Returns True if the calling object is
            in a leap year; False otherwise. """
        if self.year % 400 == 0: return True
        elif self.year % 100 == 0: return False
        elif self.year % 4 == 0: return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        """ Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.
        """
        return self.year == d2.year and self.month == d2.month and self.day == d2.day

    def tomorrow(self):
        """ups date to next date"""
        DIM = [0,31,28,31,30,31,30,31,31,30,31,30,31] # days in month arranged by month and list order to match
        
        if self.isLeapYear() == True: # modify m2 as it is increased a single day on a leap year
            DIM[2] += 1

        if self.day == DIM[self.month]: # if day limit exceeded
            if self.month == 12: # end year
                self.month = 1
                self.year += 1
            else:
                self.month += 1
            self.day = 1
            return
        self.day += 1 # plenty-o'-days to continue incrementing
        return

    def yesterday(self):
        """backs date to last date"""
        DIM = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        
        if self.isLeapYear() == True:
            DIM[2] += 1

        if self.day == 1: # if day minimum exceeded
            if self.month == 1: # beg year
                self.month = 12
                self.year -= 1
                self.day = DIM[12]
            else:
                self.month -= 1
                self.day = DIM[self.month]
            return
        self.day -= 1 # plenty-o'-days to continue decrementing
        return

    def addNDays(self, N):
        """moves to calendar date x days forward"""
        for days in range(N):
            self.tomorrow()

    def subNDays(self, N):
        """moves to calendar date x days backward"""
        for days in range(N):
            self.yesterday()

    def isBefore(self, d2):
        """checks if input is after compared object"""
        if self.year < d2.year: # check year
            return True
        elif self.year == d2.year:
            if self.month < d2.month: # else check month
                return True
            elif self.month == d2.month:
                if self.day < d2.day: # else check day
                    return True
        return False

    def isAfter(self, d2):
        """checks if input is before compared object"""
        if self.isBefore(d2) == False and self.equals(d2) == False:
            return True
        return False

    def diff(self, d2):
        """returns days between object and input"""
        temp = self.copy()
        
        if temp.equals(d2):
            return 0
        if temp.isBefore(d2) == True:
            count = 0
            while temp.equals(d2) == False:
                temp.tomorrow()
                count += 1
            return count
        if temp.isAfter(d2) == True:
            count = 0
            while temp.equals(d2) == False:
                temp.yesterday()
                count += 1
            return count*-1
        return "Danger Will Robinson!"

    def dow(self):
        """returns day of week"""
        dofw = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        temp = Date(11,6,2011)
        differ = (7 - (self.diff(temp) % 7)) # if not Sunday, gives corresp. day #
        if differ == 7: differ = 0 # if Sunday

        return dofw[differ]

#################################################################################SYSTEM.OUT.PRINT!
##################################################################################################

def prBr():
    print "-----------"

def prSp():
    print
    print

print "Test Tomorrow"
print "#1"
d = Date(12,31,2010)
print d
d.tomorrow()
print d
print "#2"
d = Date(2,28,2012)
print d
d.tomorrow()
print d
d.tomorrow()
print d

prSp()

print "Test Yesterday"
print "#1"
d = Date(1,1,2011)
print d
d.yesterday()
print d
print "#2"
d = Date(3,1,2012)
print d
d.yesterday()
print d
d.yesterday()
print d

prSp()

print "Test addNDays"
print "#1 - 3"
d = Date(11,9,2011)
print d
d.addNDays(3)
print d
print "#2 - 1283"
d = Date(11,11,2011)
print d
d.addNDays(1283)
print d

prSp()

print "Test subNDays"
print "#1 - 3"
d = Date(11,12,2011)
print d
d.subNDays(3)
print d
print "#2 - 1283"
d = Date(5,17,2015)
print d
d.subNDays(1283)
print d

prSp()

print "Test isBefore"
d = Date(11,11,2011)
print "d: " + str(d)
d2 = Date(1,1,2012)
print "d2: " + str(d2)
prBr()
print "#1 - d:d2"
print d.isBefore(d2)
print "#2 - d2:d"
print d2.isBefore(d)
print "#3 - d:d"
print d.isBefore(d)

prSp()

print "Test isAfter"
d = Date(11,11,2011)
print "d: " + str(d)
d2 = Date(1,1,2012)
print "d2: " + str(d2)
prBr()
print "#1 - d:d2"
print d.isAfter(d2)
print "#2 - d2:d"
print d2.isAfter(d)
print "#3 - d:d"
print d.isAfter(d)

prSp()

print "Test diff"
d = Date(11,9,2011)
print "d: " + str(d)
d2 = Date(12,16,2011)
print "d2: " + str(d2)
prBr()
print "#1 - d:d2"
print d.diff(d2)
print "#2 - d2:d"
print d2.diff(d)
prBr()
print "d: " + str(d)
print "d2: " + str(d2)

prSp()

print "Test dow"
print "#1"
d = Date(12, 7, 1941)
print d
print d.dow()
print "#2"
d = Date(10, 28, 1929)
print d
print d.dow()
print "#3"
d = Date(10, 19, 1987)
print d
print d.dow()
print "#4"
d = Date(1, 1, 2100)
print d
print d.dow()
print "#5"
d = Date(1, 2, 2100)
print d
print d.dow()
print "#6"
d = Date(1, 3, 2100)
print d
print d.dow()
print "#7"
d = Date(1, 4, 2100)
print d
print d.dow()
print "#8"
d = Date(1, 5, 2100)
print d
print d.dow()
print "#9"
d = Date(1, 6, 2100)
print d
print d.dow()
print "#10"
d = Date(1, 7, 2100)
print d
print d.dow()
print "#11"
d = Date(1, 8, 2100)
print d
print d.dow()
