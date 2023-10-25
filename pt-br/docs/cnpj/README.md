## Dataset

Download `empresas.csv.gz` from [here](https://brasil.io/dataset/socios-brasil/files/).

## Parsing

After decompressed, run the following command to split the content according to state of company:

```sh
./split_by_state.py empresas.csv
```
