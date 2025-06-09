from src.quiz import Quiz

class QuizCli:

    def run(self):
        self.menu()

    def runQuiz(self):
        quiz = Quiz()

        requested = 0
        simulator = True

        while True:
            try:
                requested = int(input(f"How many questions do you want (1 - 33)? "))
                break
            except:
                print("❌ Insert a integer value.")

        if not quiz.prepare(requested):
            print("⚠️ No questions available.")
            # return [], [], []
        
        while True:
            inp = input("Exame mode? (if yes you wont be able to see the incorrect answers untill the end)\n[Y]/N: ").strip().lower()
            if inp == "" or inp == "y":
                simulator = True
                break
            elif inp == "n":
                simulator = False
                break
            else:
                print("❌ Please only type Y or N")

        quiz.start()

        # stats
        score = 0.0

        while True:
            category, question, answers, selected = quiz.getCurrent()
            print(f"\n[{quiz.currentQuestion+1}/{len(quiz.questions)}] [{category}] {question}")
            for i, r in enumerate(answers):
                print(f"{i+1}. {r}")
            
            if selected == -1:
                print("Press ENTER to skip.")
                inp = input(
                "Answer / [N]ext / [P]rev / [F]inish: ").strip().lower()

                if inp == "n" or inp == "":
                    quiz.next()
                    continue
                elif inp == "p":
                    quiz.precedent()
                    continue
                elif inp == "f":
                    score = quiz.stop()
                    break
                else:
                    try:
                        ans = int(inp) - 1
                        if quiz.answerCurrent(ans):
                           
                            if simulator:
                                print("Question answered!")
                                
                            else:
                                correct = quiz.getCurrentCorrect()
                                if correct == ans:
                                    print("✅ Correct!")
                                      
                                else:
                                    print(f"❌ Wrong, correct answer: {answers[correct]}") 
                                    input("Press any key to continue...")   

                            quiz.next() 
                        else:
                            print("❌ Invalid answer index.")

                    except:
                        print("❌ Invalid input.")
            else:
                if simulator:
                    print(f"✅ Already answered: {answers[selected]}.")
                else:
                    correct = quiz.getCurrentCorrect()
                    if  correct == selected:
                        print(f"✅ Already answered: {answers[selected]}.")
                    else:
                        print(f"❌ Already answered: {answers[selected]}.\n correct answer: {answers[correct]}")

                    
                inp = input(
                    "Command: [N]ext / [P]rev / [C]hange / [F]inish: ").strip().lower()
                if inp == "n":
                    quiz.next()
                elif inp == "p":
                    quiz.precedent()
                elif inp == "c":
                    if not simulator:
                        print("You can change it only in simulator mode")
                        continue
                    quiz.answerCurrent(-1)
                elif inp == "f":
                    score = quiz.stop()
                    break    
                else:
                    print("❌ Invalid input.")

        print(f"\n🎯 Final Score: {score:.2f}/{quiz.getMaxScore()}")

        while True:
            inp = input("Do you want to save your progres? [Y]/N:  ").strip().lower()

            if inp == "n":
                break
            elif inp == "" or inp =="y":
                try:
                    quiz.save()
                    print("✅ Data saved!")
                except Exception as ex:
                    print(f"❌ Sorry, somthing went wrong data has been lost\n:C\n{ex}")
                break
            else:
                print("❌ Please only type Y or N")
                continue
    


    def menu(self):
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
                self.runQuiz()
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