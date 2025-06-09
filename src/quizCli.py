import random
from src.quiz import Quiz
from src.quizClass.dataManager import DataManager

class QuizCli:

    def run(self):
        self.menu()

    def runQuiz(self,  _customQuestions = None):
        quiz = Quiz()

        requested = 0
        simulator = False
        
        if not _customQuestions:
            while True:
                try:
                    requested = int(input(f"How many questions do you want (1 - 33)? "))
                    break
                except:
                    print("❌ Insert a integer value.")
                    
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

        if not quiz.prepare(requested, _customQuestions):
            print("⚠️ No questions available.")
            
        quiz.start() # start timer

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
    
    def addQuestion(self):
        dataManager = DataManager()
        quizData = dataManager.load("quiz")
        newId = max((q.get("id", 0) for q in quizData), default=0) + 1
        domanda = input("Inserisci la domanda: ")
        categoria = input("Inserisci la categoria: ")
        risposte = []
        while True:
            r = input("Inserisci una possibile risposta (invio per terminare): ")
            if r == "":
                break
            risposte.append(r)
        while True:
            try:
                corretta = int(
                    input(f"Indice della risposta corretta (0 - {len(risposte)-1}): "))
                if 0 <= corretta < len(risposte):
                    break
            except:
                pass
            print("Invalid index.")
        quizData.append({
            "id": newId,
            "domanda": domanda,
            "risposte": risposte,
            "corretta": corretta,
            "categoria": categoria
        })
        try:
            dataManager.overwriteInput("quiz", quizData)
            print("✅ Question added with ID", newId)
        except Exception as ex:
            print(f"❌ Sorry, somthing went wrong\n:C\n{ex}")

    def quizByCategory(self):
        dataManager = DataManager()
        quizData = dataManager.load("quiz")

        categories = sorted(set(q["categoria"] for q in quizData))
        print("\nAvailable categories:")
        for i, cat in enumerate(categories, start=1):
            print(f"{i}. {cat}")
        try:
            choice = int(input("Select the category number: ")) - 1
            if 0 <= choice < len(categories):
                selected_category = categories[choice]
                category_questions = [
                    q for q in quizData if q["categoria"] == selected_category]
                n_questions = len(category_questions)
                if n_questions == 0:
                    print("⚠️ No questions found for this category.")
                    return
                while True:
                    try:
                        requested = int(
                            input(f"How many questions do you want (1 - {n_questions})? "))
                        if 1 <= requested <= n_questions:
                            selected_questions = random.sample(
                                category_questions, requested)
                            break
                        else:
                            print("❌ Number out of range.")
                    except ValueError:
                        print("❌ Enter a valid number.")
                self.runQuiz(selected_questions)
                # update_study_stats(quiz_data, wrong, skipped)
            else:
                print("❌ Invalid choice.")
        except ValueError:
            print("❌ Enter a valid number.")


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
                self.addQuestion()
            elif choice == "3":
                print("Work In Progress")
                # recovery_quiz()
            elif choice == "4":
                self.quizByCategory()
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