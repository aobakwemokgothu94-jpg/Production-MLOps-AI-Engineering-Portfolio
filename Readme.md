# Production-MLOps-AI-Engineering-Portfolio
professional portfolio showcasing four end-to-end systems engineered for reproducibility, scalable feature serving, automated experiment tracking, and secure agentic AI deployment.  🏗️ 

🏗️ Portfolio Architecture & Core Projects
Plaintext
├── 01-reproducible-training-pipeline/  # DVC + MLflow Experiment Tracking
├── 02-realtime-feature-store/          # Feast Feature Store & Offline/Online Serving
├── 03-agentic-rag-pipeline/            # LangChain, FAISS & Pydantic Validation
└── 04-cloud-native-infra/              # Terraform, Docker & Vault Security
Project 1: Reproducible ML Training Pipeline (01-reproducible-training-pipeline)
What it does: Eliminates "it works on my machine" issues by automating and versioning data ingestion, feature extraction, and model training.

Core Stack: Python, Scikit-Learn, DVC (Data Version Control), MLflow, Git.

Key Engineering Highlights:

Configured DVC to version multi-gigabyte datasets and track raw vs. processed data splits.

Integrated MLflow for automated parameter logging, metric tracking, and model artifact registration.

Built automated shell scripts (setup.sh) to execute the entire training DAG with a single terminal command.

Project 2: Low-Latency Feature Store (02-realtime-feature-store)
What it does: Solves training-serving skew by maintaining a centralized repository for features used across both batch model training and real-time inference.

Core Stack: Feast, SQLite/PostgreSQL, Pandas, Python.

Key Engineering Highlights:

Defined feature views and entity mappings using clean configuration-driven YAML setups.

Implemented historical feature retrieval with point-in-time correctness for offline model training.

Materialized online features into a low-latency key-value store for real-time sub-millisecond model scoring.

Project 3: Secure Agentic RAG & Text-to-SQL Pipeline (03-agentic-rag-pipeline)
What it does: Powers context-aware AI agents that interact with local vector stores and databases while enforcing strict schema validation and security guardrails against prompt injection.

Core Stack: LangChain, FAISS, Pydantic, Gradio, Python.

Key Engineering Highlights:

Engineered a multi-tool agentic workflow capable of parallel and serial tool calling across vector search and cost calculation tools.

Utilized Pydantic to enforce strict output schemas, defending against improper output handling and hallucination risks.

Configured local persistent chat history and real-time token streaming interfaces via Gradio.

Project 4: Cloud-Native Infrastructure & MLOps Security (04-cloud-native-infra)
What it does: Automates the provisioning of secure cloud runtime environments and manages sensitive API credentials using Infrastructure as Code (IaC) and secrets management.

Core Stack: Terraform, Docker, Docker Compose, HashiCorp Vault, AWS/Azure CLI.

Key Engineering Highlights:

Provisioned reproducible cloud compute environments using explicit variables and modular Terraform configurations.

Integrated HashiCorp Vault AppRole authentication to manage scoped KV v2 secrets for MLflow and database pipelines.

Containerized services using Docker Compose, adhering to least-privilege security and network isolation standards.

🛠️ Quick Start & Local Execution
To clone and run any of the modular pipelines locally:

Bash
# Clone the repository
git clone https://github.com/aobakwemokgothu94/mlops-portfolio.git
cd mlops-portfolio

# Initialize virtual environment and dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


👨‍💻 Author
Aobakwe Mokgothu-Kugombo

IT Solutions Specialist, DevOps Engineer & AI/MLOps Engineer,Certifid LLM Security Expert,Cloud DevOPS Expert
