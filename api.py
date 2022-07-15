

import requests

from config import API_TOKEN


async def api_request(image_url):
        
    r = requests.post(
        "https://api.deepai.org/api/toonify",
        data={
            'image': image_url,
        },
        headers={'api-key': API_TOKEN}
    )

    data = r.json()
    
    if data:
        return data['output_url']
    return None
