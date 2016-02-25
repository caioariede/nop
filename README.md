# nop
A brainfuck-like implementation using Python operator overloading

## Commands

| Python Operators | Equivalent Brainfuck commands | Example                                                   |
| ---------------- | ----------------------------- | --------------------------------------------------------- |
| `>` `<`          | `>` `<`                       | `nop() > nop() < nop()`                                   |
| `+` `-`          | `+` `-`                       | `nop() + 1 > nop() - 1 + 2`                               |
| `^` `~`          | `.` `,`                       | `~nop() + 1 ^ nop()`                                      |
| `>>` `<<`        | `[` `]`                       | `nop() + 2 >> ( nop() - 1 > nop() + 2 < nop() ) << nop()` |

## Hello world example:

```python
from nop import nop

print(
    nop() + 8 >> (
        nop() > nop() + 4 >> (
            nop() - 1
            
            > nop() + 2
            > nop() + 3
            > nop() + 3
            > nop() + 1

            < nop()
            < nop()
            < nop()
            < nop()

        ) << nop()

        > nop() + 1
        > nop() + 1
        > nop() - 1
        > nop()
        > nop() + 1

        >> ( nop() < nop() ) <<

        nop() < nop() - 1

    ) << nop()

    > nop() > nop() ^ nop()         # H
    > nop() - 3 ^ nop()             # e

    + 7 ^ nop() ^ nop()             # ll
    + 3 ^ nop()                     # o

    > nop() > nop() ^ nop()         # <space>
    < nop() - 1 ^ nop()             # W
    < nop() ^ nop()                 # o

    + 3 ^ nop()                     # r
    - 6 ^ nop()                     # l
    - 8 ^ nop()                     # d

    > nop() > nop() + 1 ^ nop()     # !
    > nop() + 2 ^ nop()             # <newline>
)
```
