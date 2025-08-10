import argparse
import os
import subprocess
from datetime import datetime


def parse_arguments():
    parser = argparse.ArgumentParser(description="AI-Driven DevOps Code Generator")
    parser.add_argument(
        "--type",
        required=True,
        choices=["infra", "docker", "k8s"],
        help="Type of configuration to generate: infra (Terraform), docker (Dockerfile), or k8s (Kubernetes YAML)",
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Natural language description of the desired DevOps setup",
    )
    return parser.parse_args()


def call_local_llm(prompt: str) -> str:
    """Use Ollama to run the LLM with a given prompt"""
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3.2:1b"],
            input=prompt.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60
        )
        return result.stdout.decode()
    except subprocess.TimeoutExpired:
        return "[ERROR] LLM generation timed out."
    except Exception as e:
        return f"[ERROR] Failed to invoke LLM: {e}"


def save_output(file_type: str, content: str):
    """Save the generated content to a timestamped file in the correct directory"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    extension = {
        "infra": f"infra_{timestamp}.tf",
        "docker": f"Dockerfile_{timestamp}",
        "k8s": f"k8s_{timestamp}.yaml"
    }[file_type]

    folder_path = os.path.join("generated", file_type)
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, extension)
    with open(file_path, "w") as f:
        f.write(content)

    print(f"[✔] Generated file saved to: {file_path}")


def main():
    args = parse_arguments()
    print(f"[→] Generating {args.type} configuration from prompt: '{args.input}'")

    # Add type-specific instructions to help guide the LLM output
    system_prompt = {
        "infra": "Write a complete Terraform (.tf) configuration to: ",
        "docker": "Create a Dockerfile for: ",
        "k8s": "Generate a Kubernetes deployment and service YAML for: "
    }[args.type]

    full_prompt = system_prompt + args.input
    output = call_local_llm(full_prompt)
    save_output(args.type, output)


if __name__ == "__main__":
    main()
