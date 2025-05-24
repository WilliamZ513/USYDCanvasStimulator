import calendar
from assignment_system import load_assignments

def show_month(year, month):
    cal = calendar.TextCalendar()
    print(cal.formatmonth(year, month))
    print("Deadlines for this month:")
    ca = load_assignments()
    for course, lst in ca.items():
        for a in lst:
            y, m, d = map(int, a['due_date'].split('-'))
            if y == year and m == month:
                print(f"  {m}.{d} : {course} - {a['title']}")