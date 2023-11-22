# 範例程式的 Bug 猜測及 Debug 嘗試

## Bug 猜測

根據[範例程式](https://github.com/ccc112a/py2cs/blob/master/02-%E6%BC%94%E7%AE%97%E6%B3%95/02-%E6%96%B9%E6%B3%95/02a-%E5%88%97%E8%88%89%E6%B3%95/03-permutation/permutation.py)中的註解

> \# 思考：排到一半 p=[1,3] 繼續排下去<br/>
\# 對 [1,3,0..], [1,3,1..], [1,3,2..], [1,3,3..] 全部試一遍

嘗試輸出 `perm(2)` 及 `perm(3)`

_perm(2)_
```
[1, 3]
```

_perm(3)_
```
[1, 3, 0]
[1, 3, 2]
```

## Debug 嘗試

[還沒改](./permutation.py)