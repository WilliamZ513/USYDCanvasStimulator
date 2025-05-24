import user_system
import course_system
import assignment_system
import marks_system
import calendar_system

def main():
    cur_user = None

    while True:
        if not cur_user:
            print("\n=== Welcome to USYD Canvas Current Student ===")
            print("1) Register   2) Log in   3) Exit")
            cmd = input(">>> ").strip()

            if cmd == '1':
                u = input("Student Unikey: ").strip()
                p = input("Password: ").strip()
                try:
                    user_system.register_user(u, p)
                    print("Registered successfully. Please log in.")
                except ValueError as e:
                    print("Error:", e)

            elif cmd == '2':
                u = input("Student Unikey: ").strip()
                p = input("Password: ").strip()
                if user_system.login_user(u, p):
                    cur_user = u
                    print(f"Login succeeded. Welcome, {u}!")
                else:
                    print("Login failed. Check your Unikey or password.")

            elif cmd == '3':
                print("Goodbye.")
                break

            else:
                print("Invalid option.")

        
        else:
            print(f"\n=== {cur_user} Dashboard ===")
            print("1) Course   2) Assignment   3) Mark   4) Calendar   5) Logout")
            cmd = input(">>> ").strip()

            
            if cmd == '1':
                courses = course_system.load_user_courses(cur_user)
                if not courses:
                    print("You have no courses yet.")
                else:
                    print("Your courses:")
                    for c in courses:
                        info = course_system.get_course_info(c)
                        tutor = info.get('tutor', 'N/A')
                        coord = info.get('coordinator', 'N/A')
                        print(f"  - {c} (Tutor: {tutor}, Coordinator: {coord})")

                print("\n  a) Add course   d) Delete course   b) Back")
                sub = input("Select action: ").strip().lower()

                if sub == 'a':
                    course = input("Enter course code (e.g. COMP9001): ").strip().upper()
                    if course:
                        try:
                            course_system.add_course(cur_user, course)
                            print(f"Course {course} added.")
                        except ValueError as e:
                            print("Error:", e)

                elif sub == 'd':
                    course = input("Enter course code to delete: ").strip().upper()
                    if course:
                        course_system.delete_course(cur_user, course)

                elif sub == 'b':
                    pass

                else:
                    print("Invalid action.")

            
            elif cmd == '2':
                courses = course_system.load_user_courses(cur_user)
                if not courses:
                    print("You have no courses.")
                else:
                    for c in courses:
                        print(f"[{c}] Assignment list:")
                        for a in assignment_system.list_assignments(c):
                            print(f"  - {a['title']} (Deadline: {a['due_date']})")

                if 'COMP9001' in courses:
                    sub = input("Do you want to take the COMP9001 Intro Quiz now? (y/n) ").strip().lower()
                    if sub == 'y':
                        assignment_system.take_quiz(cur_user)

            
            elif cmd == '3':
                courses = course_system.load_user_courses(cur_user)
                if not courses:
                    print("You have no courses.")
                else:
                    for c in courses:
                        for a in assignment_system.list_assignments(c):
                            m = marks_system.get_mark(cur_user, c, a['title'])
                            status = m if m is not None else 'Not marked yet'
                            print(f"{c} - {a['title']}: {status}")

            
            elif cmd == '4':
                y = input("Year (YYYY): ").strip()
                m = input("Month (MM): ").strip()
                if y.isdigit() and m.isdigit():
                    calendar_system.show_month(int(y), int(m))
                else:
                    print("Invalid year/month format.")

            
            elif cmd == '5':
                print("You have been logged out.")
                cur_user = None

            else:
                print("Invalid option, try again.")

if __name__ == '__main__':
    main()
