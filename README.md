# tap-scout
<a href="https://www.singer.io/">Singer</a> tap for extracting anesthetic parameter data from <a href="https://scoutapp.vet/">Scout</a>.

Necessary Attributes for your Config file:
- `api_key`: The API key for the Scout account.
- `scout_url`: The URL of your Scout instance, ending with `/export-data-json`.
- `appointment_ids`: A list of the appointment IDs you would like to extract anesthetic data for.

Schema Discovery:
- `tap-scout --config CONFIG_FILE --discover > catalog.json`

Running the tap:
- `tap-scout --config CONFIG_FILE --catalog CATALOG_FILE`
