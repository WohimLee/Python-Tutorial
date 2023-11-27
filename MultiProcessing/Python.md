&emsp;
# Python 多进程——Multi Processing

算法在并行环境中的性能通常由必须共享的状态数量来决定
- 如果多个 Python 进程之间没有互相通信（可以认为没有共享状态），那么通信开销并不大
- 如果每一个进程都需要和其他所有Python进程之间通信，那么通信开销会比较大，事情的处理会越来越慢，最终使整体性能下降。

Python 用于单核, 实现有效的并行化会比较困难。当我们使用 n 个核心来解决问题时, 我们的速度理论上可以达到原来的 n 倍

&emsp;
## 1 Intro
multiprocessing 模块能让我们使用基于进程和基于线程的并行处理，在 Queue 上共享任务和在进程间共享数据：
- 用进程或池对象并行化一个任务
- 用哑元模块在线程池中并行化一个I/O任务
- 用队列共享捎带的工作
- 在并行工作者之间共享状态（如字节、原生数据类型、字典和列表）


multiprocessing 相关名词

>进程 process
- 一个当前进程的派生（forked）拷贝，创建了一个新的进程标识符，并且任务在操作系统中以一个独立的子进程运行

>池
- 包装了进程或线程。在一个方便的工作者线程池中共享一块工作并返回聚合的结果

>队列 Queue
- 一个先进先出（FIFP）的队列，允许多个生产者和消费者

>管理者
- 一个单向或双向的在两个进程间的通信渠道

>ctypes
- 允许在进程派生（forked）后，在父子进程间共享原生数据类型（例如，整型数、浮点数和字节数）

>同步原语
- 锁和信号量在进程间同步控制流


&emsp;
## 2 创建子进程


def f(a, b = value):
    pass

p = multiprocessing.Process(target = f, args = (a,), kwargs = {b : value}) 
p.start()
p.join()
（2）对于要创建多个子进程的情形，更简洁的办法是采用进程池：multiprocessing.Pool(processes=None, initializer=None, initargs=(), maxtasksperchild=None)

processes ：使用的工作进程的数量，如果processes是None那么使用 os.cpu_count()返回的数量。
initializer： 如果initializer不是None，那么每一个工作进程在开始的时候会调用initializer(*initargs)。
maxtasksperchild：工作进程退出之前可以完成的任务数，完成后用一个新的工作进程来替代原进程，来让闲置的资源被释放。maxtasksperchild默认是None，意味着只要Pool存在工作进程就会一直存活。
context: 用在制定工作进程启动时的上下文，一般使用 multiprocessing.Pool() 或者一个context对象的Pool()方法来创建一个池，两种方法都适当的设置了context。
而在进程池中实际创建子进程也有几个办法：

（a）最普通的方式是直接申请：

xxx.apply(func, args=(), kwds={}, callback=None, error_callback=None) #apply对应的子进程是排队执行的，实际非并行（阻塞的，即上一个子进程完成了才能进行下一个子进程；注意是单个子进程执行的，而不是按批执行的）。xxx为进程池实例。

xxx.apply_async(func, args=(), kwds={}) #apply_async对应的每个子进程是异步执行的（即并行）。异步执行指的是一批子进程并行执行，且子进程完成一个，就新开始一个，而不必等待同一批其他进程完成。xxx为进程池实例。

func(*args,**kwds)为子进程对应的活动。
callback为回调函数（在func执行完毕后执行），其应具有一个参数，该参数为func的返回值（也即func应有一个返回值）。
同样还有几个进程池通用的方法：

XXX.close() #关闭进程池，关闭后不能往pool中增加新的子进程，然后可以调用join()函数等待已有子进程执行完毕。XXX为进程池。

XXX.join() #等待进程池中的子进程执行完毕。需在close()函数后调用。XXX为进程池。

def f(a, b = value):
    pass

pool = multiprocessing.Pool() 
pool.apply_async(f, args = (a,), kwds = {b : value})
pool.close()
pool.join()
（b）如果子进程有返回值，且返回值需要集中处理，则建议采用map方式（子进程活动只允许1个参数）：

XXX.map(func, iterable, chunksize=None) #将iterable的每个元素作为参数，应用func函数，返回函数结果组成的list，阻塞版本。func(iterable[i])为子进程对应的活动。XXX为进程池实例。

XXX.map_async(func, iterable, chunksize=None, callback=None, error_callback=None) #XXX.map()的异步（并行）版本，返回MapResult实例（其具有get()方法，获取结果组成的list）。XXX为进程池实例。

def f(a): #map方法只允许1个参数
    pass

pool = multiprocessing.Pool() 
result = pool.map_async(f, (a0, a1, ...)).get()
pool.close()
pool.join()
（c）如果内存不够用，也可采用imap迭代器方式：

XXX.imap(func, iterable, chunksize=1) #XXX.map()的迭代器版本，返回迭代器实例。XXX.imap()速度远慢于XXX.map()，但是对内存需求非常小。XXX为进程池实例。

XXX.imap_unordered(func, iterable, chunksize=1) #XXX.imap()的无序版本（不会按照调用顺序返回，而是按照结束顺序返回），返回迭代器实例。XXX为进程池实例。

def f(a): #map方法只允许1个参数
    pass

pool = multiprocessing.Pool() 
result = pool.imap_unordered(f, (a0, a1, ...))
pool.close()
pool.join()

for item in result:
    pass
（d）如果子进程活动具有多个参数，则不能直接使用map方式，需采用starmap方式：

XXX.starmap(func, iterable, chunksize=None) #类似XXX.map()，但子进程活动func允许包含多个参数，也即iterable的每个元素也是iterable（其每个元素作为func的参数），返回结果组成的list。XXX为进程池实例。

XXX.starmap_async(func, iterable, chunksize=None, callback=None, error_callback=None) #xxx.starmap()的异步（并行）版本，返回MapResult实例（其具有get()方法，获取结果组成的list）。XXX为进程池实例。

def f(a, b): #starmap方法允许多个参数
    pass

pool = multiprocessing.Pool() 
result = pool.starmap_async(f, ((a0, b0), (a1, b1), ...)).get()
pool.close()
pool.join()