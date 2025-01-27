#!/bin/bash

# File containing jokes (ensure this exists or create one)
JOKES_FILE="jokes.txt"

# Function to display a random joke
function tell_joke() {
  if [[ -f "$JOKES_FILE" ]]; then
    joke=$(shuf -n 1 "$JOKES_FILE")
    echo -e "\033[1;32mHere's a joke for you:\033[0m $joke"
    espeak "$joke" 2>/dev/null
  else
    echo -e "\033[1;31mI can't find the jokes file! Make sure $JOKES_FILE exists.\033[0m"
  fi
}

# Function to tell the current time
function tell_time() {
  time=$(date +"%Y-%m-%d %H:%M:%S")
  echo -e "\033[1;34mThe current time is:\033[0m $time"
  espeak "The current time is $time" 2>/dev/null
}

# Function to calculate simple equations
function calculate() {
  local equation="$1"
  result=$(echo "scale=2; $equation" | bc 2>/dev/null)
  if [[ $? -eq 0 ]]; then
    echo -e "\033[1;33mThe result of $equation is:\033[0m $result"
    espeak "The result of $equation is $result" 2>/dev/null
  else
    echo -e "\033[1;31mInvalid equation. Please try again.\033[0m"
  fi
}

# Function to get the weather
function tell_weather() {
  location="${1:-your location}"
  echo -e "\033[1;35mFetching weather for $location...\033[0m"
  curl -s "wttr.in/$location?format=3"
}

# Interactive mode
function interactive_mode() {
  echo -e "\033[1;36mHello! I'm your friend. What can I do for you?\033[0m"
  echo -e "\033[1;36mType 'joke', 'time', 'calc', 'weather', or 'exit'.\033[0m"
  while true; do
    read -p "> " command
    case "$command" in
      joke) tell_joke ;;
      time) tell_time ;;
      calc)
        read -p "Enter equation: " equation
        calculate "$equation"
        ;;
      weather)
        read -p "Enter location (or press enter for default): " location
        tell_weather "$location"
        ;;
      exit)
        echo -e "\033[1;36mGoodbye!\033[0m"
        exit 0
        ;;
      *)
        echo -e "\033[1;31mInvalid command. Try 'joke', 'time', 'calc', 'weather', or 'exit'.\033[0m"
        ;;
    esac
  done
}

# Non-interactive mode
function non_interactive_mode() {
  case "$1" in
    joke) tell_joke ;;
    time) tell_time ;;
    calc) calculate "$2" ;;
    weather) tell_weather "$2" ;;
    *)
      echo -e "\033[1;31mInvalid command. Try 'joke', 'time', 'calc <equation>', or 'weather <location>'.\033[0m"
      ;;
  esac
}

# Main script logic
if [[ "$#" -eq 0 ]]; then
  interactive_mode
else
  non_interactive_mode "$@"
fi
