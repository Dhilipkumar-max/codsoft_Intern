from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# Function to generate caption for an image
def generate_caption(image_path):
    # Load model and processor
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Check for GPU
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)

    # Load and process the image
    image = Image.open(image_path).convert('RGB')
    inputs = processor(images=image, return_tensors="pt")
    inputs = {k: v.to(device) for k, v in inputs.items()}

    # Generate and decode the caption
    output = model.generate(**inputs)
    caption = processor.decode(output[0], skip_special_tokens=True)
    
    return caption

# Usage example
if __name__ == "__main__":
    image_path = "C:/Users/Rimuru/Desktop/Intern/Codesoft/Task_3/image.jpg"  # Replace with the path to your image
    caption = generate_caption(image_path)
    print("🖼 Caption:", caption)
