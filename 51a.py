#!/usr/bin/env python3
from sys import argv

net_mask_templ='''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
mask_templ='''
{0:<8}
{1:<8} {2:<8} {3:<8} {4:<8}
{1:08b} {2:08b} {3:08b} {4:08b}
'''
net_mask = argv[1]
net_=net_mask[:net_mask.find('/')]
mask_=net_mask[net_mask.find('/'):]
net_=net_.split('.')
print(net_mask_templ.format(int(net_[0]),int(net_[1]),int(net_[2]),int(net_[3])))
print(mask_templ.format(mask_,int(255),int(255),int(255),int(0)))
