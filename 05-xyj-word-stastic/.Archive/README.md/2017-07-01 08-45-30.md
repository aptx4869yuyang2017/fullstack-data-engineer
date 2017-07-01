## 教程笔记 实战 西游记用字统计
   * str.strip()  删除空白
   * dict.iteritems()
```python
In [1]: d={1:'one',2:'two',3:'three'}

In [2]: d.items()
Out[2]: [(1, 'one'), (2, 'two'), (3, 'three')]

In [3]: d.iteritems()
Out[3]: <dictionary-itemiterator at 0x107c9aaf8>
```
* lambad
```python
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```