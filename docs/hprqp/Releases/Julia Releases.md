# Julia Releases
A compact index of HPR-QP (Julia) releases—each entry shows the version tag and a one-line summary; click a version to view full notes, benchmarks, and downloads.

---

<details id="v010">
<summary><code>v0.1.0</code> — A preliminary release: Julia GPU-accelerated HPR-QP solver</summary>

**Release date**: 2025-07-07

**Highlights**
- First public release of **HPR-QP**.  
- GPU-accelerated QP solver in Julia implementing the Halpern–Peaceman–Rachford (HPR) method.  


**Downloads**
- [Source code (zip)](https://github.com/PolyU-IOR/HPR-QP/archive/refs/tags/v0.1.0.zip)  
- [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-QP/archive/refs/tags/v0.1.0.tar.gz)

</details>

---

<details id="v011">
<summary><code>v0.1.1</code> — Unified Architecture + CPU & GPU Support + JuMP Integration</summary>

**Release date**: 2025-12-30

**Highlights**
- *Unified Architecture*:
Single codebase for all problem types (standard QP, QAP, LASSO)
Modular Q operator system for extensibility: easily add custom problem types
- *CPU & GPU Support*:
Full CPU implementation in addition to GPU acceleration
Automatic device selection via use_gpu parameter
- *JuMP Integration*:
Native JuMP/MathOptInterface (MOI) support for easy modeling
Use HPR-QP directly as a JuMP optimizer
- *Warm-Start Capability*:
Initialize via initial_x and initial_y parameters
Resume optimization from previous (auto-saved) solutions
- *Auto-Save Feature*:
Automatically save best solution during optimization (auto_save=true)
Resume from saved states for long-running problems


**Downloads**
- [Source code (zip)](https://github.com/PolyU-IOR/HPR-QP/archive/refs/tags/v0.1.1.zip)  
- [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-QP/archive/refs/tags/v0.1.1.tar.gz)

</details>

---