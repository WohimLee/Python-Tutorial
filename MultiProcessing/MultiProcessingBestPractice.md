&emsp;
# MULTIPROCESSING BEST PRACTICES
torch.multiprocessing 是 Python 的 multiprocessing 多进程模块的替代
- 它支持完全相同的操作
- 进行了扩展, 所有通过 multiprocessing.Queue 发送的 Tensor 都能将其数据移入 Shared Memory，而且仅将其 handle 发送到另一个进程

>Note
- 当一个 Tensor 被发送到另一个 Process, torch.Tensor.data 和 torch.Tensor.grad 都会被共享

## 