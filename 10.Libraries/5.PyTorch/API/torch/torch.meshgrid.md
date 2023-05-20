&emsp;
# torch.meshgrid()
- 用来生成每个像素对应的坐标点对

```py
import torch
img_height = 4
img_width  = 5
uarange = torch.arange(img_height, dtype=torch.float32, device='cpu')
varange = torch.arange(img_width, dtype=torch.float32, device='cpu')
```


```py
u, v = torch.meshgrid(uarange, varange)
```


```py
coords = torch.stack((x, y), dim=-1).reshape(-1, 3)
```