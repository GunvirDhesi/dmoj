numQuestions = int(input())

for i in range(numQuestions):
	triangleLen = input().split()
	triangleLen = [int(x) for x in triangleLen]
	triangleLen.sort()

	def ritri():
		ans = (triangleLen[0]**2+triangleLen[1]**2)**0.5
		return ans

	if triangleLen[2] == ritri():
		print("R")
	elif triangleLen[2] > ritri():
		print("O")
	else:
		print("A")