#!/usr/bin/node
/**
 * Function to determine the message based on the number of arguments passed.
 *
 * @param {...any} args - The arguments passed to the script.
 */
function printMessageBasedOnArguments (...args) {
  if (args.length === 0) {
    console.log('No argument');
  } else if (args.length === 1) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
}

// Test Cases
printMessageBasedOnArguments(); // Output: No argument
printMessageBasedOnArguments('Hello'); // Output: Argument found
printMessageBasedOnArguments(1, 2, 3); // Output: Arguments found
