# Coding Problem Study Guide
## 0. Bitwise Operations
- emphasis on 'wise'. These are performed bit by bit, so componentwise. 
- https://realpython.com/python-bitwise-operators/ 

Operators are special symbols that designate that some sort of computation should be performed. There are several kinds including  arithmetic, logical, and comparison operators.

### Operator Defintions
#### How many?
- Unary: 1 operand
- Binary: 2 operands
- Ternary: 3 operands

#### Where?
- Prefix notation: operator goes before operand(s)
- Infix notation: operator goes between operand(s)
- Postfix notation: operator goes after operand(s)

[Augmented Assignment](https://peps.python.org/pep-0203/) performed by compound operators. E.g. += -= *= /= %= **= <<= >>= &= ^= |=


AND (logical conjunction)
||0|1|
|-|-|-|
|0|0|0
|1|0|1

- Arithmetic interpretation: component-wise multiplication: $(a&b)_i = a_i*b_i$ 
- Set interpretiation: Intersection of the two bits, with empty set resulting in 0.
- Alternatively, take the minimum of each bit pair.

OR (logical disjunction)
||0|1|
|-|-|-|
|0|0|1
|1|1|1

- Arithmetic interpretation: component-wise addition without intersection: $(a|b)_i = a_i + b_i - a_i*b_i$
- Set interpretiation: Union of the two bits
- Alternatively, take the maximum of each bit pair.

XOR (exclusive disjunction)
||0|1|
|-|-|-|
|0|0|1
|1|1|0

- Arithmetic interpretation: component-wise addition mod 2: $(a_i$ ^  $b)_i = a_i+b_i$ (mod 2)
- Set interpretiation: Symmetric difference of the two bits
- Mutually exclusive conditions and tells you whether exactly one of them is met. 

Bitwise Not (logical negation)
- Arithmetic interpretation: component-wise subtraction from 1: ~$a_i = 1-a_i$
- Flips all the bits of a number. The inverted bits are a complement to one, which turns zeros into ones and ones into zeros.
- only unary bitwise operator

Signed vs Unsigned Ints
Signed integers need an extra bit to represent the sign. This leads to either just having a single bit represent sign, using the 1's complement method, or the two's complement method. 

[Two's Complement Part 1 - An Introduction](https://www.youtube.com/watch?v=9W67I2zzAfo)
[Two's Complement Part 2 - An Introduction](https://www.youtube.com/watch?v=Hof95YlLQk0)


Bitwise shift left
- shift all digits left by one position and append 0 to the right of the binary string
- Shifting a single bit to the left by one place doubles that bits value. As a result, the entire number gets doubled as well. In general, shifting n positions to the left multiplies the value of the givben number by $2^n$
- a << n = $a \times 2^n$

Bitwise shift right
- shift all digits right by one position and drop the rightmost digit
- Shifting a single bit to the right by one place halves that bits value. As a result, the entire number gets halved as well, rounded down. In general, shifting n positions to the left divides the value of the givben number by $2^n, and rounds down$
- a >> n = $\left \lfloor{\frac{a}{2^n}}\right \rfloor $
- It’s virtually the same as a floor division by a power of two


Bitmasks
A bitmask works like a graffiti stencil that blocks the paint from being sprayed on particular areas of a surface. It lets you isolate the bits to apply some function on them selectively. Bitmasking involves both the bitwise logical operators and the bitwise shift operators that you’ve read about.

Getting a bit: use the bitwise AND against a bitmask composed of only one bit at the desired index
value & (1 << bit_index). In this example, (1 << bit_index) is the bitmask.

Setting a bit: Setting a bit is similar to getting one. You take advantage of the same bitmask as before, but instead of using bitwise AND, you use the bitwise OR operator
value | (1 << bit_index)

Unsetting a bit: To clear a bit, you want to copy all binary digits while enforcing zero at one specific index. You can achieve this effect by using the same bitmask once again, but in the inverted form.
value & ~(1 << bit_index)

Toggling a bit: Sometimes it’s useful to be able to toggle a bit on and off again periodically. That’s a perfect opportunity for the bitwise XOR operator, which can flip your bit like that. 
value ^ (1 << bit_index)


GF2
- The unique field of order 2. The two operations are logical and and logical xor - multiplication and addition, respectively.

- XOR is the addition operator in the field GF2. The induced group therefore has an identity element, each element has an inverse, and is an associative operation.
- (x^y)^z = x^(y^z)
- x ^ 0 = x (0 is the identity element)
- x ^ x = 0 (x is it's own inverse)
- Abelian group, x ^ y = y ^ x

## Tips & Tricks

### Problems that can be solved with bits

[XOR](https://florian.github.io/xor-trick/)

The XOR trick: If we have a sequence of XOR operations a ^ b ^ c ^ ..., then we can remove all pairs of duplicated values without affecting the result.

The algorithm works in any situation where there is (1) some set of potential elements and (2) a set of elements actually appearing.

- XOR is essential for:
    - finding one missing/duplicate value in a sequence
        - XOR with entire sequence, including the missing/duplicate value 
    - finding two missing/duplicate values in a sequence
        - the key is to inspect the result of the last two elements being xored (is that a word?) and partitioning based on the first occurence of a 1 bit. 
    - In place Swapping
        - x ^= y, y ^= x, x ^= y
    - Finding the complement
        - complement = number ^ (all bits set to 1)    

Addition & Subtration with logical operators:
- Addition: x+y
    - Add without the carry bit: x^y
    - Finding the carry bit: (x&y)<<1
- Subtraction: x-y
    - Subtract without borrow bit: x^y
    - Borrow bit: (~x)&y 

https://www.techiedelight.com/bit-hacks-part-1-basic/
https://www.techiedelight.com/bit-hacks-part-2-playing-kth-bit/
https://www.techiedelight.com/bit-hacks-part-3-playing-rightmost-set-bit-number/
https://www.techiedelight.com/bit-hacks-part-4-playing-letters-english-alphabet/
https://www.techiedelight.com/bit-hacks-part-5-find-absolute-value-integer-without-branching/

[Advanced and Esoteric Bit Twiddling Hacks](https://graphics.stanford.edu/~seander/bithacks.html)
