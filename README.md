Given an audio, the corresonding boundaries can be in either format

1. Index of each boundaries with 20ms sample rate
```
boundaries = [4, 8, 12, 15, ...]
```

2. Time stamps of each boundaries from left to right
```
boundaries = [0.04, 0.5, 1.2, ...]
```

The `extract_boundaries.py` contains a possible folder structure to store boundaries, however, it is totally not necessary if there is a more convenient way to do it!
