# AI-Driven DevOps Code Generator

A command-line Python tool that generates DevOps infrastructure (Terraform), Dockerfile, and Kubernetes YAML configurations from natural language prompts using a locally hosted large language model (LLaMA 3 1B) via the Ollama CLI.

The LLM runs on an AWS EC2 instance, combining cloud scalability with the privacy and cost benefits of local inference. This project demonstrates expertise in DevOps automation, infrastructure as code, container orchestration, AI integration, and cloud infrastructure management.

---

## Features

- Generate Terraform `.tf` files for infrastructure provisioning
- Create Dockerfiles for containerized applications
- Generate Kubernetes deployment and service YAML files
- Uses a local LLM on AWS EC2 via Ollama for secure, offline code generation
- Saves generated files with timestamps organized by configuration type

---

## Prerequisites

- Python 3.7+
- [Ollama CLI](https://ollama.com/docs) installed on your local machine or accessible EC2 instance
- LLaMA 3 1B model downloaded on Ollama
- Access to the EC2 instance running Ollama CLI (if using cloud setup)

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/ai-devops-codegen.git
   cd ai-devops-codegen
   ```
(Optional) Create and activate a virtual environment:

 ```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

Install any dependencies:

 ```bash
pip install -r requirements.txt
```

Ensure Ollama CLI is installed and the model is available on your EC2 instance:
 ```bash
ollama run llama3.2:1b

```
Usage
Run the generator script with required arguments:
 ```bash
python src/codegen.py --type <infra|docker|k8s> --input "your natural language description"
```

Examples:
 ```bash
python src/codegen.py --type infra --input "a Terraform config for AWS EC2 with 2 t2.micro instances"
python src/codegen.py --type docker --input "a Dockerfile for a Python Flask web application"
python src/codegen.py --type k8s --input "Kubernetes deployment for Nginx with 3 replicas and a LoadBalancer service"
# Generated files are saved in the generated/<type>/ folder with timestamps.
```

How It Works
The script parses the command-line arguments for configuration type and natural language description.

It builds a system prompt tailored to the chosen configuration type.

The prompt is sent to the local LLM through Ollama CLI running on the EC2 instance.

The LLM generates the requested DevOps configuration code.

The output is saved to a timestamped file under generated/<type>/.

Project Structure
 ```bash
ai-devops-codegen/
├── generated/                  # Auto-generated config files (ignored in git)
│   ├── infra/
│   ├── docker/
│   └── k8s/
├── src/
│   └── codegen.py              # Main Python script
├── .gitignore                  # Specifies files/folders to ignore
├── README.md                   # This file
├── requirements.txt            # Python dependencies 
└── LICENSE                    # License file 
```

Future Improvements
Add input validation and error handling enhancements

Integrate validation tools for Terraform and Kubernetes configs

Support asynchronous generation requests and queuing

Build a REST API interface for easier integration in pipelines

Add caching for common prompts to reduce latency and cost

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or contributions, please open an issue or submit a pull request.









Ask ChatGPT
