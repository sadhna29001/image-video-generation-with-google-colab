# AI Image & Video Generator

A complete Google Colab notebook for generating images and videos using AI models with an interactive Gradio interface.

## Features

### 🖼️ Image Generation
- **Stable Diffusion v1.5**: High-quality text-to-image generation
- **Customizable parameters**: Steps, guidance scale, seed control
- **Negative prompts**: Specify what to avoid in generated images
- **Memory optimized**: Uses XFormers and attention slicing for efficient GPU usage

### 🎬 Video Generation
- **Text-to-video**: Generate short videos from text descriptions
- **ModelScope integration**: Uses state-of-the-art video synthesis
- **Fallback mode**: Image-based video generation if primary model unavailable
- **Customizable**: Adjustable frame count and FPS

### 🔄 Prompt Interpolation
- **Smooth transitions**: Create videos that morph between two different scenes
- **Creative tool**: Perfect for artistic transitions and animations

## Getting Started

### 1. Upload to Google Colab
1. Go to [Google Colab](https://colab.research.google.com/)
2. Click `File` → `Upload notebook`
3. Select `image_video_generation.ipynb`

### 2. Enable GPU
**Important**: This notebook requires a GPU for optimal performance.

1. Click `Runtime` → `Change runtime type`
2. Select `GPU` from the Hardware accelerator dropdown
3. Choose `T4 GPU` (free tier) or higher
4. Click `Save`

### 3. Run the Notebook
Execute cells in order:
1. **Install Dependencies** - Installs all required packages (~2-3 minutes)
2. **Import Libraries** - Loads Python libraries
3. **Setup Image Model** - Downloads Stable Diffusion (~4 GB, first time only)
4. **Setup Video Model** - Downloads video generation model (optional)
5. **Define Functions** - Sets up generation functions
6. **Create Interface** - Builds the Gradio UI
7. **Launch** - Starts the web interface with a public link

### 4. Use the Interface
After launching, you'll get a public Gradio link. Click it to access the interface with three tabs:

#### Image Generation Tab
```
Prompt: "A serene mountain landscape at sunset, photorealistic"
Negative Prompt: "blurry, low quality"
Steps: 25 (higher = better quality, slower)
Guidance Scale: 7.5 (how closely to follow prompt)
Seed: -1 (random) or any number for reproducibility
```

#### Video Generation Tab
```
Prompt: "Ocean waves crashing on a beach"
Frames: 16 (more = longer video)
FPS: 8 (frames per second)
```

#### Prompt Interpolation Tab
```
Start: "A sunny day in the park"
End: "A starry night sky"
Frames: 30
FPS: 10
```

## Requirements

### Hardware
- **GPU Required**: T4 (free), V100, or A100
- **RAM**: 12GB+ recommended
- **Storage**: ~6-8 GB for models

### Software
All dependencies are automatically installed:
- PyTorch
- Diffusers
- Transformers
- Gradio
- ModelScope
- XFormers (optional, for optimization)

## Tips for Best Results

### Image Generation
- **Be specific**: "A red Victorian house with white trim at sunset" > "a house"
- **Add quality terms**: "photorealistic", "4k", "highly detailed", "studio lighting"
- **Use negative prompts**: "blurry, low quality, distorted, ugly, watermark"
- **Guidance scale**: 7-12 is usually best (higher = more literal prompt following)
- **Steps**: 20-30 is a good balance (50+ for highest quality)

### Video Generation
- **Keep it simple**: Videos work best with clear, straightforward descriptions
- **Describe motion**: "waves crashing", "person walking", "clouds moving"
- **Be patient**: Video generation takes significantly longer than images
- **Start small**: Use fewer frames (8-16) for testing

### Performance Tips
- First run will be slow (downloading models)
- Subsequent generations are much faster
- Lower steps/frames for faster generation
- Close other Colab notebooks to free up RAM
- Restart runtime if you encounter memory errors

## Troubleshooting

### Out of Memory Error
```python
# Add this before loading models
import torch
torch.cuda.empty_cache()
```
Or restart runtime: `Runtime` → `Restart runtime`

### Model Download Issues
Check your internet connection. Models are large:
- Stable Diffusion: ~4 GB
- Video model: ~2-3 GB

### Slow Generation
- Reduce number of steps (try 15-20)
- Use smaller guidance scale (6-8)
- Make sure GPU is enabled
- Check GPU usage: `!nvidia-smi`

### Video Model Not Loading
The notebook has a fallback that creates videos from multiple images if the primary video model fails.

## Advanced Usage

### Change Image Model
Replace the model_id in cell 3:
```python
# For different styles
model_id = "stabilityai/stable-diffusion-2-1"  # SD 2.1
model_id = "dreamlike-art/dreamlike-photoreal-2.0"  # Photorealistic
model_id = "prompthero/openjourney"  # Midjourney-style
```

### Custom Image Sizes
Modify the pipeline call:
```python
result = image_pipe(
    prompt=prompt,
    height=768,  # Change height
    width=768,   # Change width
    # ... other parameters
)
```

### Batch Generation
Generate multiple images:
```python
result = image_pipe(
    prompt=prompt,
    num_images_per_prompt=4,  # Generate 4 images
    # ... other parameters
)
```

## Model Information

### Stable Diffusion v1.5
- **Source**: RunwayML
- **License**: CreativeML Open RAIL-M
- **Size**: ~4 GB
- **Resolution**: 512x512 (default)

### ModelScope Text-to-Video
- **Source**: Alibaba DAMO Academy
- **Size**: ~2.5 GB
- **Output**: 16-24 frames

## License & Attribution

This notebook uses:
- **Stable Diffusion**: [License](https://huggingface.co/spaces/CompVis/stable-diffusion-license)
- **Gradio**: Apache 2.0
- **Diffusers**: Apache 2.0

Please follow each model's license terms for any generated content.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify GPU is enabled in Colab
3. Try restarting the runtime
4. Check Hugging Face model pages for updates

## Examples

### Image Prompts
- "A majestic lion in the African savanna, golden hour, wildlife photography"
- "Cyberpunk city street at night, neon signs, rain-soaked pavement, cinematic"
- "A cozy cottage in the forest, smoke from chimney, autumn leaves, warm lighting"
- "Abstract geometric art, vibrant colors, modern art style, 4k"

### Video Prompts
- "A campfire burning at night"
- "Cherry blossoms falling in the wind"
- "A robot walking through a futuristic city"
- "Northern lights dancing in the sky"

---

**Happy Creating! 🎨🎬**
