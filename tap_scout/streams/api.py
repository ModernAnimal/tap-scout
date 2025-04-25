import httpx


def get_headers(api_key):
    headers = {
        "Authorization": f'Bearer {api_key}',
    }

    return headers


def scout_api(scout_url, api_key, appointment_id):
    response = httpx.get(
        url=f"{scout_url}?appointment_id={appointment_id}",
        headers=get_headers(api_key)
    )

    if response.status_code == 200:
        return response.json()
    else:
        print(
            f"Error: {response.status_code}, appointment_id: {appointment_id}"
        )
        return None
