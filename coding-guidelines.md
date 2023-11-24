# Coding Guidelines

## Files structure
  Adhere to the project directory structure. This includes placing models, views, templates, static files and tests in their respective directories.

## Pre commit checks
  This project should have pre commit hooks. These hooks help to follow [PEP8](https://peps.python.org/pep-0008/) conventions and identify simple issues before committing code for review.  If an error is found an appropriate error message will be displayed then the tool will go ahead and fix them for you. Review the changes and re-stage for commit if you are happy with them.

## Dependencies 
  pass

## Python Style
- All files should be formatted using the black auto-formatter. This will be run by pre-commit if that is configured.
- The project repository includes an .editorconfig file. We recommend using a text editor with EditorConfig support to avoid indentation and whitespace issues. The Python files use 4 spaces for indentation and the HTML files use 2 spaces.
- Follow [PEP8](https://peps.python.org/pep-0008/) conventions
- String variable interpolation use f-strings
- Use underscores, not camelCase, for variable, function and method names (i.e. get_church_members(), not getChurchMembers()).
- Use InitialCaps for class names.

## Django Style
- Write docstrings for functions, classes, modules, model, model managers, model methods etc using [PEP 257](https://peps.python.org/pep-0257/) style as a guide.
  ### Model Style
  - Field names should be all lowercase, using underscores instead of camelCase.
    ```
      // Do this
      first_name = models.CharField(max_length=20)

      // Don't do this
      firstName = models.CharField(max_length=20)

      // or this
      First_Name = models.CharField(max_length=20)
    ```
  - If choices is defined for a given model field, define each choice as a list of tuples, with an all-uppercase name as a class attribute on the model.
    ```
    // Do this
    class Member(models.Model):
        PASTOR = "P"
        SINGER = "S"
        MEMBER_CHOICE = [
          (PASTOR, "Pastor"),
          (SINGER, "Singer"),
        ]

    // Don't do this
    class Member(models.Model):
        class MemberChoice(models.TextChoice):
            PASTOR = "P", "Pastor"
            SINGER = "S", "Singer"
    
    ```
  - The order of model inner classes and standard methods should be as follows (noting that these are not all required):
    - All database fields
    - Custom manager attributes
    - Class Meta
    - ``` def __str__() ```
    - ``` def save() ```
    - ``` def get_absolute_url() ```
    - Any custom method
      
  ### View Style
  - Use class based views only
 
  ### Template Style
  - Templates location to adhere to project directory structure.
  - In Django template code, put one (and only one) space between the curly brackets and the tag contents.
    ```
      //Do this
      {{ member.first_name }}

    // Don't do this
    {{member.first_name}}
    ```
- Signals, method managers, tasks should be in seperate python files.

## Git commit message 
We recommend the following simple rules on how to write good commit messages:

### Summary Line
- It should contain less than 50 characters. It is best to make it short
- Introduce what has changed, using imperatives: fix, add, modify, etc.

### Description
- Add extra explanation if you feel it will help others to understand the summary content
- If you want, use bullet points (each bullet beginning with a hyphen or an asterisk)
- Avoid writing in one line. Use line breaks so the reader does not have to scroll horizontally
For more information and tips on how to write good commit messages, see the GitHub [guide](https://github.com/erlang/otp/wiki/writing-good-commit-messages)
