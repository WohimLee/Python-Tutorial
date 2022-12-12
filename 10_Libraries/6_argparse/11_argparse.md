&emsp;
# argparse


&emsp;
# 1 argparse介绍
官方文档：https://docs.python.org/zh-cn/3/library/argparse.html#argumentparser-objects

argparse 模块是 Python 内置的一个用于命令项选项与参数解析的模块，argparse 模块可以让人轻松编写用户友好的命令行接口。通过在程序中定义好我们需要的参数，然后 argparse 将会从 sys.argv 解析出这些参数。argparse 模块还会自动生成帮助和使用手册，并在用户给程序传入无效参数时报出错误信息。


&emsp;
# 2 argparse基本使用

```python
import argparse

parser = argparse.ArgumentParser(description='test')

parser.add_argument('--sparse', action='store_true', default=False, help='GAT with sparse version or not.')
parser.add_argument('--seed', type=int, default=72, help='Random seed.')
parser.add_argument('--epochs', type=int, default=10000, help='Number of epochs to train.')

args = parser.parse_args()
print(args.sparse)
print(args.seed)
print(args.epochs)
```

>三个步骤：

- 1、创建一个解析器——创建 ArgumentParser() 对象
- 2、添加参数——调用 add_argument() 方法添加参数
- 3、解析参数——使用 parse_args() 解析添加的参数

&emsp;
## 2.1 创建一个解析器——创建 ArgumentParser() 对象
- 使用 argparse 的第一步是创建一个 ArgumentParser 对象：
```python
parser = argparse.ArgumentParser(description='test')
```
- ArgumentParser： 对象，包含将命令行解析成 Python 数据类型所需的全部信息。
- description： 大多数对 ArgumentParser 构造方法的调用都会使用 description= 关键字参数。这个参数简要描述这个程度做什么以及怎么做。在帮助消息中，这个描述会显示在命令行用法字符串和各种参数的帮助消息之间。

&emsp;
## 2.2 添加参数——调用 add_argument() 方法添加参数
- 给一个 ArgumentParser 添加程序参数信息是通过调用 add_argument() 方法完成的。通常，这些调用指定 ArgumentParser 如何获取命令行字符串并将其转换为对象。这些信息在 parse_args() 调用时被存储和使用。

- args分为可选参数（用--指定）和必选参数（不加--指定）。如果你定义参数xxx时，没有用--指定，那么该参数为需要在命令行内手动指定。此时即使通过default设置默认参数，也还是会报错。

- --max_episode_len，写成--max-episode-len，在调用的时候用的是args.max_episode_len，也没报错，在这里-对应_，表示同一个意思，代码里写的不一样或者都改成一样的都可以

>语法
```python
ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
```

>参数
- name or flags - 选项字符串的名字或者列表，例如 foo 或者 -f, --foo。
- action - 命令行遇到参数时的动作，默认值是 store。
- nargs - 应该读取的命令行参数个数，可以是具体的数字，或者是?号，当不指定值时对于 Positional argument 使用 default，对于 Optional argument 使用 const；或者是 * 号，表示 0 或多个参数；或者是 + 号表示 1 或多个参数。
- const - action 和 nargs 所需要的常量值。
- default - 不指定参数时的默认值。
- type - 命令行参数应该被转换成的类型。
- choices - 参数可允许的值的一个容器。
- required - 可选参数是否可以省略 (仅针对可选参数)。
- help - 参数的帮助信息，当指定为 argparse.SUPPRESS 时表示不显示该参数的帮助信息.
- metavar - 在 usage 说明中的参数名称，对于必选参数默认就是参数名称，对于可选参数默认是全大写的参数名称.
- dest - 解析后的参数名称，默认情况下，对于可选参数选取最长的名称，中划线转换为下划线.

>示例
```python
parser.add_argument('--sparse', action='store_true', default=False, help='GAT with sparse version or not.')
parser.add_argument('--seed', type=int, default=72, help='Random seed.')
parser.add_argument('--epochs', type=int, default=10000, help='Number of epochs to train.')
```

&emsp;
## 2.3 解析参数
ArgumentParser 通过 parse_args() 方法解析参数。它将检查命令行，把每个参数转换为适当的类型然后调用相应的操作。在大多数情况下，这意味着一个简单的 Namespace 对象将从命令行解析出的属性构建：
```python
args = parser.parse_args()
```
在脚本中，通常 parse_args() 会被不带参数调用，而 ArgumentParser 将自动从 sys.argv 中确定命令行参数。

&emsp;
# 3 YOLOv5 运用实例


>yolov5中detect.py的使用
```python
import argparse

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='yolov5s.pt', help='model path(s)')
    parser.add_argument('--source', type=str, default='data/images', help='file/dir/URL/glob, 0 for webcam')
    parser.add_argument('--imgsz', '--img', '--img-size', nargs='+', type=int, default=[640], help='inference size h,w')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='NMS IoU threshold')
    parser.add_argument('--max-det', type=int, default=1000, help='maximum detections per image')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--view-img', action='store_true', help='show results')
    parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
    parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
    parser.add_argument('--save-crop', action='store_true', help='save cropped prediction boxes')
    parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--visualize', action='store_true', help='visualize features')
    parser.add_argument('--update', action='store_true', help='update all models')
    parser.add_argument('--project', default='runs/detect', help='save results to project/name')
    parser.add_argument('--name', default='exp', help='save results to project/name')
    parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
    parser.add_argument('--line-thickness', default=3, type=int, help='bounding box thickness (pixels)')
    parser.add_argument('--hide-labels', default=False, action='store_true', help='hide labels')
    parser.add_argument('--hide-conf', default=False, action='store_true', help='hide confidences')
    parser.add_argument('--half', action='store_true', help='use FP16 half-precision inference')
    opt = parser.parse_args()
    return opt


def main(opt):
    # print(colorstr('detect: ') + ', '.join(f'{k}={v}' for k, v in vars(opt).items()))
    # check_requirements(exclude=('tensorboard', 'thop'))
    # run(**vars(opt))
    opt_dict = vars(opt)
    opt_dictitems = opt_dict.items()
    print(type(opt_dict))
    for k, v in opt_dictitems:
        print(k)
        print(v)
        break
    # print(opt_dict)
    print("---------------------------------")
    print(type(opt_dictitems))
    for k, v in opt_dictitems:
        print(k)
        print(v)
        break
    # print(opt_dictitems)


if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
```