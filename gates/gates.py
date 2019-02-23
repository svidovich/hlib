def binary_and_gate(input1, input2):
	if (type(input1) != int or type(input2) != int):
		raise TypeError
	if input1 and input2:
		return 1
	else:
		return 0

def binary_nand_gate(input1, input2):
	if (type(input1) != int or type(input2) != int):
		raise TypeError
	if input1 and input2:
		return 0
	else:
		return 1

def binary_or_gate(input1, input2):
	if (type(input1) != int or type(input2) != int):
		raise TypeError
	if input1 or input2:
		return 1
	else:
		return 0

def binary_nor_gate(input1, input2):
	if (type(input1) != int or type(input2) != int):
		raise TypeError
	if input1 or input2:
		return 0
	else:
		return 1

def binary_xor_gate(input1, input2):
	if (type(input1) != int or type(input2) != int):
		raise TypeError
	if input1 and input2:
		return 0
	elif input1 and not input2:
		return 1
	elif not input1 and input2:
		return 1
	else:
		return 0

def binary_xnor_gate(input1, input2):
	if (type(input1) != int or type(input2) != int):
		raise TypeError
	if not input1 and not input2:
		return 1
	elif not input1 and input2:
		return 0
	elif input1 and not input2:
		return 0
	elif input1 and input2:
		return 1

def binary_imply_gate(input1, input2):
	if (type(input1) != int or type(input2) != int):
		raise TypeError
	if input1 and input2:
		return 1
	elif input1 and not input2:
		return 0
	elif not input1 and input2:
		return 1
	else:
		return 1

def half_adder(input1, input2):
	if (type(input1) != int or type(input2) != int):
		raise TypeError
	s = binary_xor_gate(input1, input2)
	c = binary_and_gate(input1, input2)
	return s, c

def full_adder(input1, input2, carry):
	if (type(input1) != int or type(input2) != int or type(carry) != int):
		raise TypeError
	s1, c1 = half_adder(input1, input2)
	s, c2 = half_adder(carry, s1)
	cout = binary_or_gate(c1, c2)
	return s, cout


