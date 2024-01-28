from urllib.parse import urljoin

import requests


class SDWebAPIHandler:
    def __init__(self):
        self.base_url = "http://127.0.0.1:7860/"

    def _make_get_request(self, endpoint, params):
        url = urljoin(self.base_url, endpoint)
        response = requests.get(url, params=params)
        return response.json()

    def _make_post_request(self, endpoint, params):
        url = urljoin(self.base_url, endpoint)
        response = requests.post(url, json=params)
        return response.json()

    def queue_status(self):
        endpoint = "/queue/status"
        params = {}
        return self._make_get_request(endpoint, params)

    def txt2img(
        self,
        prompt,
        negative_prompt="EasyNegative2",
        sampler_name="DPM++ 2M Karras",
        batch_size=1,
        steps=20,
        cfg_scale=7,
        width=512,
        height=512,
        restore_faces=False,
        enable_hr=False,  # FIXME: If True, an error occurs
        hr_scale=1.5,
        hr_upscaler="SwinIR 4x",
    ):
        endpoint = "/sdapi/v1/txt2img"
        params = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "sampler_name": sampler_name,
            "batch_size": batch_size,
            "steps": steps,
            "cfg_scale": cfg_scale,
            "width": width,
            "height": height,
            "restore_faces": restore_faces,
            "enable_hr": enable_hr,
            "hr_scale": hr_scale,
            "hr_upscaler": hr_upscaler,
        }
        return self._make_post_request(endpoint, params)

    def png_info(self, image):
        endpoint = "/sdapi/v1/png-info"
        params = {"image": f"data:image/png;base64,{image}"}
        return self._make_post_request(endpoint, params)