# Part 1 - Integration
import requests
import re

urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
]

# Part 1 - Integration
# https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Integral_approximations-3-steps.png/320px-Integral_approximations-3-steps.png
def anonymous(x):
    return x**2 + 1
def integrate(fun, start, end):
    step = 0.1
    intercept = start
    area = 0
    while intercept < end:
        intercept += step
        ''' your work here '''
    return area

print(integrate(anonymous, 0, 10))

# Part 1 - Multiples of 3 and 5
print(sum(i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0))
