from torch.nn import functional as fct
import torch

'''
1、torch.topk
2、fct.softmax
3、torch.Tensor(1, 6)
4、_top_max_k_inds.item()的应用

'''

 # Find the top max_k predictions for each sample ,取前10项
_top_max_k_vals, top_max_k_inds = torch.topk(
    preds, 10, dim=1, largest=True, sorted=True
)

my_preds = torch.Tensor(1, 6)
my_pin = 0

n_preds = fct.softmax(my_preds, dim=1) # softmax的应用
#print("==============", my_preds, n_preds)

_top_max_k_inds.item() # 获取tensor的元素值

print(_top_max_k_vals, "==============", _top_max_k_inds)
cnt += 1

_top_max_k_inds = _top_max_k_inds.t()
