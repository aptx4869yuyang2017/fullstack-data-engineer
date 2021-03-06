## 5 实战 西游记用字统计
   * str.strip()  删除空白
   * dict.iteritems()  字典生成可迭代的对象
```python
In [1]: d={1:'one',2:'two',3:'three'}

In [2]: d.items()
Out[2]: [(1, 'one'), (2, 'two'), (3, 'three')]

In [3]: d.iteritems()
Out[3]: <dictionary-itemiterator at 0x107c9aaf8>
```
* lambad 匿名函数在排序中的使用
```python
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```
* 字典排序 sorted()
```python
>>> student_tuples = [
...     ('john', 'A', 15),
...     ('jane', 'B', 12),
...     ('dave', 'B', 10),
... ]
>>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```
参考文档 <https://docs.python.org/3/howto/sorting.html#sortinghowto>
