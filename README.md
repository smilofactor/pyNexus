![Build Status](https://github.com/smilofactor/pyNexus/actions/workflows/ci.yml/badge.svg)

# pyNexus 📈

### **Institutional-Grade Equities Monitor**
**Architecture:** Hexagonal (Ports & Adapters)  
**Methodology:** TDD (Test-Driven Development)  
**CI/CD:** GitHub Actions (Verified)

---

## **Overview and Project Evolution**
pyNexus is a high-concurrency market data orchestration layer, refactored from my original **PLNexus** (JavaScript) implemented into a Python stack. 

The project was specifically designed to focusing on the financial sector, strict separation of concerns, and automated integrity via CI/CD pipelines.


## **Architectural Pillars**
- **Hexagonal Design:** Complete decoupling of domain entities from external infrastructure (APIs/Databases) using the Ports and Adapters pattern.
- **TDD-First:** Test coverage for use cases backed by unit tests to ensure system integrity.

- **Observability:** Performance tracing is implemented via Python decorators to monitor execution latency—a critical metric for equities desks.
- **Performance Observability:** Custom decorators for real-time execution tracing and latency monitoring.


## **Tech Stack**
- **Language:** Python
- **Testing:** Pytest / Unittest.mock
- **CI/CD:** GitHub Actions
- **UI:** Streamlit (Implementation in progress)
