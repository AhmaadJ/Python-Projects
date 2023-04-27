class Case:
   def __init__(create, CPU, GPU, RAM, PSU): # __init__ uses double underscores
      create.CPU = CPU
      create.GPU = GPU
      create.RAM = RAM
      create.PSU = PSU
      
   def build(computer):
      print("System Specs: " + computer.CPU + computer.GPU + computer.RAM + computer.PSU)
      
pc = Case("Athlon 760K | ", "HD5450 | ", "8GB | ", "500W") #pc is a reference to the object of the Case class
pc.build() #object call to build method


#def __init__ is executed when the class is being initiated, assigns values to object properties
#create & computer is a reference to the current instance of a class, access class variables