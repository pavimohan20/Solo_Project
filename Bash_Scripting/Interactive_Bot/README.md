# Friend Bot

## Introduction
Have you ever thought that you'd rather talk to your computer than to the people around you? This project is your chance to create a virtual friend! By scripting a bot, you’ll have a companion who can interpret commands, respond intelligently, and keep you entertained with jokes, the time, calculations, and more.

## Features

### Core Functionalities
1. **Random Jokes**
   - The bot can tell jokes randomly selected from a file.
   - Uses the `shuf` command or the `$RANDOM` environment variable.

2. **Time Inquiry**
   - Provides the current date and time using the `date` command.

3. **Simple Equation Solver**
   - Handles basic arithmetic calculations like addition, subtraction, multiplication, and division.

4. **Interactive and Non-Interactive Modes**
   - Interactive Mode: Engage in a live conversation with the bot.
   - Non-Interactive Mode: Execute commands directly via the command line.

### Optional Enhancements
1. **Prettified Output**
   - Enhances the bot’s responses with formatted and colorful output for a better user experience.

2. **Audio Output**
   - Integrates the `espeak` tool to allow the bot to "speak" its responses.

3. **Weather Updates**
   - Answers weather-related queries by fetching live data from [wttr.in](https://github.com/chubin/wttr.in) using the `curl` command.

4. **Executable Script**
   - Adds the script to your `$PATH` to enable execution from anywhere on your system.

## Usage

### Interactive Mode
- Run the script and engage with the bot in real-time.
```bash
./friend.sh
```

### Non-Interactive Mode
- Use command-line arguments to execute specific functions.
```bash
./friend.sh --joke
./friend.sh --time
./friend.sh --calc "4 + 5"
./friend.sh --weather
```

### Example Commands
1. **Jokes**:
   - `./friend.sh --joke`
   - Outputs a random joke from the predefined list.

2. **Time**:
   - `./friend.sh --time`
   - Returns the current date and time.

3. **Calculations**:
   - `./friend.sh --calc "6 * 7"`
   - Solves and outputs the result of the given equation.

4. **Weather**:
   - `./friend.sh --weather`
   - Provides live weather updates.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Make the script executable:
   ```bash
   chmod +x friend.sh
   ```

3. Add the script to your `$PATH` (optional):
   ```bash
   export PATH=$PATH:$(pwd)
   ```

4. Install dependencies (if any):
   - For `espeak`:
     ```bash
     sudo apt install espeak
     ```

## Future Improvements
- Add support for additional languages for jokes and responses.
- Incorporate a small database for more complex commands.
- Add personalized greetings based on user preferences.
- Integrate AI APIs for more conversational capabilities.

## Conclusion
This Friend Bot is a fun and functional way to explore the power of shell scripting. Whether you want a quick laugh, need the current time, or want help with basic calculations, this script is here for you. Feel free to enhance it and make it your own!

