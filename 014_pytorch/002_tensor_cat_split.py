#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 18:00
# @Author  : Scheaven
# @File    :  test001.py
# @description:
import torch
from torch import nn

#
# model = torch.load("mymodel.pth")
# traced_script_module = torch.jit.script(model)
# traced_script_module.save("model.pt")

def torch_cat(x):
    xa = x[0]
    for i in range(x[1].size()[2] // x[0].size()[2] - 1):
        xa = torch.cat((xa, x[0]), 2)

    xb = x[1]
    for i in range(x[0].size()[1] // x[1].size()[1] - 1):
        xb = torch.cat((xb, x[1]), 1)

    # print(":::N::  ",x[1].size()[2] // x[0].size()[2], " : " ,x[0].size()[1] // x[1].size()[1])
    # exit()
    y = torch.cat((xa, xb), 0)

    return y


# x = x.expand(*size)
# x = x.expand_as(y)# y:[3,4

a = torch.rand([1, 3, 8, 256, 256])
b = torch.rand([1, 3, 32, 256, 256])

y = torch_cat([a, b]) # 合并

# 切分
xa, xb = y.split(1, dim=0)
xa1 = xa.split(8, dim=2)[0]  # 切分，每8个一份
xb1 = xb.chunk(8, dim=1)[0]  # 均匀切成八份，如果为奇数，最后一份为单份

z = torch_cat([xa1,xb1])