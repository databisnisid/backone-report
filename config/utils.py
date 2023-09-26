

def readable_timedelta(total_seconds):
    #duration = closed_at - created_at
    data = {}
    #data['days'], remaining = divmod(duration.total_seconds(), 86400)
    data['days'], remaining = divmod(int(total_seconds), 86400)
    data['hours'], remaining = divmod(remaining, 3600)
    data['minutes'], data['seconds'] = divmod(remaining, 60)

    time_parts = ((name, round(value)) for name, value in data.items())
    time_parts = [f'{value} {name[:-1] if value == 1 else name}' for name, value in time_parts if value > 0]
    if time_parts:
        return ' '.join(time_parts)
    else:
        return 'below 1 second'

