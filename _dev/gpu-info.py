import torch

def get_gpu_memory_info():
    gpus = []
    for i in range(torch.cuda.device_count()):
        gpu_info = torch.cuda.get_device_properties(i)
        allocated_memory = torch.cuda.memory_allocated(i)
        reserved_memory = torch.cuda.memory_reserved(i)

        gpu = {
            "name": gpu_info.name,
            "total_memory": gpu_info.total_memory // (1024 ** 2),  # Convert bytes to MB
            "allocated_memory": allocated_memory // (1024 ** 2),  # Convert bytes to MB
            "reserved_memory": reserved_memory // (1024 ** 2),  # Convert bytes to MB
            "memory_utilization": (allocated_memory + reserved_memory) / gpu_info.total_memory * 100
        }
        gpus.append(gpu)

    return gpus

# Get GPU memory information
gpu_memory_info_list = get_gpu_memory_info()

# Print the GPU memory information
for i, gpu in enumerate(gpu_memory_info_list):
    print(f"GPU {i + 1}:")
    print(f"  Name: {gpu['name']}")
    print(f"  Total Memory: {gpu['total_memory']} MB")
    print(f"  Allocated Memory: {gpu['allocated_memory']} MB")
    print(f"  Reserved Memory: {gpu['reserved_memory']} MB")
    print(f"  Memory Utilization: {gpu['memory_utilization']:.2f}%")
    print()
