# Homepage benchmark provenance

Retrieved on **2026-11-04**. Source page dated **25 Oct 2026**:

- Published results: https://plato.asu.edu/ftp/lpfeas.html
- Published logs: https://plato.asu.edu/ftp/lpfeas_logs/
- Saved source: `sources/lpfeas-2026-10-25.html`

## Main results (65 instances)

SGM10 seconds and solved counts copy the source's summary. The homepage puts
HPR-LP-C first, followed by the other GPU configurations and then the six CPU
configurations. At the user's request, the homepage Relative column uses a
single baseline across all ten rows:

`Relative = published SGM10 (s) / 8.02 (s)`

The homepage header reads only "Relative". 8.02 s is COPT-H's published SGM10,
the minimum in this table. Calculate from
the published aggregate seconds using decimal arithmetic and round half up to
two decimal places. Only COPT-H equals 1.00. This is a homepage-derived ratio,
not the source's separately normalized CPU/GPU scaled row. Preserve both below
for traceability. HPR-LP-C therefore displays 1.35 (source scaled: 1.34), and
cuOpt displays 1.36 (source scaled: 1.37).

The original main table contains ten result columns: six CPU configurations
(COPT, MOSEK, HiGHS, KNITRO, PDLP, XOPT) and four GPU configurations (cuOpt,
cuPDLPx, COPT-H, HPR-LP-C). These represent nine solver products, since COPT
appears in both groups. The homepage includes all ten columns as solver rows
with a Type column. The CPU and GPU groups use different hardware and time limits.
Both homepage comparisons show solver names without row-level version labels.
The HPR result summary in each panel identifies **HPR-LP-C (v0.1.4)** on its own
line above the numeric metrics. Other solver versions remain documented below.

| Solver | Type | Published SGM10 (s) | Source scaled | Homepage Relative | Published solved |
|---|---|---:|---:|---:|---:|
| HPR-LP-C v0.1.4 | GPU | 10.8 | 1.34 | 1.35 | 63 |
| COPT-H\* | GPU | 8.02 | 1 | 1.00 | 64 |
| cuOpt 26.10\* | GPU | 10.9 | 1.37 | 1.36 | 62 |
| cuPDLPx 0.3.0 | GPU | 28.5 | 3.55 | 3.55 | 57 |
| COPT 9.0.0 | CPU | 25.3 | 1 | 3.15 | 65 |
| MOSEK 11.3.2 | CPU | 89.2 | 3.56 | 11.12 | 56 |
| HiGHS 1.15.0 | CPU | 256 | 10.2 | 31.92 | 55 |
| KNITRO 16.0.0 | CPU | 372 | 14.8 | 46.38 | 48 |
| PDLP (OR-Tools 9.10) | CPU | 421 | 16.6 | 52.49 | 50 |
| XOPT 0.0.8 | CPU | 146 | 5.77 | 18.20 | 59 |

The compact licensing lines identify HPR-LP-C, HiGHS, PDLP, cuOpt and cuPDLPx
as open source, and COPT/COPT-H, MOSEK and KNITRO as commercial. XOPT's linked
project page does not state a license; do not infer one from its commercial goals.
License/product references:

- HPR-LP-C (MIT): https://github.com/PolyU-IOR/HPR-LP-C/blob/main/LICENSE
- cuOpt (Apache-2.0): https://github.com/NVIDIA/cuopt/blob/main/LICENSE
- cuPDLPx (Apache-2.0): https://github.com/MIT-Lu-Lab/cuPDLPx/blob/main/LICENSE
- HiGHS: https://github.com/ERGO-Code/HiGHS/blob/master/LICENSE.txt
- PDLP (OR-Tools): https://github.com/google/or-tools/blob/stable/LICENSE
- COPT commercial solver: https://www.shanshu.ai/copt
- MOSEK: https://www.mosek.com
- KNITRO: https://www.artelys.com/knitro/
- XOPT linked project page: http://sribd.cn/en/article/813

Hardware: Intel Xeon Platinum 8570, 2 TB RAM, 112 CPUs, 180 GB NVIDIA B200.
GPU time limit: 1,000 s. The CPU results use an i7-11700K (3.6 GHz), 64 GB RAM
and a 15,000 s limit. The homepage Type column and platform subtitle retain the
platform distinction while the Relative column shares a single 8.02 s baseline.

SGM10 uses a 10 s shift. The source charges timeout/failure/memory failure at
the corresponding time limit. Keep the source's published aggregate rather than
recomputing it from displayed rounded per-instance seconds.

Naming/version evidence:

- An asterisk after a solver name marks a configuration that may combine CPU
  and GPU computation or run multiple solver methods concurrently.
  COPT-H's log
  shows CPU-thread/GPU barrier execution and a PDLP outcome. cuOpt's log
  explicitly says "Running concurrent" and reports PDLP, dual simplex and
  barrier termination:
  https://plato.asu.edu/ftp/lpfeas_logs/cuo_results/L1_sixm250obs.cuo
- Source main table calls COPT's GPU column `COPTH`; the addendum calls it `COPT-H`.
  Its linked log identifies COPT 9.0.0, `LpMethod 7`, `GPUMode 2`:
  https://plato.asu.edu/ftp/lpfeas_logs/cop_results/L1_sixm250obs.cob
- The addendum log also uses COPT, LpMethod 7 and GPUMode 2, and reports GPU 0
  as NVIDIA B200. The older presentation's COPTG label also refers to COPT's GPU
  configuration; do not infer identical historical settings from the name alone:
  https://plato.asu.edu/ftp/lpfeas_logs/cop_results/heat-source-easy.cob
- HPR's log confirms version 0.1.4, tolerance 1e-6 and a 1,000 s limit:
  https://plato.asu.edu/ftp/lpfeas_logs/hpr_results/L1_sixm250obs.hpr
- The repository's latest public release at retrieval is v0.1.3. A benchmarked
  version is not necessarily the latest downloadable release; label it accordingly.

Source inconsistency: cuOpt's summary says 62 solved; counting the numeric
entries in the main table gives 63. The homepage preserves **62** from the source
summary. This discrepancy is documented here; the homepage uses a compact source
citation. Do not silently change either published aggregate.

## Separate large-scale addendum (20 instances)

Time limit 4,800 s. HPR and COPT-H use one GPU; cuOpt has 1/2/4/8-GPU columns.
Calculate SGM10 from the published per-instance times for all 20 instances using
a 10 s shift. Substitute 4,800 s for each `t`, `f`, or `m` outcome.
Count only numeric outcomes as solved.

| Configuration | Derived SGM10 (s) | Derived solved count |
|---|---:|---:|
| HPR-LP-C, 1 GPU | 272.45 | 18/20 |
| cuOpt, 1 GPU | 1,376.58 | 13/20 |
| cuOpt, 2 GPUs | 1,688.99 | 12/20 |
| cuOpt, 4 GPUs | 1,281.27 | 13/20 |
| cuOpt, 8 GPUs | 1,001.51 | 16/20 |
| COPT-H, 1 GPU | 2,190.48 | 6/20 |

The addendum contains three solvers and six configurations: cuOpt on 1/2/4/8
GPUs, COPT-H on one GPU, and HPR-LP-C on one GPU. The homepage compares the
three single-GPU runs. Divide each unrounded SGM10 by the lowest single-GPU
SGM10 (HPR-LP-C) and round to two decimal places for the Relative column.
HPR times out on
`heat_400_8_1000_400` and `heat_400_10_1000_500`. All 18 other HPR entries are
numeric. This set must not be added to the 65-instance main score.

Do not call these table values end-to-end data-loading times. For example,
`heat-source-easy` has a published table value of 1 s, but its log separates
reading time (63.88 s) from reported solve time (0.14 s):
https://plato.asu.edu/ftp/lpfeas_logs/hpr_results/heat-source-easy.hpr

## Other results are different experiments

- HPR-LP-C README / v0.1.3 release reports **49/49**, SGM10 **5.93 s**,
  and **2.15x** versus v0.1.2 (12.74 s):
  https://github.com/PolyU-IOR/HPR-LP-C/releases/tag/v0.1.3
  This is a project-reported version comparison, not the 65-instance ranking.
- `docs/hprlp/Benchmarks/index.md` now mirrors the two homepage tables as plain
  documentation tables. It also includes the two project-supplied release
  comparison figures for the 49-instance Hans set (v0.1.0 through v0.1.4,
  tolerance 1e-6, time limit 1,000 s). Those figures are a separate experiment
  from the 65-instance main benchmark and 20-instance addendum.

## Editing and refreshing

Markup and figures: `landing/index.html`, section `#benchmarks`.
Scoped presentation: `landing/benchmark.css`.
Build scripts copy `landing/` into `site/`; sync both files for local preview.

When refreshing, save the dated source, update all solver versions, counts,
SGM10 values, relative values, hardware, limits and source date together.
Use the minimum published SGM10 across all ten configurations as the common
baseline, and recalculate every homepage ratio together if that minimum changes.
Check the addendum independently. Never claim a global first place when the
published main aggregate does not support it.
