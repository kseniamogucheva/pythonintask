#������ 6. ������� 16.
#�������� ����, � ������� ��������� ���������� ��� ����� �� ����� ����������� ��� ����� IV ��������, � ����� ������ ��� �������.

#Mogucheva K.S.
#29.09.2016

import random

 zhen = ['��������� ���������',
	 '����� ����������',
	 '����� ��������',
	 '���� ����������',
	 '���� ������������', 
	 '����� �����'
		]
 
random_zhen = random.choice(zhen)
print('��������� ��������� ������� ���������� �������� ����� �� ����� ����������� ��� ����� IV ��������, � ����� ������ ��� �������.')
print('���� ����� IV ��������:', end=' ')

for x in zhen:
	print(x, end=" ")
print()
vibr_zhena = input('������� ���� �� ��� ����� IV ��������')
print()
if vibr_zhena == random_zhen:
	print('���������!!!')
else:
	print('�� �� �������!!!')
	print('���������� �����:', random_zhen)
input("\n\nHa����e Enter. ����� �����.")