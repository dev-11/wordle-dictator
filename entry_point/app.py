from services import ServiceFactory
import config as c


def lambda_handler(event, context):
    headers = event["params"]["header"]
    sf = ServiceFactory()

    get_full_list = (
        parse_bool(headers[c.get_full_list_header_key])
        if c.get_full_list_header_key in headers
        else False
    )

    if get_full_list:
        ws = sf.create_word_service()
        return ws.get_all_words()

    update_word_of_the_day = (
        parse_bool(headers[c.update_word_of_the_day_header_key])
        if c.update_word_of_the_day_header_key in headers
        else False
    )

    wds = sf.create_wordle_dictator_service()

    if update_word_of_the_day:
        wds.update_word_of_the_day()

    word_of_the_day = wds.get_word_of_the_day()

    return {
        "data": word_of_the_day
    }


def parse_bool(v):
    return str(v).lower() in ("yes", "true", "t", "1")
