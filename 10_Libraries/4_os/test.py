import os
for root, dirs, files in os.walk(".", topdown=False):
    for name in files: # 打印所有文件从 root 开始的路径
        print(os.path.join(root, name))
    # for name in dirs:  # 打印所有文件夹从 root 开始的路径
    #     print(os.path.join(root, name))