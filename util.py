
def swap(string, i, j):
	return (string[:i] + string[j] + string[i+1:j] + string[i]+string[j+1:])

def findMaxStr(A, k, maxarr):
	if k == 0 :
		return 
	n = len(A)
	for i in range(n-1):
		for j in range(i+1,n):
			if A[i] < A[j]:
				A = swap(A, i, j)
				if A > maxarr[0]:
					maxarr[0] = A
				findMaxStr(A, k-1, maxarr)
				A = swap(A, i, j)
def getcomb(A, k, temp, arr):

	if k ==0 :
		a =[]
		a.extend(temp)
		arr.append(a)
		return
	if k<0:
		return
	n = len(A)
	for i in range(n):
		temp.append(A[i])
		getcomb(A[i+1:],k-A[i],temp,arr)
		if k-A[i]<=0:
			temp.pop()
			break
		temp.pop()
def subset(A,temp, Out, k):
	if k == len(temp):
		a =[]
		a.extend(temp)
		Out.append(a)
		return
	for i in range(len(A)):
		temp.append(A[i])
		subset(A[i+1:],temp,Out,k)
		temp.pop()
def test(arr):
	a = []
	for i in arr:
		if i == '(':
			a.append('(')
		elif i == ')':
			if len(a)==0:
				return False
			a.pop()

	return len(a) == 0
def paranthesis(temp,out,k):
	if len(temp) == k:
		if test(temp):
			out.append(temp)
		return

	temp += '('
	paranthesis(temp,out,k)
	temp = temp[:-1]
	temp += ')'
	paranthesis(temp,out,k)
	temp = temp[:-1]
def sum4(A, B):
	out = []
	A.sort()
	n = len(A)
	for i in range(n-3):
		for j in range(i+1, n-2):
			k = j+1
			l = n-1
			while(k<l):
				c =A[i]+A[j]+A[k]+A[l]
				if c < B:
					k+=1
				elif c > B:
					l-=1
				else:
					out.append([A[i],A[j],A[k],A[l]])
					k+=1
	res = []
	for i in out:
		if i not in res:
			res.append(i)
	print res

def maxPoints(A, B):
	res = dict()
	out = -1
	n = len(A)
	for i in range(n):
		res = {}
		res['h'] = 0
		res['v'] = 0
		dup =1
		for j in range(i+1,n):
			if A[i] == A[j] and B[i] == B[j]:
				dup+=1
			elif A[j] != A[i]:
				m = float((B[j]-B[i]))/float((A[j]-A[i]))
				if m == 0:
					res['h'] +=1
				else:
					if m in res:
						res[m] +=1
					else:
						res[m] = 1
			else:
				res['v'] +=1
		for k in res:
			out = max(out, res[k]+dup)
			print(out, res[k]+dup)
		# out += dup
		print("for i = {}".format(i))
	# print(res)
	return out
def works(A, B):

	for i in A:
		if i not in B:
			return False
		elif B[i]<A[i]:
			return False

	return True
def minwindow(A, B):
	com1 = dict()
	com2 = dict()
	for i in B:
		if i not in com1:
			com1[i] = 1
		else:
			com1[i] +=1
	start = end = 0
	output = A
	l = len(A)
	while(start<l):
		if start == l:
			break
		if works(com1,com2) :
			
			if len(output)> end - start -1:
				print("hii",output)
				output = A[start:end-1]
			end = start+1
			start +=1
			com2 = {}

		elif end > start and end <=l:
			if A[end-1] in com2:
				com2[A[end-1]] += 1
			else:
				com2[A[end-1]] = 1
		
		if (end == l+1):
			end = start 
			start = start +1
			com2 = {}

		end+=1
	com2 = {}
	for i in output:
		if i not in com2:
			com2[i] = 1
		else:
			com2[i] +=1
	if works(com1,com2):
		return output
	return ""
def nmax(A, B):
	n = len(A)
	A.sort()
	B.sort()
	d = list()
	a1 = n-1
	a2 = n-1
	b1 = n-1
	b2 = n-1
	for i in range(n):
		d.append(A[a1]+B[b1])
		if A[a2]+B[b2]>A[a1]+B[b1]:
			a1 = a2
			b1 = b2
		elif (A[a1-1]+B[b1] >= A[a1]+B[b1-1]):
			a2 = a1
			a1-=1
			b2-=1
		else:
			b2 = b1
			b1-=1
			a2-=1

	return d
def findPerm(A, B):
	result = []
	mn,mx =1,B
	for x in A:
			if x == 'D':
				result.append(mx)
				mx -= 1
			elif x == 'I':
				result.append(mn)
				mn += 1
	result.append(mn)
	return result
def leader(A):
	res = []
	a = A[-1]-1
	for i in A[::-1]:
		if i>a:
			res.append(i)
			a = i
	return res

class coding:
	from math import sqrt
	def dpsol(self,dp,A,N):
		if N==1 or N==3:
			return False
		if N==2:
			return True
		# print dp,"hi"
		if (dp[N][A]!=-1):
			# print dp
			return dp[N][A]
		ans = 0
		if (A):
			ans = 0
		else:
			amd = 1

		for i in range(1,int(self.sqrt(N))+1,1):
			if N%i==0:
				if A:
					ans|=self.dpsol(dp,0,N-i)
				else:
					ans&=self.dpsol(dp,1,N-i)

		dp[N][A]= ans
		return dp[N][A]

	def divisorGame(self, N):
"""
		# :type N: int
		# :rtype: bool
"""
		dp=[]
		dp=[[-1 for i in range(2)] for j in range(N+1)]
		return self.dpsol(dp,1,N)
	def findMedianSortedArrays(self, nums1, nums2):
"""
        # :type nums1: List[int]
        # :type nums2: List[int]
        # :rtype: float
"""
        l1 = len(nums1)
        l2 = len(nums2)
        iseven=((l1+l2)%2==0)


	def solve(self, A):
		for i in range(1,20):
			if self.divisorGame(i):
				print 'A won the game'
			else:
				print 'B won the game'
# map(int,raw_input().split())
code = coding()
# A = raw_input()
# B = input()
A = 3
B = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5]
# code.solve(B)
# print ()
cp=[0 for i in range(12)]
cp[0]=1
n=5
r=2
for i in range(10):
	for j in range(i+1,0,-1):
		cp[j]=cp[j]+cp[j-1]
		if i==n-1 and j==r:
			print cp[j]


def number_gen(s):
	yield s
	yield from number_gen(s+1)

def prime_number_gen(s):
	m =next(s)
	yield m
	yield from prime_number_gen(i for i in s if i%s != 0)

c = 0
k = number_gen(2)
while True :
	if c == 10 :
		break
	print(number_gen(k))
	c = c + 1

