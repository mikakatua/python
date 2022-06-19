# The Counter challenge
Create a class named `Counter` which implements a simple counter. The class definition is as follows:
- It has a constructor which allows to initialize the counter with a value (by default 0)
- It has the property `value` which contains the current value of the counter
- It has a method `up` which increases the current value by 1
- It has a method `down` which decreases the current value by 1

Next, create a small program which uses the Counter class. The program logic is the following:
- Create two counters, the first with the initial value 0 and the second with the value 10
- Execute a loop which in each iteration:
  - increases the first counter
  - decreases the second counter
  - print the value of both counters (in one line)
- Exit the loop when the values of both counters are the same

The output of the script will be the following:
```
1 9
2 8
3 7
4 6
5 5
```