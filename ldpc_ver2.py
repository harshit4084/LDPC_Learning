import numpy as np

# Initialization
	def init():
		# input from user value of 
		n size of encoded bits
		k size of non redundant bits
		m = n-k

		# Use modulo 2
		 gen_matrix = []
		 parity_matrix = []
		 neg_pt = []

		 # Call a function here that creates P matrix using simple loops

		 # take  transpose and take negative to get neg_pt 

		 gen_matrix.append(np.identity(k))
		 gen_matrix.append(p)
		 parity_matrix.append(neg_pt)
		 parity_matrix.append(np.identity(n-k))

		 return (gen_matrix,parity_matrix)

def encode(input_bit_stream,gen_matrix):

	# multiply input_bit_stream with gen_matrix

	# 1. check for incorrect dimension
	# 2. do a for loop for to multiply each value input_bit_stream with gen_matrix 
	# 3. do a module for each multiplication.(Modulo can be either 2 or 256)
	# 4. save the result in corresponding entry in encoded_se
	return encoded_se # with lenght n

def decode(encoded_seq,parity_matrix):

	# multiply input_bit_stream with parity_matrix

	# If some value is missing these value has to be resolve

	# To get value of missing symbol (Solving system of equation. gauss elim method)
	# 1. Create a new_matrix simmilar to parity_matrix
	# 2. check for a symbol. if it is valid multiply it with corresponding parity_matrix row
	# 3. put this value into new_matrix and solve it.
	# 4. put symbol back in position

	return decoded_se # with lenght k


if __name__ == '__main__':
	gen_matrix,parity_matrix = init();
	encoded_se = encode(input_bit_stream,gen_matrix)
	decoded_se = decode(encoded_seq,parity_matrix)
