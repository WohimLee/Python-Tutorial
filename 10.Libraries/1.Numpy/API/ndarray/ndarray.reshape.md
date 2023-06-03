&emsp;
# ndarray.reshape
- 重新组织shu

```py
# -1 的用法
var = np.arange(24)
res = var.reshape(-1, 2, 3)
res = var.reshape(2, -1, 3)
res = var.reshape(2, 3, -1)

print(res)
print(res.shape)
```