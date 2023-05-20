




enumerate



zip

map


>:=	
- 海象运算符，可在表达式内部为变量赋值。Python3.8 版本新增运算符。
```python
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
```
- 在这个示例中，使用海象运算符赋值表达式，可以避免调用 len() 两次

