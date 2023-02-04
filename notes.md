# LSTM_text_classification

- DataLoader中的collate_fn
- 中文字和索引的映射实现vocab类
- 返回类实例的return cls()

## pad_sequence, pack_padded_sequence

```
from torch.nn.utils.rnn import pad_sequence, pack_padded_sequence
import torch
import torch.nn as nn

inputs = [torch.tensor([1,2,3]),torch.tensor([7,8,9,7])]
#将一个batch中不同长度的数据补成同样长度,不设定就补0
out = pad_sequence(inputs, batch_first=True)
print('out:',out)

embeddings = nn.Embedding(10, 5)
embedding = embeddings(out)
print('embedding:',embedding)

#压缩padding后的张量，并维护一个标记batch中每个句子长度的列表
x_pack = pack_padded_sequence(embedding, torch.tensor([3,4]), batch_first=True, enforce_sorted=False)
print('x_pack',x_pack)
```

![QQ截图20230130210636](https://pic-1316661979.cos.ap-beijing.myqcloud.com/pic-resource/QQ%E6%88%AA%E5%9B%BE20230130210636.png)
