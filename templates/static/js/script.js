async function fetchRandomFact(){
    const response=await fetch('/index');
    const data= await response.json();
    document.getElementById('fact').innerText=data.fact;
}