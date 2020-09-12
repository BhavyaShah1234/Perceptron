import random
import math

inp1 = [[0, 0],
        [0, 1],
        [1, 0],
        [1, 1]]

out1 = [[0],
        [0],
        [0],
        [1]]

lr = float(input('ENTER LEARNING RATE:'))


def perceptron(inp, out, l):
    rows = len(inp)
    row_elements = len(inp[0])

    # GETTING INITIAL RANDOM WEIGHTS
    weight = []
    for i in range(rows):
        data = []
        for j in range(row_elements):
            data.append(random.random())
        weight.append(data)
    # print('WEIGHTS1:')
    # print(weight)

    # GETTING INITIAL RANDOM BIAS
    bias = []
    for i in range(rows):
        b = random.random() * 10
        bias.append([b])
    # print('BIAS:')
    # print(bias)

    """ADD LOOP HERE"""
    mse = 1
    while mse != 0:
        # MULTIPLYING INPUTS WITH WEIGHTS
        mul = []
        for i in range(rows):
            data = []
            add = 0
            for j in range(row_elements):
                m = inp[i][j] * weight[i][j]
                add = add + m
            mul.append([add])
        # print('INPUT x WEIGHT:')
        # print(mul)

        # ADDING BIAS
        for i in range(rows):
            for j in range(1):
                mul[i][j] = mul[i][j] + bias[i][j]
        # print('INPUT x WEIGHT + BIAS:')
        # print(mul)

        # APPLYING ACTIVATION FUNCTION
        for i in range(rows):
            for j in range(1):
                mul[i][j] = math.exp(mul[i][j])/(1 + math.exp(mul[i][j]))
        # print('Y PREDICTED:')
        # print(mul)
        # print('Y ACTUAL:')
        # print(out)

        # GETTING ERROR
        err = []
        mean_square_error = []
        for i in range(rows):
            for j in range(1):
                e = out[i][j] - mul[i][j]
                c = e ** 2
                err.append([e])
                mean_square_error.append([c])
        # print('ERROR:')
        # print(err)

        add = 0
        for i in range(rows):
            for j in range(1):
                add = add + mean_square_error[i][j]
        add = add / len(err)
        print(f'MEAN SQUARED ERROR:{add}')

        mse = add

        for i in range(rows):
            for j in range(row_elements):
                weight[i][j] = weight[i][j] + l * inp[i][j] * err[i][0]
        # print('WEIGHT2:')
        # print(weight)


perceptron(inp1, out1, lr)
