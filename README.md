# Intro to Python - Quiz - Week 2

This small quiz is just for validating the concepts covered during the first week of our course. It's **not something you can pass or fail**. We use the results of this quiz to evaluate if we need to add more support sessions or improve any aspect of the course.

**PLEASE, don't cheat**. Make it honest. We'll never share the data with the rest of the class.

_To complete this quiz, fork the repo, work on the questions under quiz-questions/ and submit a Pull Request_

#### Question 1

Take a look at the following code and answer:

```python
a = 10
b = 3
c = 7


def test_scope(b):
    a = 11
    return a + b + c

c = c + test_scope(5)
```

What will be the final value of the variable `c`?

##### Options:

```
a) 23
b) 30
c) 29
d) 28
e) None  # The function gets into an infinite loop
```

**IMPORTANT**: Return the actual value as shown in the options. **DO NOT surround it with quotes**. Example, if you think that `23` is the correct answer, you should put `return 23`. Again, **DON'T use quotes**, and **DON'T** use the option number (`return a`, `return "a)"`, `return "a"`, etc).


#### Question 2

Write a function `number_of_customers_per_state` that receives a dictionary containing states (as keys) and customers for those states (as a list of dictionaries) and returns a final dictionary containing the count of customers per state.

Example:

```python
customers = {
    'UT': [{
        'name': 'Mary',
        'age': 28
    }, {
        'name': 'John',  # Eldest
        'age': 31
    }],
    'NY': [{
        'name': 'Linda',  # Eldest
        'age': 71
    }]
}
number_of_customers_per_state(customers)
```

Should return:

```python
{
    'UT': 2,
    'NY': 1
}
```

#### Question 3

Write a function `eldest_customer_per_state` that receives a dictionary containing states (as keys) and customers for those states (as a list of dictionaries) and returns a final dictionary containing the eldest customer per each state.

Example:

```python
customers = {
    'UT': [{
        'name': 'Mary',
        'age': 28
    }, {
        'name': 'John',  # Eldest
        'age': 31
    }],
    'NY': [{
        'name': 'Linda',  # Eldest
        'age': 71
    }, {
        'name': 'Lisa',
        'age': 25
    }]
}
eldest_customer_per_state(customers)
```

Should return:

```python
{
    'UT': {
        'name': 'John',
        'age': 31
    },
    'NY': {
        'name': 'Linda',
        'age': 71
    }
}
```
