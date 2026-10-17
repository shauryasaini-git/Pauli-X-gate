import numpy as np

num_options = [1, 0]
num = np.random.choice(num_options)
if num == 1:
    ket = np.array([0, 1], dtype=complex) #ket 1
else:
    ket = np.array([1, 0], dtype=complex) #ket 0

X_gate = np.array([[0, 1], [1, 0]])

def apply_gate(gate, qubit):
    return gate @ qubit

def main():
    print("Initializing qubit")
    qubit = ket
    original_qubit = ket.copy()

    print("Applying X gate")
    qubit = apply_gate(X_gate, qubit)

    print(f"Original qubit : {original_qubit}")
    print(f"New qubit: {qubit}")

if __name__ == "__main__":
    main()