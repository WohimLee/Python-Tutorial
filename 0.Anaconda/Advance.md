&emsp;
# Advance
## 1 pip 的使用

>requirements.txt
```txt
addict==2.4.0
anyio==3.5.0
argon2-cffi==21.3.0
argon2-cffi-bindings==21.2.0
argparse==1.4.0
attrs==21.4.0
babel==2.9.1
backcall==0.2.0
beautifulsoup4==4.10.0
```

>安装
```sh
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 2 Conda 的高级使用
>Conda yaml 环境文件内容
- name: 环境名称
- dependencies: 依赖项，例如您希望在创建环境时预安装的库
- channels: 下载源


### 2.1 导出与创建

>将环境导出成 yaml
- 先 activate 自己的环境
- 会生成在当前目录
    ```py
    conda env export > [自定义名称].yaml
    ```


>通过 yaml 创建环境
  ```py
  conda env create -f environment.yaml
  ```

通过这种方式创建的 conda 环境会经常碰到下载失败的问题，如何换源？

&emsp;
### 2.2 Conda 源的添加
```yaml
name: hyperparam_example
channels:
  - defaults # 还是建议使用这个
  - conda-forge
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
dependencies:
  - python=3.9
  - pip
  - numpy=1.22.2
  - click
  - pandas=1.4.1
  - scipy
  - scikit-learn=1.0.2
  - tensorflow=2.6.0
  - matplotlib=3.5.1
  - keras=2.6.0
  - mlflow=1.24.0
  - hyperopt
```


&emsp;
### 2.3 pip 源的添加
- pip 的源添加在 `pip:` 的最后一行
>pip 国内镜像源添加
```yaml
channels:
    - conda-forge
dependencies:
    - python=3.8.2
    - pip
    - pip:
      - mlflow==1.25.1
      - torchvision>=0.9.1
      - torch>=1.9.0
      - pytorch-lightning==1.6.1
      - -i https://pypi.tuna.tsinghua.edu.cn/simple
```

&emsp;
### 2.4 yaml 直接导入 requirements.txt
```yaml
name: test-env
dependencies:
  - python>=3.5
  - anaconda
  - pip
  - pip:
    - -r file:requirements.txt
```

&emsp;
### 2.5 yaml 安装 wheel 文件
- 下载 wheel 文件到 yaml 所在文件夹
```py
dependencies:
  - python>=3.5
  - anaconda
  - pip
  - pip:
    - opencv_python-3.1.0-cp35-none-win_amd64.whl
```
