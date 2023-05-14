&emsp;
# Jupyter
```shell
pip install jupyterlab
```

&emsp;
# 1 查看所有的 kernel
```shell
jupyter kernelspec list
```


&emsp;
# 2 添加 kernel
- 把自己创建的 Anaconda 虚拟环境添加到kernel

```shell
python -m ipykernel install --user --name [你创建的环境名称] --display-name "[展示在kernel的名称]"
```

&emsp;
# 3 删除 kernel
```
jupyter kernelspec remove [jupyter kernelsepc list出来的环境名]
```