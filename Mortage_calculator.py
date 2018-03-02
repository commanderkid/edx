class Mortage_Calculator(object):

    def __init__(self, *arg):
        self.P = new_line[0]   #Loan size
        self.old_P = new_line[0]
        self.R = new_line[1]    #Interest rate
        self.new_R = (self.P*self.R/12) / 100
        self.L = new_line[2]    #Length of time in months
        self.M = self.P * (1+self.R/100)/self.L
        self.shag = pow(10, new_line[3])

    def calculation(self):
        #print("{0}    {1}     {2}    {3}      {4}".format("Month", "P", "P * R/12", "-M", "new P"))
        for i in range(0, self.L):
            R_100 = (self.P*self.R/12) / 100 if (self.P*self.R/12/100%1==0) else (self.P*self.R/12) / 100
            self.new_R = (self.P*self.R/12) / 100
            new_P = self.P - self.M + self.new_R
            #print("  {1}   {0}{2}   {0}{3}   {6}{0}{4}   {0}{5}".format("$", i+1, round(self.P), round(self.new_R), round(self.M), round(new_P), "-"))
            self.P = new_P

    def new_calculation(self):
        self.calculation()
        if (self.P > 0 and self.shag >= 1):
            self.P = self.old_P
            self.M += self.shag
            return self.new_calculation()
        elif (self.P < 0 and self.shag > 1):
            self.P = self.old_P
            self.M -= self.shag
            self.shag = self.shag / 10
            return self.new_calculation()
        else:
            return print(round(self.M))

new_line = [int(i) for i in input().split()]
adder = 0
cif = new_line[0]
for i in range(cif):
    if cif > 10:
        cif = cif / 10
        adder += 1

new_line.append(adder)
#print(*new_line)
new = Mortage_Calculator(*new_line)
new.new_calculation()
