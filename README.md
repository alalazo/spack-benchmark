# How to use this extension

This extension adds a command to Spack to benchmark concretization. To set it up, clone the repository somewhere
and modify your `config.yaml` by adding the repository directory to the extensions:
```yaml
config:
  extensions:
  - /some/path/spack-benchmark
```
The extension requires `pandas`, `matplotlib` and `tqdm` - so install them in some way. For instance:
```console
$ pip install pandas matplotlib tqdm
```
At this point you should be able to print the following help:
```console
$ spack solve-benchmark -h
usage: spack solve-benchmark [-h] SUBCOMMAND ...

benchmark concretization speed

positional arguments:
  SUBCOMMAND
    run       run benchmarks and produce a CSV file of timing results
    plot      plot results recorded in a CSV file

optional arguments:
  -h, --help  show this help message and exit
```

## Benchmark concretization speed

To benchmark concretization speed, and record results in a CSV file:
```console
$ spack list -t radiuss > radiuss.txt
$ spack solve-benchmark run -o radiuss.csv radiuss.txt
```
The first command simply creates a text file where each line is an input to the concretization algorithm. The second command
goes over all the inputs and records concretization time for each of them.