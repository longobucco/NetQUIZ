from src.quizCli import QuizCli as Cli

if __name__ == "__main__":
    cli = Cli()
    
    choice = input('''

  ,88~-_            ,e,                      888 ,e,       888~-_               d8   ,e, 
 d888   \  888  888  "   ~~~d88P        e88~\888  "        888   \   e88~~8e  _d88__  "  
88888    | 888  888 888    d88P        d888  888 888       888    | d888  88b  888   888 
88888    | 888  888 888   d88P         8888  888 888       888   /  8888__888  888   888 
 Y888 \ /  888  888 888  d88P          Y888  888 888       888_-~   Y888    ,  888   888 
  `88__X   "88_-888 888 d88P___         "88_/888 888       888 ~-_   "88___/   "88_/ 888 
        \                                                                                
__________________________________________________________________________________________
                   
    
    .__.                  .              .   .    
    |  |._ __.* _ ._ *   _|* __._  _ ._ *|_ *|* * 
    |__|[_) /_|(_)[ )|  (_]|_) [_)(_)[ )|[_)||| * 
        |                      |                  
    
    Avvio da terminale: 0
    Avvio da interfaccia grafica: 1 - non ancora disponibile

selezione: > ''')
    
    if choice == 0:
        print("\n")
    else:
        print("Si rispetta la decisone dell'utente, ma data la mia autorità di programmatore verrà avviato il quiz da terminale:")
    
    cli.run()
    
    

    
    # if not os.path.exists(util.QUIZ_FILE):
    #     save_quiz([])
    # if not os.path.exists(util.RESULTS_FILE):
    #     with open(util.RESULTS_FILE, 'w', encoding='utf-8') as f:
    #         pass
    # menu()
