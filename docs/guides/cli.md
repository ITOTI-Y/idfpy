# Command line

Installing idfpy provides the `idfpy` command.

## `idfpy run`

Runs one EnergyPlus simulation and exits with the EnergyPlus return code.

```bash
idfpy run --idf model.idf --weather weather.epw --output results --readvars
```

| Option | Short | Description |
|---|---|---|
| `--idf` | `-i` | IDF file to simulate |
| `--weather` | `-w` | EPW weather file |
| `--output` | `-o` | Output directory, defaults to the IDF file's directory |
| `--readvars` | `-r` | Convert ESO output to CSV with ReadVarsESO |
| `--output-prefix` | `-p` | Prefix of the output file names |

## `idfpy codegen`

Regenerates the models from an EnergyPlus schema. You only need this when
developing idfpy or adding an [extension](extensions.md#writing-a-plugin).

```bash
idfpy codegen --schema /path/to/Energy+.schema.epJSON --output idfpy/models
```

| Option | Short | Description |
|---|---|---|
| `--schema` | `-s` | Path to `Energy+.schema.epJSON` |
| `--output` | `-o` | Output directory, defaults to `idfpy/models` |
