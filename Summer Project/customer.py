from collections import deque, defaultdict
from transaction import TransactionStack

class Customer:
    def __init__(self, name, degree, faculty, course_number):
        self.name = name
        self.degree = degree
        self.faculty = faculty
        self.course_number = course_number

class CustomersQueue:
    def __init__(self, stack):
        self.queue = deque()
        self.history = []
        self.stack = stack

    def push(self, customer, key, value):
        self.history.append([key, str(value)])
        self.queue.append([customer, key, str(value)])

    def most_popular_request(self):
        keys = ["title", "author", "price", "isbn"]
        result = []
        for key in keys:
            count = defaultdict(int)
            value = ""
            mx = -1
            for tp in self.history:
                if tp[0] == key:
                    count[tp[1]] += 1
                    if count[tp[1]] > mx:
                        value = tp[1]
                        mx = count[tp[1]]
            
            if value == "":
                result.append("No any request with " + key + " ever made")
            else:
                result.append("Most popular request by " + key + " is: " + str(value))    
        
        return result    
    
    def done(self):
        if self.queue:
            transaction = self.queue.popleft()
            self.stack.push([transaction[1], transaction[2]])

        return None