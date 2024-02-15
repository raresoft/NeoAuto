NeoAuto
=======

Automates Neopets games using string manipulation.

### Description:
NeoAuto is a collection of Python scripts that automate various actions for playing Neopets.
Automated actions include: 
- Automated Pet Trainer - Starts and pays for training courses based on your desired stat and mode
- Auto Battler - Starts and completes Battledome matches
- Automated Avatar Collector - Obtains all missing clickable avatars
- Inventory Manager - Quickly sends all items to SDB or fetches requested item from SDB, as well as can automatically buy desired item if missing in inventory through Shop Wizard (at lowest price found) 
- Altador Plot Solver - Completes all of the Altador Cup Plot including the puzzles 
- Bank Manager - Keeps minimum neopoints on hand and smartly deposits & withdraws from bank when account balance increases or decreases past this minimum 
- Cliffhanger Solver - Solves the hangman puzzle
- Automated Dailies - Completes all desired dailies and keeps track of dailies already performed today
- Automated Hotel - Checks in active or all pets into hotel 
- Shop Manager - Withdraws from shop till and restocks items at desired set price

To automate an action, the Python scripts crawl the website and record various parts of the HTML
website files. 

### Required
- Download Python 2.7 (Windows, PC, iOS, Android, Mac)
- Internet Connection

### How to use:
1. If Python is not alreay downloaded, download here: https://www.python.org/downloads/
2. Clone the repository: https://docs.github.com/en/repositories/creating-and-managing-
repositories/cloning-a-repository
3. Run the Client.py script
The script can be run in a variety of ways:
a. Double clicking on script in File explorer
b. Running &quot;Python Client.py&quot; in terminal
c. Run the program using an IDE
4. Enter username and password when prompted

To ensure the scripts are running, check for the Client.py file in Task Manager or check the logs folder.

### File Structure:
- cache: Contains previous configuration files
- classes: Contains Python classes for each automated action 
- list: Records events that occured during automation
- logs: Contains previous snapshots
- pyamf: Scripts for automating each action
- .gitattributes: .git file
- .gitignore: ignore file
- README.md: Current file
- client.py: Starting script
- new.txt: Previous work completed
