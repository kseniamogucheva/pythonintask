#������ 8. ������� 16.
#����������� ���� "���������" (��. �.������ ������������� �� Python. ��.4) ���, ����� � ������� ����� ���������� ���������. 
#����� ������ �������� ����� �� ��������� � ��� ������, ���� � ���� ��� ������� �������������. 
#������������ ������� ���������� �����, �� ������� �� ������, ���������� ����� ��� ���������, �������� ������ ���, ��� �������� ���������..

#Mogucheva K.S.
#13.10.2016

print ("����� ���������� � ���� ���������!!!" )
print ("���� ����������� ����� ���, ����� ���������� ����������� �����." )

import random
score = 10
words = ("����������", "���������", "�����")
word = random.choice(words)
dlina = len(word)
print ("� �����", dlina, " ����." )
print ("��� ���������:" )
anagrama = list(word)
random.shuffle(anagrama)
i = 0
print(anagrama)
answer = ""
while(answer!=word):
	print("�� �������� �����?(��/���)")
	answer = str(input())
	if (answer == str("��")or answer == str("��") or answer == str("��")):
		print("�����: ")
		answer = str(input())
		if (answer == word):
			if (score < 0):
				score == 0
			print("�����! ��� ����: ", str(score))
	else:
		print("���������(��/���)")
		answer = str(input())
		if (answer == str("��")or answer == str("��") or answer == str("��")):
			print("�� ������������ ���������, �� � ��� ������� ����.", i+1, "�����: ", word[i])
			score -= 2
		else:
			print("�� ��������! ������ ���!")
			break
input ("������� Enter ��� ������.")