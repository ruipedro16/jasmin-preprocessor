# jasmin-preprocessor

Fails with functions that have parenthesis in the arguments. For example

```
offset = (64u) h;
auth_path, _ = _x_memcpy_u8u8<SPX_N*SPX_FORS_HEIGHT, SPX_N>(auth_path, offset, current[SPX_N:SPX_N]);
```

works, but

```
auth_path, _ = _x_memcpy_u8u8<SPX_N*SPX_FORS_HEIGHT, SPX_N>(auth_path, (64u) h, current[SPX_N:SPX_N]);
```

doesn't
