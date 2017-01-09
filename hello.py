class Test(object):
	def method(self):
		print 1234

test = Test()
print Test, dir(Test)
print Test.method
print Test.method(test)

print test, dir(test)
print test.method, test.method()
