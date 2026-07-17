# demo_git
```python
def draw(diag, fill):
    for i in range(5):
        for j in range(5):
            if i == j or i + j == 4:
                print(diag, end = "")
            else:
                print(fill, end = "")
        print()
diag = input()
fill = input()
draw(diag, fill)
#text
```



