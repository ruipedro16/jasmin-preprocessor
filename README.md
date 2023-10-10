# jasmin-preprocessor

Run:

> $ ./preprocessor [-d] --input_file <input_file> --output_file <output_file>

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