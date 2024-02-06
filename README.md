# jasmin-preprocessor

Run:

> $ ./preprocessor [-d] -in <input_file> -out <output_file>

## Preprocessor options

- `-d`/`--debug`: Prints debugging information
- `--after_macro`: Prints the program after replacing `#expand` macros
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

## JPP

TODO: 

## TODO

Macros like C `#if`, `#ifdef`