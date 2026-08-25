#in class exrcises
#ex 1

numbers =[1,2,3,4,5]

squares = [
    number ** 2 
    for number in numbers 
    if number % 2 ==1
]

print(squares)


#ex 2

prices = [10,25 ,40]

prices_with_vat = [
    round(price *1.15,2)
    for price in prices
]

print(prices_with_vat)

#ex 3

scores = [42, 67 ,91 ,58 ,75]

passing_scores = [
    score
    for score in scores 
    if score >=60
]

print(passing_scores)

#ex 4
raw_names = [" sara " , " " ,"OMAR" ," lina"]

clean_name = [
    name.strip().title()
    for name in raw_names
    if name.strip()
]

print(clean_name)

#ex 5

numbers =[1,2]
letters = ["A", "B"]

pairs = [
    (number ,letter)
    for number in numbers
    for letter in letters
]

print(pairs)

# ex 6

scores = [42 ,67 ,91]

labels = [
    "pass" if score >= 60 else "retry"
    for score in scores 
]

print(labels)

# ex 7

emails =[
    "SARA@EXAMPLE.COM",
    "Omar@example.COM",
    "lina@school.sa"
]

domains = {
    email.split("@")[1].lower()
    for email in emails
    }
print(domains)

# ex 8

numbers = range(1,6)

sqr = {
    number: number ** 2
    for number in numbers
}

print(sqr)

#research

tuple = ([1,2],[7,6])
tuple[0][0]=5
print(tuple)