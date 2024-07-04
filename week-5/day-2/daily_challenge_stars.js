for(let i = 1; i < 7; i++){
    console.log('* '.repeat(i))
}

for(let i = 1; i < 7; i++){
    let string = '';
    for(let j = 1; j < i + 1; j++){
        string += '* '
    }
    console.log(string)
}
