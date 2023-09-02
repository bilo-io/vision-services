def generate_video(prompt, max_length=256, model_name="gpt2"):
    return ""
# # https://huggingface.co/cerspense/zeroscope_v2_576w

# import torch
# from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
# from diffusers.utils import export_to_video

# pipe = DiffusionPipeline.from_pretrained("cerspense/zeroscope_v2_576w", torch_dtype=torch.float16)
# pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
# pipe.enable_model_cpu_offload()

# prompt = "Darth Vader is surfing on waves"


# def generate_video(prompt, max_length=256, model_name="gpt2"):
#     video_frames = pipe(prompt, num_inference_steps=40, height=320, width=576, num_frames=24).frames
#     video_path = export_to_video(video_frames)
#     return video_path