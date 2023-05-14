&emsp;
# 1 安装 MiniConda
- Miniconda 和 Anaconda 有同样的功能，更加轻便
- Miniconda官网：https://docs.conda.io/en/latest/miniconda.html
- 选择自己的操作系统，下载安装

<div align=center>
    <image src='imgs/minicoda.png' width=500>
</div>

&emsp;
# 2 Conda 常用命令
>获取版本号
```
conda --version
conda -V
```

>获取帮助
```shell
conda --help
conda -h

#查看某一命令的帮助，如update命令及remove命令
conda update --help
conda remove --help
```

&emsp;
# 3 环境管理

>列举当前所有环境
```shell
conda info --envs
conda env list
```

>创建指定 python 版本的环境
```shell
conda create --name [自定义环境名称] python=2.7
conda create --name [自定义环境名称] python=3
conda create --name [自定义环境名称] python=3.5
```

# 输入y确认创建。
```
>删除某个环境
```shell
conda remove --name [自定义环境名] --all
```


>进入某个环境
```shell
conda activate [自定义环境名称]
source activate [自定义环境名称]
```
>退出当前环境
```
deactivate 
```


>分享环境
- 如果你想把你当前的环境配置与别人分享，这样ta可以快速建立一个与你一模一样的环境（同一个版本的python及各种包）来共同开发/进行新的实验。一个分享环境的快速方法就是给ta一个你的环境的 .yml 文件
- 首先通过activate [自定义环境名] 进入要分享的环境[自定义环境名]，然后输入下面的命令会在当前工作目录下生成一个 pkgs.txt 文件，
    ```shell
    conda list --explicit > pkgs.txt
    ```
- 小伙伴拿到 environment.yml 文件后，将该文件放在工作目录下，可以通过以下命令从该文件创建环境
```shell
conda create --name [自定义环境名] --file pkgs.txt
```


&emsp;
# 4 包管理
>列举当前活跃环境下的所有包
```shell
conda list
```
>列举一个非当前活跃环境下的所有包
```shell
conda list -n your_env_name
```

>为指定环境安装某个包
- 方法一：推荐
    ```shell
    # 先 activate 你想装的环境
    pip install [某个包名] -i https://pypi.tuna.tsinghua.edu.cn/simple 
    ```

- 方法二：在方法一失效的情况下使用
    - 步骤：
      - 1 找到 anaconda3 文件夹
          - 先找到自己安装的 anaconda3 在哪里，Linux 默认安装为 root 目录下
          - 终端输入cd，直接回车，就会跳到根目录
          - 接上一步，ls，Linux 系统下自动安装到这个目录底下，可以看到anaconda3文件夹
      - 2 找到自己创建的虚拟环境文件夹
          - conda create 命令创建的环境都保存在 anaconda3/envs 文件夹里
          - 找到自己的环境名称的文件夹并进入该文件夹的 bin 目录，查看 bin 目录里面的文件
          - 会发现里面包含了 pip 和 pip3
          - 将这个路径保存起来（如果记得，不保存也可以）
      - 3 保存 pip 所在路径
      ```
      ~/anaconda3/envs/PyTorch/bin/pip
      ```

      - 4 使用上面得到的 pip 路径去安装包
      ```
      ~/anaconda3/envs/PyTorch/bin/pip install [包名]
      ```