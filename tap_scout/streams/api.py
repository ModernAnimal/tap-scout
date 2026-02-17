import httpx


def get_headers(api_key):
    headers = {
        "Authorization": f'Bearer {api_key}',
    }

    return headers


def scout_api(scout_url, api_key, appointment_id):
    import httpx
    from httpx import ReadTimeout
    url = f"{scout_url}?appointment_id={appointment_id}"
    headers = get_headers(api_key)
    max_retries = 2
    for attempt in range(max_retries):
        try:
            response = httpx.get(url, headers=headers, timeout=60.0)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except ReadTimeout:
            if attempt == max_retries - 1:
                # Last attempt, fail gracefully
                return None
            # Otherwise, retry
            continue
