import quiz

class QuizCli:

    def menu():
        while True:
            print("\n=== QUIZ MENU ===")
            print("1. Run quiz")
            print("2. Add question")
            print("3. Recovery quiz")
            print("4. Quiz by category")
            print("5. Study theory")
            print("6. View study statistics")
            print("7. Exit")
            choice = input("Choice: ")
            if choice == "1":
                print("Work In Progress")
                # run_quiz()
            elif choice == "2":
                print("Work In Progress")
                # add_question()
            elif choice == "3":
                print("Work In Progress")
                # recovery_quiz()
            elif choice == "4":
                print("Work In Progress")
                # quiz_by_category()
            elif choice == "5":
                print("Work In Progress")
                # study_theory()
            elif choice == "6":
                print("Work In Progress")
                # show_study_stats()
            elif choice == "7":
                break
            else:
                print("❌ Invalid option.")