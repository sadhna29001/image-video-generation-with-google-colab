#!/usr/bin/env python3
"""
Quick test script for image generation functionality.
Run this to verify your setup is working correctly.
"""

import torch
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"CUDA version: {torch.version.cuda}")
    print(f"GPU Device: {torch.cuda.get_device_name(0)}")
    print(f"GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.2f} GB")
else:
    print("⚠️  Warning: CUDA not available. GPU acceleration will not work.")
    print("   Image generation will be very slow on CPU.")

# Test imports
try:
    from diffusers import StableDiffusionPipeline
    print("✅ Diffusers imported successfully")
except ImportError as e:
    print(f"❌ Failed to import diffusers: {e}")

try:
    import gradio as gr
    print("✅ Gradio imported successfully")
except ImportError as e:
    print(f"❌ Failed to import gradio: {e}")

try:
    import imageio
    print("✅ Imageio imported successfully")
except ImportError as e:
    print(f"❌ Failed to import imageio: {e}")

try:
    import xformers
    print("✅ XFormers imported successfully (optional but recommended)")
except ImportError:
    print("⚠️  XFormers not available (optional, improves performance)")

print("\n" + "="*50)
print("System check complete!")
print("="*50)

# Quick generation test
if input("\nRun a quick image generation test? (y/n): ").lower() == 'y':
    print("\nLoading model... (this may take a few minutes on first run)")
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        safety_checker=None
    )
    pipe = pipe.to(device)
    
    if torch.cuda.is_available():
        pipe.enable_attention_slicing()
    
    print("Generating test image...")
    result = pipe(
        prompt="a beautiful sunset over mountains",
        num_inference_steps=20
    )
    
    result.images[0].save("test_output.png")
    print("✅ Test image saved as 'test_output.png'")
    print("If the image looks good, your setup is working correctly!")
