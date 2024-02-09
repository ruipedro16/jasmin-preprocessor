# jasmin-preprocessor

Run:

> $ ./preprocessor [-d] [--arch {x86-64,arm-m4}] -in <input_file> -out <output_file>

## Preprocessor options

- `--arch`: Target architecture (either x86-64 or arm-m4 ; default is x86-64)
- `-d`/`--debug`: Prints debugging information
- `--after_rm_generic`: Prints the program after removing the generic functions from the source code
- `--after_tasks`: Prints the program after resolving the tasks
- `--after_generic_fn_calls`: Prints the program after resolving generic function calls
- `--workers`: Defines the number of worker threads for finding subtask concurrently

## Run with Docker

```
# Build the Docker image
docker build -t jasmin-preprocessor .

# Run the container
docker run -it -v "$PWD":/app jasmin-preprocessor --input_file map.jazz --output_file map.jpp
```

## Integer Templates

Sphincs+ implementation

## Functions as Arguments

## Recursive Functions

See [rec_sum.jtmpl](examples/rec_sum.jtmpl)

## usize

See [memcmp.jtmpl](examples/memcmp.jtmpl)

## TODO

Macros like C `#if`, `#ifdef`