class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,**kwargs):
        self.name=kwargs.get('name')
        self.age=kwargs.get('age')
        self.tracks=kwargs.get('tracks')
        self.score=kwargs.get('score')
        print ('name:',self.name, 'age:',self.age , 'track:',self.tracks, 'score:',self.score )

    def change_name(self,args):
        self.name=args
        print('name:',self.name)

    def change_age(self,args):
        if(isinstance(args,int)):
            self.age=args
            print('age:',self.age)
        else:
            return print('please pass in a number')
    
    def add_track(self,args):
        self.tracks.append(args)
        print('tracks:',self.tracks)

    def get_score(self):
        return print(self.score)
        

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age('joe')
Bob.add_track("UI/UX")
Bob.get_score()
