from database import get_db

def checkout_logic():
    db = get_db()
    # Fetching fees from the database
    events_list = db.execute("SELECT fee FROM events").fetchall()
    db.close()

    # TASK: Uncomment the line below for your SS2 (Crash)
    # 1 / 0

    total = 0
    # This is the INEFFICIENT logic for your baseline (SS4)
    for e in events_list:
        fee = e[0]
        while fee > 0:
            total += 1
            fee -= 1

    return total
