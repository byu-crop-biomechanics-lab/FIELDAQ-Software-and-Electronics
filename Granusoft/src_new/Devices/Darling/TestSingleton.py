class TestSingleton:
    class __TestSingleton:
        def __init__(self):
            self.clear_all()
        def clear_all(self):
            self.height = ""
            self.plot = ""
            self.pre_notes = ""
            self.post_notes = []
            self.operator = ""
            self.timestamp = ""
            self.datasets = []
            self.break_height = ""
    instance = None
    def __init__(self):
        if not TestSingleton.instance:
            TestSingleton.instance = TestSingleton.__TestSingleton()

    def clear_all(self):
        self.instance.clear_all()

    def print_test(self):
        print("Timestamp:", self.instance.timestamp)
        print("Height:", self.instance.height)
        print("Plot:", self.instance.plot)
        print("Operator:", self.instance.operator)
        print("Break Height:", self.instance.break_height)
        print("Pre Notes:", self.instance.pre_notes)
        print("Post Notes:", self.instance.post_notes)
        print("First Dataset Temp:", self.instance.datasets[0].temperature)
        print("Second Dataset Temp:", self.instance.datasets[1].temperature)

    def get_height(self):
        return self.instance.height

    def set_height(self, height):
        self.instance.height = height

    def get_plot(self):
        return self.instance.plot

    def set_plot(self, plot):
        self.instance.plot = plot

    def get_pre_notes(self):
        return self.instance.pre_notes
        
    def set_pre_notes(self, pre_notes):
        self.instance.pre_notes = pre_notes

    def get_post_notes(self):
        return self.instance.post_notes

    def set_post_notes(self, post_notes):
        self.instance.post_notes = post_notes

    def get_operator(self):
        return self.instance.operator
    def set_operator(self, operator):
        self.instance.operator = operator

    def get_timestamp(self):
        return self.instance.timestamp
    def set_timestamp(self, timestamp):
        self.instance.timestamp = timestamp

    def get_datasets(self):
        return self.instance.datasets
    def set_datasets(self, datasets):
        self.instance.datasets = datasets

    def get_break_height(self):
        return self.instance.break_height
    def set_break_height(self, break_height):
        self.instance.break_height = break_height

#class Dataset:
#    def __init__(self, name, test):
#        self.name = name
#        self.number = test

#a = TestSingleton()
#a.set_height("tall")
#d1 = Dataset("ben", "1")
#d2 = Dataset("sarah", "2")
#datasets1 = []
#datasets1.append(d1)
#datasets1.append(d2)
#a.set_datasets(datasets1)
#print("a is",a.get_height())
#print(a.get_datasets()[0].name)
#b = TestSingleton()
#b.set_height("short")
#d3 = Dataset("alexander", "3")
#d4 = Dataset("quigley", "4")
#datasets2 = []
#datasets2.append(d3)
#datasets2.append(d4)
#b.set_datasets(datasets2)
#b.clear_all()
#print("b is",b.get_height())
#print(b.get_datasets()[0].name)
#print("a is",a.get_height())
#print(a.get_datasets()[0].name)
