//DC 1

function makeAllCaps(stringsArr){
    return new Promise((res, rej) => {
        if(stringsArr.every(item => typeof item === 'string')){
            res(stringsArr.map(str => str.toUpperCase()))
        } else rej("non-string items are not allowed")
    })
}

function sortWords(capsArr){
    return new Promise((res, rej) => {
        if(capsArr.length > 4){
            res(capsArr.sort())
        } else rej("must be more than 4 words")
    })
}

//in this example, the catch method is executed
makeAllCaps([1, "pear", "banana"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result))
      .catch(error => console.log(error))

//in this example, the catch method is executed
makeAllCaps(["apple", "pear", "banana"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result))
      .catch(error => console.log(error))

//in this example, you should see in the console, 
// the array of words uppercased and sorted
makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result)) //["APPLE","BANANA", "KIWI", "MELON", "PEAR"]
      .catch(error => console.log(error))


//DC 2 


const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
  }`


function toJS(){
    return new Promise((res, rej) => {
        try {
            const morseJS = JSON.parse(morse)
            if(Object.keys(morseJS).length === 0){
                rej("empty object")
            } else res(morseJS)
        } catch (error) {
            rej(error)
        }
    })
}

function toMorse(morseJS) {
    return new Promise((res, rej) => {
        const word = prompt("Enter a word: ");
        if([...word].every(char => Object.keys(morseJS).includes(char))){
            res([...word].map(char => morseJS[char]))
        } else {
            rej("unidentified characters")
        }
    })
}

function joinWords(morseTranslation){
    return morseTranslation.join('\n')
}


toJS().then(morseJS => toMorse(morseJS).then(morseArr => document.body.innerText += joinWords(morseArr)))


