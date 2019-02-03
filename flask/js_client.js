const fetch = require('node-fetch');

const userAction = async () => {
    const response = await fetch('http://35.188.88.169/post', {
        method: 'POST',
        body: { 'data': ['hello world', 'bye world'] }, // string or object
        headers: {
            'Content-Type': 'application/json'
        }
    });
    const myJson = response.html().then(val => val).catch(err => console.log(err)); //extract JSON from the http response
    // do something with myJson
    console.log(myJson);
}

userAction();