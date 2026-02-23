# Example Usage Snippets

## Quick Start Examples

### Basic Image Generation
```python
# Generate a simple image
image = generate_image(
    prompt="a serene lake at sunset",
    num_steps=25,
    guidance_scale=7.5
)
image.save("my_image.png")
```

### Image with Negative Prompt
```python
# Generate image while avoiding certain elements
image = generate_image(
    prompt="a portrait of a woman, professional photography",
    negative_prompt="blurry, low quality, distorted, ugly",
    num_steps=30,
    guidance_scale=8.0
)
```

### Reproducible Generation with Seed
```python
# Use same seed for reproducible results
image1 = generate_image(
    prompt="a futuristic city",
    seed=42
)
image2 = generate_image(
    prompt="a futuristic city",
    seed=42
)
# image1 and image2 will be identical
```

### Video Generation
```python
# Generate a short video
video_path = generate_video(
    prompt="waves crashing on a beach",
    num_frames=16,
    fps=8
)
print(f"Video saved to: {video_path}")
```

### Interpolation Video
```python
# Create smooth transition between two scenes
video_path = create_interpolation_video(
    start_prompt="a sunny meadow with flowers",
    end_prompt="a snowy winter landscape",
    num_frames=30,
    fps=10
)
```

## Advanced Examples

### High Quality Image
```python
# Maximum quality settings
image = generate_image(
    prompt="a majestic eagle flying over mountains, highly detailed, 8k, national geographic",
    negative_prompt="blurry, low quality, amateur, distorted",
    num_steps=50,
    guidance_scale=9.0,
    seed=12345
)
```

### Batch Generation (Multiple Images)
```python
# Generate multiple variations
prompts = [
    "a red sports car",
    "a blue sports car",
    "a green sports car"
]

images = []
for i, prompt in enumerate(prompts):
    img = generate_image(
        prompt=prompt,
        seed=i * 100
    )
    img.save(f"car_{i}.png")
    images.append(img)
```

### Style Variations
```python
base_prompt = "a portrait of a cat"
styles = [
    "oil painting style",
    "watercolor style",
    "digital art style",
    "photorealistic style"
]

for style in styles:
    full_prompt = f"{base_prompt}, {style}"
    image = generate_image(prompt=full_prompt)
    image.save(f"cat_{style.replace(' ', '_')}.png")
```

### Longer Video
```python
# Generate longer video with more frames
video_path = generate_video(
    prompt="time-lapse of clouds moving across the sky",
    num_frames=32,
    fps=12
)
```

## Common Prompts by Category

### Landscapes
```python
prompts = [
    "a mountain valley at sunrise, mist rolling through trees, golden hour",
    "tropical beach with crystal clear water, palm trees, paradise",
    "desert dunes at sunset, dramatic sky, sand patterns",
    "autumn forest path, fallen leaves, soft sunlight filtering through trees"
]
```

### Portraits
```python
prompts = [
    "portrait of a young woman, natural lighting, professional photography",
    "elderly man with wisdom in his eyes, black and white, studio lighting",
    "child laughing, candid moment, outdoor natural light"
]
```

### Fantasy & Sci-Fi
```python
prompts = [
    "a dragon flying over a medieval castle, fantasy art, detailed",
    "futuristic cyberpunk city at night, neon lights, rain, cinematic",
    "space station orbiting an alien planet, stars, cosmic, 4k",
    "magical forest with glowing mushrooms, fairy tale, ethereal lighting"
]
```

### Abstract & Artistic
```python
prompts = [
    "abstract geometric patterns, vibrant colors, modern art",
    "swirling galaxies of color, fluid art, cosmic",
    "minimalist zen garden, peaceful, simple composition"
]
```

## Tips for Prompts

### Structure a Good Prompt
```
[Subject] + [Style] + [Details] + [Lighting] + [Quality]

Example:
"a majestic lion" + "oil painting style" + "in the savanna" + "golden hour lighting" + "highly detailed, 4k"
```

### Negative Prompt Template
```python
negative_prompt = "blurry, low quality, distorted, ugly, amateur, watermark, text, cropped, out of frame"
```

### Quality Boosters
Add these to your prompts:
- "highly detailed"
- "4k", "8k"
- "professional photography"
- "cinematic lighting"
- "award winning"
- "trending on artstation"

### Style Modifiers
- "oil painting"
- "watercolor"
- "digital art"
- "photorealistic"
- "anime style"
- "sketch"
- "3D render"

## Parameter Guidelines

### Steps (num_steps)
- 10-15: Fast, lower quality
- 20-30: Good balance ⭐
- 40-50: High quality, slower

### Guidance Scale
- 5-7: More creative/loose
- 7.5-9: Balanced ⭐
- 10-15: Very literal, may oversaturate
- 15+: Usually too high

### Seed
- -1: Random (different each time)
- Fixed number: Reproducible results
- Useful for comparing prompts or settings

## Gradio Interface Customization

### Custom Theme Colors
```python
demo = gr.Blocks(
    theme=gr.themes.Soft(
        primary_hue="blue",
        secondary_hue="purple"
    )
)
```

### Add Custom CSS
```python
css = """
.gradio-container {
    font-family: 'Arial', sans-serif;
}
"""
demo = gr.Blocks(css=css)
```

## Performance Optimization

### Clear GPU Memory
```python
import torch
torch.cuda.empty_cache()
```

### Reduce Memory Usage
```python
# Enable these optimizations
pipe.enable_attention_slicing()
pipe.enable_vae_slicing()
```

### Check GPU Usage
```python
import torch
if torch.cuda.is_available():
    print(f"Memory allocated: {torch.cuda.memory_allocated(0) / 1024**3:.2f} GB")
    print(f"Memory cached: {torch.cuda.memory_reserved(0) / 1024**3:.2f} GB")
```
