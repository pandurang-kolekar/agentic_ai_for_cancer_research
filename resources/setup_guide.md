# Setup Guide for Agentic AI for Cancer Research

## Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/agentic_ai_for_cancer_research.git
cd agentic_ai_for_cancer_research
```

### 2. Create Environment

#### Option A: Conda (Recommended)
```bash
conda env create -f resources/environments.yml
conda activate agentic-ai-cancer
```

#### Option B: Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r resources/requirements.txt
```

### 3. Launch Jupyter
```bash
jupyter lab
```

### 4. Navigate to a Chapter
Open `chapters/chapter_01_introduction_to_agentic_ai/notebook.ipynb`

---

## System Requirements

### Minimum
- **OS**: macOS, Linux, or Windows
- **Python**: 3.10+
- **RAM**: 8 GB
- **Disk**: 10 GB
- **CPU**: Any modern processor

### Recommended for GPU Acceleration
- **GPU**: NVIDIA (CUDA 11.8+) or Apple Metal
- **RAM**: 16+ GB
- **Storage**: SSD with 50+ GB

---

## Detailed Setup

### Step 1: Install Python

**macOS** (using Homebrew):
```bash
brew install python@3.10
```

**Ubuntu/Debian**:
```bash
sudo apt-get install python3.10 python3.10-venv
```

**Windows**:
Download from [python.org](https://www.python.org/downloads/)

### Step 2: Install Conda (Optional but Recommended)

Download [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/) or [Anaconda](https://www.anaconda.com/download)

### Step 3: Clone Repository
```bash
git clone https://github.com/yourusername/agentic_ai_for_cancer_research.git
cd agentic_ai_for_cancer_research
```

### Step 4: Create Environment

**With Conda**:
```bash
conda env create -f resources/environments.yml
conda activate agentic-ai-cancer
```

**With pip**:
```bash
python3.10 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r resources/requirements.txt
```

### Step 5: Verify Installation
```bash
python -c "import langchain, pandas, biopython; print('✓ Installation successful!')"
jupyter --version
```

---

## API Keys Setup

### OpenAI API
1. Get key from [platform.openai.com](https://platform.openai.com/api-keys)
2. Create `.env` file in repository root:
   ```
   OPENAI_API_KEY=sk-your-key-here
   ```

### Other LLM Providers
Similar setup for:
- Anthropic Claude
- Google AI Studio
- Local models (via Ollama)

---

## Troubleshooting

### Python Version Issues
```bash
python --version  # Should be 3.10+
```

If not:
```bash
python3.10 --version
alias python=python3.10
```

### Conda Environment Not Activating
```bash
# List environments
conda env list

# Activate specific env
conda activate agentic-ai-cancer

# Or initialize conda for your shell
conda init bash  # or zsh, fish, etc.
```

### Package Installation Fails

Try updating pip first:
```bash
pip install --upgrade pip setuptools wheel
```

Then install requirements:
```bash
pip install -r resources/requirements.txt
```

### Jupyter Not Found
```bash
pip install jupyter jupyterlab ipykernel
python -m ipykernel install --user --name agentic-ai-cancer
```

### GPU Not Detected

For NVIDIA:
```bash
# Check CUDA
nvidia-smi

# Install PyTorch with CUDA
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

For Apple Metal:
```bash
# Use official PyTorch build for Apple
pip install torch torchvision torchaudio
```

---

## Running Notebooks

### Launch Jupyter Lab
```bash
jupyter lab
```

### Open Specific Notebook
```bash
jupyter lab chapters/chapter_01_introduction_to_agentic_ai/notebook.ipynb
```

### Run Notebook from Command Line
```bash
jupyter nbconvert --to notebook --execute chapter_01/notebook.ipynb
```

---

## Git Setup

### Initial Configuration
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### Create a Fork and Branch
```bash
# Fork on GitHub first

git clone https://github.com/yourusername/agentic_ai_for_cancer_research.git
cd agentic_ai_for_cancer_research

# Create feature branch
git checkout -b feature/your-feature

# Make changes...

git add .
git commit -m "Your commit message"
git push origin feature/your-feature
```

---

## Docker Setup (Optional)

### Build Docker Image
```bash
docker build -t agentic-ai-cancer .
```

### Run Container
```bash
docker run -it -p 8888:8888 agentic-ai-cancer
```

---

## Next Steps

1. ✅ Environment set up
2. 📖 Read [README.md](../README.md)
3. 🚀 Start with Chapter 1
4. 💻 Run the notebooks
5. 🧪 Complete exercises
6. 🔗 Connect with community

---

## Getting Help

- 📚 Check [troubleshooting.md](troubleshooting.md)
- 🔍 Search [GitHub Issues](https://github.com/yourusername/agentic_ai_for_cancer_research/issues)
- 💬 Post in [Discussions](https://github.com/yourusername/agentic_ai_for_cancer_research/discussions)
- 📧 Email: [your-email@example.com]

---

**Last Updated**: May 2024

