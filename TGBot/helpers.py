import requests
import json
import ast


def get_schedule(group_name: str, day: str = "today"):
    response = requests.post(
        "http://127.0.0.1:8000/schedule/vstechnical_group/",
        json={"group_name": group_name}
    )
    raw = json.loads(response.content)[day]
    return ast.literal_eval(raw)


def viewSchedule(data: list):
    print(data)
    text = f"Расписание учебной группы {data[1][0]}:\n"
    prev_time, prev_lesson = None, None  
    for i in range(1, len(data[0])):
        if data[1] != "":
            text += f"\n{data[0][i]} \"{data[1][i]} : {data[2][i]}\"\n"
    return text


def markup_to_json(markup):
    return json.dumps(markup.to_dict(), sort_keys=True)
