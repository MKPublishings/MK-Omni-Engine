def collect_feedback(task, input_data, output, user_rating):
    with open("feedback_log.json", "a") as f:
        f.write(json.dumps({
            "task": task,
            "input": input_data,
            "output": output,
            "rating": user_rating
        }) + "\n")# feedback_loop.py