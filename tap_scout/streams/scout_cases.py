import json
import logging
import time

import singer

from tap_scout.streams.api import scout_api


def stream(scout_url, api_key, appointment_ids):
    """
    This function retrieves data from the Scout API and returns it as a list of dictionaries.
    :param scout_url: The URL of the Scout API. Exclude query parameters.
    :param api_key: The API key for authentication.
    :param appointment_id: The appointment ID to retrieve data for.
    :return: A list of dictionaries containing the data retrieved from the API.
    """
    for appointment_id in appointment_ids:
        case = scout_api(scout_url, api_key, appointment_id)
        if not case:  # Check if the response is empty or None
            logging.error(f"Error: No data or invalid response for appointment_id: {appointment_id}")
            continue

        try:
            case = json.loads(case)  # Attempt to parse the JSON
        except json.JSONDecodeError as e:
            logging.error(f"Unable to parse JSON for appointment_id: {appointment_id}. Error: {e}")
            continue

        patient_data = case.get("patient")

        singer.write_record(
            "scout_cases",
            {
                "appointment_id": appointment_id,
                "procedures": case.get("procedures"),
                "staff": case.get("staff"),
                "additional_medication": patient_data.get(
                    "additionalMedications"
                ),
                "anesthetic_gases": patient_data.get("anestheticGases"),
                "birthdate": patient_data.get("birthdate"),
                "breed": patient_data.get("breed"),
                "dental_chartings": patient_data.get("dentalChartings"),
                "fluid_cri_with_dilutions": patient_data.get(
                    "fluidCriWithDilutions"
                ),
                "fluid_cri_without_dilutions": patient_data.get(
                    "fluidCriWithoutDilutions"
                ),
                "monitoring_vitals": patient_data.get("monitoringVitals"),
                "name": patient_data.get("name"),
                "overall_timer": patient_data.get("overallTimer"),
                "overall_timer_notes": patient_data.get(
                    "overallTimerNotes"
                ),
                "patient_procedures": patient_data.get("patientProcedures"),
                "post_anesthetic_vitals": patient_data.get(
                    "postAnestheticVitals"
                ),
                "pre_anesthetic_medications": patient_data.get(
                    "preAnestheticMedications"
                ),
                "pre_induction_vitals": patient_data.get("preInductionVital"),
                "procedure_date": patient_data.get("procedure_date"),
                "regional_blocks": patient_data.get("regionalBlocks"),
                "resuscitate": patient_data.get("resuscitate"),
                "sex": patient_data.get('sex'),
                "species": patient_data.get("species"),
                "spayed_or_neutered": patient_data.get(
                    "spayed_or_neutered"
                ),
                "weight": patient_data.get("weight")
            }
        )

        # Rate limiting to prevent error of duplicate data
        # being written for different appointment_ids
        time.sleep(1)

    logging.info("Completed scout_cases.py")
