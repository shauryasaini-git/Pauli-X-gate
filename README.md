# X Gate

A small Python script that simulates applying the Pauli-X gate (the quantum NOT gate) to a single qubit, using NumPy state vectors.

## What it does

1. Randomly prepares the qubit in state |0⟩ or |1⟩.
2. Applies the X gate, which swaps the two amplitudes.
3. Prints the original and the resulting qubit state.

The X gate is the quantum version of a classical NOT: |0⟩ becomes |1⟩ and |1⟩ becomes |0⟩.

## Requirements

- Python 3
- NumPy

Install NumPy with:

```bash
pip install numpy
```

## Running

From the project folder:

```bash
python X_gate.py
```

## Example output

```
Initializing qubit
Applying X gate
Original qubit : [0.+0.j 1.+0.j]
New qubit: [1.+0.j 0.+0.j]
```

Each run picks |0⟩ or |1⟩ at random, so the original and new states will vary between runs.

## How it works

- **Qubit state:** a qubit is stored as a length-2 NumPy array `[a, b]`, where `a` and `b` are its amplitudes.
- **Complex amplitudes:** the arrays use `dtype=complex`, so amplitudes can be fractional or complex (for example `1/√2` or `i`), which later gates will need.
- **Gate application:** `apply_gate` multiplies the gate matrix by the state vector with `@`.
- **Copying:** `original_qubit = ket.copy()` keeps an independent copy of the starting state, so later changes to `qubit` don't affect it.

## Notes

- The script doesn't check that a state is normalized (|a|² + |b|² = 1). Passing in an unnormalized state will still run, but it isn't a valid physical qubit.
