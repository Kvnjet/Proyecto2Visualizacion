# Depression Distribution — Univariate Bar Chart

## Description
This chart shows the distribution of depression among university students in the sample. Each bar represents the count of students who reported having depression ("Yes") versus those who did not ("No").

## Key Insight
Approximately one in three students reported symptoms of depression, representing a prevalence of 34.7%. This establishes depression as a significant and measurable issue within the surveyed university population.

## Files
| File | Description |
|------|-------------|
| `u1_depresion.inja` | InjaX SVG template |
| `u1_depresion.json` | Aggregated data (counts per category) |
| `u1_depresion.svg`  | Generated chart image |

## Data Source
Student Mental Health Survey — 101 university students, August 2020.

## How to Generate
```bash
./injax u1_depresion.json u1_depresion.inja u1_depresion.svg
```
Requires the [InjaX](https://github.com/Kvnjet/Proyecto2Visualizacion) binary and `libchart.so` plugin.
