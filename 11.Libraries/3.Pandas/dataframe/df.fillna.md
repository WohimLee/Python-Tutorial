&emsp;
# df.fillna


>示例 3：填充 NaN 值
```python
data = {"grammer":["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
       "score":[1,2,np.nan,4,5,6,7,10]}
df = pd.DataFrame(data)
df.fillna(0,inplace=True)
print(df,'\n')
```

