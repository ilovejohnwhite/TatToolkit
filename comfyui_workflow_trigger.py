import json
from urllib import request, parse

workflow_json_text = """
{
    "input": {
        "handler": "RawWorkflow",
        "workflow_json": {
            "1": {
                "class_type": "CheckpointLoaderSimple",
                "inputs": {
                    "ckpt_name": "Trace.safetensors"
                }
            },
            "2": {
                "class_type": "CLIPSetLastLayer",
                "inputs": {
                    "stop_at_clip_layer": -1,
                    "clip": ["1", 1]
                }
            },
            "3": {
                "class_type": "CLIPTextEncode",
                "inputs": {
                    "text": "art by coloring-book-style (distinct black lines on white background) a line drawing, lineart, threshold, linework, .line, MONOCHROME, GREYSCALE",
                    "clip": ["10", 1]
                }
            },
            "4": {
                "class_type": "CLIPTextEncode",
                "inputs": {
                    "text": "(shading, shadows, gray), (scribbles, scratches, dots, splatter), signature, watermark, logo, photo, 3d (worst quality, low quality), noise, anime eyes, face, eyelashes, eyelids,",
                    "clip": ["10", 1]
                }
            },
            "5": {
                "class_type": "KSampler",
                "inputs": {
                    "seed": 120279898607248,
                    "steps": 30,
                    "cfg": 7.98,
                    "sampler_name": "euler",
                    "scheduler": "normal",
                    "denoise": 0.9400000000000001,
                    "model": ["10", 0],
                    "positive": ["16", 0],
                    "negative": ["16", 1],
                    "latent_image": ["59", 0]
                }
            },
            "7": {
                "class_type": "VAEDecode",
                "inputs": {
                    "samples": ["5", 0],
                    "vae": ["8", 0]
                }
            },
            "8": {
                "class_type": "VAELoader",
                "inputs": {
                    "vae_name": "vae-ema-84.safetensors"
                }
            },
            "10": {
                "class_type": "LoraLoader",
                "inputs": {
                    "lora_name": "Outline.safetensors",
                    "strength_model": 0.7000000000000001,
                    "strength_clip": 1,
                    "model": ["19", 0],
                    "clip": ["19", 1]
                }
            },
            "13": {
                "class_type": "ControlNetLoader",
                "inputs": {
                    "control_net_name": "controlnetlineart.safetensors"
                }
            },
            "16": {
                "class_type": "ControlNetApplyAdvanced",
                "inputs": {
                    "strength": 1.5,
                    "start_percent": 0.05,
                    "end_percent": 1,
                    "positive": ["3", 0],
                    "negative": ["4", 0],
                    "control_net": ["13", 0],
                    "image": ["182", 0]
                }
            },
            "19": {
                "class_type": "LoraLoader",
                "inputs": {
                    "lora_name": "Lineart.safetensors",
                    "strength_model": 0.7000000000000001,
                    "strength_clip": 1,
                    "model": ["1", 0],
                    "clip": ["2", 0]
                }
            },
            "55": {
                "class_type": "Image Load with Metadata (WLSH)",
                "inputs": {
                    "verbose": "true",
                    "image": "URL/to/user-uploaded-image.png",  # Dynamic replacement
                    "upload": "image"
                }
            },
            "57": {
                "class_type": "ConstrainImage|pysssss",
                "inputs": {
                    "max_width": 1024,
                    "max_height": 1024,
                    "min_width": 0,
                    "min_height": 0,
                    "crop_if_required": "no",
                    "images": ["73", 0]
                }
            },
            "59": {
                "class_type": "VAEEncode",
                "inputs": {
                    "pixels": ["57", 0],
                    "vae": ["8", 0]
                }
            },
            "73": {
                "class_type": "EmptyImage",
                "inputs": {
                    "width": ["55", 6],
                    "height": ["55", 7],
                    "batch_size": 1,
                    "color": 16777215
                }
            },
            "89": {
                "class_type": "ConstrainImage|pysssss",
                "inputs": {
                    "max_width": 1024,
                    "max_height": 1024,
                    "min_width": 0,
                    "min_height": 0,
                    "crop_if_required": "no",
                    "images": ["117", 0]
                }
            },
            "91": {
                "class_type": "ImageBlend",
                "inputs": {
                    "blend_factor": 1,
                    "blend_mode": "multiply",
                    "image1": ["96", 0],
                    "image2": ["137", 0]
                }
            },
            "92": {
                "class_type": "SaveImage",
                "inputs": {
                    "filename_prefix": "ComfyUI",
                    "images": ["104", 0]
                }
            },
            "96": {
                "class_type": "Image Levels Adjustment",
                "inputs": {
                    "black_level": 55.1,
                    "mid_level": 90.10000000000001,
                    "white_level": 180,
                    "image": ["7", 0]
                }
            },
            "102": {
                "class_type": "ImageUpscaleWithModel",
                "inputs": {
                    "upscale_model": ["103", 0],
                    "image": ["91", 0]
                }
            },
            "103": {
                "class_type": "UpscaleModelLoader",
                "inputs": {
                    "model_name": "4xNMKDSiax.pth"
                }
            },
            "104": {
                "class_type": "ImageScaleBy",
                "inputs": {
                    "upscale_method": "bicubic",
                    "scale_by": 1,
                    "image": ["102", 0]
                }
            },
            "111": {
                "class_type": "SuckerPunch",
                "inputs": {
                    "n_clusters": "Normal",
                    "resolution": 2048,
                    "image": ["55", 0]
                }
            },
            "117": {
                "class_type": "LinkMasterNode",
                "inputs": {
                    "resolution": 2048,
                    "image": ["111", 0]
                }
            },
            "137": {
                "class_type": "Image Levels Adjustment",
                "inputs": {
                    "black_level": 50.300000000000004,
                    "mid_level": 100.80000000000001,
                    "white_level": 220.4,
                    "image": ["89", 0]
                }
            },
            "151": {
                "class_type": "ImageBlend",
                "inputs": {
                    "blend_factor": 0.5,
                    "blend_mode": "screen"
                    // Note: The original inputs for "image1" and "image2" are missing here; you'll need to fill these in based on your workflow's logic
                }
            },
            "182": {
                "class_type": "Image Levels Adjustment",
                "inputs": {
                    "black_level": 0,
                    "mid_level": 127.80000000000001,
                    "white_level": 124.10000000000001,
                    "image": ["190", 0]
                }
            },
            "190": {
                "class_type": "LineArtPreprocessor",
                "inputs": {
                    "coarse": "disable",
                    "resolution": 2048,
                    "image": ["55", 0]
                }
            }
        }
    }
}
""".replace('placeholder_for_dynamic_image_url', user_uploaded_image_url)  # Dynamically replace the placeholder URL

def queue_workflow(workflow_json_text):
    data = workflow_json_text.encode('utf-8')  # Encode the string to bytes
    req = request.Request("http://127.0.0.1:8188/prompt", data=data, headers={'Content-Type': 'application/json'})
    response = request.urlopen(req)
    print(response.read().decode('utf-8'))

# Assuming you have obtained the user's uploaded image URL
user_uploaded_image_url = "https://example.com/path/to/user/image.png"

# Call the function with the workflow JSON text
queue_workflow(workflow_json_text)