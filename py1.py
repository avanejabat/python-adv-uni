import requests as r
l=r.get("https://cdn.ituring.ir/ex/users.json").json

class fetcher: 


    def nerds(self):
        names=set()
        for students in self.l:
            if students.get('score')>18.5:
                return[students.get('name')+students.get('last_name')]
            
    def mean(self):
        scores=[l.get('score')]
        for students in l :
            m=sum('score')/len('score')
            return m

    def sultans(self):
        maxscore= max (l.get('score'))
        for students in l :
         return[students.get('name')+students.get('last_name')] 

n=fetcher()

print(n.nerds())

