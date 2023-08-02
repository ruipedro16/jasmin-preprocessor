# jasmin-preprocessor

Run:

> python3 processor.py <input_file>

- `out`: Folder with preprocessed examples

NOTE: Generic functions must end with `//<>`. E.g.

```
inline fn g<A,B>(stack u64[A] a, reg ptr u64[B] b) -> reg u64 {
    reg u64 r;
    r = a[1];
    return r; 
}//<>
```