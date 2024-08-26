# Organizer
## Brief description
- Organizer is a small utility program that you should use to customize and organize your file structure on your computer.
- It makes use of a preferences.json file to store your configuration of the software and manage how things are to be organized.

## How it works
- Organizer reads your prefences stored in the preferences.json file in key value pairs.
- The key is to be the folder your files go in, and the value is to be some regex or string match configuration specified by you to match files into their respesctive folder.

## Preferences
- Note that the initial plan was to cater for preferences to be in JSON or not.
- I am adding additional functionality to cater for the average joe.
- The additional functionality will be some sort of string matching the file name based on:
    - Starts with: xxxxx
    - Ends with: xxxxx
    - Contains (is a substring): xxxxx
    - Sort group by extension
- As all of these options may result in some complications when combined, they will be disjoint functions of the program for now.

## Example of preferences.json
- Note that this file will have some default keys based on the options above.
- IT IS MANDATORY THAT YOU DO NOT REMOVE THESE KEYS AS THEY ARE NEEDED BY THE PROGRAM.
```json
{
    is_regex: , //can be true or false
    starts_with: ,//can be true or false
    ends_with: ,//can be true or false
    contains: ,//can be true or false
    group_extension,//can be true or false
    //Anything below this line will be custom regex categories
    //eg:
    documents: [aA-zZ]*
};
```