#!/usr/bin/env python3
ip_=input('in ip: ')
ip_=ip_.split('.')
fi=ip_[0]
print('fi=',fi)
if int(fi)>1 and int(fi)<=223:
	print('unicast')
elif int(fi)>223 and int(fi)<240:
	print ('multicast')
elif ip_[0]=='255' and ip_[1]=='255' and ip_[2]=='255' and ip_[3]=='255': 
	print ('local broadcast')
elif ip_[0]=='0' and ip_[1]=='0' and ip_[2]=='0' and ip_[3]=='0':
	print('unassigned')
else:
	print('unused')
