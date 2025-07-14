import ollama


def download_model_if_not_exists(model_name: str):
    try:
        ollama.show(model_name)
    except ollama.ResponseError as e:
        print('Error:', e.error)
        if e.status_code == 404:
            ollama.pull(model_name)
