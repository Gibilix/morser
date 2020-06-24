# morser
International morse-code translator that is also able to guess the most likely meaning of a morse-code string without any spaces. 

The point of this git project is to develop a program that is able to deal with what one may call morse-code laziness; that is when there is no indication of a new character, word, or phrase within a morse encoded message. I'd imagine a program would do this by looking at all the possible combinations of dits and dahs and spitting out any ones that look like english for the human to go over manually and pick the most likely one. However if anyone beleives to have a more effienct way for a program to accomplish this please contact me or make a pull request (there can be a lot of combinations to go through). I decided to create this project in python as I figured it would make the seperation of dits and dahs fairly easy. Though I do not think I mind the use of other languages for this project.

The reason iI have called it "morser" instead of, say, morse, is because if you where to run this program as a command, the alias morse is probably already taken. So a took a play on words with morser, meaning *more* morse.
