# dict of movies that follows basic structure:
# name of movie : [genres],[actors],[short description of story]

movies = {
    "Saving Private Ryan": 
        [
            ["action", "war", "drama"], 
            ["Tom Hanks", "Matt Damon", "Edward Burns", "Gary Lecinsohn"], 
            "Saving Private Ryan is a 1998 American epic war film directed by Steven Spielberg and written by Robert Rodat. Set in 1944 in Normandy, France, during World War II, it follows a group of soldiers, led by Captain John Miller (Tom Hanks), on a mission to locate Private James Francis Ryan (Matt Damon) and bring him home safely after his three brothers have been killed in action."
        ],
    "Shawshank Redemption": 
        [
            ["drama", "action"],
            ["Tim Robbins", "Morgan Freeman", "Bub Gunton", "William Sadler"],
            "Chronicles the experiences of a formerly successful banker as a prisoner in the gloomy jailhouse of Shawshank after being found guilty of a crime he did not commit. The film portrays the man's unique way of dealing with his new, torturous life; along the way he befriends a number of fellow prisoners, most notably a wise long-term inmate named Red"
        ],
    "The Godfather":
        [
            ["drama", "mafia", "thriller", "gangster"],
            ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
            "The Godfather \"Don\" Vito Corleone is the head of the Corleone mafia family in New York. He is at the event of his daughter's wedding. Michael, Vito's youngest son and a decorated WWII Marine is also present at the wedding. Michael seems to be uninterested in being a part of the family business. Vito is a powerful man, and is kind to all those who give him respect but is ruthless against those who do not. But when a powerful and treacherous rival wants to sell drugs and needs the Don's influence for the same, Vito refuses to do it. What follows is a clash between Vito's fading old values and the new ways which may cause Michael to do the thing he was most reluctant in doing and wage a mob war against all the other mafia families which could tear the Corleone family apart."
        ],
    "The Dark Knight": 
        [
            ["action", "superhero", "drama", "crime"], 
            ["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Michael Caine"], 
            "Set within a year after the events of Batman Begins (2005), Batman, Lieutenant James Gordon, and new District Attorney Harvey Dent successfully begin to round up the criminals that plague Gotham City, until a mysterious and sadistic criminal mastermind known only as \"The Joker\" appears in Gotham, creating a new wave of chaos. Batman's struggle against The Joker becomes deeply personal, forcing him to \"confront everything he believes\" and improve his technology to stop him. A love triangle develops between Bruce Wayne, Dent, and Rachel Dawes."
        ],
    "The Godfather Part II": 
        [
            ["drama", "mafia", "thriller", "gangster"],
            ["Al Pacino", "Robert De Niro", "Robert Duvall", "Diane Keaton"],
            "The continuing saga of the Corleone crime family tells the story of a young Vito Corleone growing up in Sicily and in 1910s New York; and follows Michael Corleone in the 1950s as he attempts to expand the family business into Las Vegas, Hollywood and Cuba."
        ],
    "12 Angry Men":
        [
            ["drama", "psychological", "crime", "legal"],
            ["Henry Fonda", "Lee J. Cobb", "Martin Balsam", "John Fiedler"],
            "The defense and the prosecution have rested, and the jury is filing into the jury room to decide if a young man is guilty or innocent of murdering his father. What begins as an open-and-shut case of murder soon becomes a detective story that presents a succession of clues creating doubt, and a mini-drama of each of the jurors' prejudices and preconceptions about the trial, the accused, AND each other. Based on the play, all of the action takes place on the stage of the jury room."
        ],
    "Lord of the Rings: The Return of the King": 
        [
            ["action", "war", "drama", "epic", "fantasy", "adventure"], 
            ["Elijah Wood", "Viggo Mortensen", "Ian McKellen", "Orlando Bloom"], 
            "The final confrontation between the forces of good and evil fighting for control of the future of Middle-earth. Frodo and Sam reach Mordor in their quest to destroy the One Ring, while Aragorn leads the forces of good against Sauron's evil army at the stone city of Minas Tirith."
        ],
    "Schindler's List": 
        [
            ["drama", "epic", "tragedy", "biography", "history"],
            ["Liam Neeson", "Ralph Fiennes", "Ben Kingsley", "Caroline Goodall"],
            "Oskar Schindler is a vain and greedy German businessman who becomes an unlikely humanitarian amid the barbaric German Nazi reign when he feels compelled to turn his factory into a refuge for Jews. Based on the true story of Oskar Schindler who managed to save about 1100 Jews from being gassed at the Auschwitz concentration camp, it is a testament to the good in all of us."
        ],
    "Pulp Fiction":
        [
            ["comedy", "gangster", "crime", "drama"],
            ["John Travolta", "Uma Thurman", "Samuel L. Jackson", "Bruce Willis"],
            "Jules Winnfield (Samuel L. Jackson) and Vincent Vega (John Travolta) are two hitmen who are out to retrieve a suitcase stolen from their employer, mob boss Marsellus Wallace (Ving Rhames). Wallace has also asked Vincent to take his wife Mia (Uma Thurman) out a few days later when Wallace himself will be out of town. Butch Coolidge (Bruce Willis) is an aging boxer who is paid by Wallace to lose his fight. The lives of these seemingly unrelated people are woven together comprising of a series of funny, bizarre and uncalled-for incidents.",
            
        ],
    "The Lord of the Rings: The Fellowship of the Ring": 
        [
            ["action", "war", "epic", "drama", "adventure", "fantasy"], 
            ["Elijah Wood", "Viggo Mortensen", "Ian McKellen", "Orlando Bloom"], 
            "An ancient Ring thought lost for centuries has been found, and through a strange twist of fate has been given to a small Hobbit named Frodo. When Gandalf discovers the Ring is in fact the One Ring of the Dark Lord Sauron, Frodo must make an epic quest to Mount Doom in order to destroy it. However, he does not go alone. He is joined by Gandalf, Legolas the elf, Gimli the Dwarf, Aragorn, Boromir, and his three Hobbit friends Merry, Pippin, and Samwise. Through mountains, snow, darkness, forests, rivers and plains, facing evil and danger at every corner the Fellowship of the Ring must go. Their quest to destroy the One Ring is the only hope for the end of the Dark Lords reign."
        ],
    "The Good, the Bad and the Ugly": 
        [
            ["drama", "action", "western", "epic"],
            ["Clint Eastwood", "Eli Wallach", "Lee Van Cleef", "Aldo Giuffrè"],
            "During the American Civil War, three men set off to find $200,000.00 in buried gold coins. Tuco and Blondie have known each other for some time, having used the reward on Tuco's head as a way of earning money. They come across a dying man, Bill Carson, who tells them of a treasure in gold coins. By chance, he reveals the name of the cemetery and the name of the grave where the gold is buried. Now rivals, the two men have good reason to keep each other alive. The third man, Angel Eyes, hears of the gold stash from someone he's been hired to kill. All he knows is to look for someone named Bill Carson. The three ultimately meet in a showdown that takes place amid a major battle between Confederate and Union forces."
        ]
}