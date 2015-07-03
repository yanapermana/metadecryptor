def decryptPediaphone(cipher):
	pediaphon = ['2','22','222','3','33','333','4','44','444','5','55','555','6','66','666','7','77','777','7777','8','88','888','9','99','999','9999','0000','11111','2222','3333','4444','5555','6666','77777','8888','99999','0','00','000','1','11','111','1111']
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',' ','.','?','!',':',';','#']
	
	myList = cipher.split()
	myArr = []
	for i in range(0, len(myList), 1):
		for j in range(0, len(pediaphon), 1):
			if myList[i] == pediaphon[j]:
				myArr.append(alphabet[j])
	return ''.join(myArr)

if __name__ == '__main__':
	cipher = '3 444 0 22 2 555 444 55 0 8 444 777 2 444 0 6 33 777 2 44'
	print(decryptPediaphone(cipher))