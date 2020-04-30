import logging
import numpy as np   

def sigmoid(x):
    logging.info("Sigmoid function")
    return 1/(1 + np.exp(-x))

def modelOutput(score,magnitude):
    logging.info("Neural network model function")
    # Parameters
    W1 = np.array([[  0.7944864,    2.5306618,   -4.5559416,    0.3835472,    0.99691343,
    -16.251022,    -4.3798785,    8.443347,    -2.4882212,    0.18412943],
    [  1.3711807,    2.76434,     -2.2028754,    1.7946438,    0.1288933,
    -13.720011,    -4.2971883,   -8.429026,    -2.3004491,    0.82452744]])

    W2 = np.array([[  1.545527 ],
    [  2.8403213],
    [  4.8268833],
    [ -2.4048   ],
    [ -1.0374035],
    [-13.8223915],
    [ -3.170226 ],
    [ 12.88139  ],
    [  3.4203565],
    [  1.0138328]])

    b1 = np.array([[-3.2464652e+00, -4.2906141e+00,  5.2482719e-03, -1.4363248e+00,
    8.6730689e-01,  5.2704124e+00,  4.4298167e+00,  5.3570614e+00,
    -1.5046034e-02, -2.4429324e+00]])

    b2 = np.array([[0.959692]])

    # Inputs
    inputArray = np.array([[score,magnitude]])

    # Layer one output
    out1 = sigmoid(inputArray.dot(np.array(W1)) + np.array(b1))

    # Layer two output
    out2 = sigmoid(out1.dot(np.array(W2)) + np.array(b2))

    return np.round(out2,1)[0][0]

# md =modelOutput(0,0)

# print(md)



print(__name__)  