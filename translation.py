from google.cloud import translate

def batch_translate_text(
    input_uri="gs://input_translation/input/input_00.txt",
    output_uri="gs://out_translation/test-dev2015_questions_00_hin/",
    project_id="singular-antler-295914",
    timeout=3600,
):
    """Translates a batch of texts on GCS and stores the result in a GCS location."""

    client = translate.TranslationServiceClient()

    location = "us-central1"
    # Supported file types: https://cloud.google.com/translate/docs/supported-formats
    gcs_source = {"input_uri": input_uri}

    input_configs_element = {
        "gcs_source": gcs_source,
        "mime_type": "text/plain",  # Can be "text/plain" or "text/html".
    }
    gcs_destination = {"output_uri_prefix": output_uri}
    output_config = {"gcs_destination": gcs_destination}
    parent = f"projects/{project_id}/locations/{location}"

    # Supported language codes: https://cloud.google.com/translate/docs/language
    operation = client.batch_translate_text(
        request={
            "parent": parent,
            "source_language_code": "en",
            "target_language_codes": ["hi"],  # Up to 10 language codes here.
            "input_configs": [input_configs_element],
            "output_config": output_config,
        }
    )

    print("Waiting for operation to complete...")
    response = operation.result(timeout)

    print("Total Characters: {}".format(response.total_characters))
    print("Translated Characters: {}".format(response.translated_characters))

source = "gs://input_translation/input/"
dest = "gs://out_translation/"

for i in range(11):
    num = i
    num_str = format(num, '02d')
    in_uri = source+"input_" + num_str + ".txt"
    out_uri = dest+"out_" + num_str + "/"
    print ("Starting to translate file = " + str(num))
    batch_translate_text(input_uri=in_uri, output_uri=out_uri)
    print ("Translation finished!\n")