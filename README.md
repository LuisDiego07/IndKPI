# IndKPIs  
**Performance Indicators for Industrial Production**

IndKPIs is an industrial telemetry and analytics platform designed to collect, process, and analyze machine data, generating **KPIs and performance indicators** for manufacturing environments.

This project simulates real-world industrial telemetry, processes operational data, and exposes metrics through analytical pipelines and dashboards.

---

## 🚗 Release 1 — Automotive Industry

The first release focuses on the **automotive manufacturing sector**, simulating production lines with automated machines such as CNCs, welding robots, and presses.

The goal is to model **realistic shop-floor behavior**, including:
- Production cycles
- Downtime and failures
- Quality losses
- Energy consumption
- Machine performance degradation

---

📦 Project Structure

IndKPIs/
 ├── data_simulator/
 │    ├── machine.py              # Machine behavior model
 │    ├── simulator.py            # Telemetry simulation engine
 │    └── run_simulation.py       # Generates telemetry_events.json
 │
 ├── kpi_engine/
 │    ├── bronze_loader.py        # Bronze layer: raw data ingestion
 │    ├── silver_transformer.py   # Silver layer: data enrichment & normalization
 │    ├── gold_oee.py             # Gold layer: OEE and KPI calculations
 │    └── run_pipeline.py         # End-to-end medallion pipeline execution
 │
 ├── data_lake/
 │    ├── bronze/                 # Raw telemetry data (Parquet)
 │    ├── silver/                 # Enriched telemetry data (Parquet)
 │    └── gold/                   # KPI datasets (Parquet or DB exports)
 │
 └── README.md
