const fs = require('fs');
const news = require('../../mocks/reddit/users_new.json');
const popular = require('../../mocks/reddit/users_popular.json');

function generateClassPython(AnyObject, className) {
    const fileName = `domain/reddit/${className}.py`
    const arr_keys = []
    let str_methods = ''

    Object.keys(AnyObject).map(e => {
        if(typeof AnyObject[e] != 'object') {
            arr_keys.push(` ${e}`)
        }
    });

    arr_keys.forEach(e => {
        const n_key = e.toString().replace(' ', '')
        str_methods += `        self.${n_key} =${e}\n`
    })

    const strClass = `class ${className}:
    def __init__(self,${arr_keys.toString()}):\n${str_methods}`


    fs.writeFile(fileName, strClass, (err) => {
        if (err) throw err;
        console.log('O arquivo foi criado: ', fileName );
    });
}

generateClassPython(news.data.children[0].data, "UsersNew")
generateClassPython(popular.data.children[0].data, "UsersPopular")
