# jasmin-preprocessor

Run:

> $ ./preprocessor [-d] --input_file <input_file> --output_file <output_file>

- [Shake256 examples](jpp_examples)

**NOTE:** Generic functions must end with `//<>`. E.g.

```
inline fn g<A,B>(stack u64[A] a, reg ptr u64[B] b) -> reg u64 {
    reg u64 r;
    r = a[1];
    return r; 
}//<>
```