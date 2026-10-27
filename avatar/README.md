# Profile avatar

A pixel-art mad-scientist drawn pixel by pixel — an original character, not a
likeness of anyone. `generate.py` builds both sizes from a single source grid:
`rick-32.png` is the true 32×32 design, `rick-512.png` is the same grid
nearest-neighbour upscaled so the edges stay hard at profile size.

Regenerate with:

```sh
python generate.py
```

The palette is a plain dict near the bottom of `generate.py`; change a colour
there and re-run.
