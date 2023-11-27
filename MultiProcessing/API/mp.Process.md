&emsp;
# mp.Process

>函数声明
```py
mp.Process(
    group=None, target=None, name=None, 
    args=(), kwargs={}, *, 
    daemon=None)
```
- group: 预留参数
- target: 可调用对象（函数对象）, 子进程对应的活动; 相当于 mp.Process 子类化中重写的 run() 方法
- name: 为线程的名称，默认（None）为"Process-N"
- args、kwargs: 进程活动（target 函数）的参数
- deamon: bool值，表示是否为守护进程

另外还有几个子进程通用的函数：

>Process.start()
- 启动进程活动 (相当于 run()), XXX为进程实例

>Process.join(timeout = None) 
- 使主调进程（包含Process.join()语句的进程）阻塞，直至被调用进程XXX运行结束或超时（如指定timeout）