# CGPA Distribution — Univariate Bar Chart

## Description
This chart displays the distribution of students across five GPA ranges (CGPA: Cumulative Grade Point Average). Each bar represents the number of students falling within a specific academic performance range, from 0–1.99 up to 3.50–4.00.

## Key Insight
The majority of students are concentrated in the upper CGPA ranges (3.00–4.00), indicating that the sample is composed primarily of high-performing students. This context is important when interpreting the relationship between academic performance and mental health conditions.

## Files
| File | Description |
|------|-------------|
| `u2_cgpa.inja` | InjaX SVG template |
| `u2_cgpa.json` | Aggregated data (counts per CGPA range) |
| `u2_cgpa.svg`  | Generated chart image |

## Data Source
Student Mental Health Survey — 101 university students, August 2020.

## How to Generate
```bash
./injax u2_cgpa.json u2_cgpa.inja u2_cgpa.svg
```
Requires the [InjaX](https://github.com/Kvnjet/Proyecto2Visualizacion) binary and `libchart.so` plugin.
