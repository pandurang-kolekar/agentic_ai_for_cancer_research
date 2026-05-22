# Appendix C: GPU Infrastructure

## Overview

This appendix covers GPU setup and configuration for running deep learning models in this book.

## Contents

1. NVIDIA CUDA Setup
2. PyTorch with GPU
3. TensorFlow with GPU
4. Performance Optimization
5. Cloud GPU Services

## 1. NVIDIA CUDA Setup

### Check GPU

```bash
# macOS/Linux
nvidia-smi

# Output example:
# NVIDIA-SMI 535.104.05             Driver Version: 535.104.05
# GPU Name                 Persistence-M | Bus-Id        Disp.A
# Tesla V100              On           | 00000000:00:1E.0
```

### Install CUDA

**NVIDIA Official**: https://developer.nvidia.com/cuda-downloads

```bash
# Ubuntu example
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-1
```

### Install cuDNN

```bash
# Download from NVIDIA
# Extract and copy to CUDA location
cp cuda/include/cudnn.h /usr/local/cuda/include/
cp cuda/lib64/libcudnn* /usr/local/cuda/lib64/
```

## 2. PyTorch with GPU

### Install

```bash
# CUDA 12.1
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# CPU only
pip install torch torchvision torchaudio

# Apple Silicon (Mac)
pip install torch torchvision torchaudio
```

### Verify GPU

```python
import torch

print(torch.cuda.is_available())  # True if GPU detected
print(torch.cuda.get_device_name(0))  # GPU name
print(torch.cuda.get_device_properties(0))  # GPU specs

# Move tensors to GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = torch.randn(1000, 1000).to(device)
y = torch.randn(1000, 1000).to(device)
z = torch.matmul(x, y)  # GPU computation
```

## 3. TensorFlow with GPU

### Install

```bash
# GPU support
pip install tensorflow[and-cuda]

# CPU only
pip install tensorflow
```

### Verify GPU

```python
import tensorflow as tf

print(tf.config.list_physical_devices('GPU'))
print(tf.reduce_sum(tf.random.normal([1000, 1000])))  # GPU computation
```

## 4. Performance Optimization

### Memory Management

```python
import torch

# Monitor memory
print(torch.cuda.memory_allocated())
print(torch.cuda.memory_reserved())

# Clear cache
torch.cuda.empty_cache()

# Memory efficient model loading
model = model.to(device)
torch.cuda.empty_cache()
```

### Mixed Precision Training

```python
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()

for data, target in dataloader:
    optimizer.zero_grad()
    
    with autocast():  # Automatic mixed precision
        output = model(data.to(device))
        loss = criterion(output, target)
    
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
```

### Distributed Training

```python
import torch.nn as nn
from torch.nn.parallel import DataParallel

# Single machine, multiple GPUs
model = DataParallel(model)

# Or with DistributedDataParallel
from torch.nn.parallel import DistributedDataParallel
model = DistributedDataParallel(model)
```

## 5. Cloud GPU Services

### AWS EC2 with GPU

```bash
# Launch GPU instance
aws ec2 run-instances \
  --image-id ami-0c94855ba95c574c8 \
  --instance-type p3.2xlarge \
  --key-name my-key
```

### Google Colab

```python
# Check GPU in Colab
import torch
print(torch.cuda.is_available())

# GPU automatically available for TensorFlow/PyTorch
import tensorflow as tf
print(len(tf.config.list_physical_devices('GPU')))
```

### Azure ML

```bash
# Create GPU compute
az ml compute create \
  --name gpu-cluster \
  --type amlcompute \
  --min-instances 0 \
  --max-instances 4 \
  --size Standard_NC6
```

## Benchmarking

```python
import time
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# CPU vs GPU benchmark
def benchmark(device, size=1000, iterations=10):
    x = torch.randn(size, size)
    y = torch.randn(size, size)
    
    x = x.to(device)
    y = y.to(device)
    
    start = time.time()
    for _ in range(iterations):
        z = torch.matmul(x, y)
    
    elapsed = time.time() - start
    return elapsed / iterations

cpu_time = benchmark(torch.device("cpu"))
gpu_time = benchmark(device)

print(f"CPU: {cpu_time*1000:.2f}ms")
print(f"GPU: {gpu_time*1000:.2f}ms")
print(f"Speedup: {cpu_time/gpu_time:.1f}x")
```

---

**Last Updated**: May 2024

