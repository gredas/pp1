class University():

    # object constructor (__init__ method)
    def __init__(self):
        # object attributes (object features)
        self.name = 'CUE'    

    # object methods (object behaviors)
    def print_name(self):
        print(self.name)
    def self_name(self,name):
        self.name = name
uni = University()
uni.print_name()
uni.self_name('UEK')
uni.print_name()
