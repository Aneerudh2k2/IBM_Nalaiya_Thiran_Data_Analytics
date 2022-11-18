async function login(){
    const email = document.getElementById('email').value
    const pass = document.getElementById('pass').value
    options = {
        method: 'POST',
        headers: {
            'Content-Type':
                'application/json;charset=utf-8'
        },
        body: JSON.stringify({"email":email,"password":pass})
    }
    const result = await fetch('/login', options)
    if(result.status == 401) alert("Invalid credentials")
    if(result.status == 200) window.location.href = "http://localhost:8501"
}

async function register(){
    const email = document.getElementById('email').value
    const pass = document.getElementById('pass').value
    options = {
        method: 'POST',
        headers: {
            'Content-Type':
                'application/json;charset=utf-8'
        },
        body: JSON.stringify({"email":email,"password":pass})
    }
    const result = await fetch('/register', options)
    if(result.status == 401) alert("User exists already")
    if(result.status == 200) window.location.reload()
}