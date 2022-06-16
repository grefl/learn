# Preprocessor

## <> vs ""

Using <> means that the preprocessor will ONLY look at system include files.
Using quotes instead will mean the preprocessor will first look in the current dir and then fallback on the system directories 

## define

At its most basic, #define allows you to define new symbols that get replaced with a text string by hte preprocessor.
Example:

```
// will return NULL anywhere that FAILED is declared
#define FAILED NULL
```
### Macros

Using #define with arguments means you can substitute function calls in the place of a #define declaration.

Example:

```
#define HANDLER(name, context) handle_context(event)
// will return the above function -> handle_context(event) 
handler = HANDLER(event, context);
```

### #undef
`#undef` allows you to erase previous definitions of #define. Useful for using `#define` in part of a file.


### #if

Useful for define blocks of text to be inserted or not depending on the condition being true or false



